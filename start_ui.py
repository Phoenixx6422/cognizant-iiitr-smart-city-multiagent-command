"""
Standalone Launcher for smart_city_dashboard UI
"""
import sys
import webbrowser
import threading
import time
import uvicorn
from pathlib import Path

# Add project root to sys.path
PROJECT_DIR = Path(__file__).resolve().parent
ROOT_DIR = PROJECT_DIR.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

def open_browser():
    time.sleep(1.5)
    webbrowser.open("http://localhost:8002")

if __name__ == "__main__":
    print("\n" + "="*70)
    print("  STARTING UI FOR SMART_CITY_DASHBOARD")
    print("  URL: http://localhost:8002")
    print("="*70 + "\n")
    threading.Thread(target=open_browser, daemon=True).start()
    uvicorn.run("server:app", host="0.0.0.0", port=8002, reload=False)
