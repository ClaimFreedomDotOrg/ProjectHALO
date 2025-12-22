"""
CLI Module
==========
Command-line interface for Project H.A.L.O.
"""

import argparse
import asyncio
import sys

from halo.monitor import HALOMonitor
from halo.processing import TRIGGER_THRESHOLD


def main():
    """Main entry point for halo-monitor CLI."""
    parser = argparse.ArgumentParser(
        description="Project H.A.L.O. - Real-time EEG monitoring for shadow work",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  halo-monitor --address 00:55:DA:B9:FA:20
  halo-monitor --address 00:55:DA:B9:FA:20 --duration 300

Find your Muse device address:
  OpenMuse find
        """
    )
    
    parser.add_argument(
        '--address',
        type=str,
        required=True,
        help='MAC address of Muse S device (find with: OpenMuse find)'
    )
    
    parser.add_argument(
        '--duration',
        type=int,
        default=None,
        help='Duration in seconds (default: infinite, stop with Ctrl+C)'
    )
    
    parser.add_argument(
        '--threshold',
        type=float,
        default=TRIGGER_THRESHOLD,
        help=f'Trigger threshold for Alpha/Beta ratio (default: {TRIGGER_THRESHOLD})'
    )
    
    args = parser.parse_args()
    
    # Create monitor
    monitor = HALOMonitor(
        address=args.address,
        duration=args.duration,
        threshold=args.threshold
    )
    
    # Run
    try:
        asyncio.run(monitor.run())
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped by user (Ctrl+C)")
    except Exception as e:
        print(f"\nFatal error: {e}")
        import traceback
        traceback.print_exc()
        return 1
        
    return 0


if __name__ == '__main__':
    sys.exit(main())
