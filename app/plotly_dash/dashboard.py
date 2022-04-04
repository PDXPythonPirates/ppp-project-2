"""Instantiate a Dash app."""
import os

import dash
from dash import dcc
from dash import html
from dash import dash_table
from flask import render_template_string
import plotly.express as px

from .coingecko_data import get_price_data


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
    df = get_price_data()

    # Custom HTML layout
    dash_app.index_string = render_base_html(server)

    # Basic Fig
    fig = px.line(df, x="datetime", y="value", color="currency_name")
    fig.update_layout(
        title={
            "text": "Coingecko Price Data",
            "y": 0.95,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        },
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        legend_title="Currency Name",
    )

    # Create Dash Layout
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(id="graph", figure=fig),
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
        style_cell={"textAlign": "center"},
        page_size=300,
    )
    return table
