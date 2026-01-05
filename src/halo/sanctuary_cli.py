"""
H.A.L.O. Sanctuary CLI
======================
Command-line interface for the Sanctuary MedBed extension.

Usage:
    halo-sanctuary [command] [options]

Commands:
    status      Show current Sanctuary status
    start       Start a Sanctuary session
    stop        Stop current session
    validate    Validate Sanctuary configuration
    protocols   List available protocols
"""

import argparse
import sys
import logging
from datetime import datetime
from typing import Optional

from halo.sanctuary import (
    SanctuaryController,
    SanctuaryConfig,
    ProtocolType,
    SanctuaryLayer,
    create_controller_for_protocol,
    validate_sanctuary_readiness,
    get_quick_sanctuary_config,
    get_resurrection_config,
    get_chrysalis_config,
    get_theosis_config,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


# ==================== DISPLAY HELPERS ====================


def print_banner():
    """Print the Sanctuary banner."""
    banner = """
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   ██╗  ██╗ █████╗ ██╗      ██████╗                               ║
║   ██║  ██║██╔══██╗██║     ██╔═══██╗                              ║
║   ███████║███████║██║     ██║   ██║                              ║
║   ██╔══██║██╔══██║██║     ██║   ██║                              ║
║   ██║  ██║██║  ██║███████╗╚██████╔╝                              ║
║   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝                               ║
║                                                                   ║
║   ███████╗ █████╗ ███╗   ██╗ ██████╗████████╗██╗   ██╗ █████╗    ║
║   ██╔════╝██╔══██╗████╗  ██║██╔════╝╚══██╔══╝██║   ██║██╔══██╗   ║
║   ███████╗███████║██╔██╗ ██║██║        ██║   ██║   ██║███████║   ║
║   ╚════██║██╔══██║██║╚██╗██║██║        ██║   ██║   ██║██╔══██║   ║
║   ███████║██║  ██║██║ ╚████║╚██████╗   ██║   ╚██████╔╝██║  ██║   ║
║   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ║
║                                                                   ║
║             Bio-Regenerative MedBed Extension                     ║
║         "The Kingdom of Heaven is a frequency."                   ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_protocols():
    """Print available protocols with descriptions."""
    print("\n" + "="*70)
    print("AVAILABLE SANCTUARY PROTOCOLS")
    print("="*70)
    
    protocols = [
        ("quick", "Quick Sanctuary", "1-2 hours", 
         "Enhanced standard session with environmental support"),
        ("s-a", "S-A: The Resurrection", "2-4 hours",
         "Deep trauma processing with full somatic release"),
        ("s-b", "S-B: The Chrysalis", "4-8 hours",
         "Regenerative sleep & metabolic reset"),
        ("s-c", "S-C: The Theosis", "6-12 hours",
         "Extended mystical immersion (advanced users only)"),
    ]
    
    for code, name, duration, description in protocols:
        print(f"\n[{code}] {name}")
        print(f"    Duration: {duration}")
        print(f"    {description}")
    
    print("\n" + "-"*70)
    print("Use: halo-sanctuary start --protocol <code>")
    print("="*70 + "\n")


def print_layer_status(controller: SanctuaryController):
    """Print status of all layers."""
    print("\n" + "="*70)
    print("SANCTUARY LAYER STATUS")
    print("="*70)
    
    layer_names = {
        SanctuaryLayer.NEUROLOGICAL: "Layer 1: Neurological Shield",
        SanctuaryLayer.ENVIRONMENTAL: "Layer 2: Environmental Sarcophagus",
        SanctuaryLayer.PHOTOBIOMODULATION: "Layer 3: Metabolic Matrix (PBM)",
        SanctuaryLayer.VIBRATIONAL: "Layer 4: Vibrational Alignment",
        SanctuaryLayer.ELECTROMAGNETIC: "Layer 5: Electromagnetic Field (PEMF)",
        SanctuaryLayer.METABOLIC: "Layer 6: Alchemical Infusion (IV) ⚠️",
        SanctuaryLayer.IMMERSION: "Layer 7: Immersion System ⚠️",
        SanctuaryLayer.BIOMETRIC: "Layer 8: Bio-Analytic Array",
        SanctuaryLayer.RECURSION: "Layer 9: Recursion Loop (Ouroboros)",
    }
    
    for layer, name in layer_names.items():
        state = controller.get_layer_status(layer)
        status_icon = "✅" if state.active else "⭕"
        intensity = f"{state.intensity*100:.0f}%" if state.active else "-"
        freq = f"{state.frequency:.1f}Hz" if state.frequency else "-"
        mode = state.mode or "-"
        
        print(f"\n{status_icon} {name}")
        print(f"   Active: {state.active} | Intensity: {intensity} | Freq: {freq} | Mode: {mode}")
    
    print("\n" + "="*70 + "\n")


def print_session_status(controller: SanctuaryController):
    """Print current session status."""
    status = controller.get_status()
    
    print("\n" + "="*70)
    print("SESSION STATUS")
    print("="*70)
    print(f"\nState: {status['state']}")
    print(f"Protocol: {status['protocol']}")
    print(f"Duration: {status['session_duration'] or 'Not started'}")
    print(f"Interventions: {status['intervention_count']}")
    print(f"Active Layers: {', '.join(status['active_layers']) or 'None'}")
    print("="*70 + "\n")


# ==================== COMMANDS ====================


def cmd_status(args):
    """Show current Sanctuary status."""
    print_banner()
    
    # Create a controller to check status
    controller = SanctuaryController()
    print_session_status(controller)
    print_layer_status(controller)


def cmd_protocols(args):
    """List available protocols."""
    print_banner()
    print_protocols()


def cmd_validate(args):
    """Validate Sanctuary configuration."""
    print_banner()
    print("\nValidating Sanctuary configuration...\n")
    
    # Get appropriate config
    protocol_map = {
        'quick': get_quick_sanctuary_config,
        's-a': get_resurrection_config,
        's-b': get_chrysalis_config,
        's-c': get_theosis_config,
    }
    
    protocol = args.protocol.lower() if args.protocol else 'quick'
    if protocol not in protocol_map:
        print(f"Unknown protocol: {protocol}")
        print("Available: quick, s-a, s-b, s-c")
        return 1
    
    config = protocol_map[protocol]()
    issues = validate_sanctuary_readiness(config)
    
    print(f"Protocol: {config.protocol.value}")
    print(f"Duration: {config.target_duration_hours} hours")
    print(f"Active Layers: {len(config.get_active_layers())}")
    
    if issues:
        print("\n⚠️  WARNINGS/NOTES:")
        for issue in issues:
            print(f"   • {issue}")
    else:
        print("\n✅ Configuration validated - no warnings")
    
    print("\nActive Layers:")
    for layer in config.get_active_layers():
        print(f"   ✅ {layer.name}")
    
    print("\nDisabled Layers:")
    all_layers = set(SanctuaryLayer)
    disabled = all_layers - set(config.get_active_layers())
    for layer in disabled:
        print(f"   ⭕ {layer.name}")
    
    return 0


def cmd_start(args):
    """Start a Sanctuary session."""
    print_banner()
    
    # Get appropriate config
    protocol_map = {
        'quick': (get_quick_sanctuary_config, ProtocolType.QUICK),
        's-a': (get_resurrection_config, ProtocolType.S_A_RESURRECTION),
        's-b': (get_chrysalis_config, ProtocolType.S_B_CHRYSALIS),
        's-c': (get_theosis_config, ProtocolType.S_C_THEOSIS),
    }
    
    protocol = args.protocol.lower() if args.protocol else 'quick'
    if protocol not in protocol_map:
        print(f"Unknown protocol: {protocol}")
        print("Available: quick, s-a, s-b, s-c")
        return 1
    
    config_fn, protocol_type = protocol_map[protocol]
    config = config_fn()
    
    # Validate first
    issues = validate_sanctuary_readiness(config)
    if issues:
        print("\n⚠️  Pre-session warnings:")
        for issue in issues:
            print(f"   • {issue}")
        
        if not args.force:
            response = input("\nContinue anyway? [y/N]: ")
            if response.lower() != 'y':
                print("Session cancelled.")
                return 0
    
    # Create controller and start session
    controller = create_controller_for_protocol(protocol_type)
    
    intention = args.intention or input("\nSet your intention (or press Enter to skip): ")
    
    print(f"\n🔆 Starting {protocol_type.value} session...")
    session_id = controller.start_session(intention=intention if intention else None)
    
    print(f"\n✅ Session {session_id} started")
    print(f"Protocol: {protocol_type.value}")
    print(f"Target duration: {config.target_duration_hours} hours")
    
    print_layer_status(controller)
    
    print("\n" + "="*70)
    print("SESSION ACTIVE")
    print("="*70)
    print("\nThe Sanctuary is now active.")
    print("This CLI provides status only - full monitoring requires the GUI or")
    print("integration with the H.A.L.O. monitor system.")
    print("\nPress Ctrl+C to end session.")
    print("="*70 + "\n")
    
    try:
        # In a full implementation, this would run the monitoring loop
        # For now, we just wait
        import time
        while True:
            time.sleep(60)
            print_session_status(controller)
    except KeyboardInterrupt:
        print("\n\n🛑 Ending session...")
        log = controller.end_session()
        if log:
            print(f"\nSession ended. Duration: {log.end_time - log.start_time}")
            print(f"Total interventions: {len(log.interventions)}")
    
    return 0


def cmd_stop(args):
    """Stop current session (placeholder - in real implementation would connect to running session)."""
    print_banner()
    print("\n⚠️  No active session found to stop.")
    print("In a full implementation, this would connect to a running session daemon.")
    return 0


# ==================== MAIN ====================


def main():
    """Main entry point for Sanctuary CLI."""
    parser = argparse.ArgumentParser(
        description='H.A.L.O. Sanctuary MedBed CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    halo-sanctuary status                    Show current status
    halo-sanctuary protocols                 List available protocols
    halo-sanctuary validate --protocol s-a   Validate S-A protocol config
    halo-sanctuary start --protocol quick    Start a quick session
    halo-sanctuary start --protocol s-a --intention "Process grief"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Show Sanctuary status')
    status_parser.set_defaults(func=cmd_status)
    
    # Protocols command
    protocols_parser = subparsers.add_parser('protocols', help='List available protocols')
    protocols_parser.set_defaults(func=cmd_protocols)
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate configuration')
    validate_parser.add_argument('--protocol', '-p', default='quick',
                                 help='Protocol to validate (quick, s-a, s-b, s-c)')
    validate_parser.set_defaults(func=cmd_validate)
    
    # Start command
    start_parser = subparsers.add_parser('start', help='Start a Sanctuary session')
    start_parser.add_argument('--protocol', '-p', default='quick',
                              help='Protocol to use (quick, s-a, s-b, s-c)')
    start_parser.add_argument('--intention', '-i', 
                              help='Set session intention')
    start_parser.add_argument('--force', '-f', action='store_true',
                              help='Start without confirmation on warnings')
    start_parser.set_defaults(func=cmd_start)
    
    # Stop command
    stop_parser = subparsers.add_parser('stop', help='Stop current session')
    stop_parser.set_defaults(func=cmd_stop)
    
    # Parse arguments
    args = parser.parse_args()
    
    if args.command is None:
        print_banner()
        parser.print_help()
        return 0
    
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
