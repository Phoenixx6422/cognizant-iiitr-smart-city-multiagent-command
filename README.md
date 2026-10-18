# 🏙️ Metropolis Command Core (`smart_city_dashboard`)

**Autonomous 3-Tier Hierarchical Multi-Agent Operations & Command Center**  
*Developed for the Cognizant – IIIT Raichur AI Hackathon using the Cognizant Neuro® AI Multi-Agent Accelerator (`neuro-san-studio`)*

---

## 📌 Problem Statement & Overview

Modern cities operate across interconnected infrastructure silos—Power Grids, Water & Sewage, Traffic Mobility, Emergency Services, Telecom/IoT, and Public Safety. When a severe incident occurs (e.g., a cloudburst causing a substation feeder trip that disables stormwater pumps and floods arterial underpasses), isolated departmental dashboards fail to predict or resolve cascading failures.

**Metropolis Command Core (`smart_city_dashboard`)** solves this by implementing a **3-tier hierarchical multi-agent network** comprising **37 specialized AI agents** across **12 municipal domains**:
- **Decomposes** complex, multi-hazard urban crises in real time.
- **Traces** cascading cross-domain failure chains across a standardized 6-zone city digital twin.
- **Resolves** inter-departmental resource conflicts using a strict life-safety priority hierarchy.
- **Synthesizes** concrete telemetry into both an executive Markdown briefing and a strict JSON payload for real-time Command Center UI visualization.

---

## 🏗️ 3-Tier Multi-Agent Architecture (37 Agents)

```text
                    [ OPERATOR / INCIDENT TRIGGER ]
                                   │
                                   ▼
          ┌─────────────────────────────────────────────────┐
          │     TIER 1: city_command_orchestrator (1)       │
          │  Crisis Decomposition • Priority Conflict Res   │
          └────────────────────────┬────────────────────────┘
                                   │
       ┌───────────────────────────┼───────────────────────────┐
       ▼                           ▼                           ▼
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│   TIER 2: Domain    │     │   TIER 2: Domain    │     │  TIER 2: Lead #12   │
│   Leads (11 Depts)  │     │   Leads (Traffic,   │     │ analytics_dashboard │
│  (`*_lead` agents)  │     │   Grid, Water...)   │     │        _lead        │
└──────────┬──────────┘     └──────────┬──────────┘     └──────────┬──────────┘
           │                           │                           │
      ┌────┴────┐                 ┌────┴────┐                 ┌────┴────┐
      ▼         ▼                 ▼         ▼                 ▼         ▼
┌──────────┐┌──────────┐    ┌──────────┐┌──────────┐    ┌──────────┐┌──────────┐
│ Worker 1 ││ Worker 2 │    │ Worker 1 ││ Worker 2 │    │Correlat. ││ Payload  │
│ (Tier 3) ││ (Tier 3) │    │ (Tier 3) ││ (Tier 3) │    │  Agent   ││ Builder  │
└──────────┘└──────────┘    └──────────┘└──────────┘    └──────────┘└──────────┘
```

### Tier 1: Front-Man Orchestrator (1 Agent)
* **`city_command_orchestrator`**: Central command hub. Decomposes operator queries, delegates to Tier-2 Domain Leads, enforces conflict resolution priorities, and calls `analytics_dashboard_lead` to format the final output.

### Tier 2 (12 Domain Leads) & Tier 3 (24 Specialist Workers)

