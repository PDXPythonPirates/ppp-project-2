"""Prepare data for Plotly Dash."""
import os

import numpy as np
import pandas as pd


def create_dataframe():
    """Create Pandas DataFrame from local CSV."""
    file_path = os.path.join(os.getcwd(), "app/plotly_dash/data/311-calls.csv")
    df = pd.read_csv(file_path, parse_dates=["created"])
    df["created"] = df["created"].dt.date
    df.drop(columns=["incident_zip"], inplace=True)
    num_complaints = df["complaint_type"].value_counts()
    to_remove = num_complaints[num_complaints <= 30].index
    df.replace(to_remove, np.nan, inplace=True)
    return df
