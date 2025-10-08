import pandas as pd
import random
import numpy as np

# Parameters
n_blocks = 5
trials_per_block = 100
standard_ratio = 0.85
deviant_ratio = 0.15
isi_mean = 2.5
isi_jitter = 0.5

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
        sound_file = 'standard.wav' if sequence[i] == 'standard' else 'deviant.wav'
        marker_value = 1 if sequence[i] == 'standard' else 2
        
        trials.append({
            'soundFile': sound_file,
            'trialType': sequence[i],
            'isi': isis[i],
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

# Save to CSV
df.to_csv(r'c:\temp\oddball_conditions.csv', index=False)
print(f"Created conditions file with {len(df)} trials")