| # | Domain | Tier-2 Lead Agent | Tier-3 Specialist Worker 1 | Tier-3 Specialist Worker 2 |
| :- | :--- | :--- | :--- | :--- |
| 1 | **Traffic & Mobility** | `traffic_mobility_lead` | `flow_and_signal_agent` | `transit_and_detour_agent` |
| 2 | **Parking Management** | `parking_management_lead` | `parking_capacity_pricing_agent` | `parking_enforcement_guidance_agent` |
| 3 | **Energy & Grid** | `energy_grid_lead` | `grid_and_renewables_agent` | `ev_and_outage_restoration_agent` |
| 4 | **Environment & Weather** | `environment_weather_lead` | `air_heat_noise_agent` | `weather_and_flood_agent` |
| 5 | **Emergency Services** | `emergency_services_lead` | `first_responder_dispatch_agent` | `green_corridor_evacuation_agent` |
| 6 | **Waste Management** | `waste_management_lead` | `bin_and_route_optimizer_agent` | `special_waste_and_dumping_agent` |
| 7 | **Water & Sewage** | `water_sewage_lead` | `water_supply_quality_agent` | `sewage_and_drainage_agent` |
| 8 | **Infrastructure Risk** | `infrastructure_vulnerability_lead` | `structural_condition_agent` | `dependency_and_risk_scoring_agent` |
| 9 | **Citizen 311** | `citizen_311_lead` | `complaint_triage_clustering_agent` | `ticket_routing_notification_agent` |
| 10 | **Public Safety & CCTV** | `public_safety_surveillance_lead` | `cctv_crowd_analytics_agent` | `public_event_security_agent` |
| 11 | **Telecom & IoT** | `telecom_iot_connectivity_lead` | `iot_sensor_telemetry_agent` | `cyber_network_resilience_agent` |
| 12 | **Analytics & Dashboard** | `analytics_dashboard_lead` | `correlation_and_forecast_agent` | `dashboard_payload_builder_agent` |

---

## ⚖️ Cross-Domain Conflict Resolution & Cascade Engine

### Resource Conflict Priority Order
When two or more domains compete for constrained city resources (e.g., road capacity on Riverside Bridge, backup feeder power from Substation S-4, or field repair crews), `city_command_orchestrator` enforces:
1. **Priority 1 — Life Safety:** Emergency Services, hospital ER power/water, active evacuations.
2. **Priority 2 — Critical Infrastructure:** Grid stability, water/sewage containment, telecom/SCADA resilience, bridge structural integrity.
3. **Priority 3 — Traffic & Mobility:** Arterial road flow, public transit continuity, freight corridors.
4. **Priority 4 — Citizen Convenience:** Standard 311 requests, dynamic parking pricing, routine waste collection.

### Embedded Cross-Domain Dependency Triggers
- **Severe Storm / Rain** $\rightarrow$ Alerts *Environment, Water/Sewage, Traffic, Energy, Infrastructure, Telecom, Emergency*.
- **Power Outage** $\rightarrow$ Alerts *Energy, Traffic (dark signals), Water/Sewage (pumps), Emergency (hospitals), Parking (EV bays/gates), Telecom (gateways)*.
- **Major Fire / Accident** $\rightarrow$ Alerts *Emergency, Traffic (green corridors), Public Safety (CCTV/perimeter), Parking (hydrant clearance), Citizen 311*.
- **Sewage / Water Main Break** $\rightarrow$ Alerts *Water/Sewage, Infrastructure (sinkhole risk), Traffic (closures), Environment (contamination), Citizen 311*.
- **Sensor / Gateway Offline** $\rightarrow$ Alerts *Telecom/IoT* to verify whether anomalous readings in *Environment, Traffic, or Water* are stale or cyber-spoofed.

---

## 🗺️ Standardized City Geography (Digital Twin Zones)

All 37 agents reference a consistent set of municipal zones and asset IDs:
* **Zone A (Downtown):** Central Station Junction, Metro Hub, City Hall, Parking Lot P1
* **Zone B (Industrial Belt):** Substation S-4, Feeder F-12, HazMat Depot, Freight Corridor
* **Zone C (Riverside):** Riverside Bridge, Underpass U-2, Pump Station 3, Stormwater Drain D-7
* **Zone D (University District):** Campus Ave, Tech Park EV Hub, University Hospital
* **Zone E (Old Town):** Heritage Market, Trunk Sewer Line T-9, Bin Cluster BC-14
* **Zone F (Suburban North):** Solar Farm SF-1, Water Treatment Plant WTP-2, Landfill Site L-1

---

## 📂 Project Structure

