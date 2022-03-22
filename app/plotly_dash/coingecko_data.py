"""Gets crypto data from coingecko API
(https://www.coingecko.com/api/docs/v3)."""

import os

import pandas as pd
from pycoingecko import CoinGeckoAPI


CG = CoinGeckoAPI()


def get_data():
    """Gets coin data.

    Return:{
            'bitcoin': {'usd': 42848, 'usd_market_cap': 814398164374.8334},
            'ethereum': {'usd': 3015.62, 'usd_market_cap': 362696885499.07214},
            'litecoin': {'usd': 120.44, 'usd_market_cap': 8426034198.539223},
            }
    """
    stock_data = CG.get_price(
        ids="bitcoin, litecoin, ethereum",
        vs_currencies="usd",
        include_market_cap=True,
        include_24hr_vol=True,
        include_24hr_change=True,
        include_last_updated_at=True,
    )

    return stock_data


def save_data(data):
    """Save the data locally for now."""
    file_dir = os.path.dirname(os.path.abspath(__file__))
    csv_folder = "data"
    data_file = os.path.join(file_dir, csv_folder, "coingecko_data.csv")

    if os.path.exists(data_file):
        os.remove(data_file)

    df = pd.DataFrame.from_dict(data, orient="index")
    df.insert(loc=0, column="coin", value=data.keys())
    df.to_csv(data_file, index=False)

    return


if __name__ == "__main__":
    data = get_data()
    save_data(data)
