<img src="https://github.com/KMN43/OB_Flowboard/blob/main/Flowboard%20LOGO-02.png" width="446" height="337">

# Outbound Flowboard

<!-- ABOUT THE PROJECT -->
## About The Project

OB Flowboard optimizes Outbound workflow by centralizing main key information shift for planning and execution and help making critical decisions points across the operation including CX, VRET and TSO process paths in order to positively CX impact and cost. 



<!-- GETTING STARTED -->
## Usage

When LSA is triggered a messega is posted tagging all present members on chime room. Message contains following info:

* Shipment ID (linked to Rodeo)
* ASIN
* Shipment quantity
* Expected Ship Date

![LSA_Bot](https://github.com/KMN43/lambda_LargeShipment/blob/main/LSA_Bot.JPG?raw=true)


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