```text
Cognizant_AIHackathon/
├── 1smart_city_dashboard/                # Custom Smart City Command Center Web UI
│   ├── static/                           # Frontend CSS/JS assets
│   ├── templates/                        # HTML dashboard templates
│   ├── agent_data.py                     # Telemetry & state parser
│   ├── server.py                         # FastAPI/Uvicorn backend server (Port 8002)
│   ├── start_ui.bat                      # One-click Windows launcher
│   └── start_ui.py                       # UI startup script
├── coded_tools/                          # Custom Python tools for sly_data manipulation
├── config/
│   ├── llm_config.hocon                  # OpenRouter / LLM model configuration
│   └── plugins.hocon                     # Neuro SAN runtime plugins
├── registries/
│   ├── project1/
│   │   └── smart_city_dashboard.hocon    # 37-agent HOCON network definition
│   └── manifest.hocon                    # Agent registry manifest
└── README.md                             # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository & Activate Virtual Environment
```powershell
git clone [https://github.com/](https://github.com/)<your-username>/smart-city-multiagent-command.git
cd Cognizant_AIHackathon
.\.venv\Scripts\Activate.ps1
```

### 2. Configure Environment Variables (`.env`)
Create a `.env` file in the root directory with your API credentials:
```env
OPENAI_API_KEY="your_openrouter_or_openai_api_key_here"
```

### 3. Verify LLM Configuration (`config/llm_config.hocon`)
```hocon
{
    "llm_config": {
        "class": "openai",
        "model_name": "google/gemini-2.5-flash",
        "base_url": "[https://openrouter.ai/api/v1](https://openrouter.ai/api/v1)",
        "temperature": 0.1
    }
}
```

Test your LLM configuration:
```powershell
ns check-config
```

---

## ▶️ Running the Application

### Option A: Launch Neuro SAN Studio & Multi-Agent Graph Visualizer
Start the Neuro SAN backend server (`localhost:8080`) and the `nsflow` client (`localhost:4173`):
```powershell
ns run
```
Open **`http://localhost:4173/?network=smart_city_dashboard`** in your browser to watch real-time agent delegation light up across the 3-tier network.

### Option B: Launch the Custom Smart City Command Center UI
Run the standalone dashboard interface on port `8002`:
```powershell
python 1smart_city_dashboard/start_ui.py
```
Open **`http://localhost:8002`** in your browser.

---

## 🧪 Demo Prompts for Testing

1. **Cascading Multi-Domain Emergency (Full Network Fan-Out):**
   > *"Severe cloudburst in Zone C (68 mm/hr) with Underpass U-2 flooding and a simultaneous Feeder F-12 power trip at Substation S-4 in Zone B. Coordinate full emergency response."*

2. **Water & Sewage Infrastructure Triage:**
   > *"Summarize the sewage and drainage situation across Trunk Sewer Line T-9 in Zone E and Stormwater Drain D-7 in Zone C."*

3. **Industrial HazMat Leak & Hospital Green Corridor:**
   > *"Chemical leak detected at HazMat Depot in Zone B during peak traffic. Establish emergency green corridors to University Hospital in Zone D and evaluate AQI plume risk."*

4. **Cyber-Physical Sensor Spoofing Check:**
   > *"Flood sensors at Underpass U-2 suddenly jumped to 3.2m with 0 mm/hr rainfall reported in Zone C. Verify whether the LoRaWAN gateway is spoofed before closing Riverside Bridge."*

---

## 📊 Output Contract (Markdown + Strict JSON)

Every response from `city_command_orchestrator` delivers:
1. **Executive Markdown Briefing:**
   - `### Situation Summary`
   - `### Domain Findings`
   - `### Cascading Cross-Domain Impacts`
   - `### Prioritized Action Plan`
   - `### 6-Hour Risk Outlook`
2. **Structured UI JSON Payload:** Includes `city_health_score` (0–100), `overall_severity` (`INFO` | `WARNING` | `CRITICAL`), per-domain telemetry & scores across all 11 operational domains, `cross_domain_chains`, prioritized `action_plan`, geospatial `map_markers`, and `forecast_next_6h`.
