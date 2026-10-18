# Project Summary: Metropolis Command Core (`smart_city_dashboard`)

**Project Title:** Metropolis Command Core — Autonomous 3-Tier Multi-Agent Smart City Operations & Command Center

**Event:** Cognizant – IIIT Raichur AI Hackathon

**Framework:** Cognizant Neuro® AI Multi-Agent Accelerator (`neuro-san-studio`)

## 1. Executive Summary & Problem Statement

Modern urban infrastructure does not fail in isolation; it fails in **cascades**. When an extreme weather event strikes a city, a lightning strike or flood at an electrical substation can trip a primary power feeder. That single electrical fault immediately disables municipal stormwater pump stations, which in turn causes arterial underpasses to flood, paralyzes commuter transit, blocks emergency ambulances from reaching trauma centers, and triggers a surge of citizen distress calls.

Traditional Smart City platforms suffer from **departmental compartmentalization**. Traffic controllers, energy grid operators, water/sewage engineers, and emergency dispatchers monitor isolated dashboards. Because these systems do not communicate autonomously in real time, human operators are forced to manually correlate telemetry across departments during high-stress crises—leading to delayed responses, conflicting resource allocations, and preventable infrastructure damage.

**Metropolis Command Core (`smart_city_dashboard`)** solves this challenge by introducing an **autonomous, 3-tier hierarchical multi-agent operations network**. Built on Cognizant’s Neuro SAN framework using declarative `.hocon` orchestration, the platform coordinates **37 specialized AI agents** across **12 municipal domains**. It decomposes complex urban crises, traces hidden cross-domain dependencies, resolves inter-departmental resource conflicts using a deterministic life-safety hierarchy, and outputs both human-readable executive briefings and structured JSON payloads for real-time geospatial visualization.

## 2. System Architecture: The 3-Tier Agent Hierarchy

To prevent context window bottlenecks, eliminate hallucinated telemetry, and mirror real-world Incident Command System (ICS) structures, the network is organized into a strict **3-tier hierarchy (1 Orchestrator** $\rightarrow$ **12 Domain Leads** $\rightarrow$ **24 Specialist Workers)**:

### Tier 1: Front-Man Orchestrator (`city_command_orchestrator`)

Acting as the central Incident Commander, the Tier-1 Orchestrator is the single point of interaction for the human operator. It never fabricates street-level metrics. Instead, it analyzes incoming incidents, identifies both primary and secondary affected municipal domains using embedded **Cross-Domain Dependency Rules**, delegates investigations to Tier-2 Domain Leads, arbitrates resource conflicts, and invokes the Analytics Lead to package the final operational response.

### Tier 2: 12 Departmental Domain Leads (`*_lead`)

Each Tier-2 Lead represents a municipal department head responsible for aggregating telemetry, flagging cross-departmental risks, and managing two specialized Tier-3 workers:

 1. **`traffic_mobility_lead`**: Arterial road flow, intersection signal timing, public transit, and detour routing.

 2. **`parking_management_lead`**: Garage/curb occupancy, dynamic pricing, EV bay overlap, and tow enforcement.

 3. **`energy_grid_lead`**: Substation feeder loads, solar/renewable output, EV load shedding, and outage restoration.

 4. **`environment_weather_lead`**: Rainfall/storm tracking, flood gauges, AQI (PM2.5/PM10), urban heat islands, and noise.

 5. **`emergency_services_lead`**: Police, Fire/HazMat, and EMS dispatch, hospital ER bed load, and green corridors.

 6. **`waste_management_lead`**: Smart bin fill levels, compactor route optimization, biomedical waste, and drain debris clearance.

 7. **`water_sewage_lead`**: Potable water pressure/quality, acoustic leak detection, trunk sewers, and stormwater pumps.

 8. **`infrastructure_vulnerability_lead`**: Bridge vibration/scour indices, subsurface sinkhole radar, and Single-Point-of-Failure (SPOF) risk scoring.

 9. **`citizen_311_lead`**: 311 complaint ingestion, spatial hotspot de-duplication, ticket routing, and geo-fenced SMS alerts.

10. **`public_safety_surveillance_lead`**: AI CCTV crowd density analytics, perimeter breach detection, and venue egress safety.

11. **`telecom_iot_connectivity_lead`**: 5G/LoRaWAN gateway uptime, sensor battery telemetry, and SCADA/OT cyber-spoofing defense.

12. **`analytics_dashboard_lead`**: Multi-domain health scoring (0–100), 6-hour trend forecasting, and UI JSON payload compilation.

