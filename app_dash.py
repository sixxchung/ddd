import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
 
import flask 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#import dash_bootstrap_components as dbc

#from utils.external_assets import ROOT, EXTERNAL_STYLESHEETS, FONT_AWSOME
#from ui.main_content import layout

import datetime
import os

server = flask.Flask(__name__)
appDash = dash.Dash(
        name=__name__, 
        server=server, 
        requests_pathname_prefix="/dash/",
        #assets_folder=ROOT+"/assets",

        # suppress_callback_exceptions=True, 
        # external_stylesheets=[
        #     dbc.themes.CYBORG, 
        #     FONT_AWSOME,
        #     #EXTERNAL_STYLESHEETS
        # ], 
        # meta_tags=[
        #     {"name": "viewport", "content": "width=device-width, initial-scale=1"}
        # ]     
    )
    #dashApp.scripts.config.serve_locally = False
    #dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'


df = pd.read_csv(
'https://gist.githubusercontent.com/chriddyp/' +
'5d1ea79569ed194d432e56108a04d188/raw/' +
'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
'gdp-life-exp-2007.csv')

appDash.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

# run following in command
# gunicorn graph:appDash.server -b :8000

# if __name__ == '__main__':
#     appDash.run_server(debug=True)