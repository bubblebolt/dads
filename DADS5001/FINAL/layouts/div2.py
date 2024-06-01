# layouts/div2.py

from dash import dcc, html
from app import animated_map

layout = html.Div(className='card treemap-container', children=[
    html.H3("Growth of Starbucks Stores Over Time by Timezone"),
    dcc.Graph(id='animated-map-graph', figure=animated_map),
    html.P("This animated map shows the growth of Starbucks stores over time, categorized by timezone. Each frame represents the opening of new stores in a given year.")
])
