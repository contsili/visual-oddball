# Quick Reference - Visual Oddball Experiment

## Experiment at a Glance

**Task**: Count the BLACK circles  
**Duration**: ~10 minutes  
**Standard**: White circle (85%)  
**Deviant**: Black circle (15%)  

### Prepare the PCs for the hands-on
1. Download code from github

2. User app:
- Download and install, BESA, psychopy the APEX driver and APEX User app.
- Connect the APEX device via USB cable. In Device Manager, verify that 'TMSi USB Devices' appears. 
- If not, reinstall the driver OR connect via dongle/bluetooth.

3. Configure the triggers: 
- Set the usb TTL timing to 1 ms via the device manager>COM ports>open properties>bits per second to 115200, then go Advanced>Latency timer to 1 ms.
- Open the USB TTL application.
- Click through the available triggers until the red indicator light on the hardware turns off.
- Once the light is off, close the USB TTL application.
- You can begin now the experiment woth psychopy.

4. Configure psychopy:
- Make sure builder opens when you double click visual_oddball.psyexp
- Set the correct COM port for APEX in the PsychoPy experiment settings (match the port shown in Device Manager).
- Click on the trials button in the flow and make sure it points to Conditions: generate_trial_csv/oddball_conditions.csv

5. Documentation:
- Find the APEX manual, driver, and User app at: \\192.168.30.3\data$\SALES\TMSi\Software\APEX\APEX User package


---

## Trial Timing

```
┌─────────────────────────────────────┐
│  Time   │  Display                  │
├─────────────────────────────────────┤
│  0.0s   │  [WHITE or BLACK CIRCLE]  │
│    ↓    │   (500ms presentation)    │
│  0.5s   │  ────────────────────     │
│    ↓    │  [FIXATION CROSS: +]      │
│  1.5s+  │   (ISI: 1.2-1.8s)         │
│    ↓    │  ────────────────────     │
│ Next    │  [Next circle appears]     │
└─────────────────────────────────────┘
```

**Key Feature**: Fixation cross appears ONLY between stimuli (not during circle presentation)

---

## Required Files

✅ **visual_oddball.psyexp** - Main experiment  
✅ **generate_trial_csv/oddball_conditions.csv** - Trial sequence  
✅ **generate_visual_stimuli/white_visual.png** - Standard stimulus  
✅ **generate_visual_stimuli/black_visual.png** - Deviant stimulus  

---

## How to Run

### In PsychoPy Builder:
1. Open `visual_oddball.psyexp`
2. Click green Run button (or Ctrl+R)

### From Command Line:
```powershell
python visual_oddball_lastrun.py
```

---

## Visual Design

- **Background**: Gray (PsychoPy default)
- **Circles**: Transparent background PNG
- **Contrast**: High (white vs black on gray)
- **Fixation**: White "+" cross, centered

---

## Data Output

Location: `data/` folder  
Format: `PARTICIPANTID_visual_oddball_DATE.csv`

Columns include:
- Trial number
- Stimulus type (standard/deviant)  
- Response times
- Block number
- ISI duration
- EEG markers (if connected)

---

## Customization

### Experiment parameters
To modify experiment parameters, edit `generate_trial_csv/generate_trial_csv.py`:
- `n_blocks` - Number of blocks
- `trials_per_block` - Trials per block
- `standard_ratio` - Proportion of standard trials (0-1)
- `stimulus_duration` - How long stimulus is displayed (seconds)
- `isi_mean` - Average time between stimuli (seconds)
- `isi_jitter` - Randomness in ISI timing (seconds)

After editing, run:
```powershell
cd generate_trial_csv
python generate_trial_csv.py
```

### Change colors of the circles:
Edit `generate_visual_stimuli/generate_visual_stimuli.py`:
```python
create_circle_stimulus('white_visual.png', color='white')
create_circle_stimulus('black_visual.png', color='red')  # Any color
```

Then run:
```powershell
cd generate_visual_stimuli
python generate_visual_stimuli.py
cd ../generate_trial_csv
python generate_trial_csv.py
```

---

## Quick Stats

- **300 trials** total
- **2 blocks** of 150 trials each
- **~255 white circles** (standard)
- **~45 black circles** (deviant)
- **Break** after first 150 trials
- **10 minutes** total duration

---

## System Requirements

- PsychoPy 2025.1.1 or later
- Python 3.8+
- Screen resolution: 1536x864 or higher recommended
- Required Python packages:
  - pandas
  - numpy
  - PIL (Pillow)
  - psychopy
  - serial (pyserial) - only if using EEG triggers

## XDF pre recorded file
You can find my XDF file here: https://drive.google.com/file/d/1ib8sTNB_I-PL-fMhbeGPImGRDXeod1AS/view?usp=sharing