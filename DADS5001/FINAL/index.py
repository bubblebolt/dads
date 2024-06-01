import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from app import app, server
from layouts import div1, div2, div3

# Assuming you have a function to create the bar chart in app.py
from app import create_bar_chart, map_fig, iso_2_to_iso_3

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H2("Sidebar", className="display-4"),
                html.Hr(),
                html.P("A simple sidebar layout with navigation links", className="lead"),
                dbc.Nav([
                    dbc.NavLink("Div1", href="/div1", active="exact"),
                    dbc.NavLink("Div2", href="/div2", active="exact"),
                    dbc.NavLink("Div3", href="/div3", active="exact")
                ], vertical=True, pills=True)
            ], className="sidebar")
        ], width=3),
        dbc.Col(html.Div(id='page-content'), width=9)
    ])
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/div1':
        return div1.layout
    if pathname == '/div2':
        return div2.layout
    if pathname == '/div3':
        return div3.layout
    if pathname == '/':
        return "Welcome to Starbucks Dashboard. Please choose a Chart."

@app.callback(
    Output('bar-chart', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_bar_chart(selected_countries):
    if not selected_countries or 'All' in selected_countries:
        selected_countries = list(iso_2_to_iso_3.values())
    return create_bar_chart(selected_countries)

if __name__ == '__main__':
    app.run_server(debug=True)
