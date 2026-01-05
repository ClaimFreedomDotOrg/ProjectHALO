"""
Project H.A.L.O.
================
Hemispheric Alignment & Limbic Override

A neuro-biological regulator for shadow work and trauma processing.

The H.A.L.O. system can be used standalone (headset only) or extended
with the H.A.L.O. Sanctuary for full environmental immersion (MedBed).
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

# Sanctuary Extension (MedBed)
from halo.sanctuary import (
    # Enums
    SanctuaryLayer,
    SessionState,
    ProtocolType,
    InterventionLevel,
    # Data classes
    LayerState,
    BiometricReading,
    SessionLog,
    SanctuaryConfig,
    # Controller
    SanctuaryController,
    # Config functions
    get_quick_sanctuary_config,
    get_resurrection_config,
    get_chrysalis_config,
    get_theosis_config,
    # Utility functions
    create_controller_for_protocol,
    validate_sanctuary_readiness,
    # Constants
    SCHUMANN_RESONANCE,
    GAMMA_BREAK,
    ALPHA_BASELINE,
    THETA_DEEP,
    DELTA_SLEEP,
)

__all__ = [
    # Core H.A.L.O.
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
    
    # Sanctuary Extension
    "SanctuaryLayer",
    "SessionState",
    "ProtocolType",
    "InterventionLevel",
    "LayerState",
    "BiometricReading",
    "SessionLog",
    "SanctuaryConfig",
    "SanctuaryController",
    "get_quick_sanctuary_config",
    "get_resurrection_config",
    "get_chrysalis_config",
    "get_theosis_config",
    "create_controller_for_protocol",
    "validate_sanctuary_readiness",
    "SCHUMANN_RESONANCE",
    "GAMMA_BREAK",
    "ALPHA_BASELINE",
    "THETA_DEEP",
    "DELTA_SLEEP",
]
