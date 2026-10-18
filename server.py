"""
FastAPI Server for smart_city_dashboard
Smart City Operations & Command Center (Sly_Data Shared-State & Contract Network)
Runs on Port 8002
"""

import os
import sys
import json
import asyncio
from pathlib import Path
from typing import Dict, Any, Optional

import httpx
from fastapi import FastAPI, Request, Query, Body, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Add parent directory to sys.path
BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from agent_data import (
    CITY_GEOGRAPHY,
    AGENT_HIERARCHY,
    SCENARIOS,
    CONFLICT_RESOLUTION_HIERARCHY,
    execute_neuro_san_query
)

app = FastAPI(
    title="Smart City Operations Command Center - smart_city_dashboard",
    description="Tier-3 Multi-Agent Network UI for Shared-State (sly_data) & Reporting Contract Architecture",
    version="1.0.0"
)

# Mount static files and Jinja2 templates
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Global State Tracker
STATE = {
    "current_scenario": "scenario_storm_flood",
    "last_execution": SCENARIOS["scenario_storm_flood"]["payload"],
    "last_query": SCENARIOS["scenario_storm_flood"]["query"],
    "last_summary": SCENARIOS["scenario_storm_flood"]["summary"],
    "last_conflict": SCENARIOS["scenario_storm_flood"]["conflict_resolved"],
    "sly_data": SCENARIOS["scenario_storm_flood"]["sly_data_state"],
    "query_history": []
}