### Tier 3: 24 Consolidated Specialist Workers (`*_agent`)

Each Domain Lead commands exactly **2 hyper-specialized worker agents** (24 total). Workers operate at the asset level—reading and updating shared state payloads via `sly_data` (or generating prototype-ready simulated telemetry tagged with `"simulated": true`). By enforcing a strict **Upward Reporting Contract**, every worker returns standardized telemetry containing `domain`, `zone`, `severity`, `key_metrics` (with exact engineering units), `recommended_action`, `confidence_pct`, `eta_min`, and `cross_domain_alerts`.

## 3. Standardized Digital Twin Geography & Shared State (`sly_data`)

To ensure all 37 agents reason over a coherent physical world without inventing arbitrary street names, the network embeds a **Standardized 6-Zone Municipal Digital Twin**:

* **Zone A (Downtown):** Central Station Junction, Metro Hub, City Hall, Parking Lot P1.

* **Zone B (Industrial Belt):** Substation S-4, Feeder F-12, HazMat Depot, Freight Corridor.

* **Zone C (Riverside):** Riverside Bridge, Underpass U-2, Pump Station 3, Stormwater Drain D-7.

* **Zone D (University District):** Campus Ave, Tech Park EV Hub, University Hospital.

* **Zone E (Old Town):** Heritage Market, Trunk Sewer Line T-9, Bin Cluster BC-14.

* **Zone F (Suburban North):** Solar Farm SF-1, Water Treatment Plant WTP-2, Landfill Site L-1.

All agents read and write state across standardized `sly_data` dictionary keys (`traffic`, `parking`, `energy`, `environment`, `emergency`, `waste`, `water_sewage`, `infrastructure`, `citizen_requests`, `public_safety`, `telecom_iot`, `analytics`, and `active_alerts`), enabling seamless prototype execution without requiring physical IoT hardware.

## 4. Key Innovations: Cascade Tracing & Deterministic Conflict Resolution

1. **Automated Cross-Domain Cascade Tracing:**

   Unlike static rule engines, the network traces multi-hop failure chains across domains. For example, during a cloudburst in **Zone C**, the system links *Solar Farm SF-1 cloud cover drop (Zone F)* $\rightarrow$ *Substation S-4 Feeder F-12 overload (Zone B)* $\rightarrow$ *Pump Station 3 power loss (Zone C)* $\rightarrow$ *Stormwater Drain D-7 surcharge (96%)* $\rightarrow$ *Underpass U-2 flooding (1.35 m)* $\rightarrow$ *Riverside Bridge detour bottleneck*.

2. **Deterministic Resource Conflict Resolution Hierarchy:**

   During crises, multiple departments inevitably compete for limited resources (e.g., `traffic_mobility_lead` wants Riverside Bridge for commuter detours while `emergency_services_lead` needs it cleared for ambulances; or `parking_management_lead` requests megawatts for Tech Park EV Hub while `water_sewage_lead` needs power for Pump Station 3). The Orchestrator enforces an immutable priority hierarchy:
   

   $$
   \text{1. Life Safety} > \text{2. Critical Infrastructure} > \text{3. Traffic \& Mobility} > \text{4. Citizen Convenience}
   $$

3. **Cyber-Physical Telemetry Verification:**

   Before acting on extreme sensor spikes (such as a sudden flood gauge jump during dry weather), environmental and water leads cross-check with `telecom_iot_connectivity_lead` (`iot_sensor_telemetry_agent` and `cyber_network_resilience_agent`) to verify gateway packet loss, battery voltage, and potential MQTT/SCADA spoofing attacks—preventing false-positive city shutdowns.

## 5. Dual-Format Output Contract & Command Center UI

Every execution cycle produces a strict dual-output response designed for both human decision-makers and automated frontend dashboards:

1. **Executive Markdown Briefing:** Features five standardized operational sections: *Situation Summary*, *Domain Findings*, *Cascading Cross-Domain Impacts*, *Prioritized Action Plan* (tabular format with owner agents, target assets, and ETAs in minutes), and a *6-Hour Risk Outlook*.

2. **Strict Schema-Compliant JSON Payload:** A single valid JSON block containing the composite `city_health_score` (0–100), `overall_severity`, individual health scores and alerts for all 11 operational domains, `cross_domain_chains`, prioritized `action_plan`, geospatial `map_markers`, and `forecast_next_6h`—powering the companion web dashboard on port `8002` alongside the real-time Neuro SAN graph visualizer (`nsflow`).