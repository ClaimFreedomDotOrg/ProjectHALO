"""
Example: Offline EEG Analysis
==============================

This script demonstrates how to analyze pre-recorded Muse S data
using OpenMuse and the H.A.L.O. signal processing functions.

Usage:
    python examples/analyze_recording.py --file path/to/recording.txt
"""

import sys
import os

import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import OpenMuse decoder
try:
    import OpenMuse
except ImportError:
    print("Error: OpenMuse not installed. Install with:")
    print("  pip install https://github.com/DominiqueMakowski/OpenMuse/zipball/main")
    sys.exit(1)

# Import H.A.L.O. functions
from halo import compute_band_power, ALPHA_BAND, BETA_BAND, THETA_BAND


def load_and_decode(filepath):
    """
    Load and decode a raw Muse S recording.
    
    Args:
        filepath: Path to .txt file from OpenMuse record
        
    Returns:
        dict: Decoded data with 'EEG', 'ACCGYRO', etc.
    """
    print(f"Loading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        messages = f.readlines()
    
    print(f"Decoding {len(messages)} messages...")
    data = OpenMuse.decode_rawdata(messages)
    
    return data


def analyze_eeg_epochs(eeg_df, epoch_seconds=5, sample_rate=256):
    """
    Analyze EEG data in epochs and compute band powers.
    
    Args:
        eeg_df: DataFrame with EEG data
        epoch_seconds: Length of each epoch in seconds
        sample_rate: EEG sampling rate
        
    Returns:
        DataFrame: Analysis results per epoch
    """
    results = []
    
    # Extract EEG channels
    channels = ['EEG_TP9', 'EEG_AF7', 'EEG_AF8', 'EEG_TP10']
    eeg_data = eeg_df[channels].values
    timestamps = eeg_df['time'].values
    
    # Split into epochs
    epoch_samples = int(epoch_seconds * sample_rate)
    n_epochs = len(eeg_data) // epoch_samples
    
    print(f"Analyzing {n_epochs} epochs of {epoch_seconds}s each...")
    
    for i in range(n_epochs):
        start_idx = i * epoch_samples
        end_idx = start_idx + epoch_samples
        
        epoch_data = eeg_data[start_idx:end_idx]
        epoch_time = timestamps[start_idx]
        
        # Average across channels
        avg_signal = np.mean(epoch_data, axis=1)
        
        # Compute band powers
        alpha = compute_band_power(avg_signal, sample_rate, ALPHA_BAND)
        beta = compute_band_power(avg_signal, sample_rate, BETA_BAND)
        theta = compute_band_power(avg_signal, sample_rate, THETA_BAND)
        
        # Compute ratio
        ratio = alpha / beta if beta > 0 else 0
        state = "OBSERVER" if ratio > 0.7 else "TRIGGERED"
        
        results.append({
            'epoch': i,
            'time': epoch_time,
            'alpha': alpha,
            'beta': beta,
            'theta': theta,
            'ratio': ratio,
            'state': state
        })
    
    return pd.DataFrame(results)


def plot_results(results_df, output_path=None):
    """
    Create visualization of analysis results.
    
    Args:
        results_df: DataFrame from analyze_eeg_epochs
        output_path: Optional path to save figure
    """
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    
    # Plot 1: Band powers over time
    ax1 = axes[0]
    ax1.plot(results_df['time'], results_df['alpha'], label='Alpha (8-12 Hz)', linewidth=2)
    ax1.plot(results_df['time'], results_df['beta'], label='Beta (13-30 Hz)', linewidth=2)
    ax1.plot(results_df['time'], results_df['theta'], label='Theta (4-8 Hz)', linewidth=2)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Power (a.u.)')
    ax1.set_title('EEG Band Powers Over Time')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Alpha/Beta ratio
    ax2 = axes[1]
    ax2.plot(results_df['time'], results_df['ratio'], linewidth=2, color='purple')
    ax2.axhline(y=0.7, color='r', linestyle='--', label='Threshold (0.7)')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Alpha/Beta Ratio')
    ax2.set_title('Alpha/Beta Ratio (H.A.L.O. Trigger Indicator)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: State timeline
    ax3 = axes[2]
    state_numeric = (results_df['state'] == 'OBSERVER').astype(int)
    ax3.fill_between(results_df['time'], 0, state_numeric, 
                     alpha=0.5, color='green', label='OBSERVER')
    ax3.fill_between(results_df['time'], 0, 1-state_numeric, 
                     alpha=0.5, color='red', label='TRIGGERED')
    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('State')
    ax3.set_title('Detected Brain State')
    ax3.set_yticks([0, 1])
    ax3.set_yticklabels(['TRIGGERED', 'OBSERVER'])
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=150)
        print(f"Figure saved to {output_path}")
    else:
        plt.show()


def print_summary(results_df):
    """Print summary statistics."""
    print("\n" + "=" * 60)
    print("  ANALYSIS SUMMARY")
    print("=" * 60)
    
    total_epochs = len(results_df)
    observer_epochs = (results_df['state'] == 'OBSERVER').sum()
    triggered_epochs = (results_df['state'] == 'TRIGGERED').sum()
    
    avg_alpha = results_df['alpha'].mean()
    avg_beta = results_df['beta'].mean()
    avg_theta = results_df['theta'].mean()
    avg_ratio = results_df['ratio'].mean()
    
    print(f"Total Epochs: {total_epochs}")
    print(f"Duration: {results_df['time'].max():.1f} seconds")
    print()
    print(f"State Distribution:")
    print(f"  OBSERVER:  {observer_epochs:3d} epochs ({observer_epochs/total_epochs*100:.1f}%)")
    print(f"  TRIGGERED: {triggered_epochs:3d} epochs ({triggered_epochs/total_epochs*100:.1f}%)")
    print()
    print(f"Average Band Powers:")
    print(f"  Alpha (8-12 Hz):  {avg_alpha:.2f}")
    print(f"  Beta (13-30 Hz):  {avg_beta:.2f}")
    print(f"  Theta (4-8 Hz):   {avg_theta:.2f}")
    print()
    print(f"Average Alpha/Beta Ratio: {avg_ratio:.2f}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze pre-recorded Muse S EEG data with H.A.L.O. algorithms"
    )
    parser.add_argument(
        '--file',
        type=str,
        required=True,
        help='Path to raw recording file (.txt from OpenMuse record)'
    )
    parser.add_argument(
        '--epoch',
        type=int,
        default=5,
        help='Epoch length in seconds (default: 5)'
    )
    parser.add_argument(
        '--plot',
        action='store_true',
        help='Display plots (requires matplotlib)'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Save plot to file (e.g., analysis.png)'
    )
    parser.add_argument(
        '--export-csv',
        type=str,
        help='Export results to CSV file'
    )
    
    args = parser.parse_args()
    
    # Load and decode
    try:
        data = load_and_decode(args.file)
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}")
        return 1
    except Exception as e:
        print(f"Error loading/decoding file: {e}")
        return 1
    
    # Check for EEG data
    if 'EEG' not in data or data['EEG'].empty:
        print("Error: No EEG data found in recording")
        return 1
    
    eeg_df = data['EEG']
    print(f"Loaded {len(eeg_df)} EEG samples")
    
    # Analyze
    results = analyze_eeg_epochs(eeg_df, epoch_seconds=args.epoch)
    
    # Print summary
    print_summary(results)
    
    # Export CSV if requested
    if args.export_csv:
        results.to_csv(args.export_csv, index=False)
        print(f"\nResults exported to {args.export_csv}")
    
    # Plot if requested
    if args.plot or args.output:
        plot_results(results, output_path=args.output)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
