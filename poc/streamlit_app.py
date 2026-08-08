"""UC-XXXX-XXXX · Use-Case PoC — Streamlit PoC.

Run: streamlit run streamlit_app.py   (from the poc/ directory)
Reads its own data/sample.csv, so it runs offline. Not production data.
Layout follows streamlit/app-starter-kit.
"""
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="UC-XXXX-XXXX · Use-Case PoC", page_icon="📊", layout="wide")


@st.cache_data
def load_data() -> pd.DataFrame:
    """Cache the extract so reruns are instant. Swap for a real query to validate."""
    return pd.read_csv("data/sample.csv", parse_dates=["period"])


df = load_data()

st.title("Use-Case PoC")
st.caption("PoC for UC-XXXX-XXXX · PLANT · process — proof-of-concept, not production data.")

with st.sidebar:
    st.header("Filters")
    lines = st.multiselect("Line", sorted(df["category"].unique()), default=list(df["category"].unique()))
    window = st.slider("Months", 1, int(df["period"].nunique()), int(df["period"].nunique()))

kept = df[df["category"].isin(lines)]
periods = sorted(kept["period"].unique())[-window:]
kept = kept[kept["period"].isin(periods)]
trend = kept.groupby("period")["value"].sum().sort_index()

c1, c2, c3 = st.columns(3)
c1.metric("Current", f"{trend.iloc[-1]:.0f}" if len(trend) else "—")
c2.metric("vs. start", f"{trend.iloc[-1] - trend.iloc[0]:+.0f}" if len(trend) > 1 else "—")
c3.metric("Coverage", "78% of cases")

left, right = st.columns(2)
with left:
    st.subheader("Trend")
    st.plotly_chart(px.line(trend.reset_index(), x="period", y="value"), use_container_width=True)
with right:
    st.subheader("By line")
    by_cat = kept.groupby("category", as_index=False)["value"].sum()
    st.plotly_chart(px.bar(by_cat, x="category", y="value"), use_container_width=True)

with st.expander("What this PoC proves"):
    st.write(
        "The headline metric is computable from existing data, and a supervisor can "
        "read the current state in seconds. Success and kill criteria live in poc/spec.md."
    )
