import pandas as pd
import random
import numpy as np

# Parameters for 10-minute visual oddball experiment
n_blocks = 2
trials_per_block = 150  # 300 total trials across 2 blocks
standard_ratio = 0.85
deviant_ratio = 0.15
# For visual stimuli: shorter ISI and stimulus duration
stimulus_duration = 0.5  # 500ms stimulus presentation
isi_mean = 1.5  # 1.5 second average ISI
isi_jitter = 0.3  # +/- 300ms jitter

# Function to generate trial sequence for a block
def generate_block_sequence(block_num):
    # Calculate number of each trial type
    n_standard = int(trials_per_block * standard_ratio)
    n_deviant = trials_per_block - n_standard
    
    # Create initial sequence
    sequence = ['standard'] * n_standard + ['deviant'] * n_deviant
    
    # Shuffle the sequence
    random.shuffle(sequence)
    
    # Ensure no consecutive deviants
    for i in range(len(sequence)-1):
        if sequence[i] == 'deviant' and sequence[i+1] == 'deviant':
            # Find a position with a standard tone not preceded by a deviant
            valid_positions = [j for j in range(len(sequence)) 
                             if sequence[j] == 'standard' and 
                             (j == 0 or sequence[j-1] != 'deviant') and
                             j != i+1]
            
            if valid_positions:
                swap_pos = random.choice(valid_positions)
                sequence[i+1], sequence[swap_pos] = sequence[swap_pos], sequence[i+1]
    
    # Generate ISIs
    isis = np.random.uniform(isi_mean - isi_jitter, isi_mean + isi_jitter, trials_per_block)
    
    # Create trial list
    trials = []
    for i in range(trials_per_block):
        # Use image files for visual stimuli (white = standard, black = deviant)
        image_file = 'white_visual.png' if sequence[i] == 'standard' else 'black_visual.png'
        marker_value = 1 if sequence[i] == 'standard' else 2
        
        trials.append({
            'imageFile': image_file,
            'trialType': sequence[i],
            'isi': isis[i],
            'stimDuration': stimulus_duration,
            'marker': marker_value,
            'block': block_num
        })
    
    return trials

# Generate all blocks
all_trials = []
for block in range(1, n_blocks + 1):
    block_trials = generate_block_sequence(block)
    all_trials.extend(block_trials)

# Create a DataFrame
df = pd.DataFrame(all_trials)

# Save to CSV in the current directory
df.to_csv('oddball_conditions.csv', index=False)
print(f"Created conditions file with {len(df)} trials")
print(f"Total blocks: {n_blocks}")
print(f"Trials per block: {trials_per_block}")
print(f"Estimated duration: ~{len(df) * (stimulus_duration + isi_mean) / 60:.1f} minutes")
