"""
Project H.A.L.O.
================
Hemispheric Alignment & Limbic Override

A neuro-biological regulator for shadow work and trauma processing.
"""

__version__ = "0.1.0"

from halo.buffer import EEGBuffer
from halo.processing import (
    compute_band_power,
    analyze_state,
    ALPHA_BAND,
    BETA_BAND,
    THETA_BAND,
    TRIGGER_THRESHOLD,
    BUFFER_SECONDS,
    SAMPLE_RATE,
    UPDATE_INTERVAL,
)
from halo.monitor import HALOMonitor

__all__ = [
    "EEGBuffer",
    "compute_band_power",
    "analyze_state",
    "HALOMonitor",
    "ALPHA_BAND",
    "BETA_BAND",
    "THETA_BAND",
    "TRIGGER_THRESHOLD",
    "BUFFER_SECONDS",
    "SAMPLE_RATE",
    "UPDATE_INTERVAL",
]
