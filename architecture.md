# System Architecture: Metropolis Command Core (`smart_city_dashboard`)

## 1. Architectural Vision: What We Are Trying to Do
Modern cities are complex, tightly coupled cyber-physical systems. However, municipal operations centers remain trapped in isolated departmental silos—Traffic Management, Power Grid Operations, Water & Sewage, Emergency Dispatch, and Telecom/IoT each monitor their own standalone dashboards. When a multi-hazard crisis occurs (for example, a severe cloudburst causing an electrical substation feeder to trip, which cuts power to stormwater pumps, floods an arterial underpass, and blocks ambulances heading to a trauma hospital), human operators cannot manually correlate cross-departmental telemetry fast enough to prevent cascading systemic failure.

**What Our Project Achieves:**
**Metropolis Command Core (`smart_city_dashboard`)** replaces fragmented municipal silos with an **autonomous, 3-tier hierarchical Multi-Agent System (MAS)** built on the **Cognizant Neuro® AI Multi-Agent Accelerator (`neuro-san-studio`)**. Our system:
1. **Autonomously Decomposes Crises:** Translates high-level operator queries or anomaly triggers into targeted, multi-departmental investigations.
2. **Traces Multi-Hop Cascading Failures:** Connects cause-and-effect chains across 12 distinct urban domains before secondary failures occur.
3. **Enforces Deterministic Conflict Resolution:** Arbitrates competing departmental requests for scarce city resources (road space, backup megawatts, field crews) using an immutable life-safety priority matrix.
4. **Delivers Dual-Mode Situational Intelligence:** Outputs both a structured 5-part Executive Markdown Briefing for human commanders and a strict, schema-validated JSON payload that drives our real-time web dashboard (`localhost:8002`) and Neuro SAN graph visualizer (`localhost:4173`).

---

## 2. Highlighting the Agentic System Design

Why use a **37-agent hierarchical architecture** instead of a single monolithic LLM prompt or a flat agent group?
* **Eliminating Context Bottlenecks & Hallucinations:** A single LLM prompted with 12 municipal domains, 24 asset categories, and complex JSON schemas suffers from attention dilution and invents vague prose. By isolating responsibilities into **1 Front-Man Orchestrator, 12 Domain Leads, and 24 Consolidated Specialist Workers**, each agent operates within a sharp, domain-specific system prompt.
* **True Departmental Autonomy with Upward Accountability:** Tier-3 Worker Agents focus exclusively on asset-level engineering telemetry (e.g., calculating intersection green-phase split seconds or pipe bar pressure). Tier-2 Domain Leads act as departmental chiefs that synthesize worker telemetry, flag cross-domain dependencies, and report upward. Tier-1 acts as the Incident Commander.
* **Shared Backstage Memory (`sly_data`) & Common Definitions (`commondefs`):** Using Neuro SAN’s declarative `.hocon` architecture, all 37 agents share a unified spatial mental model (`city_geography`), a strict upward reporting contract (`upward_reporting_contract`), and a shared backstage state dictionary (`sly_data`), ensuring zero drift in asset naming or zone boundaries.

---

## 3. High-Level System Topology

