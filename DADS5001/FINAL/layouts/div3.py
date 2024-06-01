# layouts/div3.py

from dash import dcc, html
from app import animated_bubble_map

layout = html.Div(className='card treemap-container', children=[
    html.H3("Growth of Starbucks Stores Over Time by Location"),
    dcc.Graph(id='animated-bubble-map-graph', figure=animated_bubble_map),
    html.P("This animated bubble chart on a map shows the growth of Starbucks stores over time, with the size of the bubbles representing the number of stores. Each frame represents the opening of new stores in a given year.")
])
