# MRCO Commissioning Shift Plans (X-10168):

### Checkout Goals (from commissioning sheet [TMO SCRF Commissioning V2](https://docs.google.com/spreadsheets/d/1ibrUij99RwpWNxidFLCZeuJbsXdm1EZScHPYYV-Ay5g/edit?gid=683490257#gid=683490257)):

### Initial Time Accounting

| Activity Name | Activity Objective | Estimated Beamtime (Hrs) | Beam Parameters | Note |
| :---- | :---- | ----- | ----- | :---- |
| Define focus with WFS |  | 2 | 400 eV |  |
| Align Spectrometer | Verify X,Y position of XFEL focus: MRCO XY-scan to find the center of beam with respect to the centering ring. 0 retardation. (N2) | 2 | 950 eV | Sample is Ne. Look at all the ToFs to make sure we can center the beam. |
| Retardation Optimization | Ensure homegeneity of retardation voltages | 6 | 950 eV | Sample is Ne. Set up the lens cans of the spectrometers for different retardations (5 retardations). Check that the retardation is consistent across the ToFs. |
| Photon Energy/Retardation Scan | Characterize resolution by scanning retardation and electron kinetic energy | 3 | 415 \- 1410 eV | Retardation scan of NNO for different photon energies & different retardations: hf \= Ip \+ (5 \[Vr=0\], 10 \[Vr=0,5\], 20 \[Vr=0,15\], 50 \[Vr=0,45\], 100 \[Vr=0,50,95\], 200 \[Vr=0,150,100,195\], 500 \[Vr=0,400,450,495\], 1000 \[Vr=0,500,900,950,995\]) FZP \= N, O, 613, Ne, 1200\. This also gives measurement of beta parameters |
| Spectral Reconstruction | Correlate MRCO spectra with FZP spectrum | 4 | 950 eV (& if time, 570\) | FZP/MRCO correlation measurements for spectral reconstruction Redo the above with a different hit rate (as a factor of 1, 2, 4, 8, 16\* per feature). FZP/MRCO correlation measurements for spectral reconstruction in current mode Start with Ne & 950 eV, if time do CO2 as well |
| Test Current Mode | Ensuring that the spectrometer is tuned for high signal rate mode, and validate MCP performance in cases of increased depletion | 12 | 950 eV | Sample is Ne. We need to make sure that the MCP detectors are working at the non-linear gain 5, 10, 25, 50, 75, 100, 150, 200 mV signal level (without amplifier). Repeat 5, 10, 15, 25 after adding amplifiers. |
| Spectral Reconstruction in Current Mode |  | 4 |  | See above |
| Verify position of XFEL focus: | MRCO Z-scan to find nonlinear signal (DCH in Ne) | 6 | 960 eV (if this is a struggle, we use Ar @ 350 eV) | If the non-linear is difficult to find, then consider using the blurring effect of space charge to identify the tightest focus. |
| Laser spatial overlap (paddle) |  | 6 |  | IR/x-ray overlap |
| Laser temporal overlap (paddle) |  | 6 |  | IR/x-ray overlap |
| Laser spatiotemporal overlap (gas) |  | 6 | 400 eV | IR-pumped NNO RAM |
| More Beta Scans |  | 6 |  | N2, CO2, Ne |
| **Total Hours** |  | **61** |  |  |

### Detailed Shift Plan

#### Common tasks in all the shift:

- [ ] Check for KB1 transmission (TMO)  
- [ ] Sample paddle repeatability (MRCO)  
- [ ] Bias voltage monitoring \- online plots. (MRCO)   
- [ ] FEX monitoring \- online plots (?). (MRCO)  
- [ ] Data checking  
- [ ] MRCO XY scan. (MRCO)

