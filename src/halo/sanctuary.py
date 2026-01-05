"""
H.A.L.O. Sanctuary Module
==========================
Bio-Regenerative MedBed Extension for Project H.A.L.O.

This module provides integration capabilities for the Sanctuary environmental
immersion system. It extends the core H.A.L.O. system with multi-layer
coordination, session state management, and protocol automation.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, Dict, List, Callable, Any
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


# ==================== ENUMS ====================


class SanctuaryLayer(Enum):
    """The nine layers of the Sanctuary system."""
    NEUROLOGICAL = 1      # H.A.L.O. Core (EEG, tVNS, Bilateral)
    ENVIRONMENTAL = 2     # Sarcophagus (Isolation, Faraday)
    PHOTOBIOMODULATION = 3  # PBM (Red/NIR LEDs)
    VIBRATIONAL = 4       # Cymatics (Vibroacoustic)
    ELECTROMAGNETIC = 5   # PEMF (Helmholtz Coils)
    METABOLIC = 6         # Smart IV (REQUIRES MEDICAL SUPERVISION)
    IMMERSION = 7         # Extended Session Support (REQUIRES MEDICAL SUPERVISION)
    BIOMETRIC = 8         # Multi-Sensor Array
    RECURSION = 9         # Ouroboros (Waste Analysis - FUTURE)


class SessionState(Enum):
    """State machine states for Sanctuary sessions."""
    OFFLINE = auto()
    STARTUP = auto()
    CALIBRATION = auto()
    OBSERVER = auto()
    TRIGGERED = auto()
    PROCESSING = auto()
    INTEGRATION = auto()
    DESCENT = auto()
    DEEP_STATE = auto()
    ASCENT = auto()
    EMERGENCE = auto()
    SHUTDOWN = auto()
    EMERGENCY = auto()


class ProtocolType(Enum):
    """Sanctuary protocol types."""
    QUICK = "quick"           # 1-2 hours enhanced standard
    S_A_RESURRECTION = "s-a"  # 2-4 hours trauma + somatic
    S_B_CHRYSALIS = "s-b"     # 4-8 hours regenerative sleep
    S_C_THEOSIS = "s-c"       # 6-12 hours extended mystical


class InterventionLevel(Enum):
    """Intervention intensity levels."""
    NONE = 0
    MINIMAL = 1
    LOW = 2
    MODERATE = 3
    HIGH = 4
    MAXIMUM = 5
    RESCUE = 6


# ==================== DATA CLASSES ====================


@dataclass
class LayerState:
    """Current state of a single Sanctuary layer."""
    layer: SanctuaryLayer
    active: bool = False
    intensity: float = 0.0  # 0.0 to 1.0
    frequency: Optional[float] = None  # Hz, where applicable
    mode: Optional[str] = None
    last_update: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for logging/serialization."""
        return {
            "layer": self.layer.name,
            "active": self.active,
            "intensity": self.intensity,
            "frequency": self.frequency,
            "mode": self.mode,
            "last_update": self.last_update.isoformat()
        }


