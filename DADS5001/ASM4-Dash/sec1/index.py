import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
from app import app
from apps import scatter_layout, histogram_layout, bar_layout, treemap_layout

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#31363F",
    "color": "#EEEEEE" 
}

# Main content style
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    
}

# Sidebar layout with navigation links
sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-6"),
        html.Hr(),
        html.P("A simple sidebar layout with navigation links", className="lead", style={"font-size": "16px"}),
        dbc.Nav(
            [
                dbc.NavLink([
                    html.I(className="fas fa-home mr-2"),  
                    "Home"
                ], href="/", style={'color': '#76ABAE'}, active="exact"),
                html.Br(),
                dbc.NavLink([
                    html.I(className="fas fa-spinner mr-1"),  
                    "Scatter"
                ], href="/apps/scatter_layout", style={'color': '#76ABAE'}, active="exact"),
                html.Br(),
                dbc.NavLink([
                    html.I(className="fas fa-chart-bar mr-2"),  
                    "Histogram"
                ], href="/apps/histogram_layout", style={'color': '#76ABAE'}, active="exact"),
                html.Br(),
                dbc.NavLink([
                    html.I(className="fas fa-tree mr-2"),  
                    "Treemap"
                ], href="/apps/treemap_layout", style={'color': '#76ABAE'}, active="exact"),
                html.Br(),
                dbc.NavLink([
                    html.I(className="fas fa-boxes mr-2"),  
                    "BarChart"
                ], href="/apps/bar_layout", style={'color': '#76ABAE'}, active="exact"),
            ],
            vertical=True,
            pills=True,
            id="sidebar-menu", 
        ),
    ],
    style=SIDEBAR_STYLE,
)

# Main content layout
content = html.Div(
    id='page-content',
    style=CONTENT_STYLE,
)

# App layout combining sidebar and content
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP,"https://use.fontawesome.com/releases/v5.15.4/css/all.css", "assets/styles.css"])
app.layout = html.Div([dcc.Location(id='url'), sidebar, content])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/scatter_layout':
        return scatter_layout.layout
    if pathname == '/apps/histogram_layout':
        return histogram_layout.layout
    if pathname == '/apps/treemap_layout':
        return treemap_layout.layout
    if pathname == '/apps/bar_layout':
        return bar_layout.layout
    if pathname == '/':
        return "Welcome to Chalita's Dashboard. Please choose a Chart."

if __name__ == '__main__':
    app.run_server(debug=False)


