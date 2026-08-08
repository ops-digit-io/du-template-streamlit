# UC-XXXX-XXXX · Streamlit PoC

PoC for UC-XXXX-XXXX · PLANT · process — proof-of-concept, not production data.

Layout follows the official [streamlit/app-starter-kit](https://github.com/streamlit/app-starter-kit).

```bash
cd poc
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Data is `data/sample.csv` (illustrative). Swap it for a real extract to validate.
Deploys to Streamlit Community Cloud as-is (entry: `streamlit_app.py`).
