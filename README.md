<p align="center">
<img src="https://github.com/KMN43/OB_Flowboard/blob/main/Flowboard%20LOGO-02.png" width="446" height="337">
</p>


# Outbound Flowboard


<!-- ABOUT THE PROJECT -->
## About The Project

OB Flowboard optimizes Outbound workflow by centralizing main key information shift for planning and execution and help making critical decisions points across the operation including CX, VRET and TSO process paths in order to positively CX impact and cost. 



<!-- GETTING STARTED -->
## Usage

OB Flowboard is run by `streamlit` on *localhost:8501*. For the time being app is run through a *run_app.bat* file that calls ´streamlit´ locally.
Before running app:
1. Run `pip install -r requirements.txt` to update needed libs.
2. Edit *run_app.bat* to decleare local path to `streamlit` directory

---

Flowboard data is structured according to the following pattern:

```shell
flowboard-app.py  #Main page. This is the file you run with "streamlit run"
└─── tabs/ #Tabs on main page to redirect to OB main core processes
  └─── tab1 -> Customer Experience
  └─── tab2 -> Transfer Out
  └─── tab3 -> Vendor Returns
```  


## Features

```shell
+CUSTOMER EXPERIENCIE+
-------------------------------------------------------------------------------------------------------------------------------
| ON SIDEBAR:                                         |  ON MAIN:
-----------------------------------------------------   -----------------------------------------------------------------------
* Show next ExSD                                         [IMPORTANT] All WIP metrics exclude hardcapped/non-pickable units
* Show minutes to PAD Time                               * SINGLE #Associated to PPSingleMedium
* OB TPH                                                     - PNYP / PickingPicked units
* Lagrange Capacity for Singles, Multis and Total            - Single tote diverted to Jackpot Line / On Jackpot Line dropzone
    - Delta capacity to Lagrange override                    - Total Single active totes
* TCAP% Volume for Singles, Multis and Total                 - Total (Singles + Multis) C7 units
* Alerts:                                                * Multis #Associated to PPMultiMedium
    - PPSingleMedium is *close* to FLowPause                 - ReadyToPick / PNYP / PickingPicked / RB / Sorted units
    - PPSingleMedium is in FlowPause                     * Backlog
    - Pickable Backlog < 1,5k units                          - Total (Singles + Multis) pickable units 
    - OB Backlog < 5,0k units                                - Total OB Backlog (Includings FRACS units assigned to CX PPhs)
* Ship Goal input
* Config:                                                * Recirculation #Displayed as num. of containers marked with LANE_FULL
    - App refresh rate in seconds                        * Info
    - [WIP] Number of ExSDs on CORA to be shown              - Current shift shipped units
                                                             - Suggested OB Capacity to EOS to achieve ship goal on input
                                                             - Last update timestamp

Flowboard is able to detect current shift by time range
    
```
![GUI](https://github.com/KMN43/OB_Flowboard/blob/main/GUI_Flowboard.png)

<!-- ROADMAP -->
## Roadmap

- [x] Generate Alert message
- [x] Embebed libk to shipment on Rodeo
- [ ] Multi FC Alert
- [ ] Multi-level Alert
    - [ ] Alert L.1 - When shipments are within next ExSD SLA
    - [ ] Alert L.2 - when shipments are outside it's ExSD SLA


<!-- CONTACT -->
## POC

Jorge Casas (DELGJR) - [Mail](delgjr@amazon.com)

Project Link: [LSA_Project](https://github.com/KMN43/lambda_LargeShipment)