@app.get("/", response_class=HTMLResponse)
async def serve_dashboard(request: Request):
    """Serve the main Command Center UI."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "project_name": "smart_city_dashboard",
            "project_title": "Smart City Command Center (Shared State & Contract Architecture)",
            "architecture_badge": "Sly_Data Shared State & Standardized Reporting Contract",
            "total_agents": 37,
            "total_domains": 12,
            "total_zones": 6,
            "geography": CITY_GEOGRAPHY,
            "scenarios": SCENARIOS,
            "agents": AGENT_HIERARCHY,
            "conflict_hierarchy": CONFLICT_RESOLUTION_HIERARCHY,
            "active_scenario_id": STATE["current_scenario"]
        }
    )

@app.get("/api/status")
async def get_system_status():
    """Verify connectivity to the Neuro-SAN server and return system health."""
    neuro_san_online = False
    served_agents = []

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            resp = await client.get("http://localhost:8080/api/v1/list")
            if resp.status_code == 200:
                neuro_san_online = True
                data = resp.json()
                served_agents = [a.get("agent_name") for a in data.get("agents", [])]
    except Exception:
        neuro_san_online = False

    return {
        "status": "online",
        "project": "smart_city_dashboard",
        "neuro_san_server_connected": neuro_san_online,
        "neuro_san_url": "http://localhost:8080",
        "agent_network_loaded": "smart_city_dashboard" in served_agents if neuro_san_online else False,
        "total_hierarchy_agents": 37,
        "current_scenario": STATE["current_scenario"],
        "city_health_score": STATE["last_execution"].get("city_health_score", 62.4),
        "overall_severity": STATE["last_execution"].get("overall_severity", "CRITICAL"),
        "sly_data_keys_count": len(STATE["sly_data"].keys())
    }

@app.get("/api/geography")
async def get_geography():
    return CITY_GEOGRAPHY

@app.get("/api/agents")
async def get_agents():
    return AGENT_HIERARCHY

@app.get("/api/scenarios")
async def get_scenarios():
    return SCENARIOS

@app.get("/api/sly_data")
async def get_sly_data():
    """Return the current shared sly_data state store."""
    return {
        "sly_data": STATE["sly_data"],
        "keys": list(STATE["sly_data"].keys()),
        "active_alerts": STATE["sly_data"].get("active_alerts", [])
    }

@app.post("/api/sly_data/update")
async def update_sly_data(payload: Dict[str, Any] = Body(...)):
    """Inject / modify a state key in sly_data."""
    key = payload.get("key")
    val = payload.get("value")
    if key:
        STATE["sly_data"][key] = val
    return {"success": True, "updated_key": key, "sly_data": STATE["sly_data"]}

@app.get("/api/conflict_resolution")
async def get_conflict_resolution():
    """Return the conflict resolution rules and latest arbitration."""
    return {
        "hierarchy": CONFLICT_RESOLUTION_HIERARCHY,
        "latest_arbitration": STATE["last_conflict"]
    }

@app.get("/api/current_telemetry")
async def get_current_telemetry():
    return {
        "scenario_id": STATE["current_scenario"],
        "query": STATE["last_query"],
        "summary": STATE["last_summary"],
        "conflict": STATE["last_conflict"],
        "sly_data": STATE["sly_data"],
        "payload": STATE["last_execution"]
    }

@app.post("/api/dispatch")
async def dispatch_incident(payload: Dict[str, Any] = Body(...)):
    """Handle operator queries and incident dispatches."""
    query_text = payload.get("query", "").strip()
    mode = payload.get("mode", "fast_simulation")
    scenario_id = payload.get("scenario_id")

    if not query_text and scenario_id and scenario_id in SCENARIOS:
        query_text = SCENARIOS[scenario_id]["query"]

    if not query_text:
        raise HTTPException(status_code=400, detail="Query or valid scenario_id required.")

    # Live Neuro-SAN Execution
    if mode == "neuro_san":
        result = await execute_neuro_san_query("smart_city_dashboard", query_text)
        if result.get("success") and result.get("json_payload"):
            STATE["last_execution"] = result["json_payload"]
            STATE["last_query"] = query_text
            STATE["last_summary"] = result.get("compiled_briefing", "")[:300]
            if scenario_id:
                STATE["current_scenario"] = scenario_id
                STATE["sly_data"] = SCENARIOS[scenario_id]["sly_data_state"]
                STATE["last_conflict"] = SCENARIOS[scenario_id]["conflict_resolved"]
            
            STATE["query_history"].append({
                "query": query_text,
                "mode": "neuro_san_live",
                "severity": result["json_payload"].get("overall_severity", "INFO"),
                "health_score": result["json_payload"].get("city_health_score", 0)
            })

            return {
                "success": True,
                "source": "neuro_san_live",
                "briefing": result.get("compiled_briefing", ""),
                "sly_data": STATE["sly_data"],
                "conflict": STATE["last_conflict"],
                "payload": result["json_payload"]
            }
        else:
            fallback_scenario = SCENARIOS.get(scenario_id, SCENARIOS["scenario_storm_flood"])
            data_payload = fallback_scenario["payload"]
            STATE["last_execution"] = data_payload
            STATE["last_query"] = query_text
            STATE["last_summary"] = fallback_scenario["summary"]
            STATE["sly_data"] = fallback_scenario["sly_data_state"]
            STATE["last_conflict"] = fallback_scenario["conflict_resolved"]
            
            return {
                "success": True,
                "source": "simulation_fallback",
                "note": "Live Neuro-SAN call deferred or timed out. Falling back to High-Fidelity Simulation Engine.",
                "live_error": result.get("error", "Unknown"),
                "briefing": f"### Situation Summary\n{fallback_scenario['summary']}\n\n### Prioritized Action Plan\nEnforced 4-tier conflict hierarchy across 6 multi-domain interventions.",
                "sly_data": STATE["sly_data"],
                "conflict": STATE["last_conflict"],
                "payload": data_payload
            }

    # Fast Simulation Mode
    if scenario_id and scenario_id in SCENARIOS:
        sc = SCENARIOS[scenario_id]
        STATE["current_scenario"] = scenario_id
        STATE["last_execution"] = sc["payload"]
        STATE["last_query"] = sc["query"]
        STATE["last_summary"] = sc["summary"]
        STATE["last_conflict"] = sc["conflict_resolved"]
        STATE["sly_data"] = sc["sly_data_state"]

        STATE["query_history"].append({
            "query": sc["query"],
            "mode": "fast_simulation",
            "severity": sc["payload"].get("overall_severity", "INFO"),
            "health_score": sc["payload"].get("city_health_score", 0)
        })

        return {
            "success": True,
            "source": "fast_simulation",
            "scenario_id": scenario_id,
            "summary": sc["summary"],
            "conflict": sc["conflict_resolved"],
            "sly_data": sc["sly_data_state"],
            "payload": sc["payload"]
        }

    # Custom query
    custom_payload = SCENARIOS["scenario_storm_flood"]["payload"]
    return {
        "success": True,
        "source": "custom_simulation",
        "query": query_text,
        "conflict": STATE["last_conflict"],
        "sly_data": STATE["sly_data"],
        "payload": custom_payload
    }

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*70)
    print("  LAUNCHING SMART CITY COMMAND CENTER: smart_city_dashboard")
    print("  URL: http://localhost:8002")
    print("  Architecture: Sly_Data Shared State & Reporting Contract")
    print("  Multi-Agent Hierarchy: 37 Agents | 12 Domain Leads | 6 City Zones")
    print("="*70 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=8002)
