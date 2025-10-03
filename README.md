# Silent City Dashboard

Prototype repository for a probing confidence score to estimate coordinated probes across civic services.

---

## Context
Not every cyberattack looks like a blackout.  
The more dangerous scenario is a silent choke: multiple small glitches across payments, transport, and civic systems.  
Confidence collapses before systems fully fail.

---

## Quickstart

```bash
git clone https://github.com/ainahar/silent-city-dashboard.git
cd silent-city-dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python probe_score.py data/mock_incidents.csv

## License
MIT — prototype only.

---
Note: This repository contains prototype/demo code for research and policy discussion. It is not intended for production use.
