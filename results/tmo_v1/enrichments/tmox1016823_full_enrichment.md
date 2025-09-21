# Experiment tmox1016823 - Logbook Analysis

**Total runs with logbook entries**: 377

## Run-by-Run Activities

### Run 1
**Duration**: 18.4 seconds (very short, 2nd percentile)
**Total entries**: 37 (35 unique)
**Activities**:
- first run. recording works
- Beam on IM2K0 after the summer shutdown. 400 eV at 102 Hz. Unpointed.,
- The camera on IM1K4 is not working that well.
- SQ1 endstation at the beginning of the experiment shift. This is where the metrology group left that chamber aligned with the beamline trajectory.
- Beam on IM2K4. Unpointed. Seems a bit off from the trajectory. We will aligned it by looking at IM5k4.
- Beam on IM3K4. Unpointed.
- Beam on IM5K4. Unpointed. The beam is all the way through. We will align it here. Then we will check with IM2K4.
- Beam on IM5K4 after pointing. We moved 300 um in +Y and 300 um in +X. See the unpointed imager before to compare.
- Beam on IM2K4 after pointing using the white line of IM5K4.
- TMO_KBO1 transmission: 1.2360797470050984. scan data path: /reg/g/pcds/pyps/apps/hutch-python/tmo/tmo/mirror-check/scans/TMO_KBO1/TMO_KBO1_2024-10-19--07-49-42.h5
- TMO_KBO1 transmission: 0.8350469428183832. scan data path: /reg/g/pcds/pyps/apps/hutch-python/tmo/tmo/mirror-check/scans/TMO_KBO1/TMO_KBO1_2024-10-19--07-54-57.h5
- TMO_KBO1 transmission: 0.3296432941588685. scan data path: /reg/g/pcds/pyps/apps/hutch-python/tmo/tmo/mirror-check/scans/TMO_KBO1/TMO_KBO1_2024-10-19--07-59-43.h5
- x-rays on scope. Trigger on EVR Seq:257, 19565 ticks delay
- X-ray on IMATM frosted YAG target.
- Disable arbitration for pf1k4_target The pmps is limiting us to Beam class 7 which seems wrong. JPC will double check.
- KB1 position at the start of the first shift. We are about to go to the WFS. Logging the current position so that we have record of where we were.
- Disable arbitration for im5k4_target This should be over-ridden by the pf1k4. It seems this is not working, JPC will look at this with Tong.
- KB1 positions before optimizing with WFS. Device: Position: 0 mr2k4 bender_ds 19.761467 1 mr2k4 bender_us 13.461394 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.389592 4 mr2k4 x 1.18784 5 mr2k4 y 3.001875 ...
- KB1 positions after optimizing focus with WFS. Device: Position: 0 mr2k4 bender_ds 19.145086 1 mr2k4 bender_us 13.525773 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.370351 4 mr2k4 x 1.187835 5 mr2k4 y 3.0...
- KB1 position before moving to preset position FocusIP Device: Position: 0 mr2k4 bender_ds 19.145097 1 mr2k4 bender_us 13.525785 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.376357 4 mr2k4 x 1.187835 5 mr2k...
- Move KB1 to preset position FocusIP Device: Position: 0 mr2k4 bender_ds 18.800842 1 mr2k4 bender_us 13.91176 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.391047 4 mr2k4 x 1.18784 5 mr2k4 y 3.001865 6 mr3k4...
- After optimizing the focus position, we get about 2um FWHM spot size according to the WFS.
- Update FocusIP for exp with current bender positions. Device: Position: 0 mr2k4 bender_ds 19.145037 1 mr2k4 bender_us 13.524994 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.353025 4 mr2k4 x 1.18784 5 mr2k4...
- WFS raw image at 400 eV, Target 4 in.
- Sample paddle OUT position at the beginning of the shift.
- toggled arbitration status of im5k4_target
- toggled arbitration status of pf1k4_target
- If the arb-enable goes to False and back to True. The arbiter does not check the current device status. Example, we put in IM5K4, and it asserts a requirement. We disable arbitration for IM5K4 and the...
- X-ray on Clear YAG. The cross hair on MRCO-GIGE01 shows where the beamline alignment laser was in.
- Currnetly the database is set to limit Target 4 and 5 to beam class 7. JPC will review if this is the correct setting.
- Re-positioned the cursor to point at the X-ray position in clear YAG. The sample paddle Z is optimized with the motion of sample paddle Z wrt to the beamline laser and X-rays.
- For Tong. It looks like pf1k4 does not veto im5k4.
- The damage limit for the Si targets was estimted to be 2W. The single pulse damage was estimated to be 1.5 mJ. This means that the max rate should be 1.3 kHz. At 70 pC, beam class will allow ~4 kHz. S...
- ami keeps failing to configure.
- Disable arbitration for pf1k4_target testing pf1k4 arbitration

**Run classification**: commissioning_run
**Confidence**: high
**Key evidence**: Initial beam alignment after summer shutdown, KB1 position optimization with WFS, mirror transmission checks, and beamline trajectory verification

### Run 2
**Duration**: 39.1 seconds (short, 37th percentile)
**Total entries**: 5 (4 unique)
**Activities**:
- saving run to test some problems with the DAQ.
- toggled arbitration status of im5k4_target
- by-pass im5k4 error fopr 15 minutes to looks at beam at high rate on IM5K4. Beam is attenuated to 1% so this should not be a hazard to the imager.
- starting to look for signal in the ToF

**Run classification**: diagnostic_run
**Confidence**: medium
**Key evidence**: Testing DAQ problems, checking beam at high rate on IM5K4, starting to look for signal in ToF

### Run 3
**Duration**: 1.1 minutes (medium, 61st percentile)
**Total entries**: 10 (9 unique)
**Activities**:
- first run with some counts on ToFs. Not all ToFs are working, but most have counts.
- Timed run with 492000 events Scan exited after 6 steps with status: success
- hsd start times. 99500 ns for XPM2 98200 ns for XPM4
- fex start time for mrco_hsd
- fex ymin
- fex ymax
- MRCO Labels: PCI Slot: 0 mrco_hsd_0 hsd_1B_A 1 mrco_hsd_22 hsd_1A_A 2 mrco_hsd_45 hsd_1A_B 3 mrco_hsd_67 hsd_B2_B 4 mrco_hsd_90 hsd_3E_B 5 mrco_hsd_112 hsd_01_A 6 mrco_hsd_135 hsd_01_B 7 mrco_hsd_157 ...
- accessed the hutch to attach amplifiers to 270 and 315 deg detectors
- I'm guessing these are meant to be a factor of 10 smaller

**Run classification**: commissioning_run
**Confidence**: high
**Key evidence**: First run with counts on ToFs, accessing hutch to attach amplifiers to detectors, setting up HSD timing parameters

### Run 4
**Duration**: 1.2 minutes (medium, 66th percentile)
**Total entries**: 9 (9 unique)
**Activities**:
- 1 min of data with amplifiers on all ToF. 337 still looks strange, no data.
- another grab of all detectors all wvfm.
- Voltage configuration for run 4 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2100.0 2099.984100 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.119774 False...
- Zoom for control room https://stanford.zoom.us/j/94913038467?pwd=l4TSxv83lyZl50MdMz1lm8hHCrn8OU.1
- Update FocusIP for hutch with current bender positions. Device: Position: 0 mr2k4 bender_ds 19.145071 1 mr2k4 bender_us 13.524965 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.359326 4 mr2k4 x 1.187815 5 mr...
- Update FocusIP for hutch with current bender positions. After opitimizing with WFS Device: Position: 0 mr2k4 bender_ds 19.145062 1 mr2k4 bender_us 13.524968 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.383...
- setting for FZP at 400 eV setting
- pulse energy 44 uJ at XGMD, SP1K4-ATT target 1; FZP_400eV_1 in; intensifier 650V
- increase gain on FZP after decreasing pulse energy. Currently 1% transmission (~2 uJ)

**Run classification**: commissioning_run
**Confidence**: high
**Key evidence**: Testing amplifiers on all ToF detectors, voltage configuration setup, FZP at 400 eV setting, gain adjustments

