"""Instantiate a Dash app."""
import dash
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
#from dash import dash_table


#from .data import create_dataframe
#from .layout import html_layout


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    app_dash = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashapp/",
        # external_stylesheets=[
        #     "/static/dist/css/styles.css",
        #     "https://fonts.googleapis.com/css?family=Lato",
        # ],
    )

    # Load DataFrame
    #df = create_dataframe()
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, 
        x="Fruit", y="Amount", color="City", barmode="group")
    # Custom HTML layout
    #app_dash.index_string = html_layout

    # Create Layout
    app_dash.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

    # app_dash.layout = html.Div(children=[
    #         dcc.Graph(
    #             id="histogram-graph",
    #             figure={
    #                 "data": [
    #                     {
    #                         "x": df["complaint_type"],
    #                         "text": df["complaint_type"],
    #                         "customdata": df["key"],
    #                         "name": "311 Calls by region.",
    #                         "type": "histogram",
    #                     }
    #                 ],
    #                 "layout": {
    #                     "title": "NYC 311 Calls category.",
    #                     "height": 500,
    #                     "padding": 150,
    #                 },
    #             },
    #         ),
    #         #create_data_table(df),
    #     ],
    #     id="dash-container",
    # )

    return app_dash.server


# def create_data_table(df):
#     """Create Dash datatable from Pandas DataFrame."""
#     table = dash_table.DataTable(
#         id="database-table",
#         columns=[{"name": i, "id": i} for i in df.columns],
#         data=df.to_dict("records"),
#         sort_action="native",
#         sort_mode="native",
#         page_size=300,
#     )
#     return table
