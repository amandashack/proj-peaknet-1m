### Detailed Shift Plan

#### High Level Goals:

- [ ] Establish Streaking in MRCO  
- [ ] Study the resonant AM yield of a molecular ion and a fragment ion from the same core-  
      excited state.  
      - [ ] Expect shifts in the molecular peak due to change in the geometry.  
      - [ ] Sigma\* resonance at the F edge. Does the excitation energy matter? No  
      - [ ] CF4  
            - [ ] Previously observed ultrafast decay.  
            - [ ] Energy shift of 10 eV between early and late decay patterns.  
            - [ ] Some interesting Doppler splittings  
            - [ ] Needs the relative distribution of the TOFs to be well understood.   
- [ ] Differentiate the early and late decay patterns in CF4, and derive the distribution in time.  
- [ ] Prioritize on single shot reconstruction following angular streaking.

Goals discussed on 10/11/2024:

- [ ] Step 0: All TOFs tuned for Carbon 1s angular streaking  
      - [ ] \~690 eV (at/around resonance) and 750 eV (above)  
- [ ] Step 1: Reserve the TOFs for Doppler shift (ports 0, 180, 90, 270).  
- [ ] Step 2: Reserve most number of TOFs among the rest of the 12 TOFs for Carbon Auger, followed by F Auger  
- [ ] Keep SF6 as a backup. More discussion needs to happen about changed sample.  
- [ ] Need to think about a backup plan for gas mixing with Kr with CF4.  
- [ ] Relative efficiency of the TOFs needs to be understood.

#### Shift :

- [ ] Bring beam down to TMO (45 min)  
      - [x] ~~Start with 400 eV photon energy.~~  
      - [x] ~~Beam to IM5K4~~  
      - [x] ~~Check KBO transmission~~  
      - [x] ~~On the sample paddle:~~  
            - [x] ~~Check x-ray size on the paddle with the microscope for:~~  
                  - [ ] Nominal focus, MRCO position (check spot size).   
                  - [ ] Push focus downstream:  
                        set\_KB1(bender\_preset=’50umIP\_z50mm’)  
                  - [ ] See the focus get larger on the microscope paddle.    
      - [ ] CheckIP timing on sample paddle diode  
            - [ ] Check x-ray signal  
            - [ ] Time laser signal  
- [ ] Timing ATM (1 hour):  
      - [ ] Spatial Overlap laser on IMATM  
      - [ ] Coarse timing on IMATM diode  
      - [ ] Fine timing on ATM target (txt)  
- [ ] Timing at IP with paddle (30 min):  
      - [ ] Paddle scan on SiN target for fine timing.  
- [ ] Setup XLEAP (\~1 hours) w/o spectrometer (reload config).   
- [ ] Setup FZP spectrometer at 400 eV.  
      Decision Point whether 690 or 400 eV  
      Should we go to 690 eV \+ associated FZP setup?  
- [ ] Re-establish ATM timing with XLEAP.  
        
- [ ] Use Argon to do angular streaking at 400 eV.  
- [ ] Change sample to CF4  
      - [ ] Be at photon energy of 400 eV and look at Carbon 1s photo.  
- [ ] For 690 eV, do a photon energy scan from 680 to 710 eV using CF4.  
      - [ ] Step 0: All TOFs tuned for Carbon 1s angular streaking  
            - [ ] \~690 eV (at/around resonance) and 750 eV (above)

- [x] ~~Commission 690 eV Zone plate for Photon spectrometer. (1 hour)~~  
- [ ] Photon energy scan of CF4 between 680 to 710 eV, single pulse.  
- [ ] Laser Spatial/temporal Overlap:(90 min)  
      - [ ] Check spatial overlap on sample paddle  
      - [ ]  Ask for more energy and check timing on the sample paddle  
- [ ] Switch to XLEAP  
      - [ ] Check IM2K4 and IM5K4: did the beam drift  
      - [ ] Check ATM spatial overlap:  
      - [ ] Check ATM signal (might be very weak due to less pulse energy)  
      - [ ] Check spatial overlap on sample paddle

      

      

      

Shift 2:  
	High level goal.

- [ ] 0, 90, 180, 270 (F edge \- 630 V), the rest of the carbon (20 V).  
      - [ ] w/2w setting XLEAP. (345/690 to 375/750)  
      - [ ] Establishes ATM time signal.  
      - [ ] Hf-2hf PV scan.  
      - [ ] Absorption scan with SASE.  
      - [ ] 750 eV above threshold. (Can we go there? Yes)...  
            - [ ] F or C 1s for time t \= 0  
            - [ ] Find the FZP to go over there 750 eV  
            - [ ] Make sure counts are as high as possible.

Plan:

- [ ] Bring beam down to TMO (45 min)  
      - [ ] Start with 400 eV photon energy.  
      - [ ] Beam to IM5K4  
      - [ ] Check KBO transmission  
      - [ ] On the sample paddle:  
            - [ ] Check x-ray size on the paddle with the microscope for:  
                  - [ ] Nominal focus, MRCO position (check spot size).   
      - [ ] Timing ATM (1 hour):  
            - [ ] Spatial Overlap laser on IMATM  
            - [ ] Coarse timing on IMATM diode  
            - [ ] Fine timing on ATM target (txt)  
      - [ ] Timing at IP with paddle (30 min):  
            - [ ] Paddle scan on SiN target for fine timing.  
      - [ ] Absorption scan with SASE settings (between 665 \- 705 eV).  
      - [ ] Setup the TOF spectrometer in the interleaved settings:  
            - [ ] 0, 90, 180, 270 (F edge \- 630 V), the rest of the carbon (20 V).  
            - [ ]  hf\_2hf PV scan.  
      - [ ] 750 eV to excite above resonance of F.

Shift 3:

We see very little angular streaking.

- [ ] Bring beam down to TMO (45 min)  
      - [ ] Start with 400 eV photon energy.  
      - [ ] Beam to IM5K4  
      - [ ] Check KBO transmission  
      - [ ] On the sample paddle:  
            - [ ] Check x-ray size on the paddle with the microscope for:  
                  - [ ] Nominal focus, MRCO position (check spot size).   
                  - [ ] Move to Ming-Fu, 30 um focus spot size.  
                  - [ ] Do spatial overlap of IR/X-ray. Step at different focal positions in X and Y to find the range of movement.  
      - [ ] Timing ATM (1 hour):  
            - [ ] Spatial Overlap laser on IMATM  
            - [ ] Coarse timing on IMATM diode  
            - [ ] Fine timing on ATM target (txt)  
      - [ ] 