### Run 5
**Duration**: 1.5 minutes (medium, 71st percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- all 16 detectors are working. Also FZP is on and working
- photon energy scan
- Scan hf_w: [390. 391.33333333 392.66666667 394. 395.33333333 396.66666667 398. 399.33333333 400.66666667 402. 403.33333333 404.66666667 406. 407.33333333 408.66666667 410. ] 32800 events/step Scan exi...
- setting for fzp spectrometer. Device: Position: 0 Intensifier MCP [V] 450 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 5623.0 4 solid_att TARGET1 5 solid...
- Changed the MCP gain to 1450 for run 6 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2150.0 2150.049300 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.10680...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan from 390-410 eV, FZP spectrometer settings, MCP gain adjustments

### Run 6
**Duration**: 1.2 minutes (medium, 68th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan hf_w: [390. 391.33333333 392.66666667 394. 395.33333333 396.66666667 398. 399.33333333 400.66666667 402. 403.33333333 404.66666667 406. 407.33333333 408.66666667 410. ] 32800 events/step Scan exi...
- Changed the MCP gain to 1500 for run 7 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2200.0 2199.982900 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.10549...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continued photon energy scan (390-410 eV) with MCP gain adjustment

### Run 7
**Duration**: 1.1 minutes (medium, 60th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- increasing gain on mcp, fixed photon energy of 400 eV.
- Timed run with 492000 events Scan exited after 6 steps with status: success
- Changed the MCP gain to 1550 for run 8 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2250.0 2250.043000 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.10701...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Increasing MCP gain at fixed photon energy of 400 eV for detector response calibration

### Run 8
**Duration**: 1.1 minutes (medium, 60th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- Changed the MCP gain to 1600 for run 9 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2300.0 2299.958300 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.10782...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of MCP gain calibration series, increasing to 1600V

### Run 9
**Duration**: 1.1 minutes (medium, 58th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- Changed the MCP gain to 1650 for run 10 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2350.0 2350.085200 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.1063...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of MCP gain calibration series, increasing to 1650V

### Run 10
**Duration**: 1.1 minutes (medium, 60th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- Changed the MCP gain to 1700 for run 11 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2400.0 2400.060500 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.1076...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of MCP gain calibration series, increasing to 1700V

### Run 11
**Duration**: 1.1 minutes (medium, 61st percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- Changed the MCP gain to 1700 for run 12 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2450.0 2450.111800 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.1077...
- Changed the MCP gain to 1750 for run 12 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2450.0 2450.111800 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.1077...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of MCP gain calibration series, increasing to 1750V, following the pattern from runs 6-10

### Run 12
**Duration**: 1.1 minutes (medium, 58th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- Changed the MCP gain to 1800 for run 13 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2500.0 2500.019800 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.1082...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of MCP gain calibration series, increasing to 1800V for run 13

### Run 13
**Duration**: 1.1 minutes (medium, 61st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- Changed the MCP gain to 1350 for run 14 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2050.0 2050.062000 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.1097...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of MCP gain calibration series, changing to 1350V for run 14

### Run 14
**Duration**: 1.1 minutes (medium, 59th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- Changed the MCP gain to 1350 for run 15 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2000.0 2000.099900 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.1067...
- spectrum on the SP1K4-gige and to see it on Piranha
- Changed the MCP gain to 1300 for run 15 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2000.0 2000.010100 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.1081...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of MCP gain calibration with spectrum monitoring on SP1K4-gige and Piranha, adjusting to 1300V

### Run 15
**Duration**: 1.1 minutes (medium, 59th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- Changed the MCP gain to 1250 for run 16 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1950.0 1950.084100 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.1090...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of MCP gain calibration series, decreasing to 1250V for run 16

### Run 16
**Duration**: 1.1 minutes (medium, 61st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- Changed the MCP gain to 1200 for run 17 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1900.0 1900.108200 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.1078...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of MCP gain calibration series, decreasing to 1200V for run 17

### Run 17
**Duration**: 1.1 minutes (medium, 59th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- with 400eV FZP in and Target 1 ATT in; on IM5K4 cursor and roi positions

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Final run in MCP gain calibration series at 400eV with FZP and Target 1 ATT in place

### Run 18
**Duration**: 3.5 hours (very long, 100th percentile)
**Total entries**: 7 (7 unique)
**Activities**:
- Added a retardation of 100 V. Argon is the sample. Photon energy = 400 eV. We want to remove the Ar 2s = 74 eV.
- Changed the MCP gain back to 1400 V. Added a retardation of 100 V. Run 18 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2000.000 2000.007800 False MPOD:01:M5:...
- keep crashing
- Timed run with 492000 events Scan exited after 4 steps with status: success Which probably means the scan was "stopped" before it finished, not "aborted", because the scan should have had 6 steps
- PMPS just crashed
- settings for fzp spectrometer. Device: Position: 0 Intensifier MCP [V] 450 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 0.0 4 solid_att TARGET1 5 solid_a...
- Gas needle position during the shift. Taking it to out position for safety after posting this elog.

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Argon sample measurement with 100V retardation to remove Ar 2s (74 eV) electrons, despite technical issues with PMPS crashes

### Run 19
**Duration**: 1.6 minutes (medium, 72nd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Timed run with 5000 events Scan exited after 7 steps with status: abort
- Scan sim_fast_setpoint: [-1. 0. 1.] 2000 events/step Scan exited after 6 steps with status: success
- test of scanning with daq.

**Run classification**: diagnostic_run
**Confidence**: high
**Key evidence**: Test of scanning with DAQ, using sim_fast_setpoint to verify system operation

### Run 20
**Duration**: 19.8 seconds (very short, 3rd percentile)
**Total entries**: 24 (23 unique)
**Activities**:
- Scan sim_fast_setpoint: [-1. 0. 1.] 2000 events/step Scan exited after 6 steps with status: success
- test of scanning with daq.
- Scan sim_fast_setpoint: [-1. 0. 1.] Scan sim_slow_setpoint: [-2. 0. 2.] 2000 events/step Scan exited after 6 steps with status: success
- set to 400 uJ for 12 hours
- we have 8 kHz of 400 eV at ~300 uJ. looks really nice and stable. we are dropping down to 100 Hz for alignment
- beam on IM2K0. 100 Hz, 300 uJ, 400 eV. 20% transmission. moving on
- beam on im2k4. looks off but we will take it to im5k4 and point there
- beam on im3k4. moving on
- beam on YAG2 at im5k4. we are going to point
- beam on YAG2 at im5k4 after pointing +300 um in x. we are calling this good
- Photon energy PV is setup around 400 eV. Increased transmission to 100% and th rep rate to 8.3 kHz for check_kbo1_transmission script
- TMO_KBO1 transmission: 0.6044356924403762. scan data path: /reg/g/pcds/pyps/apps/hutch-python/tmo/tmo/mirror-check/scans/TMO_KBO1/TMO_KBO1_2024-10-20--07-29-31.h5
- TMO_KBO1 transmission: 0.8904281420616483. scan data path: /reg/g/pcds/pyps/apps/hutch-python/tmo/tmo/mirror-check/scans/TMO_KBO1/TMO_KBO1_2024-10-20--07-34-11.h5
- Completed the beamline transmission scan. It was tripping the gauges near valve ST3K4 and MR2K4 and MR3K4.
- Beam down due to BCS fault.
- The pressure in the KB increases when the beam is on. At high power the outgassing cause the valves to trip in.
- The Sample Paddle X motion is having some issues. Without bringing it to the usual place, we won't be able to verify the position of X-ray at the interaction point.
- Beam on LI3K4 with the sample paddle moved in. We are setting this as a reference.
- Sample paddle position while looking at the LI3K4. We are looking at the frosted YAG.
- Using runs 5 to 17 to inspect MCP bias and max output value across 10,000 events for raw waveform (searched through 10,000 but actually ~every 8th since raw). In these runs, mcp bias scanned from 1200...
- Image didn't attach properly for previous entry on mcp calibration
- We are about to do XY scan. SQ1 position before moving.
- Valves MR2K4 and ST3K4 keep tripping closed. Dependent on beam power.

**Run classification**: commissioning_run
**Confidence**: high
**Key evidence**: Extensive beamline setup activities including transmission checks, beam pointing, KB mirror setup, and valve troubleshooting

### Run 21
**Duration**: 1.5 minutes (medium, 71st percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- run 21 is a baseline scan, 50% transmission, 400 eV, 2.35e-7 Ar
- HV settings for the XY scan. We are using a uniform MCP bias voltage of 1450 across all the detectors based on the previous datasets for gain and measurements of HSD overflow. Channel: State: Voltage ...

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Baseline scan with specified experimental parameters: 50% transmission, 400 eV, 2.35e-7 Ar sample, with optimized HV settings for data collection

### Run 22
**Duration**: 1.5 minutes (medium, 70th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Moved Y by +1 mm.
- Timed run with 492000 events Scan exited after 6 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Part of XY scan series, with Y position moved by +1 mm from starting position

### Run 23
**Duration**: 9.2 seconds (very short, 1st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Moved Y by +2 mm from start.

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Continuation of XY scan series, with Y moved by +2 mm from start position

### Run 24
**Duration**: 1.3 minutes (medium, 69th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success

**Run classification**: alignment_run
**Confidence**: medium
**Key evidence**: Part of XY scan sequence based on context from surrounding runs, though specific position not mentioned

### Run 25
**Duration**: 1.2 minutes (medium, 66th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 position at (0,0).
- Timed run with 492000 events Scan exited after 6 steps with status: success
- HV settings for the XY scan. We are using a uniform MCP bias voltage of 1400 across all the detectors based on the previous datasets for gain and measurements of HSD overflow. Channel: State: Voltage ...

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: XY scan with SQ1 position explicitly at (0,0) reference position, with MCP bias voltage adjusted to 1400V

### Run 26
**Duration**: 1.2 minutes (medium, 66th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 position at (0,5). Y is moved to +5 mm.
- Timed run with 492000 events Scan exited after 6 steps with status: success
- Look at fgrom run 25 onwards for XY scan. The previous runs 22 to 24 had higher transmission.

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: XY scan with SQ1 position at (0,5) with Y moved to +5 mm, explicitly noted as part of XY scan series

### Run 27
**Duration**: 1.2 minutes (medium, 63rd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 position at (0, -5). Y is moved to -5 mm.
- Timed run with 492000 events Scan exited after 6 steps with status: success
- We are doing the XY scan at 5% transmission.

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: XY scan with SQ1 position at (0,-5) with Y moved to -5 mm, explicitly noted as part of XY scan at 5% transmission

### Run 28
**Duration**: 1.2 minutes (medium, 63rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 position at (5, 0). X is moved to +5 mm.
- Timed run with 492000 events Scan exited after 6 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: XY scan with SQ1 position at (5,0) with X moved to +5 mm, continuing the systematic spatial alignment series

### Run 29
**Duration**: 1.2 minutes (medium, 64th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- recording while discussing. This is the nominal 0 position of MRCO.

**Run classification**: alignment_run
**Confidence**: medium
**Key evidence**: Part of alignment sequence, noting 'nominal 0 position of MRCO' which indicates spatial positioning reference

### Run 30
**Duration**: 1.2 minutes (medium, 63rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success

**Run classification**: alignment_run
**Confidence**: medium
**Key evidence**: Final run in XY scan sequence with consistent duration and step pattern to previous alignment runs

### Run 31
**Duration**: 2.2 minutes (long, 80th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Recording while discussing. Nominal 0 for SQ1
- Timed run with 984000 events Scan exited after 12 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Recording at 'Nominal 0 for SQ1' position, continuing the XY scan sequence from previous runs with consistent step pattern

### Run 32
**Duration**: 1.2 minutes (medium, 65th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- run 32 is recording with updated gain for ToFs 170 & 90 (see post above)
- Timed run with 492000 events Scan exited after 6 steps with status: success
- HV settings for the TOFs, with 270 and 90 TOFs at 1500 and 1450 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2100.0 2099.933800 False MPOD:01:M5:C0 1 Port...
- HV settings for the run 33 Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2100.0 2099.934800 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0 -0.121031 False MPOD...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Updated gain settings for ToFs 170 & 90, with specific HV settings (1500V and 1450V) for detector optimization

### Run 33
**Duration**: 1.2 minutes (medium, 64th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- We changed the bias voltage of port 90, 270 and 337 to 1500, 1450, 1425 V respectively based on estimation. Onwards to do retardation scan..

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Changed bias voltage of ports 90, 270 and 337 to specific values (1500V, 1450V, 1425V) in preparation for retardation scan

### Run 34
**Duration**: 1.2 minutes (medium, 62nd percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- run 34 is retardation scan at 150 V
- Timed run with 492000 events Scan exited after 6 steps with status: success
- HV settings for the run 34. Retardation scan at -150 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1950.000 1950.009400 False MPOD:01:M5:C0 1 Port_0_Back_M...
- HV settings for the run 35. Retardation at -175 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1925.000 1924.970800 False MPOD:01:M5:C0 1 Port_0_Back_Mesh O...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Explicitly noted as 'retardation scan at 150 V' with detailed HV settings for detector calibration

### Run 35
**Duration**: 1.2 minutes (medium, 64th percentile)
**Total entries**: 4 (3 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- For all the retardation scan we are using Argon. The chamber pressure is ~1.8E-7 Torr.
- HV settings for the run 36. Retardation at -190 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1910.0000 1909.926600 False MPOD:01:M5:C0 1 Port_0_Back_Mesh ...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of retardation scan series at -175V with Argon gas at ~1.8E-7 Torr chamber pressure

### Run 36
**Duration**: 1.2 minutes (medium, 67th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success

**Run classification**: calibration_run
**Confidence**: medium
**Key evidence**: Part of retardation scan sequence at -190V based on context from runs 34-35 and 37

### Run 37
**Duration**: 1.2 minutes (medium, 66th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Doing the retardation scan with Retardation of -190 V. There is a confusion in the run table. We are taking this data again. Compare with run 36. Same HV settings.
- Timed run with 492000 events Scan exited after 6 steps with status: success
- HV settings for the run 38. Retardation at -195 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1905.0000 1905.030400 False MPOD:01:M5:C0 1 Port_0_Back_Mesh ...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Explicitly noted as 'retardation scan with Retardation of -190 V' to repeat run 36 with same HV settings

### Run 38
**Duration**: 1.2 minutes (medium, 65th percentile)
**Total entries**: 4 (3 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- HV settings for the run 39. Retardation at -190 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1720.0000 1719.983300 False MPOD:01:M5:C0 1 Port_0_Back_Mesh ...
- HV settings for the run 39. Retardation at -380 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1720.0000 1719.983300 False MPOD:01:M5:C0 1 Port_0_Back_Mesh ...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of retardation scan series at -195V with detailed HV settings for next run

### Run 39
**Duration**: 1.2 minutes (medium, 65th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Part of retardation scan sequence at -380V based on HV settings noted in run 38

### Run 40
**Duration**: 1.2 minutes (medium, 64th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- HV settings for the run 40. Retardation at -300 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2050.000 2050.005600 False MPOD:01:M5:C0 1 Port_0_Back_Mesh O...
- HV settings for the run 41. Retardation at -50 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2050.000 2050.002700 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Retardation scan at -300V with detailed HV settings, continuing systematic voltage scan series

### Run 41
**Duration**: 1.2 minutes (medium, 62nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- HV settings for the run 42. Retardation at -100 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2000.000 1999.927400 False MPOD:01:M5:C0 1 Port_0_Back_Mesh O...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Part of retardation scan sequence at -50V as indicated in run 40, with HV settings for next run at -100V showing systematic voltage scanning

### Run 42
**Duration**: 1.2 minutes (medium, 63rd percentile)
**Total entries**: 6 (6 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success
- now we are setting up the FZP to do the retardation scans
- we are at 2% transmission, XGMD showing ~9 uJ
- settings for fzp spectrometer today. Device: Position: 0 Intensifier MCP [V] 450 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 500.0 4 solid_att TARGET1 5...
- gate was unchecked and we didn't see the spectrum for a while :)
- Intensifier setting are not correct in this post. Check the screen grab in the adjacent post. Device: Position: 0 Intensifier MCP [V] 450 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.9...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of retardation scan series with FZP spectrometer setup, intensifier settings, and detailed configuration for spectral measurements

### Run 43
**Duration**: 2.8 minutes (long, 83rd percentile)
**Status**: No logbook entries

**Run classification**: calibration_run
**Confidence**: medium
**Key evidence**: No logbook entries but follows pattern of calibration runs (41-42) and precedes photon energy scan in run 44

### Run 44
**Duration**: 1.5 minutes (medium, 72nd percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- We changed the retardation to 130 V to space out the photolines and Auger better. We are doing the scan using Argon as sample at the photon energy range of 390 eV to 410 eV at a 2.5 eV step.
- HV settings for the TOFs for the photon energy scan at run 44. Retardation is 130 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1970.0000 1970.009600 False...
- photn energy scan in Ar. 400 +- 10 eV
- Scan hf_w: [390. 392.5 395. 397.5 400. 402.5 405. 407.5 410. ] 32800 events/step Scan exited after 18 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Explicit photon energy scan in Argon (390-410 eV) with retardation voltage of 130V to 'space out the photolines and Auger better'

### Run 45
**Duration**: 1.6 minutes (medium, 72nd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- repeate run 44
- Scan hf_w: [390. 392.5 395. 397.5 400. 402.5 405. 407.5 410. ] 32800 events/step Scan exited after 18 steps with status: success
- entered hutch to pump out sample. plan is to record a background spectrum

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Explicitly noted as 'repeate run 44' with identical photon energy scan parameters (390-410 eV)

### Run 46
**Duration**: 2.1 minutes (medium, 74th percentile)
**Total entries**: 13 (13 unique)
**Activities**:
- photon energy scan of residual gas
- HV settings for the run 46. Retardation at 0 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2100.0 2100.029800 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On 0.0...
- Scan hf_w: [390. 392.5 395. 397.5 400. 402.5 405. 407.5 410. ] 32800 events/step Scan exited after 18 steps with status: success Average Duty Cycle: 0.946
- ### ################ adding we accessed the hutch right now and we use remote desktop so that the voltage on intensifer is not right; voltage should be 750 V; ######################################## ...
- ### ################ adding we use remote desktop so that the voltage on intensifer is not right; voltage should be 750 V; ######################################## settings for fzp spectrometer today ...
- settings for fzp spectrometer today (400eV and target 1 on ATT with pulse energy XGMD ~10 uJ, 8.29 kHz). Device: Position: 0 Intensifier MCP [V] 450 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Dela...
- sdjuat x_post for FEX to 8 for Ryan
- adjust ymax for FEX
- adjust ymin lower this is a positive going signal.
- We are redoing the SQ1 scan to figure out the non-uniformity in the Auger yield. This is the first of the series of runs. We are at (0,0)
- We are redoing the SQ1 scan to figure out the non-uniformity in the Auger yield. This is the first of the series of runs. We are at (0,0) in run 48.
- We are redoing the SQ1 scan to figure out the non-uniformity in the Auger yield. This is the first of the series of runs. We are at (0,0) in run 48. We moved back to Argon after discussion regarding t...
- We are redoing the SQ1 scan to figure out the non-uniformity in the Auger yield. This is the first of the series of runs. We are at (0,0) in run 49.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan of residual gas with retardation at 0V, continuing calibration sequence with FZP spectrometer settings

### Run 47
**Duration**: 9.3 seconds (very short, 1st percentile)
**Status**: No logbook entries

**Run classification**: diagnostic_run
**Confidence**: medium
**Key evidence**: Very short run (9.3 seconds) following calibration sequence, likely a quick system check before starting SQ1 scan series

### Run 48
**Duration**: 42.8 seconds (short, 47th percentile)
**Status**: No logbook entries

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: First run in SQ1 scan series at position (0,0) as mentioned in run 46 logbook entries to 'figure out the non-uniformity in the Auger yield'

### Run 49
**Duration**: 42.5 seconds (short, 46th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ is at (0, 5)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Continuation of SQ1 scan with position explicitly noted as '(0, 5)' as part of spatial scanning sequence

### Run 50
**Duration**: 38.4 seconds (short, 27th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (0, -5).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Continuation of SQ1 scan with position explicitly noted as '(0, -5)' showing systematic spatial scanning pattern

### Run 51
**Duration**: 40.5 seconds (short, 42nd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (-5, 0)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (-5, 0) continuing the systematic spatial scanning pattern started in runs 48-50

### Run 52
**Duration**: 41.1 seconds (short, 43rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 was at (5, 0)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (5, 0) as part of the systematic spatial grid scan sequence

### Run 53
**Duration**: 43.6 seconds (short, 48th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- SQ1 is at (-2, 0).
- SQ1 is at (2, 0).
- SQ1 is at (-2, 2).
- SQ1 is at (-2,-2).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Multiple SQ1 position scans at (-2, 0), (2, 0), (-2, 2), (-2,-2) continuing the spatial mapping sequence

### Run 54
**Duration**: 40.6 seconds (short, 43rd percentile)
**Status**: No logbook entries

**Run classification**: alignment_run
**Confidence**: medium
**Key evidence**: Short run with similar duration to other SQ1 scan runs, likely continuing the spatial mapping sequence

### Run 55
**Duration**: 42.0 seconds (short, 44th percentile)
**Status**: No logbook entries

**Run classification**: alignment_run
**Confidence**: medium
**Key evidence**: Short run with similar duration to other SQ1 scan runs, continuing the systematic spatial scanning pattern

### Run 56
**Duration**: 46.1 seconds (medium, 51st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ is at (2, 0)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (2, 0) continuing the systematic spatial grid mapping sequence

### Run 57
**Duration**: 43.4 seconds (short, 47th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (2,2).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (2,2) as part of the ongoing spatial mapping grid sequence

### Run 58
**Duration**: 56.3 seconds (medium, 55th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (2,-2)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (2,-2) continuing the systematic spatial grid mapping sequence

### Run 59
**Duration**: 41.9 seconds (short, 44th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Sq1 is at (0,-2)
- Sq1 is at (0,2)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scans at (0,-2) and (0,2) continuing the systematic spatial mapping sequence

### Run 60
**Duration**: 56.1 seconds (medium, 55th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is (0, 2).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (0, 2) completing the systematic spatial grid mapping sequence

### Run 61
**Duration**: 42.5 seconds (short, 46th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (1, 2)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (1, 2) continuing the systematic spatial grid mapping sequence from previous runs

### Run 62
**Duration**: 41.4 seconds (short, 44th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (1, 0).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (1, 0) as part of the ongoing spatial mapping grid sequence

### Run 63
**Duration**: 42.2 seconds (short, 45th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (1, -2)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (1, -2) continuing the systematic spatial grid mapping sequence

### Run 64
**Duration**: 42.7 seconds (short, 46th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (1, -1).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (1, -1) as part of the systematic spatial mapping grid sequence

### Run 65
**Duration**: 44.8 seconds (medium, 50th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (1,1).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (1,1) continuing the systematic spatial grid mapping sequence

### Run 66
**Duration**: 48.9 seconds (medium, 54th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (0,1).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (0,1) as part of the ongoing spatial mapping grid sequence

### Run 67
**Duration**: 45.7 seconds (medium, 51st percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- SQ is at (0,-1).
- SQ is at (0,1).
- SQ is at (0.5, 0.5)
- SQ is at (0.5, 0.5). Run 68

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Multiple SQ position scans at (0,-1), (0,1), and (0.5, 0.5) continuing the spatial mapping sequence with finer grid points

### Run 68
**Duration**: 48.0 seconds (medium, 52nd percentile)
**Status**: No logbook entries

**Run classification**: alignment_run
**Confidence**: medium
**Key evidence**: No logbook entries, but follows pattern of spatial mapping sequence and has similar duration to other alignment runs

### Run 69
**Duration**: 44.5 seconds (short, 49th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (0.5, 1).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (0.5, 1) continuing the finer-resolution spatial mapping grid sequence

### Run 70
**Duration**: 42.4 seconds (short, 45th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (0.5, 0).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (0.5, 0) completing the systematic spatial grid mapping sequence with half-unit grid points

### Run 71
**Duration**: 42.5 seconds (short, 45th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (0.5, -0.5)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (0.5, -0.5) continuing the systematic spatial grid mapping sequence

### Run 72
**Duration**: 48.3 seconds (medium, 53rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (0.5, -1)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (0.5, -1) as part of the ongoing spatial mapping grid sequence

### Run 73
**Duration**: 48.8 seconds (medium, 53rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (1, -0.5)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (1, -0.5) continuing the systematic spatial grid mapping with half-unit increments

### Run 74
**Duration**: 46.7 seconds (medium, 52nd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (1, 0.5)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (1, 0.5) as part of the ongoing spatial mapping grid sequence

### Run 75
**Duration**: 46.4 seconds (medium, 51st percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- SQ1 is at (0, 0.5)
- Need to tune fex carefully, missed this light peak (maybe it's light peak)
- Funny, np.histogram() seems a little faster actually, but has these weird edge errors that the integer math doesn't have.
- IR beam on frosted YAG. The cross-hair is where the beamline alignment laser was located. The position of the sample paddle is also noted.
- Timing of the DAQ before changing it to the event code for 8 kHz IR.

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (0, 0.5) with IR beam alignment on frosted YAG and timing adjustments for alignment purposes

### Run 76
**Duration**: 43.7 seconds (short, 48th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (0, -0.5)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (0, -0.5) continuing the systematic spatial grid mapping sequence

### Run 77
**Duration**: 42.7 seconds (short, 46th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (1,-1). We are redoing it as a sanity check.

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (1,-1) explicitly noted as 'redoing it as a sanity check' for alignment verification

### Run 78
**Duration**: 46.9 seconds (medium, 52nd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (1.5, -1)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (1.5, -1) extending the spatial mapping grid sequence to new coordinates

### Run 79
**Duration**: 45.4 seconds (medium, 50th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (1.5, -1.5)
- SQ1 is at (1, -1.5).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scans at (1.5, -1.5) and (1, -1.5) completing the extended spatial mapping grid

### Run 80
**Duration**: 42.5 seconds (short, 45th percentile)
**Status**: No logbook entries

**Run classification**: alignment_run
**Confidence**: medium
**Key evidence**: No logbook entries, but follows pattern of spatial mapping sequence and has similar duration to other alignment runs in this sequence

### Run 81
**Duration**: 44.9 seconds (medium, 50th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ1 is at (0.5, -1.5)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 position scan at (0.5, -1.5) continuing the systematic spatial grid mapping sequence from previous runs

### Run 82
**Duration**: 45.7 seconds (medium, 51st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- SQ is at (1.5, -0.5)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ position scan at (1.5, -0.5) continuing the systematic spatial mapping grid sequence

### Run 83
**Duration**: 44.3 seconds (short, 49th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (1, -1). We are done with the scan. This is potentially close to where we need to be.
- HV settings for the SQ1 XY scan from run 48 to 83. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2100.0 2100.023400 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On ...

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Final SQ1 position scan at (1, -1) with note 'We are done with the scan. This is potentially close to where we need to be' indicating completion of alignment sequence

### Run 84
**Duration**: 42.8 seconds (short, 47th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Changed the bias voltage of port 270 to 1575. Same SQ1 position. We want to see if increasing the bias voltage changes the yield.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Changed bias voltage to 1575V at same SQ1 position to test if 'increasing the bias voltage changes the yield' - clear detector calibration activity

### Run 85
**Duration**: 44.3 seconds (short, 49th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Changed the bias voltage of port 270 to 1600 V.
- We are doing retardation scan from now on. Sample is Argon.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Changed bias voltage to 1600V and explicitly states 'We are doing retardation scan from now on. Sample is Argon' indicating start of retardation scan sequence

### Run 86
**Duration**: 1.3 minutes (medium, 69th percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- Retardation is -195 V.
- HV settings for run 86. Retardation -195 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1905.0000 1905.034300 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On -195...
- Auger features from Run 86
- fix the problem, the trigger width changed to 1000 ns. it was 10,000 ns; it was running ok in the pass
- fix the problem, the trigger width is 1000 ns NOT 10,000 ns; somehow one additional 0 was keyed in.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Retardation voltage set to -195V with HV settings documented, part of systematic retardation scan sequence with Argon sample

### Run 87
**Duration**: 1.1 minutes (medium, 58th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Retardation -175 V.
- HV settings for run 87. Retardation -175 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1925.000 1924.970600 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On -175....
- temperature rise with ~10uJ at 8.29 kHz on ATT; 0.4 deg per hr

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Retardation voltage changed to -175V, continuing the systematic retardation scan sequence

### Run 88
**Duration**: 1.2 minutes (medium, 68th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Retardation is -150 V.
- HV settings for run 87. Retardation -150 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1950.000 1950.007600 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On -150....
- HV settings for run 88. Retardation -150 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1950.000 1950.007600 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On -150....

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Retardation voltage changed to -150V, continuing the systematic retardation scan sequence

### Run 89
**Duration**: 1.2 minutes (medium, 68th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation is -100 V
- HV settings for run 89. Retardation -100 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2000.000 2000.044400 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On -100....

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Retardation voltage changed to -100V, continuing the systematic retardation scan sequence

### Run 90
**Duration**: 1.2 minutes (medium, 67th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Retardation is at -50 V.
- HV settings for run 90. Retardation -50 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2050.000 2050.010700 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On -50.00...
- Timed run with 492000 events Scan exited after 6 steps with status: success Average Duty Cycle: 0.978

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Retardation voltage changed to -50V, completing the systematic retardation scan sequence with timed run of 492000 events

### Run 91
**Duration**: 4.4 minutes (very long, 97th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Retardation is -300 V.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Retardation voltage set to -300V, continuing the systematic retardation scan sequence from previous runs

### Run 92
**Duration**: 1.2 minutes (medium, 67th percentile)
**Total entries**: 6 (6 unique)
**Activities**:
- Timed run with 492000 events Scan exited after 6 steps with status: success Average Duty Cycle: 0.972
- HV settings for run 91. Retardation -300 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1800.000 1799.957900 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On -300....
- HV settings for run 91. Retardation 0 V. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 1800.000 1799.957900 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On -300.000...
- changing back to 64 points in xpost in FEX. Using 8 pre and post was useful to use the FEX as a quick hitfinder.
- Using 8 before and 8 after to isolate to one hit in a fex window, allowing it be used as a peak finder as opposed to before where 64 samples after captured multiple hits.
- temperature start from 1 pm on 10/20/2024; 3 deg over 5 hr times; ~0.6 deg per hr

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: HV settings for retardation, FEX configuration changes for peak finding, part of the ongoing retardation scan sequence

### Run 93
**Duration**: 2.2 minutes (long, 80th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 984000 events Scan exited after 12 steps with status: success Average Duty Cycle: 0.977
- We changed the retardation to an interleaved settings. Port [ 0, 2, 4, 6, 8, 10, 12, 14] is at 150 V retardation and Port [1, 3, 5, 7, 9, 11, 13, 15] is at 100 V retardation.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Interleaved retardation settings (150V and 100V) across different ports, systematic voltage testing

### Run 94
**Duration**: 1.3 minutes (medium, 70th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Timed run with 984000 events Scan exited after 6 steps with status: success Which probably means the scan was "stopped" before it finished, not "aborted", because the scan should have had 12 steps Ave...

**Run classification**: calibration_run
**Confidence**: medium
**Key evidence**: Timed run with 984000 events, appears to be continuation of retardation scan sequence but was stopped early

### Run 95
**Duration**: 2.2 minutes (long, 80th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Doing a retardation scan from 100 to 150 at a quadrature. [100.0, 112.5, 125.0, 137.5, 150.0, 137.5, 125.0, 112.5, 100.0, 112.5, 125.0, 137.5, 150.0, 137.5, 125.0, 112.5]

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Explicit retardation scan from 100V to 150V in quadrature pattern with specific voltage steps

### Run 96
**Duration**: 54.6 seconds (medium, 55th percentile)
**Status**: No logbook entries

**Run classification**: calibration_run
**Confidence**: medium
**Key evidence**: No entries but short duration and positioned between other calibration runs in the retardation scan sequence

### Run 97
**Duration**: 5.8 minutes (very long, 98th percentile)
**Total entries**: 9 (9 unique)
**Activities**:
- 10-20% tranmsmission of the pulse energy, reduced intensifier gain to 650 V (from 750V);
- We are using the same retardation settings as of run 96.
- HV settings for run 97. Retardation variable. Channel: State: Voltage Set (V): Voltage Measure (V): isTrip: Supply: 0 Port_0_Anode On 2000.0000 2000.042100 False MPOD:01:M5:C0 1 Port_0_Back_Mesh On -1...
- any damage?
- settings for fzp spectrometer today (400eV and target 1 on ATT with pulse energy XGMD ~10 uJ, 8.29 kHz). Device: Position: 0 Intensifier MCP [V] 450 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Dela...
- SQ1 at the end of the shift 2. We found that this is the best SQ1 positions.
- Needle positions at the end of the run. This is where we took our runs in shift 2. We will take the needle in its parking position.
- Moved Ryan's git repo out of private and into lcls-users/ under tmo-prefex.git "Preanalysis and Feature Extraction" repo. git@github.com:lcls-users/tmo-prefex.git
- pdf for mcp bias characterization. each page is for a separate detector. for each detector showing a histogram for each mcp bias setting (runs 5-17). i scanned through all the fex windows and took the...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Variable retardation settings, FZP spectrometer configuration at 400eV, MCP bias characterization

### Run 98
**Duration**: 26.9 seconds (very short, 5th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 20000 events Scan exited after 10 steps with status: success Average Duty Cycle: 0.867
- test of scanning with daq. No data.

**Run classification**: diagnostic_run
**Confidence**: high
**Key evidence**: Test of scanning with DAQ explicitly noted with 'No data' comment, very short duration

### Run 99
**Duration**: 26.9 seconds (very short, 4th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 20000 events Scan exited after 10 steps with status: success Average Duty Cycle: 0.862
- test of scanning with daq. No data.

**Run classification**: diagnostic_run
**Confidence**: high
**Key evidence**: Test of scanning with DAQ explicitly noted with 'No data' comment, very short duration

### Run 100
**Duration**: 26.7 seconds (very short, 4th percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- Timed run with 20000 events Scan exited after 10 steps with status: success Average Duty Cycle: 0.872
- test of scanning with daq. No data.
- Motor for sample paddle with laser spot at the cursor of X-ray position in MRCO_GIGE_02
- Needle position for the start of the laser shift
- This is the starting configuration of the VAT valve for the laser shift

**Run classification**: alignment_run
**Confidence**: medium
**Key evidence**: Motor positioning for sample paddle, needle position setup, and VAT valve configuration for laser shift

### Run 101
**Duration**: 2.2 minutes (long, 80th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Run for magnetic shielding studying of low energy argon electron. WP1 = 65. All nose to 0, except port 22. Acceleration is 45 (backmesh). MCP diff = 1400 across all.
- Run for magnetic shielding studying of low energy argon electron. WP1 = 65. All nose to 0. Acceleration is 45 (backmesh). MCP diff = 1400 across all.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Magnetic shielding study with specific voltage settings for low energy argon electron measurements, testing different WP1 settings

### Run 102
**Duration**: 2.2 minutes (long, 79th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Changed the WP1 = 90. Same settings as run 101.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of magnetic shielding study with changed WP1 setting to 90, same other settings as run 101

### Run 103
**Duration**: 1.1 minutes (medium, 58th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- All nose = 0. Acceleration = 45. Same MCP settings as run 102. WP1 = 90.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continued magnetic shielding calibration with same settings as run 102, maintaining WP1 = 90

### Run 104
**Duration**: 8.3 seconds (very short, 1st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Junk

**Run classification**: unknown_run
**Confidence**: high
**Key evidence**: Explicitly labeled as 'Junk' with very short duration (8.3 seconds)

### Run 105
**Duration**: 50.0 seconds (medium, 54th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Changed the polarization. WP1 = 45. All Nose at 0. Att_wp = 40. Same voltage settings as run 101.
- We added some mu-metal shield around the gauges. It is not the most elegant shielding, but it is something that we could given the space constraints in the area of the gauge tree.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Changed polarization (WP1 = 45) and added mu-metal shielding around gauges for magnetic shielding study

### Run 106
**Duration**: 1.9 minutes (medium, 74th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Mu-metal shield around gauge. All nose = 0. WP1 = 45. Att_WP = 40.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of mu-metal shielding calibration with WP1 = 45 and Att_WP = 40

### Run 107
**Duration**: 1.8 minutes (medium, 73rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Mu-metal shielding. All nose = 0. WP1 = 90, Att_WP = 40. Compare with 106. And 103, 104 for before shielding.
- WP1 = 90 means horizontal polarization, and 45 is vertical polarization.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Mu-metal shielding test with WP1 = 90 (horizontal polarization), explicitly compared with previous runs

### Run 108
**Duration**: 2.4 minutes (long, 81st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- We added port 0 and 315 Nose to the HV supply instead of ground plug.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Modified HV configuration by adding port 0 and 315 Nose to HV supply instead of ground plug

### Run 109
**Duration**: 1.5 minutes (medium, 72nd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- We added all the nose to power supply and applied 0 volt. This data needs to be compared with runs 107 and 108. Horizontal polarization. Same voltage as runs 107 and 108.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Added all nose connections to power supply with 0V, continuing magnetic shielding calibration with horizontal polarization

### Run 110
**Duration**: 1.5 minutes (medium, 71st percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Compare with run 109. Same settings with all nose at HV supply with 0 volt applied to them. Circular polarization. Same laser power as run 109.
- making sure 67 and 225 correspond with their HSDs by unplugging their amplifers.
- Putting the sample paddle in the position where we saw the 800 nm beam. The cursor is with beamline HeNe.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Same HV settings as run 109 but with circular polarization, testing detector response with different polarization settings

### Run 111
**Duration**: 3.1 minutes (long, 84th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Retaking data with laser after removing the gauge tree from the LI2K4. Laser WP settings = 38, Polarization is circular. Voltage is: Back mesh = 45, MCP front = 300, MCP diff = 1400 across all the TOF...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Retaking data with laser after removing gauge tree, testing circular polarization with specific voltage settings for TOF detectors

### Run 112
**Duration**: 2.7 minutes (long, 83rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Changed the polarization to horizontal. Laser WP = 38. Voltage settings at the same as run 111. Compare with previous runs from 101.
- Quick spectrum with tvalid = [int(v)>>1 for v in tofs if v<(1<<14)] h=np.zeros((1<<int(np.log2(np.max(tvalid)))+1)) for v in tvalid: h[v] += 1 plt.plot(h);plt.show()

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Changed polarization to horizontal, same voltage settings as run 111, explicitly comparing with previous runs from 101

### Run 113
**Duration**: 2.1 minutes (medium, 74th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- We are doing a IR only based excitation of Xenon at 1.3 um from OPA. Polarization is vertical and linear. The acceleration is 45 V at the back mesh for all TOF.

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: IR-only based excitation of Xenon at 1.3 um from OPA with vertical linear polarization, collecting scientific data

### Run 114
**Duration**: 1.2 minutes (medium, 68th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Background with 1.3 um (some small amount Xenon maybe present). Compare with run 113. Same voltage settings as 113.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Background measurement with 1.3 um for comparison with run 113, same voltage settings

### Run 115
**Duration**: 1.0 minutes (medium, 57th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Turned on Xenon back. IR only, 45 V acceleration. Same voltage settings as run 113 and 114. Compare with run 113 where the chamber pressure was 3.3E-7 compared to ~5E-7 for this run.
- We are doing a quarter waveplate scan of IR at 1.3 um.

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Xenon target with IR excitation at 1.3 um, comparing with different chamber pressures, beginning quarter waveplate scan

### Run 116
**Duration**: 18.1 minutes (very long, 99th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Quarter waveplate scan from 38 to 90 deg with all TOFs at 45 V acceleration.
- For the previous runs, the nominal quater waveplate setting is 41 deg for vertical and 86 deg for circular.
- Scan tmo_laser_pol_wp: [38. 39. 40. 41. 42. 43. 44. 45. 46. 47. 48. 49. 50. 51. 52. 53. 54. 55. 56. 57. 58. 59. 60. 61. 62. 63. 64. 65. 66. 67. 68. 69. 70. 71. 72. 73. 74. 75. 76. 77. 78. 79. 80. 81. ...

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Systematic quarter waveplate scan from 38 to 90 degrees with Xenon target, collecting polarization-dependent data

### Run 117
**Duration**: 3.4 minutes (long, 89th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- WE change the polarization to linear and rotating to align the ionization direction with the TOF angles. Changing lm1k4_ejx_mp1_wp2 from -45 to 45 at 11.25 step. With 98 deg as vertical and 53 as hori...
- Scan tmo_laser_pol_wp_2: [ 8. 19.25 30.5 41.75 53. 64.25 75.5 86.75 98. ] 80000 events/step Scan exited after 18 steps with status: success
- We stopped the run due to RP search of the hutch. Will redo the scan to complete the data points.

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Linear polarization scan to align ionization direction with TOF angles, systematic data collection with Xenon target

### Run 118
**Duration**: 3.6 minutes (long, 89th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Redoing the run for the linear polarization scan that was initiated in run 117. Same voltage settings with 45 V acceleration at the backmesh. Xenon as target.
- Scan tmo_laser_pol_wp_2: [ 8. 19.25 30.5 41.75 53. 64.25 75.5 86.75 98. ] 80000 events/step Scan exited after 18 steps with status: success
- Needle position for IR only work.
- Position of the SMA tip at the IP

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Continuation of linear polarization scan from run 117 with Xenon target, systematic data collection with controlled parameters

### Run 119
**Duration**: 2.6 minutes (long, 83rd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Scan tmo_laser_pol_wp_2: [-37. -25.75 -14.5 -3.25 8. 19.25 30.5 41.75 53. 64.25 75.5 86.75 98. 109.25 120.5 131.75 143. ] 80000 events/step Scan exited after 13 steps with status: success Which probab...
- We are scanning the half waveplate from -90 to 90 at 11.25 deg step. Compare with 118. Same voltage settings.
- Run aborted.

**Run classification**: measurement_run
**Confidence**: medium
**Key evidence**: Half waveplate scan from -90 to 90 degrees with Xenon target, though run was aborted

### Run 120
**Duration**: 6.5 minutes (very long, 98th percentile)
**Total entries**: 22 (22 unique)
**Activities**:
- Half waveplate scan. Redoing run 119. Compare with run 118. Scanning from -90 to 90 deg at 11.25 deg step.Scan range is from [-37. -25.75 -14.5 -3.25 8. 19.25 30.5 41.75 53. 64.25 75.5 86.75 98. 109.2...
- Scan tmo_laser_pol_wp_2: [-37. -25.75 -14.5 -3.25 8. 19.25 30.5 41.75 53. 64.25 75.5 86.75 98. 109.25 120.5 131.75 143. ] 80000 events/step Scan exited after 34 steps with status: success
- fzp intensifier ioc is working; need to set daq timing_0 at 10 kHz for testing (no X-ray)
- tpr timing trigger is still 94,000 ns
- Start of shift 3 for mrco commissioning (30-Oct-2024) bring beam to IM5K4 *check transmission * sample paddle tip * signal of SMA tip Setup energy scan PV Setup FZP for 400 eV Ramp up MRCO detectors a...
- Start of shift: ACR is seeing some faults related to arbiter, but not being seen on the TMO side...
- Beam on IM2K0. Unpointed.
- The slits position at the beginning of the shift. We need to reduce the gap of SL2K0.
- im2k4: unpointed
- im2k4 (this time not overexposed)
- im3k4 unpointed
- im5k4: unpointed
- im5k4 aligned: moved only in X = +300 um y = -100 um
- im2k4 after pointing before adjusting the slits
- Beam position after moving the SL2K0 to have the beam centered.
- TMO_KBO1 transmission: 0.7484554262933377. scan data path: /reg/g/pcds/pyps/apps/hutch-python/tmo/tmo/mirror-check/scans/TMO_KBO1/TMO_KBO1_2024-10-30--20-15-56.h5
- Doing a kb1 transmission scan. The mirror IM1K2 is asking a 5% MAP in beam class 8 mode. But, this hasn't stopped us from the kb1 transmission.
- TMO_KBO1 transmission: 0.7173744550240562. scan data path: /reg/g/pcds/pyps/apps/hutch-python/tmo/tmo/mirror-check/scans/TMO_KBO1/TMO_KBO1_2024-10-30--20-21-37.h5
- Beam on the sample paddle Clear YAG. The cursor is where the X-ray is
- Sample paddle position of the SMA tip.
- settings for fzp spectrometer today (400eV and target 1 on ATT with pulse energy XGMD ~10 uJ, 8.29 kHz). Device: Position: 0 Intensifier MCP [V] 699 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Dela...
- setting fzp

**Run classification**: commissioning_run
**Confidence**: high
**Key evidence**: Start of shift 3 for MRCO commissioning, beam pointing, transmission checks, FZP setup for 400 eV, and detector preparation

### Run 121
**Duration**: 1.3 minutes (medium, 69th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- We ramped up the TOFs and is taking a background dataset at 400 eV. The FZP is not seeing much hit according to the shared memory. We will look at this data to see if the HSDs sees anything in the dat...
- MRCO hsd 112 start time before changing it to match with others in the same XPM
- intensifier TPR trigger rate is 8.135 kHz instead of 8.29 kHz from X-ray
- We see that the start time of mrco_hsd_112 and 135 which are in the same XPM is showing different compared to other channels in the same XPM. We made them the same and they still show offset from the ...

**Run classification**: diagnostic_run
**Confidence**: high
**Key evidence**: Background dataset collection at 400 eV, checking if HSDs detect signals, troubleshooting timing offsets between different channels in the same XPM

### Run 122
**Duration**: 38.9 seconds (short, 34th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Timed run with 240000 events Scan exited after 3 steps with status: success
- We injected Argon in the interaction point. The needle is in its parking position. Retardation is 0. Photon energy 400 eV.
- starting needle position in the parking position

**Run classification**: measurement_run
**Confidence**: medium
**Key evidence**: Argon gas target at interaction point, controlled photon energy (400 eV), timed run with specific event count

### Run 123
**Duration**: 39.4 seconds (short, 38th percentile)
**Total entries**: 7 (7 unique)
**Activities**:
- start of the needle scan, the needle position is where it was good for the laser.
- We moved the needle to the position where we saw good counts during laser only commissioning. Compare with run 123.
- Timed run with 240000 events Scan exited after 3 steps with status: success
- starting position for the square-1 position (nearly optimal from the square-1 scan). We will sample in y-position while holding the x constant
- suddenly we need to use width of 1000 ns (1us) so that intensifier can run properly; we have us 10,000 ns before and it is fine.
- SQ1 at the beginnign of the shift.
- the ATM beam transport tube needed to be removed before adjusting the square-1 position. We had to ramp down the voltages to remove it.

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle positioning to optimize signal, moving to position that showed good counts during previous commissioning, preparing for spatial scan

### Run 124
**Duration**: 28.9 seconds (very short, 8th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- Device: Position: 0 rx -10.5606 1 ry -10.5728 2 rz 0.0602 3 x 6.2943 4 y -10.5803 5 z -55.9899
- SQ1 is at (0, 0)

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (0,0) coordinates, precise position measurements for rx, ry, rz, x, y, z parameters

### Run 125
**Duration**: 28.9 seconds (very short, 10th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- SQ1 is at (-1, -1).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (-1,-1) coordinates as part of systematic spatial scan

### Run 126
**Duration**: 28.9 seconds (very short, 8th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (-0.5, -1)
- Timed run with 100000.0 events Scan exited after 2 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (-0.5,-1) coordinates as part of systematic spatial scan

### Run 127
**Duration**: 28.9 seconds (very short, 7th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- SQ1 is at (0, -1).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (0,-1) coordinates as part of systematic spatial scan

### Run 128
**Duration**: 28.9 seconds (very short, 9th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (0.5, -1)
- Timed run with 100000.0 events Scan exited after 2 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (0.5,-1) coordinates as part of systematic spatial scan

### Run 129
**Duration**: 28.8 seconds (very short, 5th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (1, -1).
- Timed run with 100000.0 events Scan exited after 2 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (1,-1) coordinates as part of systematic spatial scan

### Run 130
**Duration**: 28.9 seconds (very short, 8th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (-1, -0.5)
- Timed run with 100000.0 events Scan exited after 2 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (-1,-0.5) coordinates as part of systematic spatial scan

### Run 131
**Duration**: 28.8 seconds (very short, 5th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (-0.5, -0.5)
- Timed run with 100000.0 events Scan exited after 2 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (-0.5,-0.5) coordinates as part of systematic spatial scan

### Run 132
**Duration**: 28.8 seconds (very short, 6th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (0, -0.5)
- Timed run with 100000.0 events Scan exited after 2 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (0,-0.5) coordinates as part of systematic spatial scan

### Run 133
**Duration**: 28.8 seconds (very short, 5th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (0.5, -0.5)
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- Device: Position: 0 rx -10.5611 1 ry -10.5732 2 rz 0.0602 3 x 7.2942 4 y -11.0805 5 z -55.9906

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (0.5,-0.5) coordinates with device position information as part of spatial scan

### Run 134
**Duration**: 28.8 seconds (very short, 6th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- SQ1 is at (1, -0.5).

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (1,-0.5) coordinates as part of systematic spatial scan

### Run 135
**Duration**: 29.0 seconds (very short, 11th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (-1, 0).
- Device: Position: 0 rx -10.5605 1 ry -10.5724 2 rz 0.0604 3 x 5.2942 4 y -10.5805 5 z -55.9896
- Timed run with 100000.0 events Scan exited after 2 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (-1,0) coordinates with device position information as part of spatial scan

### Run 136
**Duration**: 28.9 seconds (very short, 9th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (-0.5, 0).
- Timed run with 100000.0 events Scan exited after 2 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (-0.5,0) coordinates as part of systematic spatial scan

### Run 137
**Duration**: 28.9 seconds (very short, 8th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (0,0).
- Device: Position: 0 rx -10.5609 1 ry -10.5733 2 rz 0.0603 3 x 6.2944 4 y -10.5805 5 z -55.9905
- Timed run with 100000.0 events Scan exited after 2 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (0,0) coordinates with device position information as part of spatial scan

### Run 138
**Duration**: 29.7 seconds (very short, 12th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- SQ1 is at (0.5, 0)
- Device: Position: 0 rx -10.5611 1 ry -10.5735 2 rz 0.0599 3 x 6.7945 4 y -10.5805 5 z -55.9907
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- Device: Position: 0 rx -10.5610 1 ry -10.5731 2 rz 0.0602 3 x 7.2942 4 y -10.5804 5 z -55.9905

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (0.5,0) coordinates with multiple device position readings as part of spatial scan

### Run 139
**Duration**: 28.9 seconds (very short, 9th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- SQ1 is at (1, 0).
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- SQ1 is at (-1, 0.5)
- Device: Position: 0 rx -10.5604 1 ry -10.5723 2 rz 0.0606 3 x 5.2939 4 y -10.0805 5 z -55.9895

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at multiple coordinates (1,0) and (-1,0.5) with device position information as part of spatial scan

### Run 140
**Duration**: 28.9 seconds (very short, 10th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (-1, 0.5)
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- Device: Position: 0 rx -10.5608 1 ry -10.5734 2 rz 0.0606 3 x 5.7943 4 y -10.0805 5 z -55.9906

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (-1,0.5) coordinates with device position information as part of spatial scan

### Run 141
**Duration**: 28.9 seconds (very short, 9th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (-0.5, 0.5)
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- Device: Position: 0 rx -10.5606 1 ry -10.5729 2 rz 0.0606 3 x 6.2940 4 y -10.0804 5 z -55.9902

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (-0.5, 0.5) coordinates with device position information as part of systematic spatial scan

### Run 142
**Duration**: 29.0 seconds (very short, 11th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (0, 0.5).
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- Device: Position: 0 rx -10.5608 1 ry -10.5734 2 rz 0.0603 3 x 6.7941 4 y -10.0804 5 z -55.9903

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (0, 0.5) coordinates with device position information continuing the systematic spatial scan

### Run 143
**Duration**: 29.7 seconds (very short, 12th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (0.5, 0.5)
- Timed run with 100000.0 events Scan exited after 2 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (0.5, 0.5) coordinates as part of the ongoing systematic spatial scan

### Run 144
**Duration**: 29.5 seconds (very short, 11th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- SQ1 is at (1, 0.5).
- Device: Position: 0 rx -10.5607 1 ry -10.5729 2 rz 0.0605 3 x 7.2938 4 y -10.0804 5 z -55.9901
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- Device: Position: 0 rx -10.5604 1 ry -10.5723 2 rz 0.0605 3 x 5.2940 4 y -9.5806 5 z -55.9893

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (1, 0.5) coordinates with device position information continuing the spatial scan sequence

### Run 145
**Duration**: 28.9 seconds (very short, 10th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (-1, 1)
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- Device: Position: 0 rx -10.5608 1 ry -10.5733 2 rz 0.0607 3 x 5.7942 4 y -9.5805 5 z -55.9906

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (-1, 1) coordinates with device position information as part of the systematic spatial scan

### Run 146
**Duration**: 28.9 seconds (very short, 7th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at -0.5, 1)
- Timed run with 100000.0 events Scan exited after 2 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (-0.5, 1) coordinates continuing the systematic spatial scan sequence

### Run 147
**Duration**: 28.8 seconds (very short, 6th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- SQ1 is at (0, 1).
- Device: Position: 0 rx -10.5607 1 ry -10.5730 2 rz 0.0604 3 x 6.7940 4 y -9.5805 5 z -55.9901
- Device: Position: 0 rx -10.5608 1 ry -10.5733 2 rz 0.0605 3 x 6.7939 4 y -9.5805 5 z -55.9903

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (0, 1) coordinates with multiple device position readings as part of spatial scan

### Run 148
**Duration**: 28.9 seconds (very short, 10th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (0.5, 1).
- Timed run with 100000.0 events Scan exited after 2 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (0.5, 1) coordinates continuing the systematic spatial scan sequence

### Run 149
**Duration**: 28.9 seconds (very short, 7th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- SQ1 is at (1,1)
- Device: Position: 0 rx -10.5606 1 ry -10.5732 2 rz 0.0603 3 x 6.2940 4 y -10.5805 5 z -55.9900

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at (1,1) coordinates with device position information completing the systematic spatial scan

### Run 150
**Duration**: 29.0 seconds (very short, 11th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- SQ is at (0,0).
- Timed run with 100000.0 events Scan exited after 2 steps with status: success
- We just finished the SQ1 scan. We will move on to the needle scan. This is the starting position of the needle scan.
- Device: Position: 0 gas_nozzle_x 42.57260 1 gas_nozzle_y 29.06715 2 gas_nozzle_z 119.91730 3 sample_paddle_x 63.74745 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26935

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Completion of SQ1 scan and transition to needle scan with specific device positioning information for spatial alignment

### Run 151
**Duration**: 38.2 seconds (very short, 23rd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Needle Z is at Z = +7 mm
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 gas_nozzle_x 42.57245 1 gas_nozzle_y 29.06715 2 gas_nozzle_z 118.95245 3 sample_paddle_x 63.74750 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26935

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = +7 mm with device position coordinates, continuing from the previous needle scan setup mentioned in run 150

### Run 152
**Duration**: 38.1 seconds (very short, 14th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z at Z = +6 mm.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = +6 mm, part of a systematic Z-position scan sequence

### Run 153
**Duration**: 38.2 seconds (very short, 20th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Needle Z is at Z = +5 mm.
- Device: Position: 0 gas_nozzle_x 42.57260 1 gas_nozzle_y 29.06710 2 gas_nozzle_z 117.98260 3 sample_paddle_x 63.74745 4 sample_paddle_y 44.58805 5 sample_paddle_z 102.26940
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 rx -10.5605 1 ry -10.5743 2 rz 0.0609 3 x 6.2936 4 y -10.5802 5 z -55.9905

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = +5 mm with device position coordinates, continuing the systematic spatial alignment sequence

### Run 154
**Duration**: 38.8 seconds (short, 31st percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Needle Z is at +4 mm.
- Device: Position: 0 gas_nozzle_x 42.57240 1 gas_nozzle_y 29.06710 2 gas_nozzle_z 117.01075 3 sample_paddle_x 63.74750 4 sample_paddle_y 44.58815 5 sample_paddle_z 102.26935
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 gas_nozzle_x 42.57250 1 gas_nozzle_y 29.06710 2 gas_nozzle_z 116.01520 3 sample_paddle_x 63.74745 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26935

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = +4 mm with device position coordinates, part of the systematic Z-position alignment sequence

### Run 155
**Duration**: 38.1 seconds (very short, 17th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Needle Z is at Z = +3 mm
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 gas_nozzle_x 42.57255 1 gas_nozzle_y 29.06705 2 gas_nozzle_z 115.01990 3 sample_paddle_x 63.74750 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26940

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = +3 mm with device position coordinates, continuing the systematic spatial alignment sequence

### Run 156
**Duration**: 38.5 seconds (short, 28th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z is at Z = +2 mm
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = +2 mm, part of the systematic Z-position alignment sequence

### Run 157
**Duration**: 38.5 seconds (short, 27th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Needle Z is at Z = +1 mm
- Device: Position: 0 gas_nozzle_x 42.57250 1 gas_nozzle_y 29.06705 2 gas_nozzle_z 114.02515 3 sample_paddle_x 63.74745 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26935
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 gas_nozzle_x 42.57260 1 gas_nozzle_y 29.06705 2 gas_nozzle_z 113.05215 3 sample_paddle_x 63.74745 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26935

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = +1 mm with device position coordinates, continuing the systematic spatial alignment sequence

### Run 158
**Duration**: 38.2 seconds (very short, 22nd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Needle Z is at Z = 0 mm
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 gas_nozzle_x 42.57255 1 gas_nozzle_y 29.06700 2 gas_nozzle_z 112.05125 3 sample_paddle_x 63.74740 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26940

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = 0 mm with device position coordinates, part of the systematic Z-position alignment sequence

### Run 159
**Duration**: 38.9 seconds (short, 33rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z is at Z = -1 mm
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = -1 mm, continuing the systematic spatial alignment sequence

### Run 160
**Duration**: 38.2 seconds (very short, 18th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Needle Z at Z = -2 mm.
- Device: Position: 0 gas_nozzle_x 42.57255 1 gas_nozzle_y 29.06700 2 gas_nozzle_z 111.05350 3 sample_paddle_x 63.74750 4 sample_paddle_y 44.58815 5 sample_paddle_z 102.26940
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = -2 mm with device position coordinates, completing the systematic Z-position alignment sequence

### Run 161
**Duration**: 38.1 seconds (very short, 16th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Needle Z is at Z = -3 mm.
- Device: Position: 0 gas_nozzle_x 42.57250 1 gas_nozzle_y 29.06700 2 gas_nozzle_z 110.05700 3 sample_paddle_x 63.74745 4 sample_paddle_y 44.58815 5 sample_paddle_z 102.26940
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = -3 mm with device position coordinates, continuing the systematic Z-position alignment sequence from previous runs

### Run 162
**Duration**: 38.3 seconds (short, 26th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Needle Z is at Z = -4 mm.
- Device: Position: 0 gas_nozzle_x 42.57255 1 gas_nozzle_y 29.06700 2 gas_nozzle_z 109.06070 3 sample_paddle_x 63.74750 4 sample_paddle_y 44.58815 5 sample_paddle_z 102.26930
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = -4 mm with device position coordinates, part of the systematic Z-position alignment sequence

### Run 163
**Duration**: 38.2 seconds (very short, 20th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Needle Z is at Z = -5 mm
- Device: Position: 0 gas_nozzle_x 42.57260 1 gas_nozzle_y 29.06700 2 gas_nozzle_z 108.06220 3 sample_paddle_x 63.74745 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26935
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = -5 mm with device position coordinates, continuing the systematic spatial alignment sequence

### Run 164
**Duration**: 38.1 seconds (very short, 18th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Needle Z is at Z = -6 mm
- Device: Position: 0 gas_nozzle_x 42.57265 1 gas_nozzle_y 29.06700 2 gas_nozzle_z 107.06115 3 sample_paddle_x 63.74745 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26935
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 gas_nozzle_x 42.57265 1 gas_nozzle_y 29.06695 2 gas_nozzle_z 106.06535 3 sample_paddle_x 63.74745 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26935

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = -6 mm with device position coordinates, part of the systematic Z-position alignment sequence

### Run 165
**Duration**: 38.1 seconds (very short, 14th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Needle Z is at Z = - 7 mm.
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 gas_nozzle_x 42.57275 1 gas_nozzle_y 29.06695 2 gas_nozzle_z 105.06835 3 sample_paddle_x 63.74740 4 sample_paddle_y 44.58805 5 sample_paddle_z 102.26935

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = -7 mm with device position coordinates, continuing the systematic spatial alignment sequence

### Run 166
**Duration**: 38.1 seconds (very short, 16th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Needle Z is at Z = -8 mm.
- Device: Position: 0 gas_nozzle_x 42.57270 1 gas_nozzle_y 29.06695 2 gas_nozzle_z 104.09605 3 sample_paddle_x 63.74750 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26935

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = -8 mm with device position coordinates, part of the systematic Z-position alignment sequence

### Run 167
**Duration**: 38.2 seconds (very short, 19th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Needle Z is at Z = -9 mm
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 gas_nozzle_x 42.57285 1 gas_nozzle_y 29.06695 2 gas_nozzle_z 103.12145 3 sample_paddle_x 63.74745 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26935

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = -9 mm with device position coordinates, continuing the systematic spatial alignment sequence

### Run 168
**Duration**: 44.1 seconds (short, 48th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z is at Z = -10 mm
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z = -10 mm, part of the systematic Z-position alignment sequence

### Run 169
**Duration**: 38.1 seconds (very short, 15th percentile)
**Total entries**: 19 (19 unique)
**Activities**:
- Needle Z is at Z = -11 mm.
- Device: Position: 0 gas_nozzle_x 42.57285 1 gas_nozzle_y 29.06695 2 gas_nozzle_z 102.14825 3 sample_paddle_x 63.74750 4 sample_paddle_y 44.58810 5 sample_paddle_z 102.26935
- Timed run with 240000 events Scan exited after 3 steps with status: success
- We are moving on to do a needle voltage scan. We will park the needle at Z = 0, where needle Z motor position is 112.940.
- No retardation, can even still identify the 4 main Auger features.
- SMA tip with X-ray at the cursor.
- X-ray and laser on the SMA tip
- Device: Position: 0 lxt pos [ps] -6.306375e+06 1 txt pos [ps] -1.854275e+04 2 lxt_ttc pos [ps] -6.306375e+06 3 lxt offset [ns] 2.480082e+04 4 lxt total delay [ns] 3.110719e+04 5 txt user stage [mm] -5...
- Sample paddle position for SMA tip where we saw x-ray/laser coarse time overlap.
- these are the x-rays on the ATM diode. GMD is reading 200 uJ, transmission 2e-4
- Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] 0.001121 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31107.190000 4 lxt total delay [ns] 31107.190000 5 txt user stage [mm] -71.999912
- we are coarsely timed at the ATM here. note 2 ns/div., but this is good for right now.
- we are coarsely timed at the ATM here. note 2 ns/div., but this is good for right now. stored trace is x-rays, live trace is laser
- Diode position where we saw the timing signal at the ATM
- setup fzp in ten minutes
- FZP and intensifier conditions for 400 eV and 10 uJ; 8.29 kHz Device: Position: 0 Intensifier MCP [V] 649 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 81...
- fzp shadowing shape; with ATT target 1 aperture
- I used delay 88us and still see the signal; it shifted to 88 us (from 94 us)
- we are beginning a bias scan. Ar at 400 eV, 175 retardation

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Multiple entries about timing activities: 'coarsely timed at the ATM', LXT/TXT position adjustments, and X-ray/laser temporal overlap verification

### Run 170
**Duration**: 38.1 seconds (very short, 18th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle is at 0 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: medium
**Key evidence**: Needle voltage set to 0 V, following run 169's note about 'beginning a bias scan' with 175 retardation, indicating a voltage calibration sequence

### Run 171
**Duration**: 38.1 seconds (very short, 17th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle at +50 V
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Needle at +50V, part of a systematic voltage bias scan sequence that began in run 170 (at 0V) as mentioned in run 169's note about 'beginning a bias scan'

### Run 172
**Duration**: 38.1 seconds (very short, 14th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle is at +100 V
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Needle is at +100V, continuing the systematic voltage bias scan sequence from runs 170 (+0V) and 171 (+50V)

### Run 173
**Duration**: 38.2 seconds (very short, 21st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle is at -50 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Needle is at -50V, continuing the systematic voltage bias scan sequence now testing negative voltages

### Run 174
**Duration**: 39.1 seconds (short, 38th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle is at -100 V
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Needle is at -100V, completing the systematic voltage bias scan sequence testing both positive and negative voltages

### Run 175
**Duration**: 38.2 seconds (very short, 21st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 240000 events Scan exited after 3 steps with status: success
- We moved to (0, 0). We moved the needle further back about 30 mm from the IP

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Repositioning activity: 'We moved to (0, 0)' and 'moved the needle further back about 30 mm from the IP' indicating spatial alignment adjustments

### Run 176
**Duration**: 38.0 seconds (very short, 12th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (-2, 2).
- Device: Position: 0 rx -10.5606 1 ry -10.5731 2 rz 0.0601 3 x 4.2943 4 y -12.5805 5 z -55.9900
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at specific coordinates (-2, 2) with detailed position data for rx, ry, rz, x, y, z motors, indicating a spatial scan sequence

### Run 177
**Duration**: 38.1 seconds (very short, 13th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (-1, -2).
- Device: Position: 0 rx -10.5608 1 ry -10.5739 2 rz 0.0606 3 x 5.2942 4 y -12.5805 5 z -55.9908
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (-1, -2) with position data, continuing the systematic spatial scan sequence from run 176

### Run 178
**Duration**: 38.1 seconds (very short, 15th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (0, -2)
- Device: Position: 0 rx -10.5608 1 ry -10.5739 2 rz 0.0606 3 x 6.2941 4 y -12.5805 5 z -55.9907
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (0, -2) with position data, continuing the systematic spatial scan sequence

### Run 179
**Duration**: 38.2 seconds (very short, 22nd percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- SQ1 is at (1, -2).
- Device: Position: 0 rx -10.5608 1 ry -10.5736 2 rz 0.0608 3 x 7.2934 4 y -12.5804 5 z -55.9905
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 rx -10.5609 1 ry -10.5737 2 rz 0.0608 3 x 8.2936 4 y -12.5805 5 z -55.9905

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (1, -2) with position data, continuing the systematic spatial scan sequence

### Run 180
**Duration**: 38.9 seconds (short, 35th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (2,-2)
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (2, -2), completing the systematic spatial scan sequence that began at run 176

### Run 181
**Duration**: 38.2 seconds (very short, 23rd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ is at (-2, -1)
- Device: Position: 0 rx -10.5606 1 ry -10.5729 2 rz 0.0603 3 x 4.2939 4 y -11.5808 5 z -55.9898
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ positioning at specific coordinates (-2, -1) with detailed position data, continuing the systematic spatial scan sequence from previous runs

### Run 182
**Duration**: 38.1 seconds (very short, 16th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- SQ1 is at (-1, -1)
- Device: Position: 0 rx -10.5609 1 ry -10.5738 2 rz 0.0605 3 x 5.2943 4 y -11.5806 5 z -55.9908
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 rx -10.5612 1 ry -10.5739 2 rz 0.0602 3 x 6.2944 4 y -11.5806 5 z -55.9909

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (-1, -1) with position data, continuing the systematic spatial scan sequence

### Run 183
**Duration**: 38.2 seconds (very short, 24th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (0, -1).
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (0, -1), continuing the systematic spatial scan sequence

### Run 184
**Duration**: 38.0 seconds (very short, 13th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (1, -1)
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (1, -1), continuing the systematic spatial scan sequence

### Run 185
**Duration**: 38.2 seconds (very short, 23rd percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- SQ1 is at (2, -1)
- Device: Position: 0 rx -10.5609 1 ry -10.5735 2 rz 0.0606 3 x 8.2938 4 y -11.5805 5 z -55.9905
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 rx -10.5604 1 ry -10.5731 2 rz 0.0603 3 x 4.2939 4 y -10.5807 5 z -55.9897

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (2, -1) with position data, continuing the systematic spatial scan sequence

### Run 186
**Duration**: 38.2 seconds (very short, 24th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (-2, 0)
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (-2, 0), continuing the systematic spatial scan sequence

### Run 187
**Duration**: 38.2 seconds (very short, 21st percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (-1, 0)
- Device: Position: 0 rx -10.5609 1 ry -10.5734 2 rz 0.0608 3 x 5.2938 4 y -10.5806 5 z -55.9907
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (-1, 0) with position data, continuing the systematic spatial scan sequence

### Run 188
**Duration**: 38.9 seconds (short, 34th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (0, 0)
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (0, 0), continuing the systematic spatial scan sequence

### Run 189
**Duration**: 38.1 seconds (very short, 15th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (1, 0).
- Device: Position: 0 rx -10.5610 1 ry -10.5740 2 rz 0.0606 3 x 7.2938 4 y -10.5806 5 z -55.9909
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (1, 0) with position data, continuing the systematic spatial scan sequence

### Run 190
**Duration**: 38.2 seconds (very short, 20th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (2, 0).
- Device: Position: 0 rx -10.5610 1 ry -10.5734 2 rz 0.0606 3 x 8.2937 4 y -10.5806 5 z -55.9905
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (2, 0) with position data, completing the systematic spatial scan sequence

### Run 191
**Duration**: 38.2 seconds (very short, 22nd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (-2, 1)
- Device: Position: 0 rx -10.5603 1 ry -10.5728 2 rz 0.0608 3 x 4.2934 4 y -9.5808 5 z -55.9896
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (-2, 1) with position data, continuing the systematic spatial scan sequence from previous runs

### Run 192
**Duration**: 38.2 seconds (very short, 23rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (-1, 1)
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (-1, 1), continuing the systematic spatial scan sequence

### Run 193
**Duration**: 38.2 seconds (very short, 19th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (0, 1)
- Device: Position: 0 rx -10.5608 1 ry -10.5733 2 rz 0.0605 3 x 6.2939 4 y -9.5805 5 z -55.9906
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (0, 1) with position data, continuing the systematic spatial scan sequence

### Run 194
**Duration**: 38.3 seconds (short, 25th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (1, 1)
- Device: Position: 0 rx -10.5607 1 ry -10.5733 2 rz 0.0606 3 x 7.2935 4 y -9.5805 5 z -55.9904
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (1, 1) with position data, continuing the systematic spatial scan sequence

### Run 195
**Duration**: 38.3 seconds (short, 25th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (2, 1)
- Device: Position: 0 rx -10.5606 1 ry -10.5736 2 rz 0.0606 3 x 8.2938 4 y -9.5804 5 z -55.9902
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (2, 1) with position data, continuing the systematic spatial scan sequence

### Run 196
**Duration**: 37.9 seconds (very short, 12th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- SQ1 is at (-2, 2)
- Device: Position: 0 rx -10.5605 1 ry -10.5729 2 rz 0.0608 3 x 4.2934 4 y -8.5807 5 z -55.9897
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 rx -10.5608 1 ry -10.5732 2 rz 0.0607 3 x 5.2937 4 y -8.5806 5 z -55.9904

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (-2, 2) with position data, continuing the systematic spatial scan sequence

### Run 197
**Duration**: 38.1 seconds (very short, 14th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (-1, 2)
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (-1, 2), continuing the systematic spatial scan sequence

### Run 198
**Duration**: 38.4 seconds (short, 26th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- SQ1 is at (0, 2)
- Device: Position: 0 rx -10.5609 1 ry -10.5737 2 rz 0.0608 3 x 6.2938 4 y -8.5806 5 z -55.9908
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 rx -10.5610 1 ry -10.5734 2 rz 0.0612 3 x 7.2931 4 y -8.5808 5 z -55.9910

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (0, 2) with position data, continuing the systematic spatial scan sequence

### Run 199
**Duration**: 38.7 seconds (short, 28th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- SQ1 is at (1, 2)
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Device: Position: 0 rx -10.5613 1 ry -10.5739 2 rz 0.0610 3 x 8.2936 4 y -8.5806 5 z -55.9912

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (1, 2) with position data, continuing the systematic spatial scan sequence

### Run 200
**Duration**: 38.2 seconds (very short, 24th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- SQ1 is at (2, 2).
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: SQ1 positioning at coordinates (2, 2), completing the systematic spatial scan sequence in a grid pattern

### Run 201
**Duration**: 38.3 seconds (short, 25th percentile)
**Total entries**: 8 (8 unique)
**Activities**:
- We are redoing the SQ1 run due to xtc file corruption. SQ1 is at (2, -2).
- Device: Position: 0 rx -10.5605 1 ry -10.5733 2 rz 0.0603 3 x 8.2939 4 y -12.5806 5 z -55.9901
- Timed run with 240000 events Scan exited after 3 steps with status: success
- adjust the baseline for the fex
- change fex baseline in config db again. try to see some effect of the baseline on the signal.
- back to the original baseline value. It seems the baseline setting does not have an effect on the data.
- We are moving to Veronica's optimum
- We are moving on to do retardation scan.

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Redoing SQ1 run with specific coordinates (2, -2), position data recorded, and preparation for subsequent retardation scan

### Run 202
**Duration**: 38.3 seconds (short, 26th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Retardation = -50 V at 400 eV.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Retardation voltage set to -50 V at 400 eV, beginning of retardation scan sequence

### Run 203
**Duration**: 3.7 minutes (long, 89th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- We are about to setup a photon energy scan at retardation of 50 V. Photon energy scan is from 390 eV to 410 eV at 2 eV steps.
- Retardation = -50 eV.
- Scan hf_w: [390 392 394 396 398 400 402 404 406 408 410] 80000 events/step Scan exited after 22 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan from 390 eV to 410 eV at 2 eV steps with fixed retardation of -50 V

### Run 204
**Duration**: 3.8 minutes (very long, 93rd percentile)
**Total entries**: 5 (4 unique)
**Activities**:
- Retardation = -100 V.
- xy scan, step size 1, [-2,2] in both x and y. Figures: isotropy, mean counts (normalized by GMD), standard deviation (normalized by mean counts)
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success
- We moved the gas needle closer by 30 mm to get higher number of counts/shot

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -100 V, continuing the systematic retardation scan sequence

### Run 205
**Duration**: 3.8 minutes (very long, 90th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 0 V.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at 0 V, part of systematic retardation voltage variation series

### Run 206
**Duration**: 3.8 minutes (very long, 91st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = -50 V
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -50 V, continuing systematic calibration sequence

### Run 207
**Duration**: 3.8 minutes (very long, 91st percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Retardation = -100 V.
- Starting from run 205, we should have a look at the retardation scan with gas needle about 1 cm away from the interaction point.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success
- 400eV FZP calibration linear coefficient = 31.6+/-0.2 meV/px. Calibrated to the Ar 2p splitting 2.12eV well resolved in SDGI. This is the average of port0 and port8. The calibration result is independ...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -100 V, includes FZP calibration coefficient measurement (31.6±0.2 meV/px)

### Run 208
**Duration**: 3.8 minutes (very long, 90th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = -150 V
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -150 V, continuing systematic retardation voltage variation series

### Run 209
**Duration**: 3.8 minutes (very long, 92nd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Retardation = -175 V
- the start_ns for fex hsd_225 has a strange start time. It is 99000 and this is inconsistent with any of the other values. we should change this to be consisten with the raw start_ns.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -175 V, part of systematic retardation voltage calibration sequence

### Run 210
**Duration**: 3.8 minutes (very long, 91st percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Retardation = -190 V.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success
- xy scan, step size 1, [-2,2] in both x and y. Figures: isotropy, mean counts (normalized by GMD), standard deviation (normalized by mean counts)

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -190 V, completing comprehensive retardation voltage calibration series

### Run 211
**Duration**: 3.8 minutes (very long, 90th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan from 390-410 eV, continuing the systematic calibration sequence from previous runs

### Run 212
**Duration**: 3.8 minutes (very long, 92nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = -200 V.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -200 V, part of systematic retardation voltage calibration series

### Run 213
**Duration**: 3.8 minutes (very long, 90th percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- Retardation -350 V.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success
- adjust the fex start_ns of each channel to try to overlap the light peak. Numbers are from Ryan.
- Switch to target 2 to attenuate more of the beam. Device: Position: 0 Intensifier MCP [V] 749 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 8135.0 4 solid...
- We changed the transmission to 20%. Avg pulse energy = 60 uJ. Retardation = 0. Needle is 30 mm away from the nominal. Target 2 in the FZP is in.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -350 V, continuing calibration series with beam attenuation adjustments

### Run 214
**Duration**: 38.9 seconds (short, 33rd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Retardation = 0. Transmission = 20%.
- change start_ns for raw on 112 and 135. These were different from the fex start_ns

**Run classification**: calibration_run
**Confidence**: medium
**Key evidence**: Timed run with retardation at 0 V and transmission at 20%, likely testing detector response at different settings

### Run 215
**Duration**: 3.8 minutes (very long, 92nd percentile)
**Total entries**: 10 (10 unique)
**Activities**:
- Retardation = -150 V. Photon energy scan from 390 to 410 at high transmission.
- settings for fzp spectrometer at high transmision run (400eV and target 2 on ATT with pulse energy XGMD ~60 uJ, 8.29 kHz). Device: Position: 0 Intensifier MCP [V] 749 1 Intensifier Gate [us] 10.0 2 In...
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success
- Yay, I can see split lines even at 50V pass energy, and higher count rates with 20%
- Working streaming from fex2h5 outputs to defiant and showing live tof-count totals for each detector within each batch of 512-10k events.
- Beam on im5k4 before inserting FZP
- FZP setup for XLEAP shift. Device: Position: 0 Intensifier MCP [V] 799 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 100.0 4 solid_att TARGET1 5 solid_att...
- 400-1 zone plate aligned for ACR xleap.
- update sp1k4 target positions Device: Position: 0 state_name FZP-400_1 1 state_num 12 2 previous m1 89.0 3 new m1 88.70425 4 previous m2 -8.2 5 new m2 -8.84095 6 previous m3 0.0 7 new m3 0.000719
- FZP setup for XLEAP shift for 11-02-2024. Device: Position: 0 Intensifier MCP [V] 799 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 100.0 4 solid_att TARG...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -150 V at high transmission, FZP spectrometer calibration with visible spectral lines

### Run 216
**Duration**: 3.8 minutes (very long, 93rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = -100 V. Photon energy scan from 390 to 410 eV at high transmission.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -100 V at high transmission, continuing systematic calibration sequence

### Run 217
**Duration**: 3.9 minutes (very long, 93rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = -125 V. Photon energy scan from 390 to 410 eV at high transmission.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success Average Duty Cycle: 0.979

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -125 V at high transmission, part of comprehensive retardation voltage calibration series

### Run 218
**Duration**: 3.9 minutes (very long, 94th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Retardation = 0 V. Photon energy scan from 390 to 410 eV at high transmission.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success Average Duty Cycle: 0.981
- Changed the transmission to 40% with transmission to ~100 uJ

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at 0 V at high transmission, transmission increased to 40% during run

### Run 219
**Duration**: 3.9 minutes (very long, 94th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 0 V, Photon energy scan with 40% transmission, 100 uJ avg pulse energy.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success Average Duty Cycle: 0.979

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at 0 V at 40% transmission, continuing systematic calibration with increased pulse energy

### Run 220
**Duration**: 3.9 minutes (very long, 94th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = -100 V. Photon energy scan with 40% transmission, 100 uJ avg pulse energy
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success Average Duty Cycle: 0.980

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -100 V at 40% transmission, completing comprehensive calibration series at higher pulse energy

### Run 221
**Duration**: 3.9 minutes (very long, 93rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = -125 V, Photon energy scan with 40% transmission, 100 uJ avg pulse energy.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success Average Duty Cycle: 0.979

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -125 V at 40% transmission, continuing systematic calibration series at higher pulse energy

### Run 222
**Duration**: 3.9 minutes (very long, 93rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = -150 V, Photon energy scan with 40% transmission, 100 uJ avg pulse energy.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success Average Duty Cycle: 0.980

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at -150 V at 40% transmission, part of systematic calibration series varying retardation voltage

### Run 223
**Duration**: 28.8 seconds (very short, 6th percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 1 steps with status: success Which probably means the scan was "stopped" before it finished, not...
- Aborted the run due to PMPS fault where the SP1K4 attenuator became too hot.
- KBO temperature going up at 8.3 kHz, tripped the beam
- SP1K4 paddle temperature going up at 8.3 kHz, tripped the beam
- run 223 is trash

**Run classification**: unknown_run
**Confidence**: high
**Key evidence**: Run aborted due to PMPS fault with SP1K4 attenuator overheating, explicitly marked as 'trash' in logbook

### Run 224
**Duration**: 2.0 minutes (medium, 74th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Retardation = -190 V, Photon energy scan with 40% transmission, 100 uJ avg pulse energy.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 10 steps with status: success Which probably means the scan was "stopped" before it finished, no...
- run 224 is trash
- fzp att is getting warm with the higher average power beam.

**Run classification**: unknown_run
**Confidence**: high
**Key evidence**: Attempted photon energy scan that was stopped prematurely, explicitly marked as 'trash' in logbook due to FZP attenuator heating issues

### Run 225
**Duration**: 3.9 minutes (very long, 94th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408. 410.] 82000 events/step Scan exited after 22 steps with status: success Average Duty Cycle: 0.979
- Retardation = -190 V, Photon energy scan with 40% transmission, 100 uJ avg pulse energy.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Successful photon energy scan with retardation at -190 V at 40% transmission, completing the systematic calibration series

### Run 226
**Duration**: 22.1 seconds (very short, 4th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Timed run with 480000 events Scan exited after 1 steps with status: abort Average Duty Cycle: nan
- started scan with ST1K4 in beam.
- We are about to do Z scan. Run 226 should be considered as position Z = 0. We are at nominal XY as found at the beginning of this shift.
- this run is junk

**Run classification**: unknown_run
**Confidence**: high
**Key evidence**: Aborted run explicitly marked as 'junk', attempted to start Z scan but failed

### Run 227
**Duration**: 39.0 seconds (short, 37th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 480000 events Scan exited after 2 steps with status: success Which probably means the scan was "stopped" before it finished, not "aborted", because the scan should have had 6 steps Aver...
- run 227 is junk

**Run classification**: unknown_run
**Confidence**: high
**Key evidence**: Prematurely stopped run explicitly marked as 'junk' in logbook

### Run 228
**Duration**: 1.2 minutes (medium, 67th percentile)
**Total entries**: 11 (11 unique)
**Activities**:
- Timed run with 480000 events Scan exited after 6 steps with status: success Average Duty Cycle: 0.979
- Z = 1, Retardation = -190 V. Z scan with Argon at 400 eV.
- Augers at high transmission z=1
- TMO_KBO1 transmission: 46.398495272081455. scan data path: /reg/g/pcds/pyps/apps/hutch-python/tmo/tmo/mirror-check/scans/TMO_KBO1/TMO_KBO1_2024-10-31--20-13-58.h5
- TMO_KBO1 transmission: 0.7443304340964075. scan data path: /reg/g/pcds/pyps/apps/hutch-python/tmo/tmo/mirror-check/scans/TMO_KBO1/TMO_KBO1_2024-10-31--20-19-25.h5
- TMO_KBO1 transmission: 0.7189823689304597. scan data path: /reg/g/pcds/pyps/apps/hutch-python/tmo/tmo/mirror-check/scans/TMO_KBO1/TMO_KBO1_2024-10-31--20-24-29.h5
- we are at ~72%, first one was an 'outlier', moving on
- MRCO needle and sample paddle before the beginning of the shift 4
- SQ1 at the beginning of the shift. This is where we saw the optimized counts in Auger during previous shift.
- We moved the SQ1 to the position to see the reproducibility of the sample paddle.
- Sample paddle with X-rays at the cursor. Clear YAG. Note both the SQ1 position and the sample paddle position.

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV collecting Auger electron data at high transmission, with retardation voltage of -190 V

### Run 229
**Duration**: 39.5 seconds (short, 41st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Z = 2, Retardation = -190 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.975

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=2, continuing systematic measurement series with retardation voltage of -190 V

### Run 230
**Duration**: 39.4 seconds (short, 40th percentile)
**Total entries**: 3 (2 unique)
**Activities**:
- Z = 3, Retardation = -190 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.980

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=3, continuing systematic measurement series with retardation voltage of -190 V

### Run 231
**Duration**: 39.4 seconds (short, 40th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Z = 4, Retardation = -190 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.980

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=4, continuing systematic measurement series with retardation voltage of -190 V

### Run 232
**Duration**: 39.5 seconds (short, 40th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Z = 5, Retardation = -190 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.970

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=5, continuing systematic measurement series with retardation voltage of -190 V

### Run 233
**Duration**: 39.4 seconds (short, 39th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Z = 6, Retardation = -190 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.980

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=6, continuing systematic measurement series with retardation voltage of -190 V

### Run 234
**Duration**: 39.5 seconds (short, 41st percentile)
**Total entries**: 4 (3 unique)
**Activities**:
- Z = 7, Retardation = -190 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.973
- Changing the retardation to -175 V

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=7, completing the systematic measurement series with retardation voltage of -190 V

### Run 235
**Duration**: 19.5 seconds (very short, 3rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- run 235 is junk

**Run classification**: unknown_run
**Confidence**: high
**Key evidence**: Run explicitly marked as 'junk' in logbook with no useful data

### Run 236
**Duration**: 39.7 seconds (short, 42nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Z = 7, Retardation = -175 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.975

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=7, starting new systematic measurement series with changed retardation voltage of -175 V

### Run 237
**Duration**: 39.4 seconds (short, 40th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Z = 6, Retardation = -175 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.983

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=6, continuing systematic measurement series with retardation voltage of -175 V

### Run 238
**Duration**: 45.2 seconds (medium, 50th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Z = 5, Retardation = -175 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.980

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=5, continuing systematic measurement series with retardation voltage of -175 V

### Run 239
**Duration**: 39.5 seconds (short, 41st percentile)
**Total entries**: 4 (3 unique)
**Activities**:
- Z = 4, Retardation = -175 V. Z scan with Argon at 400 eV.
- Z = 4, Retardation = -190 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.974

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=4, continuing systematic measurement series with retardation voltage of -175 V

### Run 240
**Duration**: 39.3 seconds (short, 38th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Z = 3, Retardation = -175 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.984

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=3, continuing systematic measurement series with retardation voltage of -175 V

### Run 241
**Duration**: 39.4 seconds (short, 39th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Z = 2, Retardation = -175 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.980

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=2, continuing systematic measurement series with retardation voltage of -175 V

### Run 242
**Duration**: 19.5 seconds (very short, 3rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- run 242 is junk

**Run classification**: unknown_run
**Confidence**: high
**Key evidence**: Explicitly labeled as 'junk' with no scientific purpose indicated

### Run 243
**Duration**: 39.8 seconds (short, 42nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Z = 1, Retardation = -175 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.978

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=1, continuing systematic measurement series with retardation voltage of -175 V

### Run 244
**Duration**: 39.5 seconds (short, 41st percentile)
**Total entries**: 12 (12 unique)
**Activities**:
- Z = 0, Retardation = -175 V. Z scan with Argon at 400 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success Average Duty Cycle: 0.975
- VAT valve setting for shift 3.
- This is a display problem. The rate is measured by counting triggers in a 0.98 second interval; that's the interval that repeats in the accelerator, so it is precise. The displays need to scale up the...
- we have 200 uJ of 400 eV at 8 kHz. ACR had to tune for ~45 minutes because they were tripping off NC at 8 kHz, but they were successful which is great. Now aligning
- beam on IM2K0. 10% transmission. moving on
- FZP positions before moving out to align beamline Device: Position: 0 Intensifier MCP [V] 450 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 8135.0 4 solid...
- beam on im2k4. moving on
- beam on im3k4. moving on
- beamn on im5k4 (yag2). looks pretty good. i'm not sure we need to do anything here.
- we pointed +100 um in x and now we are green
- we are going to 100% transmission and back to 8 kHz (we were at 500 Hz for alignment) and now for the KB transmission scan

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Z scan with Argon at 400 eV at position Z=0, completing systematic Z-position measurement series with retardation voltage of -175 V

### Run 245
**Duration**: 38.9 seconds (short, 35th percentile)
**Total entries**: 5 (3 unique)
**Activities**:
- Timed run with 240000 events Scan exited after 3 steps with status: success
- MCP bias scan. 1400 V across all MCP
- MCP bias scan. 1400 V across all MCP. Retardation 175 V.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: MCP bias scan at 1400 V with retardation voltage of 175 V, starting a systematic detector calibration series

### Run 246
**Duration**: 40.2 seconds (short, 42nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- MCP bias scan. 1350 V across all. Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: MCP bias scan at 1350 V with retardation voltage of 175 V, continuing systematic detector calibration series

### Run 247
**Duration**: 38.8 seconds (short, 32nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 240000 events Scan exited after 3 steps with status: success
- MCP bias scan. 1300 V across all. Retardation 175.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: MCP bias scan at 1300 V with retardation voltage of 175 V, continuing systematic detector calibration series

### Run 248
**Duration**: 38.9 seconds (short, 33rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- MCP bias scan. 1250 V across all. Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: MCP bias scan at 1250 V with retardation voltage of 175 V, continuing systematic detector calibration series

### Run 249
**Duration**: 38.7 seconds (short, 29th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- MCP bias scan. 1200 V across all. Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: MCP bias scan at 1200 V with retardation voltage of 175 V, continuing systematic detector calibration series

### Run 250
**Duration**: 38.8 seconds (short, 31st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- MCP bias scan. 1450 V across all. Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: MCP bias scan at 1450 V with retardation voltage of 175 V, completing systematic detector calibration series

### Run 251
**Duration**: 38.8 seconds (short, 30th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- MCP bias scan. 1500 V across all. Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: MCP bias scan at 1500 V with retardation voltage of 175 V, continuing systematic detector calibration series

### Run 252
**Duration**: 38.9 seconds (short, 34th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- MCP bias scan. 1550 V across all. Retardation 175 V
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: MCP bias scan at 1550 V with retardation voltage of 175 V, continuing systematic detector calibration series

### Run 253
**Duration**: 39.0 seconds (short, 36th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- MCP bias scan. 1600 V across all. Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success
- We changed the MCP voltages to a previous bias group voltage where all ports except 0, 4, 14, 15 are 1400 across. Port 0 and 4 is at 1450 V. Port 14 is at 1425 V and Port 15 is at 1550 V.
- We are about to do a needle scan. This is the starting value of the needle Z. This is needle Z = 0.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: MCP bias scan at 1600 V followed by voltage adjustments for specific ports in preparation for needle scan

### Run 254
**Duration**: 38.7 seconds (short, 29th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Needle Z = 0, Retardation 175 V.

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: First run in needle Z position scan series (Z=0) with retardation voltage at 175 V

### Run 255
**Duration**: 39.4 seconds (short, 39th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z = 1, Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z=1 with retardation voltage at 175 V, continuing systematic alignment series

### Run 256
**Duration**: 38.8 seconds (short, 31st percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Needle Z = 2, Retardation 175 V.
- Needle position
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z=2 with explicit 'Needle position' entry, continuing systematic alignment series

### Run 257
**Duration**: 38.8 seconds (short, 30th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z = 3, Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z=3, continuing systematic needle position alignment series

### Run 258
**Duration**: 38.9 seconds (short, 36th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z = 4, Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z=4, continuing systematic needle position alignment series

### Run 259
**Duration**: 38.7 seconds (short, 29th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z = 5, Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z=5, continuing systematic needle position alignment series

### Run 260
**Duration**: 38.8 seconds (short, 31st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z = 6, Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z=6, completing systematic needle position alignment series

### Run 261
**Duration**: 38.9 seconds (short, 36th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z = 7, Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z=7, continuing systematic needle position alignment series from previous runs

### Run 262
**Duration**: 38.9 seconds (short, 33rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z = 8, Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z=8, continuing systematic needle position alignment series

### Run 263
**Duration**: 38.8 seconds (short, 32nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z = -1, Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z=-1, continuing systematic needle position alignment series with negative values

### Run 264
**Duration**: 38.8 seconds (short, 31st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z = -2, Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z=-2, continuing systematic needle position alignment series

### Run 265
**Duration**: 38.9 seconds (short, 35th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Needle Z = -3, Retardation 175 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z=-3, continuing systematic needle position alignment series

### Run 266
**Duration**: 39.0 seconds (short, 36th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Needle Z = -8, Retardation 175 V.
- We are about to do finer retardation scan for all the TOFs. We set the bias to all port 1400, with Port 0 and 4 to be 1450, Port 12 at 1550 and Port 14 at 1425 V.

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Needle Z position scan at Z=-8, final run in systematic needle position alignment series before transitioning to retardation scans

### Run 267
**Duration**: 2.1 minutes (long, 77th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Retardation 100 V. Photon energy scan between 395 and 405 eV.
- Scan hf_w: [395 397 399 401 403 405] 80000 events/step Scan exited after 12 steps with status: success
- coincidence

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan between 395-405 eV with retardation voltage at 100V, systematic spectral calibration

### Run 268
**Duration**: 2.1 minutes (long, 77th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation 120 V. Photon energy scan between 395 and 405 eV.
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan between 395-405 eV with retardation voltage at 120V, continuing systematic spectral calibration series

### Run 269
**Duration**: 2.1 minutes (long, 76th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success
- Retardation 140 V. Photon energy scan between 395 and 405 eV.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan between 395-405 eV with retardation voltage at 140V, continuing systematic spectral calibration series

### Run 270
**Duration**: 2.1 minutes (long, 77th percentile)
**Total entries**: 9 (9 unique)
**Activities**:
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success
- Run 270 is retardation 100 V, bias is 1550 if i==12 else 1450 if (i==0 or i==4) else 1400
- ~10 uJ transmission gives about 1 count per shot in Argon, Run 270
- Slits after optimizing on the beam alignment. Device: Position: 0 sl2k0_xwidth 4.798451 1 sl2k0_xcenter 1.800125 2 sl2k0_ywidth 6.498000 3 sl2k0_ycenter 1.001250
- Slits after optimizing on the beam alignment. Device: Position: 0 sl1k4_xwidth 5.09770 1 sl1k4_xcenter -2.49865 2 sl1k4_ywidth 6.99690 3 sl1k4_ycenter 0.00125
- Update tmo preset positions for slits. Axis: Old Preset: New Preset: 0 sl2k0_north 19.5994 19.59940 1 sl2k0_south -13.99915 -13.99915 2 sl2k0_top 19.35025 19.35025 3 sl2k0_bottom -14.44775 -14.44775 4...
- Update tmo preset positions for slits. Axis: Old Preset: New Preset: 0 sl2k0_north 19.5994 19.59940 1 sl2k0_south -13.9991 -13.99910 2 sl2k0_top 19.35025 19.35025 3 sl2k0_bottom -14.44775 -14.44775 4 ...
- We are bypassing the PMPS error due to LI2K4 since it took a while to put it in. Tong had to reboot the IOC since it was stuck before in OUT position.
- Turned on the voltages in all of the detectors. With Port 0 and 90 at 1450 V bias, and Port 270 at 1550 V bias. The rest of the detectors have 1400 V bias across.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation at 100V, detector bias voltage optimization, and beam alignment for spectral calibration

### Run 271
**Duration**: 2.1 minutes (long, 75th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Run 271 is retardation 120 V, bias is 1550 if i==12 else 1450 if (i==0 or i==4) else 1400
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan between 395-405 eV with retardation voltage at 120V, continuing systematic spectral calibration series with specific bias voltage settings

### Run 272
**Duration**: 2.2 minutes (long, 79th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Run 272 is retardation 140 V, bias is 1550 if i==12 else 1450 if (i==0 or i==4) else 1400
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan between 395-405 eV with retardation voltage at 140V, part of systematic retardation voltage scan series for detector calibration

### Run 273
**Duration**: 2.1 minutes (long, 77th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Run 273 is retardation 150 V, bias is 1550 if i==12 else 1450 if (i==0 or i==4) else 1400
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan between 395-405 eV with retardation voltage at 150V, continuing systematic spectral calibration with controlled bias voltage settings

### Run 274
**Duration**: 2.2 minutes (long, 79th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Run 274 is retardation 160 V, bias is 1550 if i==12 else 1450 if (i==0 or i==4) else 1400
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan between 395-405 eV with retardation voltage at 160V, part of methodical retardation voltage scan series for detector calibration

### Run 275
**Duration**: 2.1 minutes (long, 75th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Run 275 is retardation 170 V, bias is 1550 if i==12 else 1450 if (i==0 or i==4) else 1400
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan between 395-405 eV with retardation voltage at 170V, continuing systematic spectral calibration with specific detector bias settings

### Run 276
**Duration**: 2.1 minutes (long, 75th percentile)
**Total entries**: 13 (13 unique)
**Activities**:
- Run 276 is retardation 175 V, bias is 1550 if i==12 else 1450 if (i==0 or i==4) else 1400
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success
- High resolution Augers
- Sample NNO was activated by jcryan
- Sample NNO was stopped by jcryan
- TMO:LAMP:MMS:05:PLC:nEncoderCount_RBV magnet x encoder
- test post
- Device: Position: 0 solid_att OUT 1 solid_att_x -10.9838 2 solid_att_y -0.7702 3 thorlab_lens_x -10.1429 4 yag_theta 0.010866 5 yag_x -0.1007 6 yag_y 3.999922 7 yag_z -6.344925 8 zone_plate OUT 9 zone...
- test post test post
- test post 0 test post
- test post 0 test post
- test_post 0_____test_post
- _______________________Device:__Position: 0____________________solid_att________OUT 1__________________solid_att_x___-10.9838 2__________________solid_att_y____-0.7702 3_______________thorlab_lens_x__...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation voltage at 175V, part of systematic calibration series with note about 'High resolution Augers' indicating spectral calibration purpose

### Run 277
**Duration**: 2.1 minutes (long, 76th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success
- Run 277 is retardation 180 V, bias is 1550 if i==12 else 1450 if (i==0 or i==4) else 1400

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan between 395-405 eV with retardation voltage at 180V, continuing methodical retardation voltage scan series for detector calibration

### Run 278
**Duration**: 2.1 minutes (long, 75th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Run 278 is retardation 185 V, bias is 1550 if i==12 else 1450 if (i==0 or i==4) else 1400
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan between 395-405 eV with retardation voltage at 185V, part of systematic spectral calibration with controlled bias voltage settings

### Run 279
**Duration**: 2.1 minutes (long, 76th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Run 279 is retardation 190 V, bias is 1550 if i==12 else 1450 if (i==0 or i==4) else 1400
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan between 395-405 eV with retardation voltage at 190V, continuing methodical retardation voltage scan series for detector calibration

### Run 280
**Duration**: 2.1 minutes (long, 78th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Run 280 is retardation 195 V, bias is 1550 if i==12 else 1450 if (i==0 or i==4) else 1400
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan between 395-405 eV with retardation voltage at 195V, final run in systematic retardation voltage scan series for detector calibration

### Run 281
**Duration**: 2.1 minutes (long, 76th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Run 281 is retardation 200 V, bias is 1550 if i==12 else 1450 if (i==0 or i==4) else 1400
- Scan hf_w: [395. 397. 399. 401. 403. 405.] 80000 events/step Scan exited after 12 steps with status: success
- We took the amplifer off from Port 22 and Port 202.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan with retardation voltage at 200V, continuing the systematic retardation voltage scan series from previous runs

### Run 282
**Duration**: 38.2 seconds (very short, 20th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Doing a bias scan for port 22 and 202. Retardation = 0, Bias 1200 V.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for detector ports 22 and 202 with retardation 0V and bias 1200V, part of systematic detector calibration

### Run 283
**Duration**: 38.1 seconds (very short, 17th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan for Port 22 and 202. Retardation = 0, Bias 1300 V
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for detector ports with retardation 0V and bias 1300V, continuing systematic bias voltage calibration series

### Run 284
**Duration**: 38.2 seconds (very short, 22nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan for Port 22 and Port 202. Retardation = 0, Bias 1350 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 0V and bias 1350V, part of methodical detector calibration sequence

### Run 285
**Duration**: 38.1 seconds (very short, 15th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan Port 22 and Port 202. Retardation 0, Bias 1400 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 0V and bias 1400V, continuing systematic detector calibration series

### Run 286
**Duration**: 38.0 seconds (very short, 13th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan Port 22 and Port 202. Retardation 0, Bias 1450 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 0V and bias 1450V, part of methodical detector voltage calibration

### Run 287
**Duration**: 38.1 seconds (very short, 18th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan for Port 22 and Port 202. Retardation 0, Bias 1500 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 0V and bias 1500V, continuing systematic detector calibration series

### Run 288
**Duration**: 38.2 seconds (very short, 19th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan for Port 22 and 202. Retardation 0, Bias 1550 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 0V and bias 1550V, part of methodical detector voltage calibration

### Run 289
**Duration**: 38.1 seconds (very short, 16th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan for Port 22 and Port 202. Retardation 0, Bias 1600 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 0V and bias 1600V, continuing systematic detector calibration series

### Run 290
**Duration**: 43.6 seconds (short, 48th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan for port 22 and 202. Retardation 175 V, Bias 1200 V
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 175V and bias 1200V, part of systematic detector voltage calibration

### Run 291
**Duration**: 38.2 seconds (very short, 24th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan for port 22 and 202. Retardation 175 V, Bias 1300 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 175V and bias 1300V, continuing systematic detector voltage calibration series

### Run 292
**Duration**: 38.3 seconds (short, 25th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan for port 22 and 202. Retardation 175 V, Bias 1350 V
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 175V and bias 1350V, part of methodical detector voltage calibration

### Run 293
**Duration**: 15.2 minutes (very long, 98th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan for port 22 and 202. Retardation 175 V, Bias 1400 V
- Timed run with 240000 events Scan exited after 1 steps with status: success Which probably means the scan was "stopped" before it finished, not "aborted", because the scan should have had 3 steps

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 175V and bias 1400V, though scan was stopped early after 1 step instead of 3

### Run 294
**Duration**: 39.0 seconds (short, 37th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Bias scan for port 22 and 202. Retardation 175 V, Bias 1400 V
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Bias scan for port 22 and 202. Retardation 175 V, Bias 1450 V

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 175V and bias 1400V/1450V, continuing systematic detector calibration series

### Run 295
**Duration**: 38.8 seconds (short, 32nd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: medium
**Key evidence**: Timed run with 240000 events completing 3 steps, consistent with bias scan pattern of surrounding runs though specific bias values not mentioned

### Run 296
**Duration**: 38.8 seconds (short, 32nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan for port 22 and 202. Retardation 175 V, Bias 1500 V.
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 175V and bias 1500V, continuing systematic detector voltage calibration

### Run 297
**Duration**: 39.1 seconds (short, 37th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Bias scan for port 22 and 202. Retardation 175 V, Bias 1550 V
- Timed run with 240000 events Scan exited after 3 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 175V and bias 1550V, part of methodical detector voltage calibration series

### Run 298
**Duration**: 38.9 seconds (short, 35th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Bias scan for port 22 and 202. Retardation 175 V, Bias 1600 V
- Timed run with 240000 events Scan exited after 3 steps with status: success
- We are changing the transmission from 2.5% (~8 uJ) to high count mode.
- FZP and intensifier conditions for 400 eV and 130 uJ; 8.29 kHz Device: Position: 0 Intensifier MCP [V] 719 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 8...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Bias scan for ports 22 and 202 with retardation 175V and bias 1600V, with additional FZP and intensifier settings adjustments for 400 eV

### Run 299
**Duration**: 39.1 seconds (short, 38th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Timed run with 240000 events Scan exited after 3 steps with status: success
- Changed the transmission to 100 uJ (40%). Bias 1500 V for Port 22, 202.
- Retardation 175.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Changed transmission to 100 uJ (40%) with bias 1500V for ports 22 and 202, retardation 175V, continuing detector calibration with modified parameters

### Run 300
**Duration**: 1.1 minutes (medium, 59th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 480000 events Scan exited after 6 steps with status: success
- High Count mode. Needle position is 116.96. We are at full transmission at 100%., 200uJ.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: High count mode test with full transmission (100%, 200uJ) and needle position adjustment, testing detector response at maximum intensity

### Run 301
**Duration**: 1.1 minutes (medium, 62nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- We are redoing the run 300 at high count mode.
- Timed run with 480000 events Scan exited after 6 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Redoing run 300 at high count mode, continuing the detector calibration series with identical parameters to test reproducibility

### Run 302
**Duration**: 1.2 minutes (medium, 62nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 480000 events Scan exited after 6 steps with status: success
- Turned on the Port 0, 180 with amplifier. Bias at 1400. Port 22, 202 without amplifiers.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Configuration change to test ports 0 and 180 with amplifier at bias 1400V, while ports 22 and 202 without amplifiers - detector calibration

### Run 303
**Duration**: 2.1 minutes (long, 78th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- We will do a needle scan at this mode. Port 0 and 180 with amp. Port 22 and 202 without amplifier. Needle starting position 116.958.
- Timed run with 960000 events Scan exited after 12 steps with status: success
- settings

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Needle scan with specific port configuration (0/180 with amp, 22/202 without) to calibrate detector response at different needle positions

### Run 304
**Duration**: 2.1 minutes (long, 79th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Changed the retardation to 125 for all four TOFs (POrt 0 and 180 with amplifier, Port 22 and 202 without). Spectral reconstruction mode (!)
- Needle position at the start
- Timed run with 960000 events Scan exited after 12 steps with status: success
- Needle end position

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Changed retardation to 125V for all four TOFs with specific amplifier configuration and spectral reconstruction mode, needle position scan

### Run 305
**Duration**: 2.1 minutes (long, 78th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Needle starting position. Redoing run 304. Going in with the needle again.
- Timed run with 960000 events Scan exited after 12 steps with status: success
- Needle end position
- We changed the sample to NNO

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Redoing run 304 with needle scan, followed by sample change to NNO - final calibration before transitioning to sample measurements

### Run 306
**Duration**: 1.4 minutes (medium, 70th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Scan hf_w: [390. 395. 400. 405. 410. 415. 420. 425.] 80000 events/step Scan exited after 8 steps with status: success
- 30% transmission
- Photon energy scan from 390 eV to 425 eV with NNO at retardation = 0

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan from 390-425 eV with NNO sample at 30% transmission, collecting scientific data on nitrogen oxide

### Run 307
**Duration**: 1.5 minutes (medium, 70th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- NNO with 30% transmission.
- Redoing the run 306. NNO, photon energy scan from 390 eV to 425 eV at 5 eV step. Retardation = 0.
- repeat previous scan. NNO, 30% transmission, photon energy scan.
- Scan hf_w: [390. 395. 400. 405. 410. 415. 420. 425.] 80000 events/step Scan exited after 8 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Repeat of run 306 with NNO sample, photon energy scan from 390-425 eV at 5 eV steps, collecting scientific data

### Run 308
**Duration**: 2.7 minutes (long, 83rd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Scanning photon energy from 390 eV to 425 eV at 5 eV step. Retardation 0 V.
- 30% transmission.
- Scan hf_w: [390. 395. 400. 405. 410. 415. 420. 425.] 80000 events/step Scan exited after 16 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Extended photon energy scan from 390-425 eV with NNO sample at 30% transmission, doubling the statistics (16 steps vs 8 in previous runs)

### Run 309
**Duration**: 3.4 minutes (long, 88th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Increased the photon energy range from 390 to 435 eV at 5 eV steps. Retardation 0 V. We will scan retardation after this run.
- Scan hf_w: [390. 395. 400. 405. 410. 415. 420. 425. 430. 435.] 80000 events/step Scan exited after 20 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Expanded photon energy range scan from 390-435 eV with NNO sample, continuing scientific data collection with broader energy range

### Run 310
**Duration**: 4.0 minutes (very long, 96th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Increased the photon energy range from 380 eV and 435 eV. Retardation 0 V. We are still scanning to find the edge for NNO near N.
- Transmission 30%.
- Scan hf_w: [380. 385. 390. 395. 400. 405. 410. 415. 420. 425. 430. 435.] 80000 events/step Scan exited after 24 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Further expanded photon energy scan from 380-435 eV with NNO sample, specifically searching for nitrogen edge in NNO

### Run 311
**Duration**: 5.3 minutes (very long, 97th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- We found the NNO N-edge at 403 eV. Now doing a proper scan from 405 eV to 442.5 eV at a 2.5 eV step. 30% transmission. Retardation = 0 V.
- Scan hf_w: [405. 407.5 410. 412.5 415. 417.5 420. 422.5 425. 427.5 430. 432.5 435. 437.5 440. 442.5] 80000 events/step Scan exited after 32 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Detailed photon energy scan (405-442.5 eV) at 2.5 eV steps after identifying the NNO N-edge at 403 eV, collecting scientific data with optimized parameters

### Run 312
**Duration**: 5.3 minutes (very long, 97th percentile)
**Total entries**: 6 (6 unique)
**Activities**:
- We changed the retardation to -5 V. Doing a photon energy scan from 405 to 442.5 eV at 2.5 eV step.
- Scan hf_w: [405. 407.5 410. 412.5 415. 417.5 420. 422.5 425. 427.5 430. 432.5 435. 437.5 440. 442.5] 80000 events/step Scan exited after 32 steps with status: success
- FZP positions for 410 N before tweaking to have 415 eV at the middle.
- After adjust FZP position before changing the YAG. Device: Position: 0 Intensifier MCP [V] 799 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 8135.0 4 soli...
- FZP settings after adjusting to center the spectral range between 420 and 435 eV. Device: Position: 0 Intensifier MCP [V] 824 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Inte...
- starting retardation and photon eneryg scan.

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan with NNO sample at -5V retardation, with FZP adjustments to center the spectral range for optimal scientific data collection

### Run 313
**Duration**: 2.4 minutes (long, 82nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Changed the FZP settings to accomodate from 420 eV to 432.5 eV. We are doing the photon energy scan at retardation = 0.
- Scan hf_w: [420. 422.5 425. 427.5 430. 432.5 465. ] 80000 events/step Scan exited after 14 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan from 420-432.5 eV with adjusted FZP settings to accommodate specific energy range for NNO sample measurements

### Run 314
**Duration**: 2.4 minutes (long, 81st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Changed the retardation to 5 V. Scanning the photon energy from 420 eV to 465 eV. Compare with 313. Transmission is still 30% (XGMD ~ 38 uJ)
- Scan hf_w: [420. 422.5 425. 427.5 430. 432.5 465. ] 80000 events/step Scan exited after 14 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Continuation of NNO sample measurements with changed retardation (5V) while maintaining same photon energy scan range, explicitly comparing with run 313

### Run 315
**Duration**: 2.4 minutes (long, 82nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Changed the retardation 10 V. Photon energy scan from 420 eV to 465 eV
- Scan hf_w: [420. 422.5 425. 427.5 430. 432.5 465. ] 80000 events/step Scan exited after 14 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Systematic measurement with NNO sample at 10V retardation, continuing the photon energy scan series with same parameters except retardation voltage

### Run 316
**Duration**: 2.4 minutes (long, 81st percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Changed the retardation to 10 V. Photon energy scan from 420 eV to 465 eV
- Changed the retardation to 15 V. Photon energy scan from 420 eV to 465 eV
- Retardation 15 V
- Scan hf_w: [420. 422.5 425. 427.5 430. 432.5 465. ] 80000 events/step Scan exited after 14 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Continuation of systematic NNO measurements with increased retardation to 15V, maintaining same photon energy scan parameters

### Run 317
**Duration**: 38.2 seconds (very short, 19th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Changed the retardation to 40 V. Moved the photon energy to 465 eV. No scan of photon energy
- Timed run with 240000 events Scan exited after 3 steps with status: success
- single photon energy, 465 eV. 40V retardation.

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Single photon energy (465 eV) measurement with 40V retardation on NNO sample, part of systematic retardation study

### Run 318
**Duration**: 44.2 seconds (short, 49th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- single photon energy, 465 eV. 45V retardation.
- Changed the retardation to 45 V. Photon energy is 465 eV.
- Timed run with 240000 events Scan exited after 3 steps with status: success
- FZP settings for retardation scan between 420 eV and 465 eV. Device: Position: 0 Intensifier MCP [V] 824 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 813...

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Single photon energy (465 eV) measurement with increased retardation (45V) on NNO sample, continuing systematic parameter exploration

### Run 319
**Duration**: 2.5 minutes (long, 82nd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Pre-edge scan NNO 400-415
- Scan hf_w: [400. 402.5 405. 407.5 410. 412.5 415. ] 83000 events/step Scan exited after 14 steps with status: success
- FZP settings for NNO pre-edge resonance scan. Device: Position: 0 Intensifier MCP [V] 824 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 0.0 4 solid_att TA...

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Pre-edge resonance scan of NNO sample from 400-415 eV, specifically targeting the nitrogen edge region identified in earlier runs

### Run 320
**Duration**: 48.9 seconds (medium, 53rd percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Timed run with 249000 events Scan exited after 4 steps with status: success
- FZP position for 530 eV
- 515 eV, 0 V retardation.
- FZP settings for 515 ev photon energy. Device: Position: 0 Intensifier MCP [V] 849 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 0.0 4 solid_att TARGET1 5...

**Run classification**: calibration_run
**Confidence**: medium
**Key evidence**: FZP position adjustment for 530 eV and settings for 515 eV photon energy, appears to be spectral calibration rather than sample measurement

### Run 321
**Duration**: 49.8 seconds (medium, 54th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- 515 eV, 50 V retardation, NNO
- Timed run with 249000 events Scan exited after 4 steps with status: success
- Changed the retardation to 50 V. Photon energy at 515 eV

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Systematic measurement of NNO sample at 515 eV with 50V retardation, continuing the retardation study pattern from previous runs

### Run 322
**Duration**: 49.0 seconds (medium, 54th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Changed the retardation to 90 V. Photon energy of 515 eV.
- Timed run with 249000 events Scan exited after 4 steps with status: success
- 515 eV, 90 V retardation, NNO

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Continuation of NNO sample measurements at 515 eV with increased retardation (90V), part of systematic parameter exploration

### Run 323
**Duration**: 48.9 seconds (medium, 53rd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- 515 eV, 95 V retardation, NNO
- Changed the retardation to 95 V. Photon energy of 515 eV
- Timed run with 249000 events Scan exited after 4 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: NNO sample measurement at 515 eV with 95V retardation, continuing the systematic retardation study series

### Run 324
**Duration**: 58.8 seconds (medium, 55th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- 615 eV, 0 V retardation, NNO
- Photon energy 615 eV, retardation 0 .
- Timed run with 332000 events Scan exited after 5 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: NNO sample measurement at higher photon energy (615 eV) with 0V retardation, starting new energy series

### Run 325
**Duration**: 1.0 minutes (medium, 57th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Photon energy 615 ev. Retardation 50 V.
- 615 eV, 50 V retardation, NNO
- Timed run with 332000 events Scan exited after 5 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Continuation of NNO measurements at 615 eV with 50V retardation, part of systematic parameter exploration

### Run 326
**Duration**: 59.8 seconds (medium, 57th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- 615 eV, 100 V retardation, NNO
- Photon energy 615 ev. Retardation 100 V
- Timed run with 332000 events Scan exited after 5 steps with status: success Average Duty Cycle: 0.978

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: NNO sample measurement at 615 eV with 100V retardation, continuing systematic retardation study at higher photon energy

### Run 327
**Duration**: 59.8 seconds (medium, 57th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- 615 eV, 150 V retardation, NNO
- Photon energy 615 eV. Retardation 150 V.
- Timed run with 332000 events Scan exited after 5 steps with status: success Average Duty Cycle: 0.979

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: NNO sample measurement at 615 eV with 150V retardation, continuing systematic parameter exploration

### Run 328
**Duration**: 59.7 seconds (medium, 56th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- 615 eV, 190 V retardation, NNO
- Photon energy 615 eV. Retardation 190 V
- Timed run with 332000 events Scan exited after 5 steps with status: success Average Duty Cycle: 0.978

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: NNO sample measurement at 615 eV with 190V retardation, part of systematic retardation study series

### Run 329
**Duration**: 59.8 seconds (medium, 56th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- 615 eV, 195 V retardation, NNO
- Photon energy 615 eV. Retardation 195 V
- Timed run with 332000 events Scan exited after 5 steps with status: success Average Duty Cycle: 0.975

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: NNO sample measurement at 615 eV with 195V retardation, fine-tuning the retardation parameter at high values

### Run 330
**Duration**: 59.6 seconds (medium, 56th percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- 615 eV, 195 V retardation, NNO
- Timed run with 332000 events Scan exited after 5 steps with status: success Average Duty Cycle: 0.980
- FZP settings for XLEAP tuning shift. N1 FZP 405 eV, ~15uJ, no Att paddle. Device: Position: 0 Intensifier MCP [V] 749 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier ...
- Optimized position for5 fzp yag x and y and thorlabs lens x. view on sp1k4 gige and im5k4 camviewer
- FZP after a little more optimization. Device: Position: 0 Intensifier MCP [V] 819 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 100.0 4 solid_att OUT 5 so...

**Run classification**: calibration_run
**Confidence**: medium
**Key evidence**: FZP settings optimization for XLEAP tuning, position optimization for FZP YAG and Thorlabs lens, despite NNO sample mention

### Run 331
**Duration**: 17.8 seconds (very short, 1st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Timed run with 1000 events Scan exited after 2 steps with status: success Average Duty Cycle: 0.974

**Run classification**: diagnostic_run
**Confidence**: medium
**Key evidence**: Very short run (17.8s) with minimal information, likely a quick system check based on the small number of events (1000) and duty cycle verification

### Run 332
**Duration**: 2.4 minutes (long, 81st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Save some XLEAP data for David.

**Run classification**: measurement_run
**Confidence**: medium
**Key evidence**: Longer run (2.4 minutes) specifically to save XLEAP data for scientific analysis by researcher (David)

### Run 333
**Duration**: 17.6 seconds (very short, 1st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 1000 events Scan exited after 2 steps with status: success Average Duty Cycle: 0.955
- Save some XLEAP data for David.

**Run classification**: measurement_run
**Confidence**: medium
**Key evidence**: Continuation of run 332, saving XLEAP data for scientific analysis, despite short duration

### Run 334
**Duration**: 41.2 seconds (short, 44th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- 200 um LTUS for River
- Timed run with 1000 events Scan exited after 2 steps with status: success Average Duty Cycle: 0.985

**Run classification**: diagnostic_run
**Confidence**: medium
**Key evidence**: Testing with 200 um LTUS configuration for researcher (River), short run with minimal events suggests system verification rather than full measurement

### Run 335
**Duration**: 41.0 seconds (short, 43rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 1000 events Scan exited after 2 steps with status: success Average Duty Cycle: 0.988
- spreader R56 in for River

**Run classification**: diagnostic_run
**Confidence**: medium
**Key evidence**: Testing spreader R56 configuration for researcher (River), continuation of diagnostic testing from run 334

### Run 336
**Duration**: 38.6 seconds (short, 28th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 3000 events Scan exited after 6 steps with status: success Average Duty Cycle: 0.954
- ~400 eV run taking FZP spectra during ACR commissioning

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: FZP spectra collection at ~400 eV during ACR commissioning, focused on spectral characterization

### Run 337
**Duration**: 38.5 seconds (short, 27th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- +5 eV from previous run
- Timed run with 3000 events Scan exited after 6 steps with status: success Average Duty Cycle: 0.955

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of FZP spectral calibration with +5 eV energy shift from previous run, part of systematic energy scan

### Run 338
**Duration**: 38.5 seconds (short, 27th percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- Timed run with 3000 events Scan exited after 6 steps with status: success Average Duty Cycle: 0.952
- -5 eV from original point, -10 fromprevisou run
- fzp condition
- FZP after a little more optimization. for XLEAP mode tuning, 8 uJ pulse energy from XGMD; 102 Hz Device: Position: 0 Intensifier MCP [V] 799 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 9...
- FZP positions and settings

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: FZP optimization and spectral calibration with -5 eV from original point, continuing systematic energy scan with XLEAP mode tuning

### Run 339
**Duration**: 38.6 seconds (short, 28th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 3000 events Scan exited after 6 steps with status: success Average Duty Cycle: 0.951
- move SP1K4-YAG by 0.1 mm to check any dust on the yag surface; run339 Device: Position: 0 Intensifier MCP [V] 829 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig...

**Run classification**: diagnostic_run
**Confidence**: high
**Key evidence**: Diagnostic check of SP1K4-YAG by moving 0.1mm to check for dust on YAG surface, troubleshooting image quality issue

### Run 340
**Duration**: 38.7 seconds (short, 29th percentile)
**Total entries**: 21 (21 unique)
**Activities**:
- Timed run with 3000 events Scan exited after 6 steps with status: success Average Duty Cycle: 0.944
- back to sp1k4-yag +4mm that has a dust on the surface
- We found that there is a bad pixel on the piranha (1090) when the sp1k4-yag-y is at +4.00mm; we move the yag-y by 0.1 mm up to 4.1 mm and we are able to eliminate the dead pixel on the spectrum. This ...
- elog FZP condition after XLEAP testing today Device: Position: 0 Intensifier MCP [V] 829 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 100.0 4 solid_att T...
- adjust baseline offset to give more "space" for large signals.
- Beam on IM2K0. Unpointed.
- Beam on IM1K4. Looks weird as usual.
- alignment on the im2k4; 150 uK and 8.29 kHz
- We found SL2K0 wide open after RIX shift. This is the position that it was left at. We will change the gap now.
- We moved the SL2K0 to this position. This cleared the fault.
- Beam on IM3K4. Unpointed.
- Beam on IM5K4. Unpointed.
- Beam on IM5K4. After pointing. We had to move undulator X +300 um.
- after did the undulator pointing +300 um in horizontal (undo RIX's -300 um in horizontal last night); alignment looks better
- SL2K0 before optimizing to reduce cutting the beam on IM5K4.
- Slits position after optimization using Im5K4
- Beam after optmizing slit positions.
- TMO_KBO1 transmission: 157.94487502992672. scan data path: /reg/g/pcds/pyps/apps/hutch-python/tmo/tmo/mirror-check/scans/TMO_KBO1/TMO_KBO1_2024-11-03--07-59-16.h5
- check KBO transmission ( check_kbo1_transmission() ); but the first time seems not working properly; need to repeat again
- beam tripped during the last transmission check
- elog FZP and sp1k4-att conditions; not using intensifier now because accessing the hutch Device: Position: 0 Intensifier MCP [V] 599 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231...

**Run classification**: commissioning_run
**Confidence**: high
**Key evidence**: Extensive beamline commissioning activities including beam pointing, slit optimization, KBO transmission checks, and FZP condition verification after XLEAP testing

### Run 341
**Duration**: 19.3 seconds (very short, 3rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 83000 events Scan exited after 5 steps with status: success
- Retardation = 0. No gas. Just background gas in the chamber.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Background gas measurement with 0V retardation to establish baseline for subsequent retardation voltage scans

### Run 342
**Duration**: 18.8 seconds (very short, 2nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Timed run with 83000 events Scan exited after 5 steps with status: success
- Retardation = 100 V. Background only. Transmission 100%.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Systematic retardation voltage scan (100V) with background measurement, part of detector calibration sequence

### Run 343
**Duration**: 18.8 seconds (very short, 2nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 125 V. Background only. Transmission 100%.
- Timed run with 83000 events Scan exited after 5 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of retardation voltage scan (125V) with background measurement, systematic calibration of detector response

### Run 344
**Duration**: 18.9 seconds (very short, 2nd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- For FEX checkout. Wanted to see if we can see the hits.
- adjust ymin after adjusting baseline.
- adjust ymax based on new baseline

**Run classification**: diagnostic_run
**Confidence**: high
**Key evidence**: FEX checkout to verify hit detection and adjustment of baseline parameters for signal detection

### Run 345
**Duration**: 14.2 seconds (very short, 1st percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- Timed run with 41500 events Scan exited after 1 steps with status: success
- run for ryan
- check the new fex parameters
- Counts Per Shot for run 345
- Gas pressure of Argon for this shift.

**Run classification**: diagnostic_run
**Confidence**: high
**Key evidence**: Testing new FEX parameters and checking counts per shot with Argon gas, verifying detector performance

### Run 346
**Duration**: 3.2 minutes (long, 87th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Retardation = 0, Transmission = 100%, Needle position Z = 95.056.
- We are scanning photon energy from 390 to 408 eV at 2 eV steps.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Systematic photon energy scan from 390-408 eV with Argon gas at 0V retardation, collecting spectroscopic data

### Run 347
**Duration**: 3.1 minutes (long, 86th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Retardation = 100, Transmission = 100%, Needle position Z = 95.056.
- 400 eV center scan from 390 to 408 eV; 2eV step; after tuning the intensifier to align the piranha sensor to the spectrum;
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Continuation of photon energy scan (390-408 eV) with 100V retardation, collecting spectroscopic data on Argon

### Run 348
**Duration**: 3.1 minutes (long, 86th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 125, Transmission = 100%, Needle position Z = 95.056.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Final part of systematic photon energy scan series with 125V retardation, completing spectroscopic measurement set

### Run 349
**Duration**: 16.4 minutes (very long, 99th percentile)
**Total entries**: 7 (7 unique)
**Activities**:
- Moved the needle Z to -5 mm (90.096)
- Retardation = 125, Transmission = 100%, Needle position Z = 90.096.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success
- Compare 348 with 349 for ratio of counts per shot.
- New comparison of 348 and 349
- setup showing unstable triggering of qadc. The blue like is a tpr trigger, green is a laser pulse. The scope looks stable, the qadc is hopping by 40 pixels.
- Moved the needle in to Z = 15 mm (110.064 in the motor)

**Run classification**: measurement_run
**Confidence**: medium
**Key evidence**: Photon energy scan with needle position adjustment to study position-dependent effects, comparing count ratios with run 348

### Run 350
**Duration**: 30.2 minutes (very long, 99th percentile)
**Total entries**: 6 (6 unique)
**Activities**:
- Retardation = 100, Transmission = 100%, Needle position Z = 90.096.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 3 steps with status: success Which probably means the scan was "stopped" before it finished, not "abo...
- This run crashed the daq, and we needed to restart the daq.
- ## we are troubleshooting now and voltage on intensifier is reduced from 820V to 620V; no X-ray now FZP setup for_140 uJ_8.29 kHz and optimized piranha orientation to have 390-408 eV scan. Device: Pos...
- FZP setup for_140 uJ_8.29 kHz and optimized piranha orientation to have 390-408 eV scan. Device: Position: 0 Intensifier MCP [V] 619 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231...
- FZP setup for_140 uJ_8.29 kHz and optimized piranha orientation to have 390-408 eV scan. Device: Position: 0 Intensifier MCP [V] 820 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231...

**Run classification**: diagnostic_run
**Confidence**: high
**Key evidence**: Run crashed DAQ requiring restart, troubleshooting intensifier voltage issues and FZP setup problems

### Run 351
**Duration**: 3.2 minutes (long, 87th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Retardation = 100, Transmission = 100%, Needle position Z = 90.056.
- Needle Z position.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Systematic photon energy scan (390-408 eV) with 100V retardation at specific needle position (90.056), continuing measurement series

### Run 352
**Duration**: 3.1 minutes (long, 85th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 0, Transmission = 100%, Needle position Z = 90.096.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Continuation of systematic photon energy scan series with 0V retardation at needle position 90.096

### Run 353
**Duration**: 3.1 minutes (long, 85th percentile)
**Total entries**: 4 (3 unique)
**Activities**:
- Retardation = 0, Transmission = 100%, Needle position Z = 110.056.
- Retardation = 0, Transmission = 100%, Needle position Z = 115.056.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan at different needle position (110.056/115.056) with 0V retardation, part of position-dependent measurement series

### Run 354
**Duration**: 3.1 minutes (long, 86th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 100, Transmission = 100%, Needle position Z = 110.056
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Continuation of systematic scan series with 100V retardation at needle position 110.056

### Run 355
**Duration**: 3.1 minutes (long, 84th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Retardation = 125, Transmission = 100%, Needle position Z = 110.056.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success
- We moved needle Z = 20 mm (115.039 mm in the motor).

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan with 125V retardation at needle position 110.056, continuing systematic measurement series

### Run 356
**Duration**: 3.1 minutes (long, 84th percentile)
**Total entries**: 10 (10 unique)
**Activities**:
- Retardation = 125, Transmission = 100%, Needle position Z = 115.056.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success
- Runs of different count rates.
- FZP intensifier for run 361
- position before optimizing for hf_w=615 Device: Position: 0 Intensifier MCP [V] 819 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 8135.0 4 solid_att TARGE...
- We have to move the center of the SL1K0 to 0 when we moved to 615. This is the position for 400 eV
- This is the position for SL1K0 when we moved to 615 eV.
- optimzed positions for hf_w=615 Device: Position: 0 Intensifier MCP [V] 749 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 510.0 4 solid_att OUT 5 solid_at...
- optimized positions for hf_w=610-630 Device: Position: 0 Intensifier MCP [V] 799 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 510.0 4 solid_att TARGET2 5...
- We are at 600 eV photon energy. Sample is N2O. We brought the needle to Z= 0 (95.115 mm in the motor).

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Final scan in series at needle position 115.056 with 125V retardation, completing position-dependent measurement set

### Run 357
**Duration**: 3.1 minutes (long, 87th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 100, Transmission = 100%, Needle position Z = 115.056.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan with 100V retardation at needle position 115.056, part of systematic position-dependent study

### Run 358
**Duration**: 3.1 minutes (long, 87th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Retardation = 0, Transmission = 100%, Needle position Z = 115.056.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success
- Moved the needle to Z = -10 (85.165 in the motor)

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan with 0V retardation at needle position 115.056, continuing systematic measurement series

### Run 359
**Duration**: 3.1 minutes (long, 85th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 0, Transmission = 100%, Needle position Z = 85.056.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan with 0V retardation at new needle position (85.056), part of position-dependent measurement series

### Run 360
**Duration**: 3.3 minutes (long, 88th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 100, Transmission = 100%, Needle position Z = 85.056.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Final scan in systematic series with 100V retardation at needle position 85.056, completing position-dependent measurement set

### Run 361
**Duration**: 3.1 minutes (long, 85th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 125, Transmission = 100%, Needle position Z = 85.056.
- Scan hf_w: [390. 392. 394. 396. 398. 400. 402. 404. 406. 408.] 82000 events/step Scan exited after 20 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan with 125V retardation at needle position 85.056, completing systematic position-dependent measurement series

### Run 362
**Duration**: 4.0 minutes (very long, 95th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 0, photon energy from 600 to 630 eV at 2.5 eV step. Sample is N2O. Full transmission (~60 uJ).
- Scan hf_w: [600. 602.5 605. 607.5 610. 612.5 615. 617.5 620. 622.5 625. 627.5 630. ] 82000 events/step Scan exited after 26 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan from 600-630 eV with 0V retardation on N2O sample, systematic data collection with full transmission

### Run 363
**Duration**: 4.0 minutes (very long, 96th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 100 V, photon energy from 600 to 630 eV at 2.5 eV step. N2O. Full transmission (~70 uJ).
- Scan hf_w: [600. 602.5 605. 607.5 610. 612.5 615. 617.5 620. 622.5 625. 627.5 630. ] 82000 events/step Scan exited after 26 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan from 600-630 eV with 100V retardation on N2O sample, continuing systematic retardation series

### Run 364
**Duration**: 4.0 minutes (very long, 95th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 150, photon energy from 600 to 630 eV at 2.5 eV step. Sample is N2O. Full transmission (~60 uJ).
- Scan hf_w: [600. 602.5 605. 607.5 610. 612.5 615. 617.5 620. 622.5 625. 627.5 630. ] 82000 events/step Scan exited after 26 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan from 600-630 eV with 150V retardation on N2O sample, part of systematic retardation voltage series

### Run 365
**Duration**: 4.0 minutes (very long, 95th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 190, photon energy from 600 to 630 eV at 2.5 eV step. Sample is N2O. Full transmission (~70 uJ).
- Scan hf_w: [600. 602.5 605. 607.5 610. 612.5 615. 617.5 620. 622.5 625. 627.5 630. ] 82000 events/step Scan exited after 26 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan from 600-630 eV with 190V retardation on N2O sample, continuing systematic retardation series

### Run 366
**Duration**: 4.0 minutes (very long, 96th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Retardation = 195, photon energy from 600 to 630 eV at 2.5 eV step. Sample is N2O. Full transmission (~70 uJ).
- Scan hf_w: [600. 602.5 605. 607.5 610. 612.5 615. 617.5 620. 622.5 625. 627.5 630. ] 82000 events/step Scan exited after 26 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan from 600-630 eV with 195V retardation on N2O sample, final scan in systematic retardation series

### Run 367
**Duration**: 4.0 minutes (very long, 96th percentile)
**Total entries**: 10 (10 unique)
**Activities**:
- Retardation = 50, photon energy from 600 to 630 eV at 2.5 eV step. Sample is N2O. Full transmission (~70 uJ).
- Scan hf_w: [600. 602.5 605. 607.5 610. 612.5 615. 617.5 620. 622.5 625. 627.5 630. ] 82000 events/step Scan exited after 26 steps with status: success
- x-ray and laser overlapped on the ATM paddle
- Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] -0.005177 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31094.815000 4 lxt total delay [ns] 31094.815000 5 txt user stage [mm] -72.000030
- timing at ATM. coarse
- the control loop for the gas attenuator has trouble regulating the pressure at moderate (10-80 %) transmission values.
- Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] -0.004270 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31094.846500 4 lxt total delay [ns] 31094.846500 5 txt user stage [mm] -72.000013
- found ATM fine timing
- nicer edge on target2b
- edge on target3b

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: X-ray and laser overlap on ATM paddle, timing optimization with entries about 'timing at ATM', 'found ATM fine timing'

### Run 368
**Duration**: 5.2 minutes (very long, 97th percentile)
**Total entries**: 14 (14 unique)
**Activities**:
- data taking with ATM target2b
- Settings for timing measurement. Device: Position: 0 ATM MR tip 1311 1 ATM MR tilt 1329 2 ATM target TARGET2b 3 ATM y-Motor -41.25145 4 tm1k4_target TARGET2b 5 tm1k4_x_motor 11.40675 6 tm1k4_y_motor -...
- Laser X-ray spatial overlap at IP1 clear yag
- coarse timing at the IP. This is further off than we initially expected. Device: Position: 0 lxt pos [ps] 14200.000000 1 txt pos [ps] 0.005070 2 lxt_ttc pos [ps] 14200.000000 3 lxt offset [ns] 31094.8...
- coarse timing at the IP. Zeroed lxt at this position. Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] 0.000374 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31080.646500 4 lxt total delay [ns...
- KB1 position before moving to preset position 50umIP_z50mm Device: Position: 0 mr2k4 bender_ds 19.145084 1 mr2k4 bender_us 13.52501 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.369935 4 mr2k4 x 1.187755 5 ...
- Move KB1 to preset position 50umIP_z50mm Device: Position: 0 mr2k4 bender_ds 20.567307 1 mr2k4 bender_us 14.955191 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.39139 4 mr2k4 x 1.18774 5 mr2k4 y 3.001185 6 ...
- move to new position
- Temporary position of the SiN for fine timing at the IP
- The position of the SiN for X-ray laser overlap.
- X-ray laser on the SMA tip. Note the position. This is where we found the time overlap after realizing about goose timing early on.
- Repeat coarse timing at IP. The previous attempts were done by timing the goose to the x-rays. Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] 0.003683 2 lxt_ttc pos [ps] 0.000000 3 lxt offse...
- this was done with the goose enabled, and the scope was locked to the goose.
- this was done with the goose trigger locked to the scope, and we timed the goose.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Extensive timing activities including 'coarse timing at the IP', 'X-ray laser overlap', LXT/TXT adjustments, and timing with goose trigger

### Run 369
**Duration**: 16.0 seconds (very short, 1st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-1.e-10 -5.e-11 0.e+00 5.e-11 1.e-10] 5000 events/step Scan exited after 10 steps with status: success
- starting with run 369 we are scanning timing on the sample paddle.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT timing scan on sample paddle, explicitly noted as 'scanning timing on the sample paddle'

### Run 370
**Duration**: 1.5 minutes (medium, 71st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.e-10 -5.e-11 0.e+00 5.e-11 1.e-10] 5000 events/step Scan exited after 100 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Extended LXT timing scan with 100 steps, continuing timing optimization from previous run

### Run 371
**Duration**: 3.4 minutes (long, 88th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-1.e-10 -5.e-11 0.e+00 5.e-11 1.e-10] 83000 events/step Scan exited after 20 steps with status: success
- fine timing between lxt = -50 and 50 ps

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT timing scan with fine timing between -50 and 50 ps, continuing the timing optimization sequence from previous runs

### Run 372
**Duration**: 3.7 minutes (long, 89th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-5.e-11 -4.e-11 -3.e-11 -2.e-11 -1.e-11 0.e+00 1.e-11 2.e-11 3.e-11 4.e-11 5.e-11] 83000 events/step Scan exited after 22 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Detailed LXT timing scan with 11 delay points between -50ps and +50ps, higher resolution continuation of previous timing optimization

### Run 373
**Duration**: 1.8 minutes (medium, 73rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-5.e-11 -4.e-11 -3.e-11 -2.e-11 -1.e-11 0.e+00 1.e-11 2.e-11 3.e-11 4.e-11 5.e-11] 83000 events/step Scan exited after 9 steps with status: success Which probably means the scan was "stoppe...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Same LXT timing scan pattern as run 372 but stopped early, continuing the timing optimization sequence

### Run 374
**Duration**: 1.8 minutes (medium, 73rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-3.0e-11 -2.5e-11 -2.0e-11 -1.5e-11 -1.0e-11] 83000 events/step Scan exited after 10 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Focused LXT timing scan with 5 delay points between -30ps and -10ps, narrowing down optimal timing region

### Run 375
**Duration**: 3.4 minutes (long, 88th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-3.0e-11 -2.5e-11 -2.0e-11 -1.5e-11 -1.0e-11] 83000 events/step Scan exited after 20 steps with status: success
- scaning the delay from -30 ps to -10 ps

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT timing scan explicitly noted as 'scanning the delay from -30 ps to -10 ps', continuing timing optimization

### Run 376
**Duration**: 6.0 minutes (very long, 98th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-3.00e-11 -2.75e-11 -2.50e-11 -2.25e-11 -2.00e-11 -1.75e-11 -1.50e-11 -1.25e-11 -1.00e-11] 83000 events/step Scan exited after 36 steps with status: success
- scanning delays with 2.5ps steps

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Detailed LXT timing scan with 2.5ps steps, further refining the timing optimization in the -30ps to -10ps range

### Run 377
**Duration**: 3.1 minutes (long, 84th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Scan lxt: [-2.5e-11 -2.4e-11 -2.3e-11 -2.2e-11 -2.1e-11 -2.0e-11 -1.9e-11 -1.8e-11 -1.7e-11] 83000 events/step Scan exited after 18 steps with status: success
- scanning delay with 1ps step
- Position of the beam on SiN (the cursors on MRCO_GIGE 01 and 02. X-ray and laser are spatially overlapped completely on MRCO_GIGE_02.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Fine LXT timing scan with 1ps steps and spatial overlap verification on SiN, final precision timing optimization