@dataclass
class BiometricReading:
    """A single biometric data point."""
    timestamp: datetime
    hrv: Optional[float] = None  # ms RMSSD
    hrv_coherence: Optional[float] = None  # 0-100
    gsr: Optional[float] = None  # µS
    alpha_power: Optional[float] = None
    beta_power: Optional[float] = None
    theta_power: Optional[float] = None
    alpha_beta_ratio: Optional[float] = None
    heart_rate: Optional[int] = None  # BPM
    spo2: Optional[float] = None  # Percentage
    temperature: Optional[float] = None  # Celsius
    glucose: Optional[float] = None  # mg/dL
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for logging/serialization."""
        return {k: v for k, v in {
            "timestamp": self.timestamp.isoformat(),
            "hrv": self.hrv,
            "hrv_coherence": self.hrv_coherence,
            "gsr": self.gsr,
            "alpha_power": self.alpha_power,
            "beta_power": self.beta_power,
            "theta_power": self.theta_power,
            "alpha_beta_ratio": self.alpha_beta_ratio,
            "heart_rate": self.heart_rate,
            "spo2": self.spo2,
            "temperature": self.temperature,
            "glucose": self.glucose
        }.items() if v is not None}


@dataclass
class SessionLog:
    """Complete log of a Sanctuary session."""
    session_id: str
    protocol: ProtocolType
    start_time: datetime
    end_time: Optional[datetime] = None
    intention: Optional[str] = None
    suds_pre: Optional[int] = None
    suds_post: Optional[int] = None
    layer_states: List[LayerState] = field(default_factory=list)
    biometric_readings: List[BiometricReading] = field(default_factory=list)
    state_transitions: List[tuple] = field(default_factory=list)
    interventions: List[Dict] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


# ==================== CONFIGURATION ====================


@dataclass
class SanctuaryConfig:
    """Configuration for Sanctuary session."""
    
    # Protocol settings
    protocol: ProtocolType = ProtocolType.QUICK
    target_duration_hours: float = 1.0
    
    # Layer activation
    layers_enabled: Dict[SanctuaryLayer, bool] = field(default_factory=lambda: {
        SanctuaryLayer.NEUROLOGICAL: True,
        SanctuaryLayer.ENVIRONMENTAL: True,
        SanctuaryLayer.PHOTOBIOMODULATION: True,
        SanctuaryLayer.VIBRATIONAL: True,
        SanctuaryLayer.ELECTROMAGNETIC: True,
        SanctuaryLayer.METABOLIC: False,  # Requires medical supervision
        SanctuaryLayer.IMMERSION: False,  # Requires medical supervision
        SanctuaryLayer.BIOMETRIC: True,
        SanctuaryLayer.RECURSION: False,  # Future implementation
    })
    
    # Thresholds
    shadow_spike_threshold: float = 0.7  # Alpha/Beta ratio
    hrv_crash_threshold: float = 20.0  # ms RMSSD
    gsr_spike_threshold: float = 5.0  # µS change
    
    # Timing
    calibration_duration_minutes: int = 20
    integration_duration_minutes: int = 15
    
    # Safety
    emergency_timeout_minutes: int = 5
    max_intervention_intensity: InterventionLevel = InterventionLevel.HIGH
    
    def get_active_layers(self) -> List[SanctuaryLayer]:
        """Return list of enabled layers."""
        return [layer for layer, enabled in self.layers_enabled.items() if enabled]


# ==================== DEFAULT CONFIGURATIONS ====================


def get_quick_sanctuary_config() -> SanctuaryConfig:
    """Configuration for Quick Sanctuary protocol (1-2 hours)."""
    return SanctuaryConfig(
        protocol=ProtocolType.QUICK,
        target_duration_hours=1.5,
        layers_enabled={
            SanctuaryLayer.NEUROLOGICAL: True,
            SanctuaryLayer.ENVIRONMENTAL: True,
            SanctuaryLayer.PHOTOBIOMODULATION: True,
            SanctuaryLayer.VIBRATIONAL: True,
            SanctuaryLayer.ELECTROMAGNETIC: False,
            SanctuaryLayer.METABOLIC: False,
            SanctuaryLayer.IMMERSION: False,
            SanctuaryLayer.BIOMETRIC: True,
            SanctuaryLayer.RECURSION: False,
        },
        calibration_duration_minutes=15,
    )


def get_resurrection_config() -> SanctuaryConfig:
    """Configuration for S-A Resurrection protocol (2-4 hours)."""
    return SanctuaryConfig(
        protocol=ProtocolType.S_A_RESURRECTION,
        target_duration_hours=3.0,
        layers_enabled={
            SanctuaryLayer.NEUROLOGICAL: True,
            SanctuaryLayer.ENVIRONMENTAL: True,
            SanctuaryLayer.PHOTOBIOMODULATION: True,
            SanctuaryLayer.VIBRATIONAL: True,
            SanctuaryLayer.ELECTROMAGNETIC: True,
            SanctuaryLayer.METABOLIC: False,
            SanctuaryLayer.IMMERSION: False,
            SanctuaryLayer.BIOMETRIC: True,
            SanctuaryLayer.RECURSION: False,
        },
        calibration_duration_minutes=30,
        integration_duration_minutes=30,
    )


def get_chrysalis_config() -> SanctuaryConfig:
    """Configuration for S-B Chrysalis protocol (4-8 hours)."""
    return SanctuaryConfig(
        protocol=ProtocolType.S_B_CHRYSALIS,
        target_duration_hours=6.0,
        layers_enabled={
            SanctuaryLayer.NEUROLOGICAL: True,
            SanctuaryLayer.ENVIRONMENTAL: True,
            SanctuaryLayer.PHOTOBIOMODULATION: True,
            SanctuaryLayer.VIBRATIONAL: True,
            SanctuaryLayer.ELECTROMAGNETIC: True,
            SanctuaryLayer.METABOLIC: False,  # Enable only with medical supervision
            SanctuaryLayer.IMMERSION: False,
            SanctuaryLayer.BIOMETRIC: True,
            SanctuaryLayer.RECURSION: False,
        },
        calibration_duration_minutes=30,
    )


def get_theosis_config() -> SanctuaryConfig:
    """Configuration for S-C Theosis protocol (6-12 hours)."""
    return SanctuaryConfig(
        protocol=ProtocolType.S_C_THEOSIS,
        target_duration_hours=8.0,
        layers_enabled={
            SanctuaryLayer.NEUROLOGICAL: True,
            SanctuaryLayer.ENVIRONMENTAL: True,
            SanctuaryLayer.PHOTOBIOMODULATION: True,
            SanctuaryLayer.VIBRATIONAL: True,
            SanctuaryLayer.ELECTROMAGNETIC: True,
            SanctuaryLayer.METABOLIC: False,  # Enable only with medical supervision
            SanctuaryLayer.IMMERSION: False,  # Enable only with medical supervision
            SanctuaryLayer.BIOMETRIC: True,
            SanctuaryLayer.RECURSION: False,
        },
        calibration_duration_minutes=60,
        integration_duration_minutes=45,
    )


# ==================== FREQUENCY CONSTANTS ====================


# Standard frequencies used across layers
SCHUMANN_RESONANCE = 7.83  # Hz - Earth's electromagnetic resonance
GAMMA_BREAK = 40.0  # Hz - For breaking rumination loops
ALPHA_BASELINE = 10.0  # Hz - Calm alertness
THETA_DEEP = 6.0  # Hz - Deep meditation, insight
DELTA_SLEEP = 2.0  # Hz - Deep sleep

# Cymatics frequency ranges
CYMATICS_FREQUENCIES = {
    "gamma_sync": (30, 40),
    "full_body": (40, 60),
    "muscle_relax": (60, 80),
    "deep_tissue": (80, 120),
}

# PBM wavelengths
PBM_RED = 660  # nm - Surface/skin
PBM_NIR = 850  # nm - Deep tissue penetration


# ==================== SANCTUARY CONTROLLER ====================


class SanctuaryController:
    """
    Central controller for the H.A.L.O. Sanctuary system.
    
    Coordinates all nine layers through a time-division multiplexing approach,
    manages session state, and handles intervention triggering.
    """
    
    def __init__(self, config: Optional[SanctuaryConfig] = None):
        """Initialize the Sanctuary controller."""
        self.config = config or SanctuaryConfig()
        self.state = SessionState.OFFLINE
        self.session_log: Optional[SessionLog] = None
        
        # Layer states
        self.layer_states: Dict[SanctuaryLayer, LayerState] = {
            layer: LayerState(layer=layer)
            for layer in SanctuaryLayer
        }
        
        # Callbacks for hardware integration
        self._layer_callbacks: Dict[SanctuaryLayer, List[Callable]] = {
            layer: [] for layer in SanctuaryLayer
        }
        
        # Intervention history
        self._intervention_count = 0
        self._last_intervention_time: Optional[datetime] = None
        
        logger.info("SanctuaryController initialized")
    
    # ==================== STATE MANAGEMENT ====================
    
    def transition_state(self, new_state: SessionState) -> None:
        """Transition to a new session state."""
        old_state = self.state
        self.state = new_state
        
        if self.session_log:
            self.session_log.state_transitions.append(
                (datetime.now().isoformat(), old_state.name, new_state.name)
            )
        
        logger.info(f"State transition: {old_state.name} -> {new_state.name}")
        self._on_state_change(old_state, new_state)
    
    def _on_state_change(self, old_state: SessionState, new_state: SessionState) -> None:
        """Handle state change events."""
        if new_state == SessionState.EMERGENCY:
            self._trigger_emergency_protocol()
        elif new_state == SessionState.TRIGGERED:
            self._trigger_shadow_response()
        elif new_state == SessionState.INTEGRATION:
            self._begin_integration()
    
    # ==================== SESSION MANAGEMENT ====================
    
    def start_session(self, intention: Optional[str] = None) -> str:
        """Start a new Sanctuary session."""
        if self.state != SessionState.OFFLINE:
            raise RuntimeError("Session already in progress")
        
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        self.session_log = SessionLog(
            session_id=session_id,
            protocol=self.config.protocol,
            start_time=datetime.now(),
            intention=intention
        )
        
        # Activate enabled layers
        for layer in self.config.get_active_layers():
            self._activate_layer(layer)
        
        self.transition_state(SessionState.STARTUP)
        logger.info(f"Session {session_id} started with protocol {self.config.protocol.value}")
        
        return session_id
    
    def end_session(self) -> Optional[SessionLog]:
        """End the current session and return the log."""
        if self.state == SessionState.OFFLINE:
            return None
        
        self.transition_state(SessionState.SHUTDOWN)
        
        # Deactivate all layers
        for layer in SanctuaryLayer:
            self._deactivate_layer(layer)
        
        if self.session_log:
            self.session_log.end_time = datetime.now()
        
        log = self.session_log
        self.session_log = None
        self.transition_state(SessionState.OFFLINE)
        
        logger.info(f"Session ended. Duration: {log.end_time - log.start_time}")
        return log
    
    def emergency_stop(self) -> None:
        """Immediately stop all systems and enter emergency state."""
        logger.critical("EMERGENCY STOP TRIGGERED")
        self.transition_state(SessionState.EMERGENCY)
        
        # Deactivate all layers immediately
        for layer in SanctuaryLayer:
            self._deactivate_layer(layer, immediate=True)
        
        if self.session_log:
            self.session_log.notes.append(
                f"EMERGENCY STOP at {datetime.now().isoformat()}"
            )
    
    # ==================== LAYER CONTROL ====================
    
    def _activate_layer(self, layer: SanctuaryLayer) -> None:
        """Activate a specific layer."""
        if not self.config.layers_enabled.get(layer, False):
            logger.warning(f"Layer {layer.name} is not enabled in config")
            return
        
        state = self.layer_states[layer]
        state.active = True
        state.last_update = datetime.now()
        
        # Notify callbacks
        for callback in self._layer_callbacks[layer]:
            try:
                callback(layer, "activate", state)
            except Exception as e:
                logger.error(f"Layer callback error: {e}")
        
        logger.debug(f"Layer {layer.name} activated")
    
    def _deactivate_layer(self, layer: SanctuaryLayer, immediate: bool = False) -> None:
        """Deactivate a specific layer."""
        state = self.layer_states[layer]
        state.active = False
        state.intensity = 0.0
        state.last_update = datetime.now()
        
        # Notify callbacks
        for callback in self._layer_callbacks[layer]:
            try:
                callback(layer, "deactivate", state)
            except Exception as e:
                logger.error(f"Layer callback error: {e}")
        
        logger.debug(f"Layer {layer.name} deactivated")
    
    def set_layer_intensity(
        self, 
        layer: SanctuaryLayer, 
        intensity: float,
        frequency: Optional[float] = None
    ) -> None:
        """Set the intensity (and optionally frequency) of a layer."""
        if not self.layer_states[layer].active:
            logger.warning(f"Cannot set intensity - Layer {layer.name} is not active")
            return
        
        intensity = max(0.0, min(1.0, intensity))  # Clamp 0-1
        
        state = self.layer_states[layer]
        state.intensity = intensity
        if frequency is not None:
            state.frequency = frequency
        state.last_update = datetime.now()
        
        # Notify callbacks
        for callback in self._layer_callbacks[layer]:
            try:
                callback(layer, "update", state)
            except Exception as e:
                logger.error(f"Layer callback error: {e}")
    
    def register_layer_callback(
        self, 
        layer: SanctuaryLayer, 
        callback: Callable[[SanctuaryLayer, str, LayerState], None]
    ) -> None:
        """Register a callback for layer state changes."""
        self._layer_callbacks[layer].append(callback)
    
    # ==================== BIOMETRIC PROCESSING ====================
    
    def process_biometrics(self, reading: BiometricReading) -> None:
        """Process incoming biometric data and trigger interventions if needed."""
        if self.session_log:
            self.session_log.biometric_readings.append(reading)
        
        # Check for Shadow Spike
        if reading.alpha_beta_ratio is not None:
            if reading.alpha_beta_ratio < self.config.shadow_spike_threshold:
                if self.state == SessionState.OBSERVER:
                    logger.warning(f"Shadow Spike detected! Ratio: {reading.alpha_beta_ratio:.2f}")
                    self.transition_state(SessionState.TRIGGERED)
        
        # Check for HRV crash
        if reading.hrv is not None:
            if reading.hrv < self.config.hrv_crash_threshold:
                logger.warning(f"HRV crash detected! RMSSD: {reading.hrv:.1f}ms")
                self._trigger_hrv_support()
        
        # Check for GSR spike
        if reading.gsr is not None:
            if self._check_gsr_spike(reading.gsr):
                logger.warning(f"GSR spike detected! {reading.gsr:.1f}µS")
        
        # Check for recovery
        if self.state == SessionState.TRIGGERED:
            if reading.alpha_beta_ratio and reading.alpha_beta_ratio > self.config.shadow_spike_threshold:
                logger.info("Recovery detected - returning to OBSERVER state")
                self.transition_state(SessionState.OBSERVER)
    
    def _check_gsr_spike(self, current_gsr: float) -> bool:
        """Check if GSR has spiked significantly."""
        if not self.session_log or not self.session_log.biometric_readings:
            return False
        
        # Compare to recent readings
        recent = [r.gsr for r in self.session_log.biometric_readings[-10:] if r.gsr]
        if not recent:
            return False
        
        baseline = sum(recent) / len(recent)
        return (current_gsr - baseline) > self.config.gsr_spike_threshold
    
    # ==================== INTERVENTION LOGIC ====================
    
    def _trigger_shadow_response(self) -> None:
        """Multi-layer response to Shadow Spike detection."""
        logger.info("Executing Shadow Spike response protocol")
        
        # Layer 1: tVNS increase
        self.set_layer_intensity(
            SanctuaryLayer.NEUROLOGICAL, 
            intensity=0.7, 
            frequency=25.0
        )
        
        # Layer 3: PBM breath pacing
        self.set_layer_intensity(
            SanctuaryLayer.PHOTOBIOMODULATION,
            intensity=0.6
        )
        self.layer_states[SanctuaryLayer.PHOTOBIOMODULATION].mode = "breath_pace"
        
        # Layer 4: Cymatics gamma break
        self.set_layer_intensity(
            SanctuaryLayer.VIBRATIONAL,
            intensity=0.5,
            frequency=GAMMA_BREAK
        )
        
        # Layer 5: PEMF rescue burst
        if self.layer_states[SanctuaryLayer.ELECTROMAGNETIC].active:
            self.set_layer_intensity(
                SanctuaryLayer.ELECTROMAGNETIC,
                intensity=0.8,
                frequency=10.0  # Rescue burst
            )
            self.layer_states[SanctuaryLayer.ELECTROMAGNETIC].mode = "rescue_burst"
        
        self._log_intervention("shadow_response")
    
    def _trigger_hrv_support(self) -> None:
        """Response to HRV crash."""
        logger.info("Executing HRV support protocol")
        
        # Increase vagal tone support
        self.set_layer_intensity(
            SanctuaryLayer.NEUROLOGICAL,
            intensity=0.8
        )
        
        # PEMF Schumann grounding
        if self.layer_states[SanctuaryLayer.ELECTROMAGNETIC].active:
            self.set_layer_intensity(
                SanctuaryLayer.ELECTROMAGNETIC,
                intensity=0.6,
                frequency=SCHUMANN_RESONANCE
            )
        
        self._log_intervention("hrv_support")
    
    def _trigger_emergency_protocol(self) -> None:
        """Emergency protocol - all systems to grounding mode."""
        logger.critical("Executing emergency protocol")
        
        # All active layers to minimal/grounding
        for layer, state in self.layer_states.items():
            if state.active:
                if layer == SanctuaryLayer.ELECTROMAGNETIC:
                    # PEMF to Schumann only
                    self.set_layer_intensity(layer, 0.3, SCHUMANN_RESONANCE)
                elif layer == SanctuaryLayer.VIBRATIONAL:
                    # Cymatics to alpha
                    self.set_layer_intensity(layer, 0.3, ALPHA_BASELINE)
                else:
                    # Others to minimum
                    self.set_layer_intensity(layer, 0.2)
        
        self._log_intervention("emergency_protocol")
    
    def _begin_integration(self) -> None:
        """Transition all systems to integration mode."""
        logger.info("Beginning integration phase")
        
        # Reduce all intensities
        for layer, state in self.layer_states.items():
            if state.active:
                current = state.intensity
                self.set_layer_intensity(layer, current * 0.5)
        
        # Cymatics to alpha
        if self.layer_states[SanctuaryLayer.VIBRATIONAL].active:
            self.set_layer_intensity(
                SanctuaryLayer.VIBRATIONAL,
                intensity=0.3,
                frequency=ALPHA_BASELINE
            )
        
        self._log_intervention("integration_begin")
    
    def _log_intervention(self, intervention_type: str) -> None:
        """Log an intervention event."""
        self._intervention_count += 1
        self._last_intervention_time = datetime.now()
        
        if self.session_log:
            self.session_log.interventions.append({
                "timestamp": datetime.now().isoformat(),
                "type": intervention_type,
                "count": self._intervention_count,
                "layer_states": {
                    layer.name: state.to_dict() 
                    for layer, state in self.layer_states.items()
                    if state.active
                }
            })
    
    # ==================== STATUS & REPORTING ====================
    
    def get_status(self) -> Dict[str, Any]:
        """Get current Sanctuary status."""
        return {
            "state": self.state.name,
            "protocol": self.config.protocol.value,
            "session_duration": str(
                datetime.now() - self.session_log.start_time
            ) if self.session_log else None,
            "intervention_count": self._intervention_count,
            "active_layers": [
                layer.name for layer, state in self.layer_states.items()
                if state.active
            ],
            "layer_states": {
                layer.name: state.to_dict()
                for layer, state in self.layer_states.items()
            }
        }
    
    def get_layer_status(self, layer: SanctuaryLayer) -> LayerState:
        """Get status of a specific layer."""
        return self.layer_states[layer]


# ==================== UTILITY FUNCTIONS ====================


def create_controller_for_protocol(protocol: ProtocolType) -> SanctuaryController:
    """Create a SanctuaryController configured for a specific protocol."""
    configs = {
        ProtocolType.QUICK: get_quick_sanctuary_config,
        ProtocolType.S_A_RESURRECTION: get_resurrection_config,
        ProtocolType.S_B_CHRYSALIS: get_chrysalis_config,
        ProtocolType.S_C_THEOSIS: get_theosis_config,
    }
    
    config_fn = configs.get(protocol, get_quick_sanctuary_config)
    return SanctuaryController(config=config_fn())


def validate_sanctuary_readiness(config: SanctuaryConfig) -> List[str]:
    """
    Validate that the Sanctuary is ready for a session.
    Returns a list of warnings/errors.
    """
    issues = []
    
    # Check for medically supervised layers
    if config.layers_enabled.get(SanctuaryLayer.METABOLIC, False):
        issues.append(
            "WARNING: Layer 6 (Metabolic/IV) requires licensed medical supervision"
        )
    
    if config.layers_enabled.get(SanctuaryLayer.IMMERSION, False):
        issues.append(
            "WARNING: Layer 7 (Immersion) requires licensed medical supervision"
        )
    
    # Check protocol requirements
    if config.protocol == ProtocolType.S_C_THEOSIS:
        issues.append(
            "WARNING: S-C Theosis protocol is for experienced users only. "
            "Ensure support person is available."
        )
    
    # Check duration
    if config.target_duration_hours > 4:
        issues.append(
            "NOTE: Extended sessions (>4 hours) require careful preparation. "
            "Review S-B or S-C protocol documentation."
        )
    
    return issues


# ==================== EXPORTS ====================


__all__ = [
    # Enums
    "SanctuaryLayer",
    "SessionState", 
    "ProtocolType",
    "InterventionLevel",
    
    # Data classes
    "LayerState",
    "BiometricReading",
    "SessionLog",
    "SanctuaryConfig",
    
    # Controller
    "SanctuaryController",
    
    # Config functions
    "get_quick_sanctuary_config",
    "get_resurrection_config",
    "get_chrysalis_config",
    "get_theosis_config",
    
    # Utility functions
    "create_controller_for_protocol",
    "validate_sanctuary_readiness",
    
    # Constants
    "SCHUMANN_RESONANCE",
    "GAMMA_BREAK",
    "ALPHA_BASELINE",
    "THETA_DEEP",
    "DELTA_SLEEP",
    "CYMATICS_FREQUENCIES",
    "PBM_RED",
    "PBM_NIR",
]
