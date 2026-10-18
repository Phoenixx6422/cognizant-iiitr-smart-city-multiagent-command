# Smart City Command Center

A FastAPI dashboard for a multi-agent smart city operations network (shared-state `sly_data` and reporting contracts). It has a clean light-mode UI with a city map, incident scenarios, conflict resolution, domain health cards, a 6-hour forecast and an agent hierarchy view.

## Project structure

```
server.py            FastAPI app (port 8002)
start_ui.py          Launcher that also opens the browser
start_ui.bat         Windows launcher (runs server.py)
start_new_ui.bat     Windows launcher (checks UI files, runs start_ui.py)
templates/index.html Dashboard template
static/css/styles.css
static/js/app.js
```

## Requirements

- Python 3.9+
- `agent_data.py` in the parent folder of this project. `server.py` imports it for city geography, agent hierarchy, scenarios and the Neuro-SAN query helper. It is not included in this repo.

## Run

```bash
pip install -r requirements.txt
python server.py
```

Then open http://localhost:8002.

On Windows you can double-click `start_new_ui.bat`.

## Live mode

The "Live Neuro-SAN" button calls a Neuro-SAN server at http://localhost:8080. If it is not running, the dashboard falls back to the built-in simulation.
