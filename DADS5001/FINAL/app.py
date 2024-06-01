# app.py

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# ISO-2 to ISO-3 country code mapping for Southeast Asian countries
iso_2_to_iso_3 = {
    'BN': 'BRN', 'KH': 'KHM', 'TL': 'TLS', 'ID': 'IDN', 'LA': 'LAO',
    'MY': 'MYS', 'MM': 'MMR', 'PH': 'PHL', 'SG': 'SGP', 'TH': 'THA', 'VN': 'VNM'
}

# Load the Starbucks data
df = pd.read_csv('starbuck.csv')

# Filter data for Southeast Asia countries
df_sea = df[df['Country'].isin(iso_2_to_iso_3.keys())].copy()

# Map ISO-2 codes to ISO-3 codes
df_sea['Country_ISO3'] = df_sea['Country'].map(iso_2_to_iso_3)

# Generate mock opening dates for demonstration purposes
np.random.seed(42)
num_entries = len(df_sea)
df_sea['Opening_Date'] = pd.to_datetime(np.random.randint(2000, 2023, size=num_entries), format='%Y')

# Extract the year from the 'Opening_Date' column
df_sea['Opening_Year'] = df_sea['Opening_Date'].dt.year

# Ensure we have a cumulative count per year per country
df_sea['Store Count'] = 1
df_cumulative = df_sea.groupby(['Opening_Year', 'Country_ISO3']).size().reset_index(name='Store Count')
df_cumulative['Cumulative Count'] = df_cumulative.groupby('Country_ISO3')['Store Count'].cumsum()

# Create bar chart figure
def create_bar_chart(selected_countries):
    if not selected_countries or "All" in selected_countries:
        filtered_df = df_cumulative
    else:
        filtered_df = df_cumulative[df_cumulative['Country_ISO3'].isin(selected_countries)]
    return px.bar(filtered_df, x='Country_ISO3', y='Cumulative Count', animation_frame='Opening_Year', range_y=[0, df_cumulative['Cumulative Count'].max()], title="Number of Starbucks Stores in Southeast Asia")

# Create map figure focused on Southeast Asia
map_fig = px.choropleth(
    df_cumulative,
    locations="Country_ISO3",
    locationmode="ISO-3",
    color="Cumulative Count",
    hover_name="Country_ISO3",
    title="Starbucks Stores Distribution",
    color_continuous_scale=px.colors.sequential.Plasma,
    scope='asia'
)

# Create animated map figure
animated_map = px.scatter_geo(
    df_sea,
    lat='Latitude',
    lon='Longitude',
    color='Timezone',
    hover_name='City',
    animation_frame='Opening_Year',
    title='Growth of Starbucks Stores Over Time by Timezone',
    scope='asia'
)

# Create animated bubble chart on a map focused on Southeast Asia
df_bubble = df_sea.groupby(['Opening_Year', 'Country_ISO3', 'Latitude', 'Longitude']).size().reset_index(name='Store Count')

animated_bubble_map = px.scatter_geo(
    df_bubble,
    lat='Latitude',
    lon='Longitude',
    size='Store Count',
    color='Country_ISO3',
    hover_name='Country_ISO3',
    animation_frame='Opening_Year',
    title='Growth of Starbucks Stores Over Time by Location',
    labels={'Store Count': 'Number of Stores', 'Country_ISO3': 'Country'},
    scope='asia'
)

# Callback to update the bar chart based on selected countries
@app.callback(
    Output('bar-chart', 'figure'),
    Input('country-dropdown', 'value')
)
def update_bar_chart(selected_countries):
    return create_bar_chart(selected_countries)

# Export the app object for use in index.py
server = app.server