```text
+-----------------------------------------------------------------------------------+
|                        PRESENTATION & VISUALIZATION LAYER                         |
|  +-------------------------------------+   +-----------------------------------+  |
|  | Custom Command Center Web UI        |   | Neuro SAN Studio (nsflow)         |  |
|  | (FastAPI / Uvicorn on Port 8002)    |   | Real-Time Agent Graph (Port 4173) |  |
|  +------------------+------------------+   +-----------------+-----------------+  |
+---------------------|----------------------------------------|--------------------+
                      | REST / WebSocket                       | gRPC / HTTP (8080)
+---------------------v----------------------------------------v--------------------+
|                   TIER 1: FRONT-MAN INCIDENT COMMANDER (1 Agent)                  |
|                         [ city_command_orchestrator ]                             |
|   • Parses operator intent & triggers Cross-Domain Dependency Rules               |
|   • Resolves inter-domain resource conflicts (P1 Life Safety -> P4 Convenience)   |
|   • Invokes analytics_dashboard_lead for final UI & Markdown synthesis            |
+-----------------------------------------+-----------------------------------------+
                                          |
        +---------------------------------+---------------------------------+
        | Tool Delegation                 | Tool Delegation                 | Final Synthesis
        v                                 v                                 v
+-------+-----------------------+ +-------+-----------------------+ +-------+-----------------------+
| TIER 2: OPERATIONAL LEADS     | | TIER 2: INFRASTRUCTURE LEADS  | | TIER 2: INTELLIGENCE LEAD     |
| (Domains 1 - 6)               | | (Domains 7 - 11)              | | (Domain 12)                   |
| • traffic_mobility_lead       | | • water_sewage_lead           | | • analytics_dashboard_lead    |
| • parking_management_lead     | | • infrastructure_vuln_lead    | +---------------+---------------+
| • energy_grid_lead            | | • citizen_311_lead            |                 |
| • environment_weather_lead    | | • public_safety_surv_lead     |        +--------+--------+
| • emergency_services_lead     | | • telecom_iot_connect_lead    |        |                 |
| • waste_management_lead       | +---------------+---------------+        v                 v
+---------------+---------------+                 |               +----------------+ +----------------+
                |                                 |               | correlation_   | | dashboard_     |
       +--------+--------+               +--------+--------+      | and_forecast_  | | payload_       |
       |                 |               |                 |      | agent (Tier 3) | | builder (T3)   |
       v                 v               v                 v      +----------------+ +----------------+
+--------------+  +--------------+ +--------------+  +--------------+
| Worker 1     |  | Worker 2     | | Worker 1     |  | Worker 2     |
| (Tier 3)     |  | (Tier 3)     | | (Tier 3)     |  | (Tier 3)     |
| 12 Agents    |  | 12 Agents    | | (Asset Telemetry & Actions)    |
+------+-------+  +------+-------+ +------+-------+  +------+-------+
       |                 |                |                 |
+------v-----------------v----------------v-----------------v-----------------------+
|                     SHARED STATE & SIMULATION SUBSTRATE                           |
|  • Shared `sly_data` State Channels: traffic, parking, energy, environment,       |
|    emergency, waste, water_sewage, infrastructure, citizen_requests,              |
|    public_safety, telecom_iot, analytics, active_alerts                           |
|  • Standardized 6-Zone Digital Twin Geography (Zones A, B, C, D, E, F)            |
+-----------------------------------------------------------------------------------+
```

---

## 4. Detailed Breakdown of the 3-Tier Agent Network

### Tier 1: The Front-Man Orchestrator (1 Agent)
* **`city_command_orchestrator`**: The central brain of the `.hocon` network. It has 12 registered tools corresponding to the 12 Tier-2 Domain Leads. When an operator submits a query or crisis scenario, the orchestrator:
  1. Consults its embedded **Cross-Domain Dependency Rules** to identify both obvious primary domains and hidden secondary domains.
  2. Dispatches parallel or sequential tool calls to the relevant Tier-2 Domain Leads.
  3. Evaluates upward reports from the leads and resolves resource contentions using the **4-Tier Priority Matrix**.
  4. Calls `analytics_dashboard_lead` to compute composite health scores and format the final dual-mode output.

### Tier 2 & Tier 3: The 12 Domain Leads and 24 Specialist Workers
Each Tier-2 Domain Lead manages a specific municipal department and delegates granular telemetry gathering to **2 Consolidated Tier-3 Specialist Workers**:

