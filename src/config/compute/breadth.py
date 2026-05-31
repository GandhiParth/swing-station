class MarketBreadthConfig:
    # -----------------------------------------------------------------------------
    # CONFIGURATION
    # -----------------------------------------------------------------------------

    SMA_DAYS = [20, 50]
    HL_DAYS = [20, 252]  # 252 = 52-week
    MICRO_WINDOW = 20  # Rolling rank window (1-month context for swing trading)
    EWM_SPANS = {"fast": 5, "medium": 10, "slow": 20}
    MCO_SPANS = (19, 39)  # McClellan Oscillator EMA spans
    HL_INDEX_SPAN = 10  # EMA span for High-Low Index

    # Universe filters
    MIN_PRICE = 10.0  # Minimum close price
    MIN_AVG_VOL = 50_000  # Minimum 20-day average volume
