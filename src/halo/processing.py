"""
Signal Processing Module
=========================
EEG signal processing and analysis functions.
"""

import numpy as np
from scipy import signal
from scipy.fft import rfft, rfftfreq


# ==================== CONFIGURATION ====================

# EEG Frequency Bands (Hz)
ALPHA_BAND = (8, 12)
BETA_BAND = (13, 30)
THETA_BAND = (4, 8)

# Detection Threshold
# Ratio below this triggers "SHADOW DETECTED" alert
TRIGGER_THRESHOLD = 0.7  # Alpha/Beta ratio

# Buffer Configuration
BUFFER_SECONDS = 5  # Seconds of data to analyze
SAMPLE_RATE = 256  # Muse S EEG sampling rate (Hz)

# Display Update Rate
UPDATE_INTERVAL = 0.5  # Seconds between status updates


# ==================== FUNCTIONS ====================


def compute_band_power(data, sample_rate, band):
    """
    Compute average power in a frequency band using FFT.
    
    Args:
        data: 1D array of EEG samples
        sample_rate: Sampling rate in Hz
        band: Tuple (low_freq, high_freq) in Hz
        
    Returns:
        float: Average power in band
    """
    # Detrend and apply window
    data = signal.detrend(data)
    window = signal.windows.hamming(len(data))
    data_windowed = data * window
    
    # Compute FFT
    fft_vals = np.abs(rfft(data_windowed))
    fft_freqs = rfftfreq(len(data), 1.0 / sample_rate)
    
    # Extract band power
    band_mask = (fft_freqs >= band[0]) & (fft_freqs <= band[1])
    band_power = np.mean(fft_vals[band_mask] ** 2) if np.any(band_mask) else 0.0
    
    return band_power


def analyze_state(eeg_buffer, threshold=None):
    """
    Analyze current brain state from EEG buffer.
    
    Args:
        eeg_buffer: EEGBuffer instance
        threshold: Optional custom trigger threshold (uses TRIGGER_THRESHOLD if None)
        
    Returns:
        dict: Analysis results with keys 'alpha', 'beta', 'theta', 'ratio', 'state'
    """
    if threshold is None:
        threshold = TRIGGER_THRESHOLD
        
    data, _ = eeg_buffer.get_data()
    
    if data is None or len(data) < 256:  # Need at least 1 second
        return None
        
    # Average across all channels
    avg_data = np.mean(data, axis=1)
    
    # Compute band powers
    alpha = compute_band_power(avg_data, SAMPLE_RATE, ALPHA_BAND)
    beta = compute_band_power(avg_data, SAMPLE_RATE, BETA_BAND)
    theta = compute_band_power(avg_data, SAMPLE_RATE, THETA_BAND)
    
    # Compute ratio
    ratio = alpha / beta if beta > 0 else 0
    
    # Determine state
    state = "OBSERVER" if ratio > threshold else "TRIGGERED"
    
    return {
        'alpha': alpha,
        'beta': beta,
        'theta': theta,
        'ratio': ratio,
        'state': state
    }
