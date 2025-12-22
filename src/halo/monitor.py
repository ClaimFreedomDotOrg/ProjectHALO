"""
HALO Monitor Module
===================
Main monitoring class for real-time EEG analysis.
"""

import asyncio
import time
import sys
import os

from halo.buffer import EEGBuffer
from halo.processing import (
    analyze_state,
    BUFFER_SECONDS,
    SAMPLE_RATE,
    UPDATE_INTERVAL,
    TRIGGER_THRESHOLD,
)

# OpenMuse imports
# Add OpenMuse to path if installed locally in sources/
sources_path = os.path.join(os.path.dirname(__file__), '..', '..', 'sources', 'OpenMuse')
if os.path.exists(sources_path):
    sys.path.insert(0, sources_path)

try:
    import OpenMuse
    from OpenMuse.muse import MuseS
    from OpenMuse.decode import parse_message
    from OpenMuse.backends import create_backend
except ImportError as e:
    print("ERROR: OpenMuse not found. Please install with:")
    print("  pip install https://github.com/DominiqueMakowski/OpenMuse/zipball/main")
    sys.exit(1)


class HALOMonitor:
    """Main monitoring class for Project H.A.L.O."""
    
    def __init__(self, address, duration=None, threshold=None):
        """
        Initialize H.A.L.O. monitor.
        
        Args:
            address: MAC address of Muse S device
            duration: Optional duration in seconds (None = infinite)
            threshold: Optional custom trigger threshold
        """
        self.address = address
        self.duration = duration
        self.threshold = threshold if threshold is not None else TRIGGER_THRESHOLD
        self.eeg_buffer = EEGBuffer(
            channels=4,
            buffer_seconds=BUFFER_SECONDS,
            sample_rate=SAMPLE_RATE
        )
        
        self.start_time = None
        self.last_update = 0
        self.sample_count = 0
        self.trigger_count = 0
        
        self.running = False
        
    async def on_eeg_data(self, sender, data):
        """
        Callback for EEG data from Muse device.
        
        Args:
            sender: BLE characteristic UUID
            data: Raw bytes from device
        """
        try:
            # Parse message using OpenMuse decoder
            decoded = parse_message(data)
            
            if not decoded or 'EEG' not in decoded:
                return
                
            # Extract EEG samples
            eeg_data = decoded['EEG']
            
            # Process each sample in the message
            for sample in eeg_data['samples']:
                # Sample format: [TP9, AF7, AF8, TP10]
                timestamp = time.time()
                self.eeg_buffer.add_sample(sample, timestamp)
                self.sample_count += 1
                
        except Exception as e:
            print(f"Error processing EEG data: {e}")
            
    async def display_loop(self):
        """Async loop for displaying brain state analysis."""
        print("\n" + "=" * 70)
        print("  H.A.L.O. MONITOR ACTIVE - The Watcher is Online")
        print("=" * 70)
        print(f"  Trigger Threshold: Alpha/Beta < {self.threshold}")
        print(f"  Buffer: {BUFFER_SECONDS}s | Sample Rate: {SAMPLE_RATE}Hz")
        print("=" * 70 + "\n")
        
        while self.running:
            current_time = time.time()
            
            # Update at specified interval
            if current_time - self.last_update >= UPDATE_INTERVAL:
                self.last_update = current_time
                
                if self.eeg_buffer.is_full():
                    result = analyze_state(self.eeg_buffer, threshold=self.threshold)
                    
                    if result:
                        elapsed = current_time - self.start_time
                        
                        # Build status line
                        status_line = (
                            f"[{elapsed:>7.1f}s] "
                            f"State: {result['state']:<10} | "
                            f"Ratio: {result['ratio']:>5.2f} | "
                            f"α: {result['alpha']:>8.2f} | "
                            f"β: {result['beta']:>8.2f} | "
                            f"θ: {result['theta']:>8.2f}"
                        )
                        print(status_line)
                        
                        # Alert on trigger
                        if result['state'] == "TRIGGERED":
                            self.trigger_count += 1
                            print("\n" + "!" * 70)
                            print("  >>> SHADOW DETECTED: ENGAGE VAGUS STIMULATION <<<")
                            print("  ACTION: Slowly turn TENS dial up to therapeutic level")
                            print("!" * 70 + "\n")
                else:
                    print(f"Buffering... ({len(self.eeg_buffer.buffers[0])}/{self.eeg_buffer.buffer_size} samples)")
                    
            await asyncio.sleep(0.1)
            
    async def run(self):
        """Main monitoring loop."""
        print("\n" + "=" * 70)
        print("  Project H.A.L.O. - Initializing...")
        print("=" * 70)
        print(f"  Device: {self.address}")
        print(f"  Duration: {'Infinite (Ctrl+C to stop)' if self.duration is None else f'{self.duration}s'}")
        print("=" * 70 + "\n")
        
        # Create BLE backend
        backend = create_backend()
        
        try:
            # Connect to device
            print(f"Connecting to Muse S at {self.address}...")
            async with backend(self.address) as client:
                print("✓ Connected")
                
                # Initialize device with preset for EEG
                print("Initializing device (preset p1041 - all channels)...")
                await MuseS.initialize_device(client, preset="p1041", verbose=False)
                print("✓ Device initialized")
                
                # Start notifications on EEG characteristic
                print("Starting EEG stream...")
                await client.start_notify(MuseS.EEG_UUID, self.on_eeg_data)
                print("✓ EEG stream active\n")
                
                # Start monitoring
                self.running = True
                self.start_time = time.time()
                
                # Create display task
                display_task = asyncio.create_task(self.display_loop())
                
                # Run for duration or until interrupted
                if self.duration:
                    await asyncio.sleep(self.duration)
                else:
                    # Run until cancelled
                    try:
                        await asyncio.Event().wait()
                    except asyncio.CancelledError:
                        pass
                        
                # Stop monitoring
                self.running = False
                
                # Wait for display task to finish
                await display_task
                
                # Stop notifications
                await client.stop_notify(MuseS.EEG_UUID)
                
        except Exception as e:
            print(f"\nError: {e}")
            raise
        finally:
            self.running = False
            
        # Final statistics
        print("\n" + "=" * 70)
        print("  H.A.L.O. Monitor - Session Complete")
        print("=" * 70)
        elapsed = time.time() - self.start_time if self.start_time else 0
        print(f"  Duration: {elapsed:.1f}s")
        print(f"  Samples: {self.sample_count}")
        print(f"  Triggers: {self.trigger_count}")
        print("=" * 70 + "\n")
