"""
EEG Buffer Module
=================
Ring buffer for storing and analyzing EEG data.
"""

from collections import deque
import numpy as np


class EEGBuffer:
    """Ring buffer for storing and analyzing EEG data."""
    
    def __init__(self, channels=4, buffer_seconds=5, sample_rate=256):
        """
        Initialize EEG buffer.
        
        Args:
            channels: Number of EEG channels (default 4: TP9, AF7, AF8, TP10)
            buffer_seconds: Seconds of data to store
            sample_rate: Sampling rate in Hz
        """
        self.channels = channels
        self.buffer_size = int(buffer_seconds * sample_rate)
        self.sample_rate = sample_rate
        
        # Ring buffer: each channel gets a deque
        self.buffers = [deque(maxlen=self.buffer_size) for _ in range(channels)]
        self.timestamps = deque(maxlen=self.buffer_size)
        
    def add_sample(self, sample, timestamp):
        """
        Add a single sample across all channels.
        
        Args:
            sample: Array of channel values [TP9, AF7, AF8, TP10]
            timestamp: Unix timestamp
        """
        for i, value in enumerate(sample):
            self.buffers[i].append(value)
        self.timestamps.append(timestamp)
        
    def get_data(self):
        """
        Get buffer data as numpy array.
        
        Returns:
            tuple: (data, timestamps) where data is shape (samples, channels)
        """
        if not self.buffers[0]:
            return None, None
            
        data = np.array([list(buf) for buf in self.buffers]).T
        timestamps = np.array(list(self.timestamps))
        return data, timestamps
        
    def is_full(self):
        """Check if buffer has enough data for analysis."""
        return len(self.buffers[0]) >= self.buffer_size * 0.5  # At least 50% full
