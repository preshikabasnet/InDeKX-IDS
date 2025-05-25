# 📂 InDeKX-Edge-IDS: A Research Showcase on Secure Edge Architecture

Welcome! This repository shares the story behind **InDeKX**, a research-driven framework I developed to address real-world security challenges in edge computing environments. While the code isn’t published here, you’ll find everything needed to understand the architecture, data generation, and the evaluation process — all designed and tested in a virtual lab setting.


## 🌟 What This Project Is About

As edge computing continues to grow, securing thousands of IoT devices without centralized control is a massive challenge. **InDeKX** (Intrusion Detection and Knowledge eXchange) proposes a hierarchical system that detects threats at the edge and shares those alerts across the network — fast, lightweight, and scalable.

I built and tested this system using simulated data, custom microservices, and open-source tools like **Snort IDS** and **EdgeX Foundry**, running everything inside a virtualized testbed.
---

## 🧱 What’s Inside This Repository

```bash
InDeKX-Edge-IDS/
├── frameworks/             # Posters, papers, and diagrams explaining the architecture
│   ├── InDeKX-Architecture.png
│   ├── InDeKX-Paper.pdf
│   ├── InDeKX-Poster.png
│   ├── device_data_packets_25_nodes_specific.csv   --  datasets simulated IoT traffic used in testing
│   ├── device_data_packets_50_nodes_specific.csv
│   ├── device_data_packets_75_nodes_specific.csv
│   ├── device_data_packets_100_nodes_specific.csv
│   └── indekx_traffic_simulator.py
│
├── README.md              
└── LICENSE
```

### 📊 What dataset were used for Experimentation 
 We utilized the VARIoT Dataset of Legitimate IoT Data to simulate various types of sensor data. The dataset is modified to contain the desired number of Edge Nodes, based on unique device identifiers. Additionally, we also inject variable percentages of randomly placed anomalous data patterns to perform experimentation on the desired InDeKX functionalities.

The datasets were generated using a Python script [`normalized_iot_data_generator.py`](./datasets/normalized_iot_data_generator.py) that takes real-world weather station data and normalizes it to simulate behavior from IoT devices.

**What it does:**
- Loads raw weather sensor data (e.g., temperature, wind speed)
- Normalizes data ranges using `MinMaxScaler`
- Assigns device labels to mimic edge nodes
- Outputs structured CSV files for 25, 50, 75, and 100-node test cases

These CSVs were then used to simulate IoT device behavior in a testbed environment, feeding into Snort IDS to evaluate detection accuracy and system scalability.


## 🔒 About the Code

While I contributed to the prototype implementation and model accuracy testing — including Java services, Snort rule sets, and the testbed — the **code is not included here** due to infrastructure constraints. Instead, this repo serves as a **public record of the system design, evaluation methods, and key outcomes**.

Think of this as a **living blueprint** for anyone interested in building secure edge systems or understanding how edge IDS frameworks can work in practice.


## 📘 Dive Deeper into the Work

If you're curious about the details, check out the following resources:

- 📄 [Research Paper (PDF)](InDeKX-Paper.pdf) – Full write-up of the architecture, motivation, and results
- 🖼 [Research Poster](InDeKX-Poster.png) – A visual summary presented at a research showcase
- 🧩 [Architecture Diagram](InDeKX-Architecture.png) – How everything fits together


## 🙋 Who I Am

Hi! I’m Preshika, an aspiring IT and cloud security professional passionate about making systems smarter and safer. This project reflects my interest in edge computing, system design, and applied security — and I'm always open to collaboration, feedback, or new opportunities.

📬 Let's connect:
- [LinkedIn](https://www.linkedin.com/in/preshikabasnet/)  


## 📜 License

This project is shared under the [MIT License](./LICENSE). Feel free to explore and build on these ideas!

Thanks for stopping by ✨