| Domain # | Tier-2 Domain Lead | Tier-3 Specialist Worker Agents | Core Agentic Responsibilities & Telemetry Metrics |
| :--- | :--- | :--- | :--- |
| **1. Traffic & Mobility** | `traffic_mobility_lead` | • `flow_and_signal_agent`<br>• `transit_and_detour_agent` | Corridor speeds (km/h), v/c ratios, intersection green-phase split adjustments (sec), bus/metro headway gaps, detour ETAs (min). |
| **2. Parking Management** | `parking_management_lead` | • `parking_capacity_pricing_agent`<br>• `parking_enforcement_guidance_agent` | Lot/street occupancy (%), EV bay overlap, dynamic surge tariffs (Rs/hr), hydrant/lane tow dispatch ETAs, driver guidance. |
| **3. Energy & Grid** | `energy_grid_lead` | • `grid_and_renewables_agent`<br>• `ev_and_outage_restoration_agent` | Substation feeder loads (%), solar output vs. forecast (MW), smart streetlight dimming, EV hub load-shedding (MW), crew ETAs. |
| **4. Environment & Weather** | `environment_weather_lead` | • `air_heat_noise_agent`<br>• `weather_and_flood_agent` | Zone AQI (PM2.5/PM10 $\mu\text{g/m}^3$), urban heat-island deltas ($^\circ\text{C}$), noise (dB), rainfall (mm/hr), wind (km/h), flood gauge depth (m). |
| **5. Emergency Services** | `emergency_services_lead` | • `first_responder_dispatch_agent`<br>• `green_corridor_evacuation_agent` | Police/Fire/ALS ambulance dispatch, hydrant bar verification, hospital ER/ICU load (%), green corridor signal preemption, shelters. |
| **6. Waste Management** | `waste_management_lead` | • `bin_and_route_optimizer_agent`<br>• `special_waste_and_dumping_agent` | Ultrasonic smart-bin fill (%), compactor route optimization (km/fuel saved), biomedical/HazMat queues, drain debris clearance. |
| **7. Water & Sewage** | `water_sewage_lead` | • `water_supply_quality_agent`<br>• `sewage_and_drainage_agent` | Pipe pressure (bar), acoustic leak loss (kL/hr), chlorine/turbidity, trunk sewer blockage (%), stormwater pump flow ($\text{m}^3\text{/hr}$). |
| **8. Infrastructure Risk** | `infrastructure_vulnerability_lead` | • `structural_condition_agent`<br>• `dependency_and_risk_scoring_agent` | Bridge vibration (Hz) & scour depth, subsurface sinkhole radar, Single-Point-of-Failure (SPOF) mapping, 0–100 risk scores, repair cost (Rs Lakhs). |
| **9. Citizen 311** | `citizen_311_lead` | • `complaint_triage_clustering_agent`<br>• `ticket_routing_notification_agent` | 311 report ingestion, spatial de-duplication into P1–P4 clusters, ticket ID routing (`TKT-YYYY-XXXX`), geo-fenced SMS alerts. |
| **10. Public Safety & CCTV** | `public_safety_surveillance_lead` | • `cctv_crowd_analytics_agent`<br>• `public_event_security_agent` | AI CCTV crowd density ($\text{persons/m}^2$), unattended object/perimeter breach detection, smart barricades, venue egress rates. |
| **11. Telecom & IoT** | `telecom_iot_connectivity_lead` | • `iot_sensor_telemetry_agent`<br>• `cyber_network_resilience_agent` | 5G/LoRaWAN gateway uptime (%), packet loss (%), sensor battery SoC (%), SCADA/MQTT spoofing & DDoS detection, mesh failover. |
| **12. Analytics & Dashboard** | `analytics_dashboard_lead` | • `correlation_and_forecast_agent`<br>• `dashboard_payload_builder_agent` | Domain & city health scoring (0–100), multi-domain cascade chain tracing, 1–6h trend forecasting, strict UI JSON compilation. |

---

## 5. Core Agentic Mechanics & Protocols

### A. Standardized Digital Twin Geography (`city_geography`)
Injected via `commondefs.replacement_strings` into all 37 agents, the network operates over a deterministic 6-zone municipal map so that agents across different departments reference the exact same physical assets:
* **Zone A (Downtown):** Central Station Junction, Metro Hub, City Hall, Parking Lot P1.
* **Zone B (Industrial Belt):** Substation S-4, Feeder F-12, HazMat Depot, Freight Corridor.
* **Zone C (Riverside):** Riverside Bridge, Underpass U-2, Pump Station 3, Stormwater Drain D-7.
* **Zone D (University District):** Campus Ave, Tech Park EV Hub, University Hospital.
* **Zone E (Old Town):** Heritage Market, Trunk Sewer Line T-9, Bin Cluster BC-14.
* **Zone F (Suburban North):** Solar Farm SF-1, Water Treatment Plant WTP-2, Landfill Site L-1.

### B. Strict Upward Reporting Contract (`upward_reporting_contract`)
To prevent conversational drift between Tier-3 Workers, Tier-2 Leads, and the Tier-1 Orchestrator, every upward response is bound by a strict telemetry contract:
* **No Vague Prose:** Agents are prohibited from returning generic statements (e.g., *"Traffic is congested"*). They must output concrete asset IDs, zones, numerical values, engineering units, and ETAs in minutes (tagging fallback simulation metrics with `"simulated": true`).
* **Structured Schema:** Every upward report contains `domain`, `zone`, `severity` (`INFO` | `WARNING` | `CRITICAL`), `key_metrics`, `recommended_action`, `confidence_pct`, `eta_min`, and `cross_domain_alerts`.

