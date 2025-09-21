# Experiment tmol1034523 - Logbook Analysis

**Total runs with logbook entries**: 123

## Run-by-Run Activities

### Run 1
**Duration**: 12.9 seconds (very short, 2nd percentile)
**Total entries**: 7 (7 unique)
**Activities**:
- run 1 is test run after elog switch
- Beam on MRCO_GIGE4
- Beam on MRCO_GIGE01
- Beam on MRCO_GIGE02
- x-rays on the atm
- beam on im2k4; SASE
- on SP1K4-ATT at 690 eV; by passed this

**Run classification**: commissioning_run
**Confidence**: high
**Key evidence**: Test run after elog switch with beam checks on multiple detectors (MRCO_GIGE4, MRCO_GIGE01, MRCO_GIGE02) and initial system verification

### Run 2
**Duration**: 21.9 seconds (very short, 5th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- CF4 at 690 eV reported energy. Interleaved retardation with 630 V retardation for port 0, 90, 180, and 270. The rest of the TOF is at 20 V retardation.
- 690 eV, FZP-690-1 setting, SP1K4-ATT target 1, 42 uJ at 510 Hz Device: Position: 0 Intensifier MCP [V] 669 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 5...
- setting screen shot

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: CF4 at 690 eV with interleaved retardation voltage settings (630V for specific ports, 20V for others) and intensifier settings adjustment

### Run 3
**Duration**: 40.5 seconds (very short, 9th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan hf_w: [665 667 669 671 673 675 677 679 681 683 685 687 689 691 693 695 697 699 701 703 705] 13000 events/step Scan exited after 21 steps with status: success

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Photon energy scan (hf_w) from 665-705 eV with 13000 events per step

### Run 4
**Duration**: 21.8 seconds (very short, 4th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan hf_w: [665. 667. 669. 671. 673. 675. 677. 679. 681. 683. 685. 687. 689. 691. 693. 695. 697. 699. 701. 703. 705.] 14300 events/step Scan exited after 7 steps with status: success Which probably me...

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Continuation of photon energy scan (hf_w) from 665-705 eV with 14300 events per step

### Run 5
**Duration**: 6.9 minutes (long, 87th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Scan hf_w: [665. 667. 669. 671. 673. 675. 677. 679. 681. 683. 685. 687. 689. 691. 693. 695. 697. 699. 701. 703. 705.] 14300 events/step Scan exited after 42 steps with status: success
- for run 5 the intensifier was running at 720 V. we dropped to 670 V for run 6
- Photon energy scan. Sample CF4. We are in interleaved retardation mode with 0, 90, 180, 270,
- Run 5: Photon energy scan. Sample CF4. We are in interleaved retardation mode with 0, 90, 180, 270 at 630 V retardation, and the rest of the TOFs are at 20 V retardation.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Complete photon energy scan with CF4 sample using interleaved retardation mode (630V/20V) and intensifier voltage adjustment

### Run 6
**Duration**: 6.9 minutes (long, 86th percentile)
**Total entries**: 10 (10 unique)
**Activities**:
- Scan hf_w: [665. 667. 669. 671. 673. 675. 677. 679. 681. 683. 685. 687. 689. 691. 693. 695. 697. 699. 701. 703. 705.] 14300 events/step Scan exited after 42 steps with status: success
- we tweaked the intensifier for XLEAP tuning Device: Position: 0 Intensifier MCP [V] 869 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 30.0 4 solid_att TAR...
- Needle and VAT settings for high count rate.
- x-rays on the atm YAG
- with 0.5 um carbon filter in
- laser on atm. we are going to the diode
- bypassing these faults. they are holding us off beam on the paddle but should be letting us pass.
- having an issue with the pmps for tm1k4. It is holding off beam, possibly because the gas attenuator is having issues regulating the pressure. we are setting the gas attenuator to a lower setting by-h...
- here on GaAs 3 we have the edge at 1000 Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] 0.004376 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31110.441200 4 lxt total delay [ns] 31110.441200...
- Laser / X-ray spatial overlap on the microscope. Using Frosted YAG.

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Laser/X-ray spatial overlap on microscope using frosted YAG and positioning adjustments

### Run 7
**Duration**: 1.8 minutes (short, 30th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Scan lxt: [-5.0e-11 -2.5e-11 0.0e+00 2.5e-11 5.0e-11] 41500 events/step Scan exited after 20 steps with status: success
- Coarse LXT scan at IP
- Sample paddle position for SiN where we see time overlap.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Coarse LXT scan at IP with time ranges of -50ps to +50ps to establish temporal overlap

### Run 8
**Duration**: 1.6 minutes (very short, 21st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-5.0e-12 -2.5e-12 0.0e+00 2.5e-12 5.0e-12] 41500 events/step Scan exited after 16 steps with status: abort
- LXT scan, aborted due to bad LXT range and no apparent signal.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Fine LXT scan with smaller time range (-5ps to +5ps) to refine temporal overlap, aborted due to bad range

### Run 9
**Duration**: 2.2 minutes (short, 36th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-2.5e-11 -2.0e-11 -1.5e-11 -1.0e-11 -5.0e-12 0.0e+00] 41500 events/step Scan exited after 24 steps with status: success
- LXT scan. Possibly signal.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with adjusted time range (-25ps to 0ps) with note about possible signal detection

### Run 10
**Duration**: 2.2 minutes (short, 39th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-2.5e-11 -2.0e-11 -1.5e-11 -1.0e-11 -5.0e-12 0.0e+00] 41500 events/step Scan exited after 24 steps with status: success
- Moved the paddle for more IR transmission, but it looks like we lost the signal. Might be spatial overlap.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Continued LXT scan with same parameters as run 9, with paddle adjustment for IR transmission to improve temporal overlap

### Run 11
**Duration**: 2.2 minutes (short, 38th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Scan lxt: [-2.5e-11 -2.0e-11 -1.5e-11 -1.0e-11 -5.0e-12 0.0e+00] 41500 events/step Scan exited after 24 steps with status: success
- Returned to the sample paddle position of run 10, but the IR on the LI3K4 diode is now much brighter and we do not see a clear signal. We think we damaged the target.
- Histogram of GMD and XGMD. Energy looks like what we want.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with same parameters as previous timing runs (-25ps to 0ps), attempting to find temporal overlap after sample position adjustment

### Run 12
**Duration**: 2.2 minutes (short, 39th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-2.5e-11 -2.0e-11 -1.5e-11 -1.0e-11 -5.0e-12 0.0e+00] 41500 events/step Scan exited after 24 steps with status: success
- Tried a new paddle position but still no signal.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Continued LXT scan with same parameters (-25ps to 0ps) at new paddle position, still searching for temporal overlap signal

### Run 13
**Duration**: 1.9 minutes (short, 34th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-5.0e-12 -2.5e-12 0.0e+00 2.5e-12 5.0e-12] 41500 events/step Scan exited after 20 steps with status: success
- Trying to reproduce run 7 scan range and sample position. Maybe did.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Attempting to reproduce run 7 LXT scan range (-5ps to +5ps) and sample position to find temporal overlap

### Run 14
**Duration**: 4.1 minutes (long, 75th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Filled in the run with a fly scan. Signal is consistent.

**Run classification**: timing_run
**Confidence**: medium
**Key evidence**: Fly scan to fill in timing data, with note that signal is consistent, continuing temporal characterization

### Run 15
**Duration**: 3.2 minutes (medium, 56th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.0e-12 -5.0e-13 0.0e+00 5.0e-13 1.0e-12 1.5e-12 2.0e-12 2.5e-12 3.0e-12] 41500 events/step Scan exited after 36 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Fine LXT scan with narrow time range (-1ps to +3ps) for precise temporal overlap determination

### Run 16
**Duration**: 1.2 minutes (very short, 17th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Narrow LXT window with some fly scanning at the end. No clear signal.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Narrow LXT window with fly scanning, continuing temporal overlap optimization despite no clear signal

### Run 17
**Duration**: 1.8 minutes (short, 26th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-5.0e-11 -2.5e-11 0.0e+00 2.5e-11 5.0e-11] 41500 events/step Scan exited after 20 steps with status: success
- signal is not very clear in this scan. perhaos there is likely not a signal.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with wider range (-50ps to +50ps) to search for temporal overlap signal

### Run 18
**Duration**: 4.6 minutes (long, 78th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- extending the range with hand scanning. Hard to see any signal in this.

**Run classification**: timing_run
**Confidence**: medium
**Key evidence**: Extended range hand scanning for temporal overlap, continuing timing optimization efforts

### Run 19
**Duration**: 1.8 minutes (short, 30th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-5.0e-11 -2.5e-11 0.0e+00 2.5e-11 5.0e-11] 41500 events/step Scan exited after 20 steps with status: success
- not much signal here, but the gmd was also very unstable for this run. repeating

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan (-50ps to +50ps) repeated due to unstable GMD, continuing temporal overlap search

### Run 20
**Duration**: 1.8 minutes (short, 27th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-5.0e-11 -2.5e-11 0.0e+00 2.5e-11 5.0e-11] 41500 events/step Scan exited after 20 steps with status: success
- maybe a signal, maybe the laser is always late in these scan.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan (-50ps to +50ps) with note about possible signal and laser timing relationship

### Run 21
**Duration**: 3.5 minutes (medium, 69th percentile)
**Status**: No logbook entries

**Run classification**: timing_run
**Confidence**: medium
**Key evidence**: No logbook entries but follows multiple timing runs (16-20) and precedes run 22 which is clearly a timing run with LXT scan

### Run 22
**Duration**: 1.8 minutes (short, 28th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [4.00e-10 4.25e-10 4.50e-10 4.75e-10 5.00e-10] 41500 events/step Scan exited after 20 steps with status: success
- maybe there is a signal... hard to make a definitive statement.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with specific timing range (400-500ps) searching for temporal overlap signal

### Run 23
**Duration**: 1.8 minutes (short, 26th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Increased transmission to 20%
- Scan lxt: [4.00e-10 4.25e-10 4.50e-10 4.75e-10 5.00e-10] 41500 events/step Scan exited after 20 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with same timing range as run 22 (400-500ps) but with increased transmission to improve signal detection

### Run 24
**Duration**: 1.8 minutes (very short, 25th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-1.e-10 -5.e-11 0.e+00 5.e-11 1.e-10] 41500 events/step Scan exited after 20 steps with status: success
- not a clear signal

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with different timing range (-100ps to +100ps) continuing temporal overlap search

### Run 25
**Duration**: 1.8 minutes (very short, 23rd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Scan lxt: [-1.e-10 -5.e-11 0.e+00 5.e-11 1.e-10] 41500 events/step Scan exited after 20 steps with status: success
- SiN position wher we saw some big signal.
- bumpled the paddle and the signal returns. It looks like tthis entire scan was after t0

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with note about signal detection after bumping paddle, indicating temporal overlap optimization

### Run 26
**Duration**: 4.4 minutes (long, 77th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- fly scanning to look for t0
- extended range and see a clear t0 between 1.725 and 1.7 ns on lxt. (not so helpful)
- lxt offset Device: Position: 0 lxt pos [ps] 1710.000000 1 txt pos [ps] 0.006084 2 lxt_ttc pos [ps] 1710.000000 3 lxt offset [ns] 31110.441200 4 lxt total delay [ns] 31108.731200 5 txt offset [ns] 5.41...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Fly scanning to find t0, clear identification of temporal overlap between 1.725-1.7ns, LXT offset adjustment

### Run 27
**Duration**: 2.2 minutes (short, 37th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- looks like we have slightly the wrong range..... It looks like we are always laser early.
- Scan lxt: [1.700e-09 1.705e-09 1.710e-09 1.715e-09 1.720e-09 1.725e-09] 41500 events/step Scan exited after 24 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with refined timing range (1.7-1.725ns) based on previous run's t0 finding

### Run 28
**Duration**: 2.5 minutes (medium, 50th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- fly scan to extend the range
- looks like t0 is between 1575 and 1525 on lxt (see timing post for offset).
- lxt offset for run 28. Device: Position: 0 lxt pos [ps] 1545.000000 1 txt pos [ps] 0.005924 2 lxt_ttc pos [ps] 1545.000000 3 lxt offset [ns] 31110.441200 4 lxt total delay [ns] 31108.896200 5 txt offs...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Fly scan to extend timing range, identification of t0 between 1575-1525ps, LXT offset adjustment

### Run 29
**Duration**: 3.8 minutes (medium, 73rd percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- lxt offset for run 28. Device: Position: 0 lxt pos [ps] 1560.000000 1 txt pos [ps] 0.006138 2 lxt_ttc pos [ps] 1560.000000 3 lxt offset [ns] 31110.441200 4 lxt total delay [ns] 31108.881200 5 txt offs...
- signal between 1535 and 1550 on lxt (see fs_timing post for offset).
- Scan lxt: [1.525e-09 1.530e-09 1.535e-09 1.540e-09 1.545e-09 1.550e-09 1.555e-09 1.560e-09 1.565e-09 1.570e-09 1.575e-09] 41500 events/step Scan exited after 44 steps with status: success
- narowing range.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with narrowed timing range (1525-1575ps) based on previous t0 finding, signal identified between 1535-1550ps

### Run 30
**Duration**: 2.5 minutes (medium, 51st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- pretty good t0 signal.
- Scan lxt: [1.5350e-09 1.5375e-09 1.5400e-09 1.5425e-09 1.5450e-09 1.5475e-09 1.5500e-09] 41500 events/step Scan exited after 28 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Further narrowed LXT scan (1535-1550ps) with note about 'pretty good t0 signal' indicating successful temporal overlap

### Run 31
**Duration**: 1.4 minutes (very short, 20th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [1.5370e-09 1.5375e-09 1.5380e-09 1.5385e-09 1.5390e-09 1.5395e-09 1.5400e-09 1.5405e-09 1.5410e-09 1.5415e-09 1.5420e-09 1.5425e-09 1.5430e-09] 41500 events/step Scan exited after 14 steps ...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Very fine LXT scan (1.537-1.543ns) with 0.5ps steps, continuing the timing optimization sequence from previous runs

### Run 32
**Duration**: 3.6 minutes (medium, 71st percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- lxt offset for run 32. Device: Position: 0 lxt pos [ps] 1539.500000 1 txt pos [ps] 0.005817 2 lxt_ttc pos [ps] 1539.500000 3 lxt offset [ns] 31110.441200 4 lxt total delay [ns] 31108.901700 5 txt offs...
- good timing signal at the ip lxt is close to 1537 ps
- Scan lxt: [1.5340e-09 1.5345e-09 1.5350e-09 1.5355e-09 1.5360e-09 1.5365e-09 1.5370e-09 1.5375e-09 1.5380e-09 1.5385e-09 1.5390e-09 1.5395e-09 1.5400e-09] 41500 events/step Scan exited after 40 steps ...
- GMD and XGMD for the last run. Much higher than we used yesterday.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Further refined LXT scan (1.534-1.54ns), identified 'good timing signal at the ip' at 1537ps, LXT offset adjustment

### Run 33
**Duration**: 5.7 minutes (long, 86th percentile)
**Total entries**: 9 (9 unique)
**Activities**:
- t0 with 50 fs precision.
- lxt near t0. Device: Position: 0 lxt pos [ps] 1537.550000 1 txt pos [ps] 0.005711 2 lxt_ttc pos [ps] 1537.550000 3 lxt offset [ns] 31110.441200 4 lxt total delay [ns] 31108.903650 5 txt offset [ns] 5....
- Scan lxt: [1.53750e-09 1.53755e-09 1.53760e-09 1.53765e-09 1.53770e-09 1.53775e-09 1.53780e-09 1.53785e-09 1.53790e-09 1.53795e-09 1.53800e-09 1.53805e-09 1.53810e-09 1.53815e-09 1.53820e-09 1.53825e-...
- This is fine timing on the paddle at IP. Before zeroing LXT. Device: Position: 0 lxt pos [ps] 1537.650000 1 txt pos [ps] 0.005337 2 lxt_ttc pos [ps] 1537.650000 3 lxt offset [ns] 31110.441200 4 lxt to...
- timing edge
- This is fine timing on the paddle at IP. After setting LXT to zero. Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] 0.006031 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31108.903550 4 lxt t...
- laser on atm
- This is coarse timing at the ATM using TXT with LXT set at time overlap at IP1 Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] 1535.051025 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31108....
- Set TXT to 0 Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] 0.000160 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31108.903550 4 lxt total delay [ns] 31108.903550 5 txt offset [ns] 3.882208...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Ultra-fine timing with '50fs precision', zeroing LXT at time overlap, setting up timing at both IP and ATM locations

### Run 34
**Duration**: 4.3 minutes (long, 76th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- collecting tof data while setting ATM timing.
- Fine timing at ATM with fine timing at IP1.
- Set TXT to 0 with fine timing at IP1 and ATM. Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] 0.000587 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31108.903550 4 lxt total delay [ns] 31108....
- run 34 was linear streaking

**Run classification**: measurement_run
**Confidence**: medium
**Key evidence**: Linear streaking data collection with optimized timing at both IP and ATM, 'collecting tof data' indicates scientific measurement

### Run 35
**Duration**: 11.3 minutes (very long, 94th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- looking for streaking while recovering xleap.
- x-rays were blocked..... junk.

**Run classification**: diagnostic_run
**Confidence**: medium
**Key evidence**: Troubleshooting run 'looking for streaking while recovering xleap', noted as 'junk' due to blocked x-rays

### Run 36
**Duration**: 5.7 minutes (long, 84th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- first scan looking for streaking. scanning lxt in the range where we expect streaking.
- Sample CF4, with 70 V retardation.
- stopped run to change the retardation.
- Needle settings for CF4 for run 37

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: First streaking scan with CF4 sample and 70V retardation, scanning LXT in expected streaking range

### Run 37
**Duration**: 18.7 minutes (very long, 98th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Changed the retardation = 0 for all TOF. We are at w/2w.
- Spectra from ~1/4 of the run.
- Pre-edge secondaries visible, Carbon 1s is right most "square ish" peak with beta~1.5, the next left minor peak seems to have beta=2.

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Extended data collection (18.7 min) with CF4 sample at w/2w, retardation=0, spectral features observed including 'Carbon 1s' peak

### Run 38
**Duration**: 3.0 minutes (medium, 54th percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- set txt to center of lxt range
- move txt to the center of the lxt scan range. Hope to see some edges. Device: Position: 0 lxt pos [ps] -3.000000 1 txt pos [ps] -2.957139 2 lxt_ttc pos [ps] -3.000000 3 lxt offset [ns] 31108.903550 4 ...
- gmd/xgmd distribution for run 38
- timing at the end of the shift. Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] -2.953510 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31108.903550 4 lxt total delay [ns] 31108.903550 5 txt ...
- Update tmo preset positions for slits. Axis: Old Preset: New Preset: 0 sl2k0_north 19.5994 19.69870 1 sl2k0_south -13.9991 -15.10050 2 sl2k0_top 19.35025 17.29805 3 sl2k0_bottom -14.44775 -16.00230 4 ...

**Run classification**: timing_run
**Confidence**: medium
**Key evidence**: TXT/LXT adjustments to 'center of lxt scan range', 'timing at the end of the shift' indicates temporal optimization

### Run 39
**Duration**: 4.5 minutes (long, 78th percentile)
**Status**: No logbook entries

**Run classification**: unknown_run
**Confidence**: low
**Key evidence**: No logbook entries available, moderate duration (4.5 min) but insufficient context to determine purpose

### Run 40
**Duration**: 19.1 seconds (very short, 4th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Scan sim_fast_setpoint: [0.1 0.2 0.3] 16600 events/step Scan exited after 6 steps with status: success Average Duty Cycle: 0.883
- Laser positions at the beginning of the shift 2. Device: Position: 0 atm_mr3_tt_tip 1341 1 atm_mr3_tt_tilt 1329 2 att_wp 8.000164 3 ejx_pol -0.010045 4 ejx_qwp 185.002232 5 ejx_shutter close 6 inj_mr ...
- Scan tmo_laser_lens_z: [15. 16. 17. 18. 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32. 33. 34. 35. 36. 37. 38. 39. 40. 41. 42. 43. 44. 45.] 41500 events/step Scan exited after 1 steps with st...

**Run classification**: diagnostic_run
**Confidence**: medium
**Key evidence**: Very short run with system parameter checks including sim_fast_setpoint scan, laser position verification at beginning of shift

### Run 41
**Duration**: 5.7 minutes (long, 85th percentile)
**Total entries**: 7 (7 unique)
**Activities**:
- IR-only lens_z scan to find position of highest IR intensity.
- Scan tmo_laser_lens_z: [15. 16. 17. 18. 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32. 33. 34. 35. 36. 37. 38. 39. 40. 41. 42. 43. 44. 45.] 41500 events/step Scan exited after 62 steps with s...
- Beam on IM1K4. We are setting up for XLEAP tuning.
- Bypassing the SP1K4 issue due to the mismatch between 690 eV FZP pulse energy requirements and what we can actually have from SASE
- Beam on IM2K4, unpointed.
- 690 eV using fzp-690-1, setting same as yesterday, XLEAP mode Device: Position: 0 Intensifier MCP [V] 849 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 10...
- 345 eV and 690 eV with FZP on 690 eV, XGMD is ~6 uJ but this include 345 eV

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: IR-only lens_z scan to find position of highest IR intensity, beam positioning on IM1K4/IM2K4 for XLEAP tuning setup

### Run 42
**Duration**: 5.5 minutes (long, 81st percentile)
**Total entries**: 18 (16 unique)
**Activities**:
- Laser only, Z scan from z = 10 to 40 mm at 1 mm step. Sample is Xenon. IR only 1.3 um.
- Scan tmo_laser_lens_z: [10. 11. 12. 13. 14. 15. 16. 17. 18. 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32. 33. 34. 35. 36. 37. 38. 39.] 41500 events/step Scan exited after 60 steps with statu...
- We are bypassing this pmps error due to 690 eV FZP. The database for PMPS needs to be updated for this error not to occur for this zone plate.
- X-ray only.
- IR overlapped with X-ray at the ATM.
- toggled arbitration status of tm1k4_target
- coarse timing at the ATM Device: Position: 0 lxt pos [ps] -305.000000 1 txt pos [ps] -2.950841 2 lxt_ttc pos [ps] -305.000000 3 lxt offset [ns] 31108.903550 4 lxt total delay [ns] 31109.208550 5 txt o...
- timing - coarse at ATM
- there was a big jump in timing. here are the x-rays
- coarse timing at the ATM after the big jump (1 ns) Device: Position: 0 lxt pos [ps] -30.000000 1 txt pos [ps] -2.950201 2 lxt_ttc pos [ps] -30.000000 3 lxt offset [ns] 31109.208550 4 lxt total delay [...
- Edge on QADC over the past 40 minutes. We see several jumps.
- coarse timing at the ATM after rechecking, we saw 50 ps drift which also seems like it showed up on the QADC Device: Position: 0 lxt pos [ps] 26.000000 1 txt pos [ps] -2.949667 2 lxt_ttc pos [ps] 26.0...
- we are moving out to protect the FZP Device: Position: 0 Intensifier MCP [V] 649 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 510.0 4 solid_att TARGET1 5...
- fine timing at the ATM Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] -2.949774 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31109.223550 4 lxt total delay [ns] 31109.223550 5 txt offset [n...
- we are here at the FZP for F resonance scan Device: Position: 0 Intensifier MCP [V] 649 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 3260.0 4 solid_att T...
- Run 42 is test run for Kurtis

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Multiple coarse and fine timing adjustments at the ATM, timing drift monitoring, and temporal overlap of IR with X-ray

### Run 43
**Duration**: 10.0 seconds (very short, 1st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Timed run with 33000 events Scan exited after 1 steps with status: success

**Run classification**: diagnostic_run
**Confidence**: medium
**Key evidence**: Very short timed run (10 seconds) with 33000 events, likely checking system performance

### Run 44
**Duration**: 1.8 minutes (very short, 24th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan hf_w: [680. 682. 684. 686. 688. 690. 692. 694. 696. 698. 700. 702. 704. 706. 708.] 32000 events/step Scan exited after 30 steps with status: success
- We are doing a photon energy scan with CF4 from 680 to 708 eV. For this run, we set all the TOF to have retardation of 630 V to look mostly at the F edge.

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Photon energy scan with CF4 sample from 680-708 eV with 630V retardation specifically to examine F edge

### Run 45
**Duration**: 3.0 minutes (medium, 55th percentile)
**Total entries**: 23 (23 unique)
**Activities**:
- Photon energy scan with bigger window from 665 to 715 eV at 2 eV step. Same retardation settings as run 44.
- Scan hf_w: [665. 667. 669. 671. 673. 675. 677. 679. 681. 683. 685. 687. 689. 691. 693. 695. 697. 699. 701. 703. 705. 707. 709. 711. 713. 715.] 32000 events/step Scan exited after 52 steps with status:...
- x-rays on atm
- laser on atm
- coarse timing at the ATM Device: Position: 0 lxt pos [ps] -40.000000 1 txt pos [ps] -2.949294 2 lxt_ttc pos [ps] -40.000000 3 lxt offset [ns] 31109.603550 4 lxt total delay [ns] 31109.643550 5 txt off...
- coarse timing at the ATM again Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] -2.949294 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31109.613550 4 lxt total delay [ns] 31109.613550 5 txt o...
- atm on the OPAL. The piranha is looking atound pixel 680, which is a little higher than the edge. This probably means that the x-rays have moved in the vertical direction.
- See fine timing signal on OPAL. We do not see an edge on the Piranha. Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] -2.948600 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31109.608550 4 lx...
- Timing before adjusting anything on txt. Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] -2.946785 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31109.608550 4 lxt total delay [ns] 31109.6085...
- Moved txt to Mats predicted delay to compensate for ND filters. Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] -4.472161 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31109.608550 4 lxt tota...
- Moved lxt to put timing at pixel ~180 on the Opal. Device: Position: 0 lxt pos [ps] -1.570000 1 txt pos [ps] -4.470986 2 lxt_ttc pos [ps] -1.570000 3 lxt offset [ns] 31109.608550 4 lxt total delay [ns...
- Put both lxt and txt offset to 0. Device: Position: 0 lxt pos [ps] 0.00000 1 txt pos [ps] 0.00016 2 lxt_ttc pos [ps] 0.00000 3 lxt offset [ns] 31109.61012 4 lxt total delay [ns] 31109.61012 5 txt offs...
- another edge on OPAL. after adjusting txt and lxt offsets.
- Here's the beam on YAG2 for IM5K4 at 400 eV. We were only seeing timetool signal at the OPAL and not on the Piranha.
- Lens scan before shift: optimal position from z = +32 mm.
- We did the lens Z scan, and found that the focus position is at 32 mm. We are putting lens Z at 30 mm for the angular streaking to avoid being near the Guoy phase.
- Beam on IM5K4 with XLEAP w/2w (345/690)
- Laser positions at the XLEAP/ IR spatial overlap. Device: Position: 0 atm_mr3_tt_tip 1346 1 atm_mr3_tt_tilt 1369 2 att_wp 7.999665 3 ejx_pol -0.010045 4 ejx_qwp 184.992188 5 ejx_shutter open 6 inj_mr ...
- MRCO GIGE4 with IR in the XLEAP position. See the cursor and the paddle position.
- recovered timing on OPAL, txt is best guess from Mat for time offset from 2 x filters Device: Position: 0 lxt pos [ps] 383.615000 1 txt pos [ps] 0.002562 2 lxt_ttc pos [ps] 383.615000 3 lxt offset [ns...
- here is a nice edge but not the nicest we have seen
- we are here for the XLEAP scans we are about to do Device: Position: 0 Intensifier MCP [V] 869 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 0.0 4 solid_a...
- second time this has happened

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Extensive timing adjustments including coarse/fine timing at ATM, txt/lxt offset adjustments, and timing edge optimization on OPAL

### Run 46
**Duration**: 3.4 minutes (medium, 66th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...
- laser shutter closed!!

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, though laser shutter was closed (likely unintentionally)

### Run 47
**Duration**: 4.1 minutes (medium, 73rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- laser shutter closed!!

**Run classification**: diagnostic_run
**Confidence**: medium
**Key evidence**: Run with laser shutter closed, likely checking background or system performance

### Run 48
**Duration**: 13.1 seconds (very short, 3rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, very short run likely testing timing parameters

### Run 49
**Duration**: 3.4 minutes (medium, 59th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- We are doing a 2d scan (photon energy and lxt) to look for angular streaking. The TOFs at port 0, 90, 180, 270 has 630 V retardation. The rest of the TOFs are at 20 V retardation and tuned for Carbon ...
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: 2D scan (photon energy and lxt) specifically to look for angular streaking with TOFs configured for Fluorine resonance

### Run 50
**Duration**: 3.4 minutes (medium, 61st percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- We are doing a 2d scan (photon energy and lxt) to look for angular streaking. The TOFs at port 0, 90, 180, 270 has 630 V retardation and tuine for Fluorine resonance. The rest of the TOFs are at 20 V ...
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: 2D scan (photon energy and lxt) for angular streaking with TOFs configured for both Fluorine and Carbon resonances

### Run 51
**Duration**: 3.4 minutes (medium, 62nd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, continuing the timing optimization sequence from previous runs

### Run 52
**Duration**: 3.4 minutes (medium, 65th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, part of a series of timing optimization runs

### Run 53
**Duration**: 3.4 minutes (medium, 60th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, consistent with timing optimization sequence

### Run 54
**Duration**: 3.0 minutes (medium, 53rd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...
- we suffered a bucket jump again. we recovered timing on the OPAL Device: Position: 0 lxt pos [ps] -383.715000 1 txt pos [ps] 0.004963 2 lxt_ttc pos [ps] -383.715000 3 lxt offset [ns] 31109.226505 4 lx...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with timing recovery after bucket jump, explicit timing parameters mentioned

### Run 55
**Duration**: 3.4 minutes (medium, 58th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, part of timing optimization sequence without 2ω

### Run 56
**Duration**: 3.5 minutes (medium, 68th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, continuing timing optimization without 2ω

### Run 57
**Duration**: 2.6 minutes (medium, 52nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...
- runs 55 - 57 did not have the 2w in

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with explicit note about not having 2ω in, part of timing optimization sequence

### Run 58
**Duration**: 3.4 minutes (medium, 63rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, continuing timing optimization sequence

### Run 59
**Duration**: 3.4 minutes (medium, 65th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, part of consistent timing optimization sequence

### Run 60
**Duration**: 3.4 minutes (medium, 60th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, final run in timing optimization sequence

### Run 61
**Duration**: 30.8 seconds (very short, 8th percentile)
**Status**: No logbook entries

**Run classification**: diagnostic_run
**Confidence**: medium
**Key evidence**: Very short run (30.8s) with no logbook entries, likely a quick system check following timing runs

### Run 62
**Duration**: 1.2 minutes (very short, 17th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- run 62 is 2w=750 eV

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Run with 2ω=750 eV setting, indicating scientific data collection with specific harmonic energy

### Run 63
**Duration**: 2.5 minutes (short, 48th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, continuing timing optimization sequence

### Run 64
**Duration**: 2.5 minutes (short, 49th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...
- we rechecked timing, the edge looked awesome and it had not moved at all

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with explicit note about rechecking timing and edge quality verification

### Run 65
**Duration**: 10.3 seconds (very short, 1st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: medium
**Key evidence**: Very short LXT scan, likely a quick timing verification

### Run 66
**Duration**: 5.3 minutes (long, 80th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...
- Lens positions after stopping lens scan. Device: Position: 0 atm_mr3_tt_tip 1346 1 atm_mr3_tt_tilt 1369 2 att_wp 7.999904 3 ejx_pol -0.012556 4 ejx_qwp 184.994699 5 ejx_shutter open 6 inj_mr 176.99863...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with detailed lens positions recorded, indicating comprehensive timing optimization

### Run 67
**Duration**: 3.4 minutes (medium, 64th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, continuing timing optimization sequence

### Run 68
**Duration**: 3.4 minutes (medium, 57th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, part of consistent timing optimization sequence

### Run 69
**Duration**: 3.4 minutes (medium, 67th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan across picosecond range, continuing timing optimization sequence

### Run 70
**Duration**: 3.5 minutes (medium, 69th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...
- lost beam at the end of the run

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with note about beam loss at end, final run in timing optimization sequence

### Run 71
**Duration**: 22.7 seconds (very short, 6th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...
- no beam

**Run classification**: timing_run
**Confidence**: medium
**Key evidence**: LXT scan attempted but 'no beam' noted, continuing the timing optimization sequence from previous runs

### Run 72
**Duration**: 40.4 seconds (very short, 8th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- junk scan
- Scan tmo_laser_lens_x: [2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3. 3.1] Scan tmo_laser_lens_y: [16.15 16.25 16.35 16.45 16.55 16.65 16.75 16.85 16.95 17.05 17.15] 30000 events/step Scan exited after 11 st...

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Laser lens X/Y scan for spatial positioning, labeled as 'junk scan' but clearly performing spatial alignment

### Run 73
**Duration**: 1.3 minutes (very short, 19th percentile)
**Status**: No logbook entries

**Run classification**: unknown_run
**Confidence**: low
**Key evidence**: No logbook entries available, insufficient context to determine purpose

### Run 74
**Duration**: 4.1 minutes (medium, 74th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Quarter wave plate scan from 0 to 360 at 1 degree step.
- IR-only scan collecting electrons at nominal circular polarization. This is waveplate position used for earlier runs.
- Scan tmo_laser_ejx_qwp: [ 0. 1. 2. 3. 4. 5. 6. 7. 8. 9. 10. 11. 12. 13. 14. 15. 16. 17. 18. 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32. 33. 34. 35. 36. 37. 38. 39. 40. 41. 42. 43. 44. 45. ...
- Aborted. This was a scan over 360. We will sit at nominal circular for a while. Then we will take a small 4 point scan in the vicinity.

**Run classification**: calibration_run
**Confidence**: high
**Key evidence**: Quarter wave plate scan from 0-360 degrees to calibrate polarization settings for IR-only electron collection

### Run 75
**Duration**: 24.5 minutes (very long, 99th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- IR-only scan in Xenon at the nominal circular polarization used for the previous runs. Ignore runs 73 and 74.

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: IR-only scan in Xenon at nominal circular polarization for data collection, extended duration (24.5 min) indicates scientific measurement

### Run 76
**Duration**: 32.1 minutes (very long, 100th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- IR-only scan in Xenon near nominal circular polarization.
- Scan tmo_laser_ejx_qwp: [184. 184.5 185. 185.5 186. ] 249000 events/step Scan exited after 13 steps with status: success Which probably means the scan was "stopped" before it finished, not "aborted", ...

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: IR-only scan in Xenon with QWP parameter scan, very long duration (32.1 min) indicates scientific data collection

### Run 77
**Duration**: 40.7 seconds (very short, 10th percentile)
**Status**: No logbook entries

**Run classification**: unknown_run
**Confidence**: low
**Key evidence**: No logbook entries, very short duration (40.7s) suggests test or aborted run

### Run 78
**Duration**: 3.6 minutes (medium, 72nd percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- IR-only. Repeating same scan range as 76 because the run did not finish.
- Scan tmo_laser_ejx_qwp: [184. 184.5 185. 185.5 186. ] 124500 events/step Scan exited after 15 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: IR-only scan repeating same QWP scan range as run 76, explicitly continuing previous measurement

### Run 79
**Duration**: 2.8 minutes (medium, 52nd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan tmo_laser_ejx_qwp: [184. 184.5 185. 185.5 186. ] 124500 events/step Scan exited after 10 steps with status: success

**Run classification**: measurement_run
**Confidence**: high
**Key evidence**: Continuation of QWP scan series with same parameters as runs 76 and 78, part of systematic measurement campaign

### Run 80
**Duration**: 1.1 minutes (very short, 13th percentile)
**Total entries**: 46 (46 unique)
**Activities**:
- Fly scan of sim_fast_setpoint with 30000 events/step. Scan exited after 9 steps with status: success
- junk scan, testing tweak.
- im1k4 unpointed beginning of 3rd shift before spectrometer alignment. No filter
- im2k4 unpointed start of 3rd shift.
- im3k4 unpointed start of 3rd shift.
- im5k4 unpointed start of 3rd shift
- im5k4 : beam pointing alignment x = + 400 um y = +100 um
- Start of 3rd shift beam delivered ~9:00 pm, beginning to set up zone-plate spectrometer for X-leap team after beam alignment.
- FZP positions after alignment at start of the 3rd shift Device: Position: 0 Intensifier MCP [V] 649 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 510.0 4 ...
- sample paddle at the start of the 3rd shift: gige1 gige2 gige3
- sample paddle positions for increasing the beam size procedure for finding timing
- mirror positions for the 50 um spot, before blowing it up to 100 um for timing
- we are having an issue with the laser shutter, we had beam come through even though it was closed...
- moved the sample paddle in x and y even further for increasing the size for timing (disregard last post)
- Laser position where we want to spatial parameter scan
- We made the laser spot size bigger and bumped the sample paddle. This is the new spot reference and the sample paddle position.
- laser focus is 5 mm downstream Device: Position: 0 atm_mr3_tt_tip 1371 1 atm_mr3_tt_tilt 1369 2 att_wp 9.999313 3 ejx_pol -0.012556 4 ejx_qwp 185.002232 5 ejx_shutter close 6 inj_mr 176.998677 7 lens_...
- we are overlapped on the paddle, x + 0 um, y + 0um Device: Position: 0 atm_mr3_tt_tip 1371 1 atm_mr3_tt_tilt 1369 2 att_wp 9.999305 3 ejx_pol -0.010045 4 ejx_qwp 185.002232 5 ejx_shutter open 6 inj_mr...
- Laser overlapped with X-ray. Cursor is the x-ray position
- Y = -100 um
- Y = -200 um
- Y = -300 um
- steering laser on paddle, x + 0 um, y - 300 um Device: Position: 0 atm_mr3_tt_tip 1371 1 atm_mr3_tt_tilt 1369 2 att_wp 9.999296 3 ejx_pol -0.007533 4 ejx_qwp 185.002232 5 ejx_shutter open 6 inj_mr 176...
- Y = +100 um
- Y = +200 um
- Y = +300 um
- X = +100 um
- X = +200 um
- X = +300 um
- X = -100 um
- X = -200 um
- X = -300 um
- before moving to 20 um from MFL table Device: Position: 0 mr2k4 bender_ds 20.567346 1 mr2k4 bender_us 14.955183 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.364624 4 mr2k4 x 1.187875 5 mr2k4 y 3.001635 6 m...
- at 20 um from MFL table Device: Position: 0 mr2k4 bender_ds 19.869915 1 mr2k4 bender_us 14.161043 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.405476 4 mr2k4 x 1.187895 5 mr2k4 y 3.001615 6 mr3k4 bender_ds...
- at z=20 from MFL table (530 eV, x49720, 2/11/2022) Device: Position: 0 mr2k4 bender_ds 19.869915 1 mr2k4 bender_us 14.161043 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.405476 4 mr2k4 x 1.187895 5 mr2k4 y...
- 20 um focus for X-ray
- at z=80 from MFL table ()530 eV, x49720, 2/11/2022 Device: Position: 0 mr2k4 bender_ds 21.520021 1 mr2k4 bender_us 15.490085 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.397621 4 mr2k4 x 1.187885 5 mr2k4 y...
- at z=80 from MFL table (530 eV, x49720, 2/11/2022) Device: Position: 0 mr2k4 bender_ds 21.520021 1 mr2k4 bender_us 15.490085 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.397621 4 mr2k4 x 1.187885 5 mr2k4 y...
- 80 um focus spot for X-ray.
- x-rays on atm
- laser on atm
- coarse timing at the ATM Device: Position: 0 lxt pos [ps] 410.000000 1 txt pos [ps] -0.022629 2 lxt_ttc pos [ps] 410.000000 3 lxt offset [ns] 31109.610220 4 lxt total delay [ns] 31109.200220 5 txt off...
- Coarsely timed at ATM
- Fine timing on the Opal.
- fine timing at the ATM, pix 1000 on the Piranha and pix 180 on the ATM Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] -0.022416 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31109.169720 4 l...
- X-ray laser spatially overlapped for IP paddle.

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Extensive spatial alignment activities including laser-xray overlap, beam positioning, focus adjustments, and paddle alignment

### Run 81
**Duration**: 3.5 minutes (medium, 70th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-1.00000000e-11 -8.00000000e-12 -6.00000000e-12 -4.00000000e-12 -2.00000000e-12 -1.61558713e-27 2.00000000e-12 4.00000000e-12 6.00000000e-12 8.00000000e-12] 41500 events/step Scan exited af...
- Sample paddle position for SiN where we saw timing signal.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT timing scan with picosecond-scale delays, sample paddle position noted for timing signal observation

### Run 82
**Duration**: 11.1 minutes (very long, 93rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- LXT scan on the paddle at IP with some fly scanning at the end.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan at IP (interaction point) with fly scanning, continuing timing optimization from previous run

### Run 83
**Duration**: 1.6 minutes (very short, 21st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-8.5e-11 -8.3e-11 -8.1e-11 -7.9e-11 -7.7e-11 -7.5e-11] 41500 events/step Scan exited after 16 steps with status: abort

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with picosecond-scale delays, aborted before completion

### Run 84
**Duration**: 1.9 minutes (short, 34th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-8.5e-11 -8.3e-11 -8.1e-11 -7.9e-11 -7.7e-11 -7.5e-11] 41500 events/step Scan exited after 20 steps with status: abort
- we aborted run 84 because we saw no signal anywhere

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with same parameters as run 83, explicitly aborted due to 'no signal anywhere'

### Run 85
**Duration**: 1.2 minutes (very short, 16th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.8e-10 -8.0e-11 2.0e-11] 41500 events/step Scan exited after 12 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with wider range of delay values, continuing timing optimization sequence

### Run 86
**Duration**: 1.8 minutes (short, 31st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.e-10 -5.e-11 0.e+00 5.e-11 1.e-10] 41500 events/step Scan exited after 20 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with systematic delay values from -100ps to +100ps

### Run 87
**Duration**: 1.1 minutes (very short, 15th percentile)
**Status**: No logbook entries

**Run classification**: timing_run
**Confidence**: medium
**Key evidence**: Very short run (1.1 min) with no entries, but consistent with timing scan sequence in runs 81-86

### Run 88
**Duration**: 1.8 minutes (short, 29th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.e-10 -5.e-11 0.e+00 5.e-11 1.e-10] 41500 events/step Scan exited after 20 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Identical LXT scan parameters as run 86, continuing systematic timing optimization

### Run 89
**Duration**: 9.1 minutes (very long, 91st percentile)
**Status**: No logbook entries

**Run classification**: timing_run
**Confidence**: medium
**Key evidence**: Longer run (9.1 min) with no entries, but in sequence with other timing scans and consistent with extended timing measurements

### Run 90
**Duration**: 1.9 minutes (short, 33rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.e-10 -5.e-11 0.e+00 5.e-11 1.e-10] 41500 events/step Scan exited after 20 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Identical LXT scan parameters as runs 86 and 88, completing systematic timing optimization sequence

### Run 91
**Duration**: 1.8 minutes (short, 32nd percentile)
**Total entries**: 11 (11 unique)
**Activities**:
- Scan lxt: [-1.e-10 -5.e-11 0.e+00 5.e-11 1.e-10] 41500 events/step Scan exited after 20 steps with status: success
- IR burning through the SiN as we moved the paddle around.
- we now have the edge on the ATM Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] -0.025191 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31109.167720 4 lxt total delay [ns] 31109.167720 5 txt ...
- we now have txt at the position we were at with fine timing at the IP and the ATM, but the visible light and ND filters in Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] 4.452307 2 lxt_ttc p...
- we now have txt at the position we were at with fine timing at the IP and the ATM, but the visible light and ND filters in AND fine timing at the ATM Device: Position: 0 lxt pos [ps] 0.000000 1 txt po...
- edge at 180 on the ATM Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] 0.000534 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31109.163250 4 lxt total delay [ns] 31109.163250 5 txt offset [ns...
- We moved back to 20 um X-ray spot size. We are keeping the laser focus large for the next sets of scan.
- We are now back at Z = 20 mm, with 20 um focus. Device: Position: 0 mr2k4 bender_ds 19.869904 1 mr2k4 bender_us 14.161049 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.358122 4 mr2k4 x 1.18789 5 mr2k4 y 3.0...
- run 91 is junk
- The voltage settings of the TOF are: Port 0, 90, 180, and 270 have 600 V retardation. All other ports are at 20 V retardation.
- Laser positions for the set of scans that we will take from here onwards Device: Position: 0 atm_mr3_tt_tip 1341 1 atm_mr3_tt_tilt 1369 2 att_wp 9.999923 3 ejx_pol -0.012556 4 ejx_qwp 185.004743 5 ejx...

**Run classification**: alignment_run
**Confidence**: high
**Key evidence**: Multiple entries about spatial positioning: 'IR burning through the SiN as we moved the paddle around', 'edge on the ATM Device', 'moved back to 20 um X-ray spot size', 'back at Z = 20 mm, with 20 um focus'

### Run 92
**Duration**: 2.3 minutes (short, 40th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Scan lxt: [-8.0e-12 -7.9e-12 -7.8e-12 -7.7e-12 -7.6e-12 -7.5e-12 -7.4e-12 -7.3e-12 -7.2e-12 -7.1e-12 -7.0e-12 -6.9e-12 -6.8e-12 -6.7e-12 -6.6e-12 -6.5e-12 -6.4e-12 -6.3e-12 -6.2e-12 -6.1e-12 -6.0e-12 ...
- run 92 is searching for streaking at where we saw spatial overlap on the paddle. the x-rays are at nominal 30 um focus, the laser is 5 mm downstream, we are at nominal 350/700 XLEAP. we are scanning l...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with fine picosecond steps searching for streaking at spatial overlap position, explicitly mentioned 'searching for streaking'

### Run 93
**Duration**: 2.4 minutes (short, 44th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-8.0e-12 -7.9e-12 -7.8e-12 -7.7e-12 -7.6e-12 -7.5e-12 -7.4e-12 -7.3e-12 -7.2e-12 -7.1e-12 -7.0e-12 -6.9e-12 -6.8e-12 -6.7e-12 -6.6e-12 -6.5e-12 -6.4e-12 -6.3e-12 -6.2e-12 -6.1e-12 -6.0e-12 ...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Identical LXT scan pattern as run 92 with fine picosecond steps, continuing the timing optimization sequence

### Run 94
**Duration**: 2.4 minutes (short, 45th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-5.5e-12 -5.4e-12 -5.3e-12 -5.2e-12 -5.1e-12 -5.0e-12 -4.9e-12 -4.8e-12 -4.7e-12 -4.6e-12 -4.5e-12 -4.4e-12 -4.3e-12 -4.2e-12 -4.1e-12 -4.0e-12 -3.9e-12 -3.8e-12 -3.7e-12 -3.6e-12 -3.5e-12 ...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with fine picosecond steps in a different range (-5.5ps to -3.5ps), continuing systematic timing optimization

### Run 95
**Duration**: 2.4 minutes (short, 46th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-3.0e-12 -2.9e-12 -2.8e-12 -2.7e-12 -2.6e-12 -2.5e-12 -2.4e-12 -2.3e-12 -2.2e-12 -2.1e-12 -2.0e-12 -1.9e-12 -1.8e-12 -1.7e-12 -1.6e-12 -1.5e-12 -1.4e-12 -1.3e-12 -1.2e-12 -1.1e-12 -1.0e-12 ...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with fine picosecond steps in a different range (-3.0ps to -1.0ps), continuing systematic timing optimization

### Run 96
**Duration**: 2.4 minutes (short, 43rd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-1.80000000e-12 -1.70000000e-12 -1.60000000e-12 -1.50000000e-12 -1.40000000e-12 -1.30000000e-12 -1.20000000e-12 -1.10000000e-12 -1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with fine picosecond steps in a different range (-1.8ps to sub-ps), continuing systematic timing optimization

### Run 97
**Duration**: 2.4 minutes (short, 47th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Scan lxt: [-4.3e-12 -4.2e-12 -4.1e-12 -4.0e-12 -3.9e-12 -3.8e-12 -3.7e-12 -3.6e-12 -3.5e-12 -3.4e-12 -3.3e-12 -3.2e-12 -3.1e-12 -3.0e-12 -2.9e-12 -2.8e-12 -2.7e-12 -2.6e-12 -2.5e-12 -2.4e-12 -2.3e-12 ...
- TPR for timing scans. Device: Position: 0 On-Time Rate: 7653.061224 1 On-Time Sequence Code: 280 2 Goose Rate: 637.755102 3 Goose Sequence Code: 281 4 Goose Delay [ns]: -16.153846 5 Goose Overlap [pul...
- Laser positions for timing scans. Device: Position: 0 atm_mr3_tt_tip 1341 1 atm_mr3_tt_tilt 1369 2 att_wp 9.999925 3 ejx_pol -0.010045 4 ejx_qwp 185.002232 5 ejx_shutter open 6 inj_mr 176.999558 7 len...
- Timing offsets for timing scan. Device: Position: 0 lxt pos [ps] -6.800000 1 txt pos [ps] 0.000961 2 lxt_ttc pos [ps] -6.800000 3 lxt offset [ns] 31109.163250 4 lxt total delay [ns] 31109.170050 5 txt...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with explicit entries about 'TPR for timing scans' and 'Timing offsets for timing scan', continuing the timing optimization sequence

### Run 98
**Duration**: 2.4 minutes (short, 41st percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-6.8e-12 -6.7e-12 -6.6e-12 -6.5e-12 -6.4e-12 -6.3e-12 -6.2e-12 -6.1e-12 -6.0e-12 -5.9e-12 -5.8e-12 -5.7e-12 -5.6e-12 -5.5e-12 -5.4e-12 -5.3e-12 -5.2e-12 -5.1e-12 -5.0e-12 -4.9e-12 -4.8e-12 ...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with fine picosecond steps in a different range (-6.8ps to -4.8ps), continuing systematic timing optimization

### Run 99
**Duration**: 1.2 minutes (very short, 18th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-8.0e-12 -7.9e-12 -7.8e-12 -7.7e-12 -7.6e-12 -7.5e-12 -7.4e-12 -7.3e-12 -7.2e-12 -7.1e-12 -7.0e-12 -6.9e-12] 41500 events/step Scan exited after 12 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with fine picosecond steps in a different range (-8.0ps to -6.9ps), continuing systematic timing optimization

### Run 100
**Duration**: 2.4 minutes (short, 43rd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- We just moved Lens X = +100 um, Lens Y = 0. We are doing a lens scan from this run.
- Scan lxt: [-8.0e-12 -7.9e-12 -7.8e-12 -7.7e-12 -7.6e-12 -7.5e-12 -7.4e-12 -7.3e-12 -7.2e-12 -7.1e-12 -7.0e-12 -6.9e-12 -6.8e-12 -6.7e-12 -6.6e-12 -6.5e-12 -6.4e-12 -6.3e-12 -6.2e-12 -6.1e-12 -6.0e-12 ...
- runs 100 - 104 is lens at +100 um X

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan combined with lens position adjustment ('Lens X = +100 um'), part of a lens scan series while maintaining timing optimization

### Run 101
**Duration**: 2.4 minutes (short, 42nd percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-5.5e-12 -5.4e-12 -5.3e-12 -5.2e-12 -5.1e-12 -5.0e-12 -4.9e-12 -4.8e-12 -4.7e-12 -4.6e-12 -4.5e-12 -4.4e-12 -4.3e-12 -4.2e-12 -4.1e-12 -4.0e-12 -3.9e-12 -3.8e-12 -3.7e-12 -3.6e-12 -3.5e-12 ...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with fine picosecond steps (-5.5ps to -3.5ps), continuing the lens scan series with timing optimization from run 100

### Run 102
**Duration**: 2.4 minutes (short, 47th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-3.0e-12 -2.9e-12 -2.8e-12 -2.7e-12 -2.6e-12 -2.5e-12 -2.4e-12 -2.3e-12 -2.2e-12 -2.1e-12 -2.0e-12 -1.9e-12 -1.8e-12 -1.7e-12 -1.6e-12 -1.5e-12 -1.4e-12 -1.3e-12 -1.2e-12 -1.1e-12 -1.0e-12 ...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with fine picosecond steps (-3.0ps to -1.0ps), part of the systematic timing optimization sequence with lens at +100um X position

### Run 103
**Duration**: 41.2 seconds (very short, 11th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -1.61558713e-27] 41500 events/step Scan exited after 6 steps with status: success

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with fine femtosecond steps (-500fs to 0fs), continuing the timing optimization sequence with lens at +100um X position

### Run 104
**Duration**: 1.1 minutes (very short, 14th percentile)
**Total entries**: 6 (6 unique)
**Activities**:
- Scan lxt: [-6.65e-12 -6.60e-12 -6.55e-12 -6.50e-12 -6.45e-12 -6.40e-12 -6.35e-12 -6.30e-12 -6.25e-12 -6.20e-12 -6.15e-12] 41500 events/step Scan exited after 11 steps with status: success
- We moved the lens X back to X = 0. Now scanning on a smaller range arounf -6.4 ps.
- We think we see streaking at this lxt in the previous runs. Checking ATM. Device: Position: 0 lxt pos [ps] -6.400000 1 txt pos [ps] -0.000053 2 lxt_ttc pos [ps] -6.400000 3 lxt offset [ns] 31109.16325...
- Timing on the ATM where we think we saw streaking at the IP. Device: Position: 0 lxt pos [ps] -6.400000 1 txt pos [ps] -7.289363 2 lxt_ttc pos [ps] -6.400000 3 lxt offset [ns] 31109.163250 4 lxt total...
- ATM signal at 400 eV, at nominal streaking delay; pulse energy 73 uJ, 510 Hz
- Timing after setting lxt and txt to 0. We think that pixel 180 on the OPAL is timing at the IP. Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] -0.000160 2 lxt_ttc pos [ps] 0.000000 3 lxt off...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Fine LXT scan around -6.4ps where streaking was observed, with lens moved back to X=0, explicit timing checks at ATM and IP

### Run 105
**Duration**: 25.6 seconds (very short, 7th percentile)
**Total entries**: 1 (1 unique)
**Activities**:
- Scan lxt: [-2.50000000e-13 -2.00000000e-13 -1.50000000e-13 -1.00000000e-13 -5.00000000e-14 -5.04870979e-29 5.00000000e-14 1.00000000e-13 1.50000000e-13 2.00000000e-13 2.50000000e-13] 41500 events/step...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Fine LXT scan around t0 (-250fs to +250fs) following the retiming activities in run 104

### Run 106
**Duration**: 47.3 seconds (very short, 12th percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- confirming t0 after retiming on ATM. 2w tuning in the background.
- stopper was in for the start of the run
- Scan lxt: [-5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -1.00974196e-28 1.00000000e-13 2.00000000e-13 3.00000000e-13 4.00000000e-13 5.00000000e-13] 41500 events/step...
- bad scan, stopper was in.
- Voltages are ramped back to port 0, 90, 180, 270 set at 600 V retardation. All other TOFs are at 20 V retardation.

**Run classification**: timing_run
**Confidence**: medium
**Key evidence**: LXT scan to confirm t0 after retiming on ATM, though scan was aborted due to stopper being in

### Run 107
**Duration**: 2.1 minutes (short, 35th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- Now scanning the timing at the IP, looking for streaking.
- pulse energy seems very low
- Scan lxt: [-5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -1.00974196e-28 1.00000000e-13 2.00000000e-13 3.00000000e-13 4.00000000e-13 5.00000000e-13] 41500 events/step...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan explicitly 'looking for streaking' at the IP, continuing timing optimization

### Run 108
**Duration**: 3.1 minutes (medium, 56th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- repeating timing scan around t0
- Scan lxt: [-5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -1.00974196e-28 1.00000000e-13 2.00000000e-13 3.00000000e-13 4.00000000e-13 5.00000000e-13] 41500 events/step...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Explicitly 'repeating timing scan around t0', continuing the timing optimization sequence

### Run 109
**Duration**: 1.1 minutes (very short, 13th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- same as 108 and 107. lens at nominal 0.
- Scan lxt: [-5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -1.00974196e-28 1.00000000e-13 2.00000000e-13 3.00000000e-13 4.00000000e-13 5.00000000e-13] 41500 events/step...
- abort 109, because we did not see streaking in 107.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Same timing scan as runs 107-108, explicitly noted as 'same as 108 and 107' with lens at nominal position

### Run 110
**Duration**: 5.6 minutes (long, 82nd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- increasing the scan range to +- 1.5 ps around were we think we saw streaking.
- Lens at nominal zero position. Device: Position: 0 atm_mr3_tt_tip 1341 1 atm_mr3_tt_tilt 1369 2 att_wp 9.999933 3 ejx_pol -0.012556 4 ejx_qwp 185.002232 5 ejx_shutter open 6 inj_mr 176.999555 7 lens_x...
- Scan lxt: [-1.50000000e-12 -1.40000000e-12 -1.30000000e-12 -1.20000000e-12 -1.10000000e-12 -1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Expanded LXT scan range (±1.5ps) around where streaking was observed, with lens at nominal zero position

### Run 111
**Duration**: 5.6 minutes (long, 82nd percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- We moved the lens Y = +50 um, X = 0 um.
- Lens at y +50 um. Device: Position: 0 atm_mr3_tt_tip 1341 1 atm_mr3_tt_tilt 1369 2 att_wp 9.999933 3 ejx_pol -0.010045 4 ejx_qwp 185.002232 5 ejx_shutter open 6 inj_mr 176.999559 7 lens_x 2.597698 8 l...
- Scan lxt: [-1.50000000e-12 -1.40000000e-12 -1.30000000e-12 -1.20000000e-12 -1.10000000e-12 -1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with lens position adjustment (Y = +50 um) to optimize temporal overlap and streaking conditions

### Run 112
**Duration**: 5.0 minutes (long, 79th percentile)
**Total entries**: 8 (8 unique)
**Activities**:
- Lens at y -50 um. Device: Position: 0 atm_mr3_tt_tip 1341 1 atm_mr3_tt_tilt 1369 2 att_wp 9.999928 3 ejx_pol -0.010045 4 ejx_qwp 185.004743 5 ejx_shutter open 6 inj_mr 176.999555 7 lens_x 2.597698 8 l...
- We moved the lens Y = -50 um, X = 0 um.
- Scan lxt: [-1.50000000e-12 -1.40000000e-12 -1.30000000e-12 -1.20000000e-12 -1.10000000e-12 -1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-...
- We see a bucket jump. Abort run 112 and fix timing.
- move to SASE to fix bucket jump.
- adjust timing back by -384.615 ps
- Recover timing after bucket jump looking ATM. Device: Position: 0 lxt pos [ps] -384.615000 1 txt pos [ps] -0.000267 2 lxt_ttc pos [ps] -384.615000 3 lxt offset [ns] 31109.169650 4 lxt total delay [ns]...
- Set lxt to zero after recovering from bucket jump using SASE on the ATM. Device: Position: 0 lxt pos [ps] 0.000000 1 txt pos [ps] -0.000320 2 lxt_ttc pos [ps] 0.000000 3 lxt offset [ns] 31109.554265 4...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with lens position adjustment (Y = -50 um), bucket jump detection and timing recovery activities

### Run 113
**Duration**: 5.6 minutes (long, 83rd percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Scan lxt: [-1.50000000e-12 -1.40000000e-12 -1.30000000e-12 -1.20000000e-12 -1.10000000e-12 -1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-...
- We moved back Lens Y = 0. Lens X = 0
- back to nominal lens zero. Timing scan to verfiy streaking after timing jump.
- settings and view on all giges

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan to verify streaking after timing jump, with lens returned to nominal zero position

### Run 114
**Duration**: 14.4 minutes (very long, 97th percentile)
**Total entries**: 9 (9 unique)
**Activities**:
- move photon energy to pixel 1100 on FZP (edge of resonance) and scan timing at the nominal lens 0 position.
- Lens at nominal zero Device: Position: 0 atm_mr3_tt_tip 1341 1 atm_mr3_tt_tilt 1369 2 att_wp 9.999918 3 ejx_pol -0.010045 4 ejx_qwp 185.004743 5 ejx_shutter open 6 inj_mr 176.999554 7 lens_x 2.597691 ...
- TPR for timing scans. Device: Position: 0 On-Time Rate: 7653.061224 1 On-Time Sequence Code: 280 2 Goose Rate: 637.755102 3 Goose Sequence Code: 281 4 Goose Delay [ns]: -16.153846 5 Goose Overlap [pul...
- timing offsets. Device: Position: 0 lxt pos [ps] -0.400000 1 txt pos [ps] -0.000854 2 lxt_ttc pos [ps] -0.400000 3 lxt offset [ns] 31109.554265 4 lxt total delay [ns] 31109.554665 5 txt offset [ns] 3....
- timing offsets. Device: Position: 0 lxt pos [ps] 0.500000 1 txt pos [ps] -0.000854 2 lxt_ttc pos [ps] 0.500000 3 lxt offset [ns] 31109.554265 4 lxt total delay [ns] 31109.553765 5 txt offset [ns] 3.88...
- Scan lxt: [-1.50000000e-12 -1.40000000e-12 -1.30000000e-12 -1.20000000e-12 -1.10000000e-12 -1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-...
- gmd distribution
- We changed the interleaving of the TOF sets for Run 115. Port [ 0, 2, 4, 6, 8, 10, 12, 14] are set to 600 V retardation. Port [ 1, 3, 5, 7, 9, 11, 13, 15] are set to 0 V retardation.
- We changed the interleaving of the TOF sets. Port [ 0, 2, 4, 6, 8, 10, 12, 14] are set to 600 V retardation. Port [ 1, 3, 5, 7, 9, 11, 13, 15] are set to 0 V retardation.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan at edge of resonance (pixel 1100 on FZP), with multiple timing offset adjustments and TPR settings for timing optimization

### Run 115
**Duration**: 11.5 minutes (very long, 95th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- repeat 114 but with interleaved tofs (8 F/8 C)
- Scan lxt: [-5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-13 2.00000000e-13 3.00000000e-13 4.00000000e-13 5.00000000e-13 6.00000000e-13 7.0...
- 114 - blue 115 - orange
- photon energy scan (+-5 eV at resonance and one point at 750)

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Repeat of run 114 with interleaved TOFs (8F/8C) and LXT scan, continuing timing optimization sequence

### Run 116
**Duration**: 11.5 minutes (very long, 95th percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- Interleaved TOF (4 F/ 8 C).
- Scan lxt: [-5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-13 2.00000000e-13 3.00000000e-13 4.00000000e-13 5.00000000e-13 6.00000000e-13 7.0...
- green - 116
- back to full interleaved ToFs.
- 720 eV (lcls energy) should be pixel 1100 on spectrometer, which we think is the shoulder of the CF4 resonance.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with different TOF interleaving configuration (4F/8C) at the CF4 resonance edge

### Run 117
**Duration**: 11.5 minutes (very long, 96th percentile)
**Total entries**: 2 (2 unique)
**Activities**:
- Interleaved TOF (8 C/ 8 F). Compare with run 115.
- Scan lxt: [-5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-13 2.00000000e-13 3.00000000e-13 4.00000000e-13 5.00000000e-13 6.00000000e-13 7.0...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with interleaved TOF configuration (8C/8F), explicitly compared with run 115

### Run 118
**Duration**: 7.9 minutes (long, 89th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- back to 4+12 in ToF
- Scan lxt: [0.0e+00 1.0e-13 2.0e-13 3.0e-13 4.0e-13 5.0e-13 6.0e-13 7.0e-13 8.0e-13 9.0e-13 1.0e-12 1.1e-12 1.2e-12 1.3e-12 1.4e-12 1.5e-12 1.6e-12 1.7e-12 1.8e-12 1.9e-12 2.0e-12] Scan hf_w2w: [717.5 ...
- Interleaved TOF (4F/ 12 C)

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Combined LXT and photon energy scan with 4F/12C TOF configuration, continuing timing optimization sequence

### Run 119
**Duration**: 7.8 minutes (long, 88th percentile)
**Total entries**: 4 (4 unique)
**Activities**:
- Interleaved TOF (8F/ 8 C)
- Scan lxt: [0.0e+00 1.0e-13 2.0e-13 3.0e-13 4.0e-13 5.0e-13 6.0e-13 7.0e-13 8.0e-13 9.0e-13 1.0e-12 1.1e-12 1.2e-12 1.3e-12 1.4e-12 1.5e-12 1.6e-12 1.7e-12 1.8e-12 1.9e-12 2.0e-12] Scan hf_w2w: [717.5 ...
- going to all 0 retardation and above edge ionization for PCI effect. delay between C and F 1s electrons
- pulse energy drifted down in Run 119. having ACR try to recover some of the energy.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: Combined LXT and photon energy scan with 8F/8C TOF configuration, investigating delay between C and F 1s electrons

### Run 120
**Duration**: 9.8 minutes (very long, 92nd percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- Changed the TOF settings to have all TOF retardation = 0 V. We are getting to the PCI settings.
- brown in 119. drop in pulse energy. ACR recoverd for Run 120
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...
- gmd distribution is back. pink is 120
- streaking signal appears before time 0 + electron hits per shot per tof.

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with all TOF retardation at 0V for PCI settings, noting streaking signal appears before time zero

### Run 121
**Duration**: 7.9 minutes (very long, 90th percentile)
**Total entries**: 3 (3 unique)
**Activities**:
- back to 2+12 interleaved ToFs around the resonance.
- Interleaved TOF (4F/ 12 C). 600 V retardation for F, 20 V retardation for C.
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with interleaved TOF configuration (4F/12C) and specific retardation voltages, continuing the timing optimization sequence from previous runs

### Run 122
**Duration**: 1.8 minutes (very short, 22nd percentile)
**Total entries**: 5 (5 unique)
**Activities**:
- back to 0V ret and above edge scan
- MPS fault in the machine.... no beam in this run.
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...
- run 122 is junk, dropped beam and stopped scan...
- For the last part of the shift we scanned three different configuratios: 1. CF4 F-edge resonance scans: scanning timing and photon energy around the should of the resonance: 1a. 12 ToFs for C1s, 4 ToF...

**Run classification**: unknown_run
**Confidence**: high
**Key evidence**: Run explicitly marked as 'junk' due to MPS fault with no beam, scan was stopped and data is invalid

### Run 123
**Duration**: 8.8 minutes (very long, 91st percentile)
**Total entries**: 10 (10 unique)
**Activities**:
- Changed the retardation of all tof to 0 V.
- beam is back. restarting run.
- Scan lxt: [-1.00000000e-12 -9.00000000e-13 -8.00000000e-13 -7.00000000e-13 -6.00000000e-13 -5.00000000e-13 -4.00000000e-13 -3.00000000e-13 -2.00000000e-13 -1.00000000e-13 -2.01948392e-28 1.00000000e-1...
- Finished scan early. Ran out of time. We had all points but 750 eV.
- end of run, before switching off FZP-II Device: Position: 0 Intensifier MCP [V] 924 1 Intensifier Gate [us] 10.0 2 Intensifier TPR Delay [us] 93.999231 3 Intensifier Trig Rate 0.0 4 solid_att TARGET1 ...
- leaving mirrors at 20 um position. Device: Position: 0 mr2k4 bender_ds 19.869875 1 mr2k4 bender_us 14.161043 2 mr2k4 coating B4C 3 mr2k4 pitch 14604.380585 4 mr2k4 x 1.187905 5 mr2k4 y 3.00149 6 mr3k4...
- TPR for timing scans. Device: Position: 0 On-Time Rate: 8290.816327 1 On-Time Sequence Code: 280 2 Goose Rate: 0.0 3 Goose Sequence Code: 281 4 Goose Delay [ns]: 0 5 Goose Overlap [pulses]: 0.0 6 Goos...
- laser at the end of the shift. Device: Position: 0 atm_mr3_tt_tip 1341 1 atm_mr3_tt_tilt 1369 2 att_wp 10.000012 3 ejx_pol -0.015067 4 ejx_qwp -0.002511 5 ejx_shutter close 6 inj_mr 176.999555 7 lens_...
- preliminary streaking results, first photon energy
- average number of electrons per shot

**Run classification**: timing_run
**Confidence**: high
**Key evidence**: LXT scan with all TOF retardation at 0V, continuing the timing optimization sequence with preliminary streaking results noted

