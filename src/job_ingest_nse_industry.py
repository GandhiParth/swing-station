import argparse

from brokers.kite import KiteLogin, fetch_instruments
from config.brokers import KiteConfig
from utils import setup_logger
from website.nse import fetch_nse_industry_classification

setup_logger()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run NSE Industry Classification")
    parser.add_argument("--fetch_date", required=True, help="Fetch date YYYY-MM-DD")
    args = parser.parse_args()

    kite = KiteLogin(credentials_path=KiteConfig.CREDENTIALS_PATH)()
    nse_kite_df = fetch_instruments(kite=kite, exchange="NSE").select(
        "instrument_token", "symbol", "name", "segment"
    )

    fetch_nse_industry_classification(ins_df=nse_kite_df, fetch_date=args.fetch_date)
