"""Instantiate a Dash app."""
import os

import dash
from dash import dcc
from dash import html
from dash import dash_table
from flask import render_template_string

from .data import create_dataframe


def render_base_html(server):

    with server.app_context(), server.test_request_context():
        layout_dash = os.path.join(
            os.getcwd(), "app/plotly_dash/dash_layout.html"
        )
        with open(layout_dash, "r") as f:
            html_body = render_template_string(f.read())

    return html_body


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""

    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dash/",
        external_stylesheets=[
            "/dashapp/dash_assets/header.css",
            "/dashapp/dash_assets/typography.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Load DataFrame
    df = create_dataframe()

    # Custom HTML layout
    dash_app.index_string = render_base_html(server)

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id="histogram-graph",
                figure={
                    "data": [
                        {
                            "x": df["complaint_type"],
                            "text": df["complaint_type"],
                            "customdata": df["key"],
                            "name": "311 Calls by region.",
                            "type": "histogram",
                        }
                    ],
                    "layout": {
                        "title": "NYC 311 Calls category.",
                        "height": 500,
                        "padding": 150,
                    },
                },
            ),
            create_data_table(df),
        ],
        id="dash-container",
    )
    return dash_app.server


def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table
