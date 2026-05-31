import streamlit as st

from mkt_db_app.modules.breadth import render as render_breadth
from mkt_db_app.modules.overview import render as render_overview
from mkt_db_app.modules.scanner import render as render_scanner
from mkt_db_app.services.data_loader import (
    available_dates,
    load_mkt_breadth_data,
    load_mkt_db_data,
    load_scanner_data,
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="SwingBot Market Dashboard", layout="wide")

st.title("SwingBot Market Dashboard")


# ------------------------------------------------
# DATE SELECTOR
# ------------------------------------------------

dates = available_dates()

selected_date = st.sidebar.selectbox("Select Date", dates)

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------

indices_df, stocks_df = load_mkt_db_data(selected_date)
mkt_breadth_df, mkt_regime_df = load_mkt_breadth_data(selected_date)
long_scanner_df, short_scanner_df = load_scanner_data(selected_date)

st.header(f"Market Data: {selected_date}")

# ------------------------------------------------
# PAGES
# ------------------------------------------------

tabs = st.tabs(["MARKET OVERVIEW", "MARKET BREADTH", "SCANNER"])

with tabs[0]:
    render_overview(stocks_df=stocks_df, indices_df=indices_df)

with tabs[1]:
    render_breadth(breadth_df=mkt_breadth_df, regime_df=mkt_regime_df)

with tabs[2]:
    render_scanner(long_scanner_df=long_scanner_df, short_scanner_df=short_scanner_df)