[Shift Coverage\_X10168](https://docs.google.com/spreadsheets/d/1wmmxYHoP6mg4CePa0Kyd6obk5MqHoz83b6O5WNRpwb0/edit?gid=0#gid=0)

#### Shift 1:

- [x] ~~Bring beam down TMO beamline and check timing of imagers~~   
      ~~(timing should be fine, but just be mindful timing could have shifted)~~  
      - [ ] Run beamline transmission script  
- [x] ~~Ramp up of MRCO detectors (no retardation, 400 eV)~~  
      - [x] ~~Check relative timing (XPM-2 vs XPM-4 should be \~1.3 us)~~  
      - [x] ~~Align MRCO in X/Y plane (no retardation)~~  
            - [x] ~~Measure AM electrons for different XY positions, and optimize on uniformity.~~   
                  - [x] ~~400 eV \- Ar \-\> L-MM (200 eV)~~  
                  - [x] ~~Optimize the relative yield between opposite ToFs.~~   
            - [x] ~~Also check the flight time for the different ToFs (we can see if this shows something)~~   
- [ ] **We need to be above 1000 Hz to continue.**    
- [x] ~~MCP gain scan (with amplifier): bias scan: 1100:1500:50 V (in counting mode)~~   
      ~~(1 min each @ 1000 hz)~~   
- [x] ~~Ramp MRCO Retardation (400 eV)~~  
      ~~Adjust the retardation while looking at the angular distribution of Ar L-MM (200 eV).~~  
      - [x] ~~50 V, 100V, 150 V, 175 V, 190 V, 195 V.~~  
- [x] ~~Setup energy scan PV with ACR.~~   
- [x] ~~Spectrometer checkout [Ming-Fu Lin](mailto:mfl@stanford.edu) (400 eV)~~  
      - [x] ~~Check the timing of Piranha and Intensifier.~~  
      - [x] ~~Align FZP w/ no attenuator (500 Hz)~~  
      - [x] ~~Align Attenuator, then go to high rate.~~   
- [ ] Swap to NNO  
- [ ] Retardation scan (5-10 min at 1 kHz \=\> 3 hrs)  
      hf \= Ip \+ (5 \[Vr=0\], 10 \[Vr=0,5\], 20 \[Vr=0,15\], 50 \[Vr=0,45\], 100 \[Vr=0,50,95\], 200 \[Vr=0,150,100,195\], 500 \[Vr=0,400,450,495\], 1000 \[Vr=0,500,900,950,995\])

| FZP | Nitrogen (410 FZP) |  |  | ~~Ti (460)~~ | Oxygen (530) | Si (613) | ~~950 FZP~~ | ~~1212 (fzp)~~ |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Ret/hf | \+5 | \+10 | \+20 | \+50 | \+100 | \+200 | \+500 | \+800 |
| 0 | 417.5 | 422.5 | 432.5 | ~~462.5~~ | 512.5 | 612.5 | ~~912.5~~ | ~~1212.5~~ |
| 5 |  | 422.5 |  |  |  |  |  |  |
| 15 |  |  | 432.5 |  |  |  |  |  |
| 45 |  |  |  | ~~462.5~~ |  |  |  |  |
| 50 |  |  |  |  | 512.5 |  |  |  |
| 95 |  |  |  |  |  |  |  |  |
| 100 |  |  |  |  | 512.5 | 612.5 |  |  |
| 150 |  |  |  |  |  | 612.5 |  |  |
| 195 |  |  |  |  |  | 612.5 |  |  |
| 400 |  |  | 432.5 (V) |  | 512.5 (V) |  | ~~912.5~~ |  |
| 450 |  |  |  |  |  |  | ~~912.5~~ |  |
| 495 |  |  |  |  |  |  | ~~912.5~~ |  |
| 500 |  |  |  |  |  |  |  |  |

- [ ] Measure covariance of electron spectrum and photon spectrum  
- [ ] Request 800 eV, 950 eV and see what the pulse energy (and count rate)

#### Shift 2:

- [ ] **We need to be above 1000 Hz to continue.**    
- [ ] High-Rate scan (400 eV, Argon)  
      - [ ] Adjust sample gas pressure (and x-ray flux) to have consistent signal in polarization ToFs.  
      - [ ] MCP gain scan (no amplifier): bias scan: 1200:1850:50 V   
            (1 min each @ 1000 hz)   
- [ ] Setup Energy scan PV  
- [ ] Spectral Reconstruction scans  
      - [ ] Argon L-edge (400 eV)  
      - [ ] Retardations: 0, 100, 125 V  
      - [ ] Different hit rate (as a factor of 1, 2, 4, 8, 16\* per feature).  
      - [ ] Scanning photon energy across the FZP range.   
      - [ ] 5 min at each retardation 

#### Shift 3:

Pre-shift steps:

- [ ] Setup Argon gas line.  
- [ ] Setup N2O in the gas cabinet (ready to be switched).  
- [x] ~~Check all MRCO cameras.~~  
- [x] ~~Make sure that the SMA pin in the sample paddle is connected to the scope.~~  
- [x] ~~Check that the voltage ramper scripts have correct bias voltage for individual MCPs.~~

With Beam:

- [x] ~~Bring the beam down to the TMO beamline. Note down and point the beam in the same locations of IM2K4 and IM5K4. Day-to-day variations should be noted. **(30 mins)**~~  
      - [x] ~~Check for KB1 transmission~~  
      - [x] ~~Check for Sample paddle repeatability.~~  
      - [ ] See if signal on the SMA tip. (Could try coarse timing at IP)  
- [x] ~~Setup energy scan PV. **(10 mins)**~~  
- [x] ~~Setup FZP at 400 eV. **(30 mins)**~~  
      - [ ] If higher pulse energy \> 40 uJ, use Target 2 of the attenuator.  
- [x] ~~Ramp up of MRCO detectors and TOFs (no retardation, 400 eV) **(10 mins)**~~  
- [x] ~~Measure background. **(10 mins)**~~  
      - [ ] Start with 2-5% transmission (\~10 uJ avg in the XGMD).  
- [x] ~~Open Gas Needle valve connected to Argon line. **(10 min)**~~  
- [x] ~~Do SQ1 XY scan around the current position. Delta X \= \+/- 1, Delta Y \= \+/- 1\. Raster scanning by hand. **(30 mins)**~~  
- [x] ~~Needle position scan in XYZ. **(30 mins)**~~  
      - [ ] 100 V retardation.  
      - [x] ~~Voltage scan at the needle. \[-100 V to 100 V\] ...~~   
- [ ] Signal checking with and without amplifier **(1 hour)**  
      - [ ] At most 4 TOF without amplifier.  
      - [ ] Make sure FZP is in a safe state.   
      - [ ] Transmission : 2% \- 100%.  
- [ ] **Laser timing can be done here. (1 hour)**  
      - [ ] Spatial overlap on ATM  
      - [ ] Temporal overlap at IP (could do this, optional)  
      - [ ] Temporal overlap on ATM  
- [x] ~~Adjust the retardation while looking at the angular distribution of Ar L-MM (200 eV). **(30 mins @ 8.3 kHz, 2 mins /run) (\~2-5% transmission)**~~  
      - [x] ~~50 V, 100V, 150 V, 175 V, 190 V, 195 V, 200 V, 350 V at hv \= \[390 to 415 eV at 2 eV steps\]~~  
- [x] ~~Do SQ1 Z scan around the optimized XY positions. **(30 mins)**~~  
- [ ] Move the focus downstream and repeat the retardation scan. Compare different Z **(1 hour) Why?** Do we see any non-linearity?  
      - [ ] Z between \+10 mm and \-1 mm (make sure to account for Y due to beamline elevation. 0.04 deg)

- [ ] Spectral Reconstruction scans **(2 hour)**  
      - [x] ~~Argon L-edge (400 eV).~~  
      - [x] ~~Retardations: 0, 100, 125 V.~~  
      - [x] ~~Different hit rate (as a factor of 1, 2, 4, 8, 16\* per feature).~~  
      - [x] ~~Scanning photon energy across the FZP range.~~   
      - [ ] 5 min at each retardation 

- [ ] Move on to NNO. **(30 mins)**  
- [ ] Retardation scan (2 min at 8 kHz,  **4 hours** including setup of two FZPs)  
      hf \= Ip \+ (5 \[Vr=0\], 10 \[Vr=0,5\], 20 \[Vr=0,15\], 50 \[Vr=0,45\], 100 \[Vr=0,50,95\], 200 \[Vr=0,150,100,195\], 500 \[Vr=0,400,450,495\],   
      - [ ] Do photon energy/retardation scans around 400 eV FZP.  
      - [ ] Change photon energy centered at 530 eV. Set up the FZP.  
      - [ ] Do photon energy/retardation scans around 530 eV.  
      - [ ] Change photon energy centered at 613 eV. Needs commissioning by Ming-Fu.  
      - [ ] Do photon energy/retardation scans around 613 eV.  
            

| FZP | Nitrogen (410 FZP) |  |  | Oxygen (530) | Si (613) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Ret/hf | \+5 | \+10 | \+20 | \+100 | \+200 |
| 0 | 417.5 | 422.5 | 432.5 | 512.5 | 612.5 |
| 5 |  | 422.5 |  |  |  |
| 15 |  |  | 432.5 |  |  |
| 45 |  |  |  |  |  |
| 50 |  |  |  | 512.5 |  |
| 95 |  |  |  |  |  |
| 100 |  |  |  | 512.5 | 612.5 |
| 150 |  |  |  |  | 612.5 |
| 195 |  |  |  |  | 612.5 |
| 400 |  |  | 432.5 (V) | 512.5 (V) |  |
| 450 |  |  |  |  |  |

- [ ] Measure covariance of electron spectrum and photon spectrum  
- [ ] Request 800 eV, 950 eV and see what the pulse energy (and count rate).

      

In parallel, if time allows:

- [ ] laser/x-ray spatial overlap on sample paddle  
- [ ] Laser timing signal on sample paddle (SMA pin)  
- [ ] ATM Setup

Contingencies and notes:

1. Note down the bias voltages of the MCPs. The angular distribution of the Auger line should have a beta parameter \= 0.05. If not, then evaluate the cause.

#### Shift 4

With Beam:

- [ ] Bring the beam down to the TMO beamline. Note down and point the beam in the same locations of IM2K4 and IM5K4. Day-to-day variations should be noted. **(30 mins)**  
      - [ ] Check for KB1 transmission  
      - [ ] Check for Sample paddle repeatability.  
      - [ ] See if signal on the SMA tip. (Could try coarse timing at IP)  
- [ ] Setup energy scan PV. **(10 mins)**  
- [ ] Setup FZP at 400 eV. **(30 mins)**  
      - [ ] If higher pulse energy \> 40 uJ, use Target 2 of the attenuator.  
- [ ] Signal checking with and without amplifier **(1 hour)**  
      - [ ] At most 4 TOF without amplifier.  
      - [ ] Make sure FZP is in a safe state.   
      - [ ] Transmission : 2% \- 40%.  
- [ ] Resolution adjustment scan:  
      - [ ] Opposing TOFs resolution. Tweak retardation to match the resolution and collection of each opposing TOF pairs.  
            - [ ] Retardation of 175 , \+/- 15 V retardation at a step of 5 V   
- [ ] **Laser timing can be done here. (1 hour)**  
      - [ ] Spatial overlap on ATM  
      - [ ] Temporal overlap at IP (could do this, optional)  
      - [ ] Temporal overlap on ATM  
- [ ] Move the focus downstream and repeat the retardation scan. Compare different Z **(1 hour) Why?** Do we see any non-linearity?  
      - [ ] Z between \+10 mm and \-1 mm (make sure to account for Y due to beamline elevation. 0.04 deg)  
- [ ] Needle Scan? We need to look at the data for Retardation \= 0\.  
      - [ ] We might want to repeat it with higher retardation, 190 V.

- [ ] Move on to NNO. **(30 mins)**  
- [ ] Retardation scan (2 min at 8 kHz,  **4 hours** including setup of two FZPs)  
      hf \= Ip \+ (5 \[Vr=0\], 10 \[Vr=0,5\], 20 \[Vr=0,15\], 50 \[Vr=0,45\], 100 \[Vr=0,50,95\], 200 \[Vr=0,150,100,195\], 500 \[Vr=0,400,450,495\],   
      - [ ] Do photon energy/retardation scans around 400 eV FZP.  
      - [ ] Change photon energy centered at 530 eV. Set up the FZP.  
      - [ ] Do photon energy/retardation scans around 530 eV.  
      - [ ] Change photon energy centered at 613 eV. Needs commissioning by Ming-Fu.  
      - [ ] Do photon energy/retardation scans around 613 eV.  
            

| FZP | Nitrogen (410 FZP) |  |  | Oxygen (530) | Si (613) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Ret/hf | \+5 | \+10 | \+20 | \+100 | \+200 |
| 0 | 417.5 | 422.5 | 432.5 | 512.5 | 612.5 |
| 5 |  | 422.5 |  |  |  |
| 15 |  |  | 432.5 |  |  |
| 45 |  |  |  |  |  |
| 50 |  |  |  | 512.5 |  |
| 95 |  |  |  |  |  |
| 100 |  |  |  | 512.5 | 612.5 |
| 150 |  |  |  |  | 612.5 |
| 195 |  |  |  |  | 612.5 |
| 400 |  |  | 432.5 (V) | 512.5 (V) |  |
| 450 |  |  |  |  |  |

- [ ] Measure covariance of electron spectrum and photon spectrum  
- [ ] Request 800 eV, 950 eV and see what the pulse energy (and count rate).

#### Shift 5

With Beam:

- [ ] Bring the beam down to the TMO beamline. Note down and point the beam in the same locations of IM2K4 and IM5K4. Day-to-day variations should be noted. **(30 mins)**  
      - [ ] Check for KB1 transmission  
      - [ ] Check for Sample paddle repeatability.  
      - [ ] See if signal on the SMA tip. (Could try coarse timing at IP)

- [ ] Setup energy scan PV. **(10 mins). Ask to have a wider range of \+/-250 eV.**  
- [ ] Setup FZP at 400 eV. **(30 mins)**  
      - [ ] If higher pulse energy \> 40 uJ, use Target 2 of the attenuator.  
- [ ] Spectral Reconstruction scans  
      - [ ] Increase the transmission to 100% (\~200 uJ)  
      - [ ] Argon L-edge (400 eV)  
      - [ ] Retardations: 0, 100, 125 V  
      - [ ] Different hit rate (as a factor of 1, 2, 4, 8, 16\* per feature) as a function of needle position  
      - [ ] Scanning photon energy across the FZP range.   
      - [ ] 30s at each retardation   
- [ ] Change sample to NNO.  
      - [ ] Commission 615 eV FZP.  
      - [ ] Complete the Shift 4 measurement with FZP.  
      - [ ] Scan with continuous FZP positioning.  
      - [ ] Keep the FZP position at the center of the camera for each energy points, and calibrate the YAG-X and Lens-X position.  
      - [ ] Do a photon energy scan around 400 eV, (390 \- 410 eV).  
      - [ ] Do a pre-edge scan at the Oxygen edge (515 \- 535 eV).

	

| FZP | Nitrogen (410 FZP) |  |  | Si (613) |
| :---- | :---- | :---- | :---- | :---- |
| Ret/hf | \-10 | \-5 | 0 | \+200 |
| 0 | 402.5 | 405.5 | 412.5 | 612.5 |
| 5 |  |  |  |  |
| 15 |  |  |  |  |
| 45 |  |  |  |  |
| 50 |  |  |  |  |
| 95 |  |  |  |  |
| 100 |  |  |  | 612.5 |
| 150 |  |  |  | 612.5 |
| 195 |  |  |  | 612.5 |

- [ ] Find fine timing at the ATM using Target 1b (GaAs).  
      - [ ] Take 3 minutes of ATM data  
      - [ ] Repeat for Target 2b  
      - [ ] Repeat for Target 3b  
- [ ] Spatial and temporal overlap with 1.3 um at the IP.  
      - [ ] Align the sample paddle YAG and SiN with the X-ray/laser. Do spatial overlap. Use microscope for this.  
      - [ ] Measure t0 using the solid target \- clear YAG and SiN.  
- [ ] Measure t0 using NNO.  
      - [ ] Use photon energy of \~402 eV.   
      - [ ] Pump-probe with 1.3 um  
            - [ ] Linear polarization  
            - [ ] Circular polarization

#### Things we still need to do:

Things that need to be added to a shift plan.

- [ ] Sample paddle repeatability.  
- [ ] More retardation scans.  
- [ ] NNO measurements (photon energy and retardation)  
- [ ] Correlation between FZP and ToF.  
- [ ] Bias \- is there more info needed here?  
- [ ] MRCO Z-scan.   
- [ ] FZP commissioning \- Try 613 eV FZP.  
- [ ] Establish Downstream focus condition \- maybe a low priority  
- [ ] Check-out ATM (parasitic) \- (coarse timing)  
      - [ ] Look for signals parasitically.   
- [ ] 

#### 

#### 

- [ ] 

#### Shift 5:

- [ ] laser/x-ray spatial overlap on sample paddle  
- [ ] Laser timing signal on sample paddle   
- [ ] ATM Setup  
- [ ] Fine timing in gas phase target (N2)

* Verify X,Y position of XFEL focus: MRCO XY-scan to find the center of beam with respect to the centering ring. 0 retardation. (N2)  
* Demonstrate all spectrometers and detectors working with variable retardation  
  * set up the retardation and the lens-can of the spectrometers for different retardation  
  * Retardation independent spectra for few features at different energy points of N2/NNO.  
  * Beta parameters for 0 to full retardation for N2, CO2, Ne.   
* Test Current Mode: Ensuring that the spectrometer is tuned for high signal rate mode, and validate MCP performance in cases of increased depletion  
  * we need to make sure that the MCP detectors are working at the non-linear gain  
  * 5, 10, 25, 50, 75, 100, 150, 200 mV signal level (without amplifier).  
  * Repeat 5, 10, 15, 25 after adding amplifiers.  
  * (laser only) find the common bias voltage for the MCP. Find the responsivity curve for each MCPs in the wagon-wheel. Measure the current through the MCP. Too many detectors, therefore needs more diagnostics.  
* Verify position of XFEL focus: MRCO Z-scan to find nonlinear signal (DCH in N2/NNO/?)  
  * If the non-linear is difficult to find, then consider using the blurring effect of space charge to identify the tightest focus.  
* Ne/Ar Calibration measurements  
  * FZP/MRCO correlation measurements for spectral reconstruction  
  * Redo the above with a different hit rate (as a factor of 1, 2, 4, 8, 16\* per feature).  
  * FZP/MRCO correlation measurements for spectral reconstruction in current mode  
* Laser Spatial overlap on paddle  
* Laser temporal overlap on paddle (some scope can be shared with X-10096)  
  * Verify optimal spatial overlap in same place for paddle vs. gas (SFI of N2)

