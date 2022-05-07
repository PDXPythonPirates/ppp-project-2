"""Gets crypto data from coingecko API.

References:
1. https://www.coingecko.com/api/docs/v3
2. https://algotrading101.com/learn/coingecko-api-guide/
"""

import os

import pandas as pd
from pycoingecko import CoinGeckoAPI


CG = CoinGeckoAPI()

COINS = [
    "bitcoin",
    "ethereum",
    "litecoin",
]

DAYS = 7  # Gets 7 days worth of historical data. 1 hr granularity.


def save_df_locally(df, file_name):
    """Save the data locally for now."""
    file_dir = os.path.dirname(os.path.abspath(__file__))
    csv_folder = "data"
    data_file = os.path.join(file_dir, csv_folder, f"{file_name}.csv")
    # remove the file everytime we run this
    if os.path.exists(data_file):
        os.remove(data_file)

    df.to_csv(data_file, index=False)

    return


def get_coins_info():
    """Gets the info for supported coins on CoinGecko.

    Output: List of dictionaries with coin id, coin symbol, and coin name.
        ex: [{'id': 'zytara-dollar', 'symbol': 'zusd', 'name': 'Zytara Dollar'},
                {'id': 'zyx', 'symbol': 'zyx', 'name': 'ZYX'}]
    """
    coin_info_df = pd.DataFrame(CG.get_coins_list())

    return coin_info_df


def get_dev_coin_data_for_ui():
    """Stores data locally that will be used to start rendering the
    user page.

    UI info: Show a list of coin names and for each coin name show a plot with
    data.
    """
    # let's get data for trending coins
    trending_coins = CG.get_search_trending()
    data = [
        (coin.get("item").get("id"), coin.get("item").get("name"))
        for coin in trending_coins.get("coins")
    ]
    df = pd.DataFrame(data, columns=["coin_id", "coin_name"])
    # TODO: get coin data

    return df


def get_price_data():
    """Gets coin price data."""

    data = {}
    for coin in COINS:
        try:
            timestamp_price_lists = CG.get_coin_market_chart_by_id(
                id=coin, vs_currency="usd", days=DAYS
            ).get("prices")
            data[coin] = {}
            data[coin]["timestamps"], data[coin]["values"] = zip(
                *timestamp_price_lists
            )

        except Exception as e:
            print(e)
            print("coin: " + coin)

    frame_list = [
        pd.DataFrame(
            data[coin]["values"], index=data[coin]["timestamps"], columns=[coin]
        )
        for coin in COINS
        if coin in data
    ]

    df = pd.concat(frame_list, axis=1).sort_index()
    df["datetime"] = pd.to_datetime(df.index, unit="ms")
    df["date"] = df["datetime"].dt.date
    df["hour"] = df["datetime"].dt.hour
    df = df.melt(
        id_vars=["datetime", "date", "hour"],
        var_name="currency_name",
        ignore_index=True,
    )
    df = df[df["value"].notna()]

    return df


if __name__ == "__main__":
    data = get_price_data()
    save_df_locally(data, filename="coingecko_price_data")
    coin_info = get_coins_info()
    save_df_locally(coin_info, file_name="coingecko_coin_info")
    get_dev_coin_data_for_ui()