### C. Cross-Domain Dependency & Cascade Rules (`cross_domain_rules`)
Both the Orchestrator and Domain Leads are programmed with reactive cascade triggers:
1. **Severe Storm / Rain** $\rightarrow$ Triggers *Environment, Water/Sewage, Traffic, Energy, Infrastructure, Telecom, Emergency*.
2. **Power Outage** $\rightarrow$ Triggers *Energy, Traffic (dark signals), Water/Sewage (Pump Station 3), Emergency (University Hospital), Parking (EV hubs), Telecom (gateways)*.
3. **Major Fire / Accident** $\rightarrow$ Triggers *Emergency, Traffic (green corridors), Public Safety (CCTV), Parking (hydrant tow), Citizen 311*.
4. **Sewage / Water Main Break** $\rightarrow$ Triggers *Water/Sewage, Infrastructure (sinkhole risk), Traffic, Environment, Citizen 311*.
5. **High AQI / Heatwave** $\rightarrow$ Triggers *Environment, Energy (HVAC load), Emergency, Traffic (Freight Corridor emission limits)*.
6. **Stadium Event / Crowd Surge** $\rightarrow$ Triggers *Public Safety, Traffic, Parking, Waste, Energy, Telecom (5G load)*.
7. **Sensor / Gateway Offline** $\rightarrow$ Triggers *Telecom/IoT* to verify whether anomalous spikes in *Environment, Traffic, or Water* are stale or cyber-spoofed.

### D. Deterministic Conflict Resolution Hierarchy
When two or more Domain Leads request conflicting actions on a shared city asset, `city_command_orchestrator` resolves the deadlock using an explicit priority ordering:

$$
\text{Priority 1: Life Safety} > \text{Priority 2: Critical Infrastructure} > \text{Priority 3: Traffic \& Mobility} > \text{Priority 4: Citizen Convenience}
$$

* **Example 1 (Road Space Conflict):** `traffic_mobility_lead` wants to route commuter detours across **Riverside Bridge**, while `emergency_services_lead` requires an unobstructed Green Corridor across **Riverside Bridge** for ambulances heading to **University Hospital**. **Result:** Priority 1 overrides Priority 3; lanes are preempted for EMS.
* **Example 2 (Electrical Load Conflict):** During a **Substation S-4** transformer overload, `parking_management_lead` requests power for **Tech Park EV Hub**, while `water_sewage_lead` needs power for **Pump Station 3** to prevent **Underpass U-2** from flooding. **Result:** Priority 2 overrides Priority 4; EV chargers are throttled via load-shedding to keep stormwater pumps online.

---

## 6. End-to-End Execution Lifecycle (Sequence Flow)

1. **Operator Input / Incident Trigger:** The user submits a query via the Neuro SAN Studio client (`localhost:4173`) or the custom Command Center UI (`localhost:8002`).
2. **Orchestrator Decomposition:** `city_command_orchestrator` evaluates the prompt against the `cross_domain_rules` and selects the affected Tier-2 Domain Leads.
3. **Departmental Delegation:** Each invoked Tier-2 Lead calls its two Tier-3 Specialist Worker tools in parallel.
4. **Telemetry Computation & State Sync:** Tier-3 Workers inspect `sly_data` (or generate realistic simulated sensor readings with `"simulated": true`), compute engineering interventions and ETAs, and return their structured payload to their Tier-2 Lead.
5. **Lead Aggregation & Conflict Flagging:** Tier-2 Leads merge worker payloads, attach `cross_domain_alerts`, and report back to `city_command_orchestrator`.
6. **Analytics & Payload Compilation:** The Orchestrator resolves any inter-departmental conflicts and passes the consolidated findings to `analytics_dashboard_lead`, which invokes `correlation_and_forecast_agent` (to score all 11 domains from 0–100 and project 6-hour trends) and `dashboard_payload_builder_agent` (to construct the UI JSON).
7. **Dual-Format Output Delivery:** The Orchestrator returns the 5-section Executive Markdown Briefing followed immediately by the validated JSON block, updating map markers, health gauges, and action tables on the operator's screen.

---

## 7. Technology Stack & Deployment Topology

* **Multi-Agent Orchestration Framework:** Cognizant Neuro® AI Multi-Agent Accelerator (`neuro-san` & `neuro-san-studio`)
* **Agent Network Configuration:** Declarative HOCON (`registries/project1/smart_city_dashboard.hocon`) utilizing `commondefs` string interpolation
* **LLM Backbone:** OpenRouter API (`google/gemini-2.5-flash` / `google/gemini-3-flash-preview` configured via `config/llm_config.hocon` at `temperature: 0.1` for deterministic tool calling)
* **Backend & Visualization Services:**
  * **Neuro SAN Server:** Port `8080` (Agent runtime & tool execution engine)
  * **nsflow Visualizer Client:** Port `4173` (Interactive real-time multi-agent call graph and trace logs)
  * **Custom Smart City Command UI:** Port `8002` (FastAPI/Uvicorn web dashboard in `1smart_city_dashboard/` rendering live domain health cards, map markers, and cascade chains)