#!/usr/bin/env python3
"""
Generate ultra-clear, high-resolution SVG and PNG diagrams for the Fumer Plant project.
- Figure 1: Strategic Roadmap (Tracks A & B, perfectly spaced, crystal clear text)
- Figure 2: Digital Twin Architecture (Cleaned: removed 32T charge, removed soft sensor section)
- Figure 3: Performance Projections (Ag in slag trend + Digital Twin accuracy)
"""

import subprocess
import os

def render_svg_to_png(svg_content, out_png_path, width=None):
    svg_temp = out_png_path.replace('.png', '.svg')
    with open(svg_temp, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    cmd = ['rsvg-convert']
    if width:
        cmd.extend(['-w', str(width)])
    else:
        cmd.extend(['--zoom', '2.0'])
    cmd.extend(['-o', out_png_path, svg_temp])
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error rendering {out_png_path}: {res.stderr}")
    else:
        print(f"Successfully generated {out_png_path} and {svg_temp}")

def make_figure_1():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 820" width="1440" height="820" style="background:#ffffff; font-family:'Segoe UI', Inter, -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <defs>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.06"/>
    </filter>
    <marker id="arrowNavy" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M1,1 L7,4 L1,7 Z" fill="#1E3A8A"/>
    </marker>
    <marker id="arrowTeal" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M1,1 L7,4 L1,7 Z" fill="#0F766E"/>
    </marker>
    <marker id="arrowGreen" markerWidth="8" markerHeight="8" refX="4" refY="2" orient="auto">
      <path d="M1,1 L4,2 L1,3 Z" fill="#0D9488"/>
    </marker>
  </defs>

  <!-- Title Header -->
  <text x="720" y="46" font-size="26" font-weight="800" fill="#0F172A" text-anchor="middle" letter-spacing="-0.5">Project Ag-X — Strategic Roadmap</text>
  <text x="720" y="74" font-size="14.5" font-style="italic" font-weight="500" fill="#475569" text-anchor="middle">From root-cause diagnosis (192 ppm) to sustained control at target (≤25 ppm)</text>

  <!-- ==================== TRACK A ==================== -->
  <!-- Track A Banner -->
  <rect x="50" y="105" width="1340" height="40" rx="6" fill="#1E3A8A"/>
  <text x="720" y="130" font-size="13.5" font-weight="700" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.8">TRACK A — METALLURGICAL / OPERATIONAL FIX  <tspan font-weight="400" fill="#93C5FD">(drives the 192 → 25 ppm gap)</tspan></text>

  <!-- Track A Phase Cards -->
  <!-- Card 1 -->
  <g transform="translate(50, 160)">
    <rect width="295" height="155" rx="10" fill="#F8FAFC" stroke="#1E3A8A" stroke-width="2" filter="url(#cardShadow)"/>
    <rect x="15" y="14" width="265" height="24" rx="4" fill="#EFF6FF"/>
    <text x="147" y="30" font-size="12" font-weight="800" fill="#1E3A8A" text-anchor="middle" letter-spacing="0.5">PHASE 1</text>
    <text x="147" y="66" font-size="16" font-weight="800" fill="#0F172A" text-anchor="middle">Root-Cause Diagnosis</text>
    <text x="147" y="94" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Slag SEM / EDS analysis</text>
    <text x="147" y="114" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Entrainment vs. dissolution split</text>
    <text x="147" y="140" font-size="11.5" font-weight="700" fill="#B45309" text-anchor="middle">Duration: 1–2 wks</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <line x1="355" y1="237" x2="388" y2="237" stroke="#1E3A8A" stroke-width="2.5" marker-end="url(#arrowNavy)"/>

  <!-- Card 2 -->
  <g transform="translate(398, 160)">
    <rect width="295" height="155" rx="10" fill="#F8FAFC" stroke="#1E3A8A" stroke-width="2" filter="url(#cardShadow)"/>
    <rect x="15" y="14" width="265" height="24" rx="4" fill="#EFF6FF"/>
    <text x="147" y="30" font-size="12" font-weight="800" fill="#1E3A8A" text-anchor="middle" letter-spacing="0.5">PHASE 2</text>
    <text x="147" y="66" font-size="16" font-weight="800" fill="#0F172A" text-anchor="middle">Quick-Win Trials</text>
    <text x="147" y="94" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Settling time &amp; reductant dosing</text>
    <text x="147" y="114" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Basicity &amp; tapping practice review</text>
    <text x="147" y="140" font-size="11.5" font-weight="700" fill="#B45309" text-anchor="middle">Duration: 4–8 wks</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <line x1="703" y1="237" x2="736" y2="237" stroke="#1E3A8A" stroke-width="2.5" marker-end="url(#arrowNavy)"/>

  <!-- Card 3 -->
  <g transform="translate(746, 160)">
    <rect width="295" height="155" rx="10" fill="#F8FAFC" stroke="#1E3A8A" stroke-width="2" filter="url(#cardShadow)"/>
    <rect x="15" y="14" width="265" height="24" rx="4" fill="#EFF6FF"/>
    <text x="147" y="30" font-size="12" font-weight="800" fill="#1E3A8A" text-anchor="middle" letter-spacing="0.5">PHASE 3</text>
    <text x="147" y="66" font-size="16" font-weight="800" fill="#0F172A" text-anchor="middle">Process / Design Fix</text>
    <text x="147" y="94" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Slag settling / cleaning stage</text>
    <text x="147" y="114" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Launder redesign &amp; feed blending</text>
    <text x="147" y="140" font-size="11.5" font-weight="700" fill="#B45309" text-anchor="middle">Duration: 3–6 mo</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <line x1="1051" y1="237" x2="1084" y2="237" stroke="#1E3A8A" stroke-width="2.5" marker-end="url(#arrowNavy)"/>

  <!-- Card 4 -->
  <g transform="translate(1095, 160)">
    <rect width="295" height="155" rx="10" fill="#F8FAFC" stroke="#1E3A8A" stroke-width="2" filter="url(#cardShadow)"/>
    <rect x="15" y="14" width="265" height="24" rx="4" fill="#EFF6FF"/>
    <text x="147" y="30" font-size="12" font-weight="800" fill="#1E3A8A" text-anchor="middle" letter-spacing="0.5">PHASE 4</text>
    <text x="147" y="66" font-size="16" font-weight="800" fill="#0F172A" text-anchor="middle">Stabilize &amp; Hold Target</text>
    <text x="147" y="94" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">SOPs &amp; statistical control limits</text>
    <text x="147" y="114" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Operator training · ≤25 ppm sustained</text>
    <text x="147" y="140" font-size="11.5" font-weight="700" fill="#059669" text-anchor="middle">Status: Ongoing</text>
  </g>

  <!-- ==================== VERTICAL LINK ==================== -->
  <path d="M 197 325 L 197 410" fill="none" stroke="#0D9488" stroke-width="2" stroke-dasharray="4,4"/>
  <polygon points="197,416 193,408 201,408" fill="#0D9488"/>
  <text x="215" y="372" font-size="12.5" font-style="italic" font-weight="600" fill="#0F766E">feeds data collection from day one</text>

  <!-- ==================== TRACK B ==================== -->
  <!-- Track B Banner -->
  <rect x="50" y="425" width="1340" height="40" rx="6" fill="#0F766E"/>
  <text x="720" y="450" font-size="13.5" font-weight="700" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.8">TRACK B — DATA &amp; DIGITAL TWIN  <tspan font-weight="400" fill="#99F6E4">(holds the gains, prevents drift)</tspan></text>

  <!-- Track B Phase Cards -->
  <!-- Card 5 -->
  <g transform="translate(50, 480)">
    <rect width="295" height="155" rx="10" fill="#F0FDFA" stroke="#0F766E" stroke-width="2" filter="url(#cardShadow)"/>
    <rect x="15" y="14" width="265" height="24" rx="4" fill="#CCFBF1"/>
    <text x="147" y="30" font-size="12" font-weight="800" fill="#0F766E" text-anchor="middle" letter-spacing="0.5">PHASE 5</text>
    <text x="147" y="66" font-size="16" font-weight="800" fill="#0F172A" text-anchor="middle">Data Foundation</text>
    <text x="147" y="94" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Historian (1-min) + LIMS + MES</text>
    <text x="147" y="114" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Batch-linked production data</text>
    <text x="147" y="140" font-size="11.5" font-weight="700" fill="#B45309" text-anchor="middle">Timeline: In parallel from Ph.1</text>
  </g>

  <!-- Arrow 5 -> 6 -->
  <line x1="355" y1="557" x2="388" y2="557" stroke="#0F766E" stroke-width="2.5" marker-end="url(#arrowTeal)"/>

  <!-- Card 6 -->
  <g transform="translate(398, 480)">
    <rect width="295" height="155" rx="10" fill="#F0FDFA" stroke="#0F766E" stroke-width="2" filter="url(#cardShadow)"/>
    <rect x="15" y="14" width="265" height="24" rx="4" fill="#CCFBF1"/>
    <text x="147" y="30" font-size="12" font-weight="800" fill="#0F766E" text-anchor="middle" letter-spacing="0.5">PHASE 6</text>
    <text x="147" y="66" font-size="16" font-weight="800" fill="#0F172A" text-anchor="middle">Predictive ML Model</text>
    <text x="147" y="94" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Real-time process state estimation</text>
    <text x="147" y="114" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Ag ppm forecast ahead of lab assay</text>
    <text x="147" y="140" font-size="11.5" font-weight="700" fill="#B45309" text-anchor="middle">Timeline: After Ph.2</text>
  </g>

  <!-- Arrow 6 -> 7 -->
  <line x1="703" y1="557" x2="736" y2="557" stroke="#0F766E" stroke-width="2.5" marker-end="url(#arrowTeal)"/>

  <!-- Card 7 -->
  <g transform="translate(746, 480)">
    <rect width="295" height="155" rx="10" fill="#F0FDFA" stroke="#0F766E" stroke-width="2" filter="url(#cardShadow)"/>
    <rect x="15" y="14" width="265" height="24" rx="4" fill="#CCFBF1"/>
    <text x="147" y="30" font-size="12" font-weight="800" fill="#0F766E" text-anchor="middle" letter-spacing="0.5">PHASE 7</text>
    <text x="147" y="66" font-size="16" font-weight="800" fill="#0F172A" text-anchor="middle">Physics + ML Digital Twin</text>
    <text x="147" y="94" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Mass / heat balance + thermodynamics</text>
    <text x="147" y="114" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">ML correction + optimizer engine</text>
    <text x="147" y="140" font-size="11.5" font-weight="700" fill="#B45309" text-anchor="middle">Timeline: After Ph.3</text>
  </g>

  <!-- Arrow 7 -> 8 -->
  <line x1="1051" y1="557" x2="1084" y2="557" stroke="#0F766E" stroke-width="2.5" marker-end="url(#arrowTeal)"/>

  <!-- Card 8 -->
  <g transform="translate(1095, 480)">
    <rect width="295" height="155" rx="10" fill="#F0FDFA" stroke="#0F766E" stroke-width="2" filter="url(#cardShadow)"/>
    <rect x="15" y="14" width="265" height="24" rx="4" fill="#CCFBF1"/>
    <text x="147" y="30" font-size="12" font-weight="800" fill="#0F766E" text-anchor="middle" letter-spacing="0.5">PHASE 8</text>
    <text x="147" y="66" font-size="16" font-weight="800" fill="#0F172A" text-anchor="middle">Advisory → Closed-Loop</text>
    <text x="147" y="94" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Operator advisory setpoints</text>
    <text x="147" y="114" font-size="12.5" font-weight="500" fill="#475569" text-anchor="middle">Then DCS / PLC auto-execution</text>
    <text x="147" y="140" font-size="11.5" font-weight="700" fill="#047857" text-anchor="middle">Timeline: Long-term</text>
  </g>

  <!-- ==================== TARGET GATE BANNER ==================== -->
  <g transform="translate(220, 675)">
    <rect width="1000" height="46" rx="23" fill="#FEF3C7" stroke="#D97706" stroke-width="1.8" filter="url(#cardShadow)"/>
    <text x="500" y="29" font-size="13.5" font-weight="700" fill="#92400E" text-anchor="middle" letter-spacing="0.2">
      Target gate: Ag in slag ≤ 25 ppm sustained across ≥ 90% of batches, before advancing to closed-loop control
    </text>
  </g>
</svg>'''
    return svg

def make_figure_2():
    # Cleaned Figure 2:
    # 1. Removed "(32 T BATCH FEED)" -> "PLANT FURNACE OPERATION & FEED"
    # 2. Removed "AI SOFT SENSOR" block entirely!
    # Streamlined flow:
    # 1 -> Plant Operation & Feed
    # 2 -> Data Platform
    # 3 -> Digital Twin Core (Physics + ML Correction)
    # 4 -> Constrained Optimization Engine
    # 5 -> Recommended Setpoints & Explainability
    # 6 -> Operator Advisory -> DCS/PLC Closed Loop
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1150" width="1000" height="1150" style="background:#ffffff; font-family:'Segoe UI', Inter, -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <defs>
    <filter id="shadowBox" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arrowDown" markerWidth="8" markerHeight="8" refX="4" refY="6" orient="auto">
      <path d="M1,2 L4,6 L7,2 Z" fill="#475569"/>
    </marker>
    <marker id="arrowUp" markerWidth="8" markerHeight="8" refX="4" refY="2" orient="auto">
      <path d="M1,6 L4,2 L7,6 Z" fill="#0F766E"/>
    </marker>
  </defs>

  <!-- Title Header -->
  <text x="500" y="44" font-size="24" font-weight="800" fill="#0F172A" text-anchor="middle" letter-spacing="-0.5">Project Ag-X: Digital Twin Architecture</text>
  <text x="500" y="70" font-size="13.5" font-style="italic" font-weight="500" fill="#475569" text-anchor="middle">Physics model + ML correction, closing the loop from feed to operator recommendation</text>

  <!-- Left Feedback Loop Line -->
  <path d="M 65 1040 L 45 1040 L 45 225 L 75 225" fill="none" stroke="#0F766E" stroke-width="2" stroke-dasharray="5,4"/>
  <polygon points="75,225 65,220 65,230" fill="#0F766E"/>
  <text transform="translate(32, 630) rotate(-90)" font-size="11.5" font-style="italic" font-weight="600" fill="#0F766E" text-anchor="middle">
    Lab assay verification feeds back → continuous model retraining &amp; bias calibration
  </text>

  <!-- ==================== BOX 1: PLANT OPERATION ==================== -->
  <g transform="translate(80, 95)">
    <rect width="840" height="90" rx="8" fill="#1E3A8A" filter="url(#shadowBox)"/>
    <text x="30" y="32" font-size="14.5" font-weight="800" fill="#FFFFFF" letter-spacing="0.5">1 — PLANT FURNACE OPERATION &amp; FEED</text>
    <text x="45" y="58" font-size="12.5" font-weight="500" fill="#DBEAFE">• Feed Assay: Ag, Pb, Cu, Fe, Zn, S, SiO₂, CaO, Al₂O₃, moisture</text>
    <text x="45" y="77" font-size="12.5" font-weight="500" fill="#DBEAFE">• Operating Setpoints: Temperature, pressure, blast air / O₂, flux dosing, reductant</text>
  </g>

  <!-- Down Arrow 1 -> 2 -->
  <line x1="500" y1="185" x2="500" y2="210" stroke="#475569" stroke-width="2.5" marker-end="url(#arrowDown)"/>

  <!-- ==================== BOX 2: DATA PLATFORM ==================== -->
  <g transform="translate(80, 215)">
    <rect width="840" height="75" rx="8" fill="#2563EB" filter="url(#shadowBox)"/>
    <text x="30" y="30" font-size="14.5" font-weight="800" fill="#FFFFFF" letter-spacing="0.5">2 — DATA PLATFORM</text>
    <text x="45" y="56" font-size="12.5" font-weight="500" fill="#EFF6FF">• OSIsoft PI Historian (1-min tags) + LIMS lab results + MES batch records</text>
  </g>

  <!-- Down Arrow 2 -> 3 -->
  <line x1="500" y1="290" x2="500" y2="315" stroke="#475569" stroke-width="2.5" marker-end="url(#arrowDown)"/>

  <!-- ==================== BOX 3: DIGITAL TWIN CORE ==================== -->
  <g transform="translate(80, 320)">
    <!-- Container Card -->
    <rect width="840" height="235" rx="10" fill="#F8FAFC" stroke="#1E3A8A" stroke-width="2" filter="url(#shadowBox)"/>
    <text x="420" y="28" font-size="15" font-weight="800" fill="#0F172A" text-anchor="middle" letter-spacing="0.5">3 — DIGITAL TWIN CORE (HYBRID MODEL)</text>
    
    <!-- Physics Sub-Card -->
    <g transform="translate(20, 42)">
      <rect width="385" height="175" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
      <text x="192" y="26" font-size="13" font-weight="800" fill="#1E3A8A" text-anchor="middle" letter-spacing="0.5">PHYSICS LAYER</text>
      <text x="25" y="56" font-size="12" font-weight="600" fill="#1E293B">• Mass &amp; heat balances</text>
      <text x="25" y="82" font-size="12" font-weight="600" fill="#1E293B">• Slag thermodynamics &amp; redox (FactSage)</text>
      <text x="25" y="108" font-size="12" font-weight="600" fill="#1E293B">• Liquidus &amp; viscosity relations</text>
      <text x="25" y="134" font-size="12" font-weight="600" fill="#1E293B">• Fuming reaction kinetics &amp; settling rate</text>
    </g>

    <!-- Center Plus -->
    <circle cx="420" cy="130" r="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="420" y="137" font-size="20" font-weight="800" fill="#0F766E" text-anchor="middle">+</text>

    <!-- ML Sub-Card -->
    <g transform="translate(435, 42)">
      <rect width="385" height="175" rx="8" fill="#F0FDFA" stroke="#0D9488" stroke-width="1.5"/>
      <text x="192" y="26" font-size="13" font-weight="800" fill="#0F766E" text-anchor="middle" letter-spacing="0.5">ML CORRECTION LAYER</text>
      <text x="25" y="56" font-size="12" font-weight="600" fill="#1E293B">• Learns furnace-specific operational bias</text>
      <text x="25" y="82" font-size="12" font-weight="600" fill="#1E293B">• Captures feed variability &amp; moisture effects</text>
      <text x="25" y="108" font-size="12" font-weight="600" fill="#1E293B">• Adjusts for refractory wear &amp; campaign drift</text>
      <text x="25" y="134" font-size="12" font-weight="600" fill="#1E293B">• Compensates for unmeasured disturbances</text>
    </g>
  </g>

  <!-- Down Arrow 3 -> 4 -->
  <line x1="500" y1="555" x2="500" y2="585" stroke="#475569" stroke-width="2.5" marker-end="url(#arrowDown)"/>

  <!-- ==================== BOX 4: CONSTRAINED OPTIMIZATION ENGINE ==================== -->
  <g transform="translate(80, 590)">
    <rect width="840" height="110" rx="8" fill="#581C87" filter="url(#shadowBox)"/>
    <text x="30" y="30" font-size="14.5" font-weight="800" fill="#FFFFFF" letter-spacing="0.5">4 — CONSTRAINED OPTIMIZATION ENGINE</text>
    <text x="45" y="58" font-size="12.5" font-weight="600" fill="#F3E8FF">• Objective: Minimize Ag loss + λ₁·Energy + λ₂·Flux consumption + λ₃·Fume loss</text>
    <text x="45" y="82" font-size="12.5" font-weight="500" fill="#E9D5FF">• Hard Constraints: Temperature &amp; pressure OEM limits, basicity (CaO/SiO₂), FeO redox window</text>
  </g>

  <!-- Down Arrow 4 -> 5 -->
  <line x1="500" y1="700" x2="500" y2="730" stroke="#475569" stroke-width="2.5" marker-end="url(#arrowDown)"/>

  <!-- ==================== BOX 5: RECOMMENDED SETPOINTS & EXPLAINABILITY ==================== -->
  <g transform="translate(80, 735)">
    <rect width="840" height="115" rx="8" fill="#B45309" filter="url(#shadowBox)"/>
    <text x="30" y="30" font-size="14.5" font-weight="800" fill="#FFFFFF" letter-spacing="0.5">5 — RECOMMENDED SETPOINTS + EXPLAINABILITY</text>
    <text x="45" y="58" font-size="12.5" font-weight="600" fill="#FEF3C7">• Actionable Recommendations: T, pressure, blast air / O₂, flux dosing, reductant, hold / settling time</text>
    <text x="45" y="82" font-size="12.5" font-weight="500" fill="#FDE68A">• Explainable Drivers: Quantified attribution (basicity shift, settling gain, slag viscosity reduction)</text>
  </g>

  <!-- Down Arrow 5 -> 6 -->
  <line x1="500" y1="850" x2="500" y2="880" stroke="#475569" stroke-width="2.5" marker-end="url(#arrowDown)"/>

  <!-- ==================== BOX 6: OPERATOR ADVISORY -> DCS/PLC ==================== -->
  <g transform="translate(80, 885)">
    <rect width="840" height="110" rx="8" fill="#1E293B" filter="url(#shadowBox)"/>
    <text x="30" y="30" font-size="14.5" font-weight="800" fill="#FFFFFF" letter-spacing="0.5">6 — OPERATOR ADVISORY → DCS / PLC (CLOSED LOOP)</text>
    <text x="45" y="58" font-size="12.5" font-weight="600" fill="#E2E8F0">• Phase 1 (Advisory): Metallurgist &amp; operator review setpoints before approving implementation</text>
    <text x="45" y="82" font-size="12.5" font-weight="500" fill="#94A3B8">• Phase 2 (Closed-Loop): Automatic setpoint transmission to DCS / PLC after extended validation</text>
  </g>

  <!-- Bottom Subtitle / Compliance -->
  <text x="500" y="1030" font-size="12.5" font-weight="600" fill="#047857" text-anchor="middle">
    ✔ Continuous validation ensures Ag in slag ≤ 25 ppm while maintaining full thermal and equipment safety
  </text>
</svg>'''
    return svg

def make_figure_3():
    # High clarity Figure 3:
    # Left chart: Ag in Slag Trend across Phases (192 ppm down to <= 25 ppm)
    # Right chart: Digital Twin Model Prediction Accuracy
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 640" width="1440" height="640" style="background:#ffffff; font-family:'Segoe UI', Inter, -apple-system, BlinkMacSystemFont, Roboto, sans-serif;">
  <defs>
    <filter id="boxShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.07"/>
    </filter>
  </defs>

  <!-- Title -->
  <text x="720" y="40" font-size="24" font-weight="800" fill="#0F172A" text-anchor="middle" letter-spacing="-0.5">Project Ag-X: Digital Twin Performance Projections</text>
  <text x="720" y="66" font-size="13.5" font-style="italic" font-weight="500" fill="#475569" text-anchor="middle">Empirical model: Ag loss trajectory across implementation phases (left) and model accuracy convergence (right)</text>

  <!-- ==================== LEFT PANEL: AG IN SLAG TRAJECTORY ==================== -->
  <g transform="translate(50, 95)">
    <rect width="645" height="500" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" filter="url(#boxShadow)"/>
    <text x="322" y="32" font-size="15" font-weight="800" fill="#1E3A8A" text-anchor="middle">Ag-in-Slag Trajectory Across Programme Phases</text>

    <!-- Grid lines -->
    <!-- Y-axis labels: 200, 150, 100, 50, 25, 0 -->
    <!-- Plot area: x=65 to 605 (width 540), y=60 to 420 (height 360) -->
    <!-- y(200)=70, y(150)=150, y(100)=230, y(50)=310, y(25)=350, y(0)=390 -->
    <line x1="65" y1="70" x2="605" y2="70" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="74" font-size="11" font-weight="600" fill="#64748B" text-anchor="end">200</text>

    <line x1="65" y1="150" x2="605" y2="150" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="154" font-size="11" font-weight="600" fill="#64748B" text-anchor="end">150</text>

    <line x1="65" y1="230" x2="605" y2="230" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="234" font-size="11" font-weight="600" fill="#64748B" text-anchor="end">100</text>

    <line x1="65" y1="310" x2="605" y2="310" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="314" font-size="11" font-weight="600" fill="#64748B" text-anchor="end">50</text>

    <!-- 25 ppm Target Band -->
    <rect x="65" y="340" width="540" height="20" fill="#DCFCE7" opacity="0.7"/>
    <line x1="65" y1="350" x2="605" y2="350" stroke="#059669" stroke-width="2" stroke-dasharray="6,3"/>
    <text x="55" y="354" font-size="11" font-weight="700" fill="#059669" text-anchor="end">25 ppm</text>
    <text x="595" y="335" font-size="11" font-weight="700" fill="#047857" text-anchor="end">OEM TARGET: ≤25 ppm</text>

    <!-- Axes -->
    <line x1="65" y1="390" x2="605" y2="390" stroke="#475569" stroke-width="1.5"/>
    <line x1="65" y1="60" x2="65" y2="390" stroke="#475569" stroke-width="1.5"/>

    <!-- Phase vertical zones: Wks 0-2 (Ph 1), Wks 2-10 (Ph 2), Wks 10-26 (Ph 3), Wks 26-52 (Ph 4-8) -->
    <!-- Width 540: x=65 (0w), x=110 (2w), x=230 (10w), x=390 (26w), x=605 (52w) -->
    <line x1="110" y1="60" x2="110" y2="390" stroke="#CBD5E1" stroke-dasharray="3,3"/>
    <line x1="230" y1="60" x2="230" y2="390" stroke="#CBD5E1" stroke-dasharray="3,3"/>
    <line x1="390" y1="60" x2="390" y2="390" stroke="#CBD5E1" stroke-dasharray="3,3"/>

    <!-- Phase Labels at bottom -->
    <text x="87" y="415" font-size="10.5" font-weight="700" fill="#1E3A8A" text-anchor="middle">Ph.1</text>
    <text x="87" y="430" font-size="9.5" fill="#64748B" text-anchor="middle">Diag.</text>

    <text x="170" y="415" font-size="10.5" font-weight="700" fill="#1E3A8A" text-anchor="middle">Ph.2: Quick Wins</text>
    <text x="170" y="430" font-size="9.5" fill="#64748B" text-anchor="middle">Settling &amp; Flux Trials</text>

    <text x="310" y="415" font-size="10.5" font-weight="700" fill="#1E3A8A" text-anchor="middle">Ph.3: Design Fix</text>
    <text x="310" y="430" font-size="9.5" fill="#64748B" text-anchor="middle">Launder &amp; Slag Stage</text>

    <text x="497" y="415" font-size="10.5" font-weight="700" fill="#0F766E" text-anchor="middle">Ph.4–8: Digital Twin &amp; Closed Loop</text>
    <text x="497" y="430" font-size="9.5" fill="#64748B" text-anchor="middle">Sustained Control &amp; Optimization</text>

    <!-- Variance confidence interval shaded polygon -->
    <!-- Points:
      0w: upper=192+35 (227->26), lower=192-35 (157->138)
      2w: upper=225(29), lower=160(134)
      10w: upper=115(206), lower=75(270)
      26w: upper=48(313), lower=28(345)
      52w: upper=25(350), lower=18(361)
    -->
    <polygon points="65,26 110,29 230,206 390,313 605,350 605,361 390,345 230,270 110,134 65,138" fill="#93C5FD" opacity="0.35"/>

    <!-- Mean Ag in Slag line -->
    <!-- Points: (65,83) -> (110,83) -> (230,238) -> (390,329) -> (605,355) -->
    <path d="M 65,83 L 110,83 Q 170,120 230,238 Q 310,310 390,329 L 605,355" fill="none" stroke="#1D4ED8" stroke-width="3.5"/>

    <!-- Point Callouts -->
    <!-- Baseline 192 ppm -->
    <circle cx="87" cy="83" r="5" fill="#EF4444" stroke="#FFFFFF" stroke-width="2"/>
    <text x="100" y="76" font-size="11.5" font-weight="800" fill="#DC2626">Baseline: 192 ppm</text>

    <!-- Target 22 ppm -->
    <circle cx="605" cy="355" r="5" fill="#059669" stroke="#FFFFFF" stroke-width="2"/>
    <text x="590" y="375" font-size="11.5" font-weight="800" fill="#047857" text-anchor="end">Sustained: ~22 ppm (±3 ppm)</text>

    <!-- Legend box -->
    <g transform="translate(180, 455)">
      <line x1="0" y1="12" x2="30" y2="12" stroke="#1D4ED8" stroke-width="3"/>
      <text x="38" y="16" font-size="11" font-weight="600" fill="#1E293B">Average Ag ppm in Slag</text>

      <rect x="195" y="4" width="20" height="15" fill="#93C5FD" opacity="0.45"/>
      <text x="222" y="16" font-size="11" font-weight="600" fill="#1E293B">Batch Variance Band (90% CI)</text>
    </g>
  </g>

  <!-- ==================== RIGHT PANEL: DIGITAL TWIN ACCURACY ==================== -->
  <g transform="translate(745, 95)">
    <rect width="645" height="500" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" filter="url(#boxShadow)"/>
    <text x="322" y="32" font-size="15" font-weight="800" fill="#0F766E" text-anchor="middle">Digital Twin Prediction Accuracy Maturation</text>

    <!-- Grid / Plot Area: x=65 to 605, y=60 to 420 -->
    <!-- X-axis: 0 to 500 batches; Y-axis: -30 ppm to +30 ppm error -->
    <!-- y(+30)=80, y(+20)=130, y(+10)=180, y(0)=230, y(-10)=280, y(-20)=330, y(-30)=380 -->
    <line x1="65" y1="80" x2="605" y2="80" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="84" font-size="11" font-weight="600" fill="#64748B" text-anchor="end">+30</text>

    <line x1="65" y1="130" x2="605" y2="130" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="134" font-size="11" font-weight="600" fill="#64748B" text-anchor="end">+20</text>

    <line x1="65" y1="180" x2="605" y2="180" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="184" font-size="11" font-weight="600" fill="#64748B" text-anchor="end">+10</text>

    <!-- ±5 ppm Target Band -->
    <rect x="65" y="205" width="540" height="50" fill="#CCFBF1" opacity="0.8"/>
    <line x1="65" y1="205" x2="605" y2="205" stroke="#0D9488" stroke-width="1.5" stroke-dasharray="4,3"/>
    <line x1="65" y1="255" x2="605" y2="255" stroke="#0D9488" stroke-width="1.5" stroke-dasharray="4,3"/>
    <text x="595" y="222" font-size="11" font-weight="700" fill="#0F766E" text-anchor="end">Target Accuracy: ±5 ppm</text>

    <line x1="65" y1="230" x2="605" y2="230" stroke="#0F766E" stroke-width="2"/>
    <text x="55" y="234" font-size="11" font-weight="700" fill="#0F766E" text-anchor="end">0</text>

    <line x1="65" y1="280" x2="605" y2="280" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="284" font-size="11" font-weight="600" fill="#64748B" text-anchor="end">-10</text>

    <line x1="65" y1="330" x2="605" y2="330" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="334" font-size="11" font-weight="600" fill="#64748B" text-anchor="end">-20</text>

    <line x1="65" y1="380" x2="605" y2="380" stroke="#E2E8F0" stroke-width="1"/>
    <text x="55" y="384" font-size="11" font-weight="600" fill="#64748B" text-anchor="end">-30</text>

    <!-- Axes -->
    <line x1="65" y1="60" x2="65" y2="390" stroke="#475569" stroke-width="1.5"/>
    <line x1="65" y1="390" x2="605" y2="390" stroke="#475569" stroke-width="1.5"/>

    <!-- X-axis batch labels -->
    <text x="65" y="410" font-size="10.5" font-weight="600" fill="#64748B" text-anchor="middle">0</text>
    <text x="173" y="410" font-size="10.5" font-weight="600" fill="#64748B" text-anchor="middle">100</text>
    <text x="281" y="410" font-size="10.5" font-weight="600" fill="#64748B" text-anchor="middle">200</text>
    <text x="389" y="410" font-size="10.5" font-weight="600" fill="#64748B" text-anchor="middle">300</text>
    <text x="497" y="410" font-size="10.5" font-weight="600" fill="#64748B" text-anchor="middle">400</text>
    <text x="605" y="410" font-size="10.5" font-weight="600" fill="#64748B" text-anchor="middle">500</text>
    <text x="335" y="432" font-size="11.5" font-weight="700" fill="#334155" text-anchor="middle">Number of Operating Batches Trained</text>

    <!-- Error envelope compression: narrows from ±26 ppm down to ±3 ppm -->
    <polygon points="65,95 150,130 280,185 450,215 605,217 605,243 450,245 280,275 150,330 65,365" fill="#5EEAD4" opacity="0.4"/>

    <!-- Scatter dots showing batches -->
    <!-- Early wide scatter -->
    <circle cx="80" cy="115" r="3.5" fill="#0D9488" opacity="0.6"/>
    <circle cx="95" cy="340" r="3.5" fill="#0D9488" opacity="0.6"/>
    <circle cx="110" cy="140" r="3.5" fill="#0D9488" opacity="0.6"/>
    <circle cx="130" cy="310" r="3.5" fill="#0D9488" opacity="0.6"/>
    <circle cx="150" cy="160" r="3.5" fill="#0D9488" opacity="0.6"/>
    <circle cx="170" cy="285" r="3.5" fill="#0D9488" opacity="0.6"/>
    <!-- Mid tightening -->
    <circle cx="200" cy="190" r="3.5" fill="#0D9488" opacity="0.7"/>
    <circle cx="230" cy="265" r="3.5" fill="#0D9488" opacity="0.7"/>
    <circle cx="260" cy="205" r="3.5" fill="#0D9488" opacity="0.7"/>
    <circle cx="300" cy="250" r="3.5" fill="#0D9488" opacity="0.7"/>
    <circle cx="340" cy="215" r="3.5" fill="#0D9488" opacity="0.7"/>
    <circle cx="380" cy="242" r="3.5" fill="#0D9488" opacity="0.7"/>
    <!-- Mature tight band -->
    <circle cx="420" cy="225" r="3.5" fill="#047857" opacity="0.85"/>
    <circle cx="450" cy="235" r="3.5" fill="#047857" opacity="0.85"/>
    <circle cx="480" cy="228" r="3.5" fill="#047857" opacity="0.85"/>
    <circle cx="510" cy="232" r="3.5" fill="#047857" opacity="0.85"/>
    <circle cx="540" cy="226" r="3.5" fill="#047857" opacity="0.85"/>
    <circle cx="570" cy="234" r="3.5" fill="#047857" opacity="0.85"/>
    <circle cx="600" cy="229" r="3.5" fill="#047857" opacity="0.85"/>

    <!-- Legend box -->
    <g transform="translate(180, 455)">
      <rect x="0" y="4" width="20" height="15" fill="#CCFBF1" stroke="#0D9488" stroke-width="1"/>
      <text x="28" y="16" font-size="11" font-weight="600" fill="#1E293B">±5 ppm Accuracy Specification Band</text>

      <circle cx="250" cy="12" r="4" fill="#047857"/>
      <text x="260" y="16" font-size="11" font-weight="600" fill="#1E293B">Batch Prediction vs Lab Residual</text>
    </g>
  </g>
</svg>'''
    return svg

if __name__ == '__main__':
    assets_dir = '/home/voidnode/Work/FUMER/assets'
    os.makedirs(assets_dir, exist_ok=True)

    fig1_svg = make_figure_1()
    render_svg_to_png(fig1_svg, os.path.join(assets_dir, 'figure_1.png'), width=2880)

    fig2_svg = make_figure_2()
    render_svg_to_png(fig2_svg, os.path.join(assets_dir, 'figure_2.png'), width=2000)

    fig3_svg = make_figure_3()
    render_svg_to_png(fig3_svg, os.path.join(assets_dir, 'figure_3.png'), width=2880)
    print("All diagrams generated successfully!")
