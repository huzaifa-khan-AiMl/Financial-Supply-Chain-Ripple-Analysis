import yfinance as yf
import os
import pandas as pd

print("Making the path for our csv files")

current_path = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_path)

data_dir = os.path.join(root_dir, "data")
Output_dir = os.path.join(data_dir, "raw")

os.makedirs(data_dir, exist_ok=True)
os.makedirs(Output_dir, exist_ok=True)

print("Assets data")


def Asset():
    assets = [
        {
            "ticker": "AAPL",
            "company_name": "Apple Inc.",
            "sector": "Consumer Electronics",
            "role": "Focal Company"
        },
        {
            "ticker": "QCOM",
            "company_name": "QUALCOMM Incorporated",
            "sector": "Semiconductors",
            "role": "Upstream Supplier"
        },
        {
            "ticker": "GLW",
            "company_name": "Corning Incorporated",
            "sector": "Electronic Components",
            "role": "Upstream Supplier"
        },
        {
            "ticker": "XLK",
            "company_name": "State Street Technology Select Sector SPDR ETF",
            "sector": "Technology",
            "role": "Sector Benchmark"
        }
    ]

    assets_df = pd.DataFrame(assets)

    file_path = os.path.join(Output_dir, "assets.csv")
    assets_df.to_csv(file_path, index=False)

    return assets_df


def fetch_daily_prices(ticker_list):

    starting_date = "2017-01-01"
    ending_date = "2020-03-01"

    raw_df = yf.download(
        tickers=ticker_list,
        start=starting_date,
        end=ending_date,
        interval="1d",
        group_by="ticker",
        auto_adjust=False
    )

    records = []

    for current_ticker in ticker_list:
        ticker_df = raw_df[current_ticker].reset_index()
        ticker_df["Ticker"] = current_ticker
        records.append(ticker_df)

    combined_df = pd.concat(records, ignore_index=True)

    combined_df = combined_df.rename(columns={
        "Date": "trade_date",
        "Ticker": "ticker",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Adj Close": "adj_close",
        "Volume": "volume"
    })

    combined_df = combined_df[
        [
            "trade_date",
            "ticker",
            "open",
            "high",
            "low",
            "close",
            "adj_close",
            "volume"
        ]
    ]

    prices_path = os.path.join(Output_dir, "market_data.csv")
    combined_df.to_csv(prices_path, index=False)

    print(f"Saved: {prices_path} ({len(combined_df)} records)")


if __name__ == "__main__":

    assets_df = Asset()

    ticker_list = assets_df["ticker"].tolist()

    fetch_daily_prices(ticker_list)