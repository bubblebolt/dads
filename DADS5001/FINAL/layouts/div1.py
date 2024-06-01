# layouts/div1.py

from dash import dcc, html
from app import iso_2_to_iso_3, create_bar_chart, map_fig

layout = html.Div(className='card treemap-container', children=[
    html.H3("Number of Starbucks Stores in Southeast Asia"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': 'All Countries', 'value': 'All'}] + [{'label': country, 'value': iso_3} for country, iso_3 in iso_2_to_iso_3.items()],
        value=['All'],
        multi=True,
        placeholder="Select countries",
        style={'width': '80%', 'margin': 'auto'}
    ),
    dcc.Graph(id='bar-chart'),
    html.P("This bar chart shows the cumulative number of Starbucks stores in each Southeast Asian country over time. Use the dropdown to filter by specific countries."),
    dcc.Graph(id='map-chart', figure=map_fig),
    html.P("This map visualizes the distribution of Starbucks stores across Southeast Asia, with colors representing the cumulative count of stores in each country.")
])
