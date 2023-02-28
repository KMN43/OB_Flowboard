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
Before running app run `pip install -r requirements.txt` to update needed libs

```shell
flowboard-app.py  #Main page. This is the file you run with "streamlit run"
└─── tabs/ #Tabs on main page to redirect to OB main core processes
  └─── tab1 -> Customer Experience
  └─── tab2 -> Transfer Out
  └─── tab3 -> Vendor Returns
```  



## Features

### On Sidebar
* Show next ExSD
* Show minutes to PAD Time
* OB TPH
* Lagrange Capacity for Singles, Multis and Total
    * Delta capacity to Lagrange override
* TCAP% Volume for Singles, Multis and Total
* Alerts:
    * PPSingleMedium is *close* to FLowPause
    * PPSingleMedium **is** in FlowPause
    * Pickable Backlog < 1,5k units
    * OB Backlog < 5,0k units
* Config:
    * App refresh rate in seconds

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
