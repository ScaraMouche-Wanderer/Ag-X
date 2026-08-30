# Project Ag-X: Silver Loss Reduction in Fumer Plant Slag

> **A Dual-Track Metallurgical & Hybrid Physics+AI Digital Twin Programme**  
> *Target: Eliminate silver loss from 192 ppm to &le;25 ppm across &ge;90% of production batches.*  
> **-By Pratham**

---

## 🎯 Executive Summary

In lead and zinc pyrometallurgical fuming furnaces, precious metals (predominantly Silver / Ag) are lost to tapped waste slag at baseline concentrations averaging **192 ppm**. 

**Project Ag-X** delivers an integrated two-track engineering solution:
1. **Track A (Metallurgical Engineering)**: Immediate physical settling, launder fluid dynamics, basicity fluxing ($CaO/SiO_2 = 1.15$), and slag cleaning hold time ($45\text{ min}$) to eliminate mechanical entrainment of bullion prills.
2. **Track B (Hybrid Digital Twin)**: Combines first-principles thermodynamics (*FactSage / Thermo-Calc mass & energy balance*) with machine learning residual correction (*LightGBM on 1-min OSIsoft PI tags*) for closed-loop DCS/PLC setpoint control.

---

## 📊 Key Performance & Value Metrics

| Metric | Baseline | Project Ag-X Target | Impact |
| :--- | :--- | :--- | :--- |
| **Slag Ag Concentration** | **192.4 ppm** | **&le; 25.0 ppm** | **-167.4 ppm** loss elimination |
| **Batch Compliance** | &lt; 15% | **&ge; 90%** of batches | Process variance compression |
| **Annual Recovered Ag** | Baseline | **16,700 kg / yr** | &asymp; **5,36,920 Troy Oz / yr** |
| **Annual Gross Net Value** | — | **₹141.95 Crore / yr** | **₹1,41,95,00,000 / yr** recurring revenue |
| **Capital Payback** | — | **&lt; 2.5 Months** | Rapid ROI on CapEx |

---

## 🔬 Core Pyrometallurgical Mechanisms

SEM/EDS slag profiling (500x magnification) demonstrates the root-cause split of silver losses:
- **70–80% Mechanical Entrainment (Dominant)**: Microscopic Pb/Cu bullion prills suspended in viscous slag failing to settle before tapping.
- **15–20% Chemical Dissolution**: Ionic $Ag^+$ and $Ag_2O$ dissolved in high-$FeO$ silicate slag.
- **< 5% Volatilization**: Sub-oxide vapor species reporting to baghouse flue dust.

---

## 💻 Interactive Features

- **60 FPS Interactive Furnace Blast & Multi-Phase Settling Simulator**: HTML5 Canvas visualizing submerged tuyere blast convection, slag/bullion boundary layer stratification, and live telemetry HUD.
- **Interactive ROI Calculator**: Real-time Indian Rupee (₹) financial model with customizable slag tonnage, silver market price, and target recovery.
- **Filterable 8-Phase Strategic Roadmap**: Interactive phase selector across Track A (Metallurgy) and Track B (Digital Twin).
- **Responsive Industrial Design**: Clean typography, dark mode accents, and a custom scroll meter indicator.

---

## 🚀 Quick Start (Running Locally)

To view the interactive engineering proposal locally:

```bash
# Clone the repository
git clone https://github.com/ScaraMouche-Wanderer/Ag-X.git
cd Ag-X

# Run a local HTTP server
python3 -m http.server 8000
```

Open your browser and navigate to: `http://localhost:8000/`

---

## 📁 Repository Structure

```
Ag-X/
├── index.html               # Main interactive platform
├── style.css                # Custom responsive design system
├── generate_diagrams.py     # High-resolution architectural diagram generator
├── assets/                  # Diagrams, SEM micrographs, and hero furnace imagery
│   ├── figure_1.png         # Strategic Roadmap (Tracks A & B)
│   ├── figure_2.png         # Hybrid Digital Twin Architecture
│   ├── figure_3.png         # Performance Projections & Error Convergence
│   ├── sem_microstructure.jpg # SEM/EDS 500x micrograph of bullion prills in slag
│   └── hero_furnace.jpg     # Blast furnace operation visual
└── README.md                # Project documentation
```

---

## 👤 Author

- **-By Pratham**  
*Project Ag-X · Fumer Pyrometallurgy & Digital Twin Engineering*
