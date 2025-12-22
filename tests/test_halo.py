"""
Unit tests for Project H.A.L.O.
================================

Basic test suite to verify signal processing and buffer functionality.

Run with: pytest tests/test_halo.py -v
"""

import numpy as np
import pytest
from halo import EEGBuffer, compute_band_power, analyze_state


class TestEEGBuffer:
    """Test the EEGBuffer ring buffer implementation."""
    
    def test_initialization(self):
        """Test buffer initializes with correct parameters."""
        buffer = EEGBuffer(channels=4, buffer_seconds=5, sample_rate=256)
        assert buffer.channels == 4
        assert buffer.buffer_size == 5 * 256
        assert buffer.sample_rate == 256
        assert len(buffer.buffers) == 4
    
    def test_add_sample(self):
        """Test adding samples to buffer."""
        buffer = EEGBuffer(channels=4, buffer_seconds=1, sample_rate=10)
        
        sample = [1.0, 2.0, 3.0, 4.0]
        timestamp = 1234567890.0
        
        buffer.add_sample(sample, timestamp)
        
        assert len(buffer.buffers[0]) == 1
        assert buffer.buffers[0][0] == 1.0
        assert buffer.buffers[3][0] == 4.0
        assert buffer.timestamps[0] == timestamp
    
    def test_buffer_overflow(self):
        """Test that buffer maintains max size."""
        buffer = EEGBuffer(channels=4, buffer_seconds=1, sample_rate=10)
        
        # Add more samples than buffer size
        for i in range(20):
            buffer.add_sample([i, i, i, i], float(i))
        
        # Should only keep last 10 (buffer_seconds * sample_rate)
        assert len(buffer.buffers[0]) == 10
        assert buffer.buffers[0][0] == 10  # First value should be 10, not 0
        assert buffer.buffers[0][-1] == 19  # Last value should be 19
    
    def test_get_data(self):
        """Test retrieving data from buffer."""
        buffer = EEGBuffer(channels=4, buffer_seconds=1, sample_rate=10)
        
        for i in range(5):
            buffer.add_sample([i, i*2, i*3, i*4], float(i))
        
        data, timestamps = buffer.get_data()
        
        assert data.shape == (5, 4)
        assert timestamps.shape == (5,)
        assert np.array_equal(data[:, 0], [0, 1, 2, 3, 4])
        assert np.array_equal(data[:, 1], [0, 2, 4, 6, 8])
    
    def test_is_full(self):
        """Test buffer fullness detection."""
        buffer = EEGBuffer(channels=4, buffer_seconds=1, sample_rate=10)
        
        assert not buffer.is_full()
        
        # Add 50% of buffer size
        for i in range(5):
            buffer.add_sample([i, i, i, i], float(i))
        
        assert buffer.is_full()


class TestSignalProcessing:
    """Test signal processing functions."""
    
    def test_compute_band_power_alpha(self):
        """Test alpha band power computation."""
        # Generate 10 Hz sine wave (in alpha band)
        sample_rate = 256
        duration = 2  # seconds
        freq = 10  # Hz
        
        t = np.linspace(0, duration, sample_rate * duration)
        signal = np.sin(2 * np.pi * freq * t)
        
        alpha_power = compute_band_power(signal, sample_rate, (8, 12))
        beta_power = compute_band_power(signal, sample_rate, (13, 30))
        
        # Alpha power should be much higher than beta for 10 Hz signal
        assert alpha_power > beta_power
        assert alpha_power > 0
    
    def test_compute_band_power_beta(self):
        """Test beta band power computation."""
        # Generate 20 Hz sine wave (in beta band)
        sample_rate = 256
        duration = 2
        freq = 20
        
        t = np.linspace(0, duration, sample_rate * duration)
        signal = np.sin(2 * np.pi * freq * t)
        
        alpha_power = compute_band_power(signal, sample_rate, (8, 12))
        beta_power = compute_band_power(signal, sample_rate, (13, 30))
        
        # Beta power should be much higher than alpha for 20 Hz signal
        assert beta_power > alpha_power
        assert beta_power > 0
    
    def test_compute_band_power_empty(self):
        """Test band power with insufficient data."""
        sample_rate = 256
        signal = np.array([1.0, 2.0, 3.0])  # Very short signal
        
        # Should not crash, should return some value
        power = compute_band_power(signal, sample_rate, (8, 12))
        assert power >= 0


class TestStateAnalysis:
    """Test brain state analysis."""
    
    def test_analyze_state_insufficient_data(self):
        """Test analysis with insufficient data."""
        buffer = EEGBuffer(channels=4, buffer_seconds=1, sample_rate=256)
        
        # Add only a few samples
        for i in range(10):
            buffer.add_sample([i, i, i, i], float(i))
        
        result = analyze_state(buffer)
        assert result is None  # Should return None for insufficient data
    
    def test_analyze_state_observer(self):
        """Test detection of OBSERVER state (high alpha, low beta)."""
        buffer = EEGBuffer(channels=4, buffer_seconds=2, sample_rate=256)
        
        # Generate signal with strong alpha, weak beta
        t = np.linspace(0, 2, 256 * 2)
        alpha_signal = 5 * np.sin(2 * np.pi * 10 * t)  # Strong 10 Hz
        beta_signal = 0.5 * np.sin(2 * np.pi * 20 * t)  # Weak 20 Hz
        signal = alpha_signal + beta_signal
        
        for i, val in enumerate(signal):
            sample = [val, val, val, val]
            buffer.add_sample(sample, float(i) / 256)
        
        result = analyze_state(buffer)
        assert result is not None
        assert result['state'] == 'OBSERVER'
        assert result['ratio'] > 0.7
    
    def test_analyze_state_triggered(self):
        """Test detection of TRIGGERED state (low alpha, high beta)."""
        buffer = EEGBuffer(channels=4, buffer_seconds=2, sample_rate=256)
        
        # Generate signal with weak alpha, strong beta
        t = np.linspace(0, 2, 256 * 2)
        alpha_signal = 0.5 * np.sin(2 * np.pi * 10 * t)  # Weak 10 Hz
        beta_signal = 5 * np.sin(2 * np.pi * 20 * t)  # Strong 20 Hz
        signal = alpha_signal + beta_signal
        
        for i, val in enumerate(signal):
            sample = [val, val, val, val]
            buffer.add_sample(sample, float(i) / 256)
        
        result = analyze_state(buffer)
        assert result is not None
        assert result['state'] == 'TRIGGERED'
        assert result['ratio'] < 0.7


class TestIntegration:
    """Integration tests for full system."""
    
    def test_full_pipeline(self):
        """Test complete pipeline: buffer → analysis → state."""
        buffer = EEGBuffer(channels=4, buffer_seconds=2, sample_rate=256)
        
        # Simulate real EEG data (random walk)
        np.random.seed(42)
        for i in range(512):
            noise = np.random.randn(4) * 0.1
            sample = noise + np.sin(2 * np.pi * 10 * i / 256)  # 10 Hz base
            buffer.add_sample(sample.tolist(), float(i) / 256)
        
        assert buffer.is_full()
        
        result = analyze_state(buffer)
        assert result is not None
        assert 'alpha' in result
        assert 'beta' in result
        assert 'theta' in result
        assert 'ratio' in result
        assert 'state' in result
        assert result['state'] in ['OBSERVER', 'TRIGGERED']


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
