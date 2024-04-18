#Reference: https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Dash%20Components/Graph/dash-graph.py
import dash
import random
from dash import dcc, html
import plotly.express as px

df = px.data.gapminder()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def random_rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def rgb_to_str(rgb_tuple):
    return 'rgb' + str(rgb_tuple)

countrycl = {country: rgb_to_str(random_rgb_color()) for country in df['country'].unique()}


app.layout = html.Div([
    dcc.Dropdown(
        id='dpdn2',
        value=['Germany', 'Brazil'],
        multi=True,
        options=[{'label': x, 'value': x} for x in df.country.unique()], 
        style={'margin-bottom': '0px'},
    ),
    html.Div([
        html.Div([
            dcc.Graph(
                id='my-graph',
                figure={},
                clickData=None,
                hoverData=None,
                selectedData=None,
                config={
                    'staticPlot': False,
                    'scrollZoom': True,
                    'doubleClick': 'reset',
                    'showTips': False,
                    'displayModeBar': True,
                    'watermark': True,
                },
            ),
        ], style={'grid-row': '1', 'grid-column': '1 / span 2','height':'50vh', 'margin-bottom': '10px'}),  
         html.Div([
            # Pie Chart อยู่ข้างล่างซ้าย
            dcc.Graph(id='pie-graph', figure={}),
        ], style={'grid-row': '2', 'grid-column': '1', 'margin-right': '10px', 'margin-bottom': '10px'}),  # Pie Chart อยู่ข้างล่างซ้าย

        html.Div([
            # Bar Chart อยู่ข้างล่างขวา
            dcc.Graph(id='bar-graph', figure={}),
        ], style={'grid-row': '2', 'grid-column': '2', 'margin-left': '10px', 'margin-bottom': '10px'}),  # Bar Chart อยู่ข้างล่างขวา
    ], style={'display': 'grid', 'grid-template-rows': 'auto 1fr', 'grid-template-columns': '1fr 1fr', 'gap': '10px'})
])

@app.callback(
    dash.dependencies.Output('my-graph', 'figure'),
    dash.dependencies.Input('dpdn2', 'value'),
)
def update_graph(country_chosen):
    dff = df[df.country.isin(country_chosen)]
    fig = px.line(
        data_frame=dff,
        x='year',
        y='gdpPercap',
        color='country',
        color_discrete_map= countrycl,
        hover_data=["lifeExp", "pop", "iso_alpha"]
    )
    fig.update_traces(mode='lines+markers')
    return fig

@app.callback(
    dash.dependencies.Output('pie-graph', 'figure'),
    dash.dependencies.Input('my-graph', 'hoverData'),
    dash.dependencies.Input('dpdn2', 'value')
)
def update_pie_chart(hov_data, country_chosen):
    if hov_data is None:
        dff2 = df[df.country.isin(country_chosen)]
        dff2 = dff2[dff2.year == 1952]
        fig2 = px.pie(
            data_frame=dff2,
            values='pop',
            names='country',
            color='country',
            color_discrete_map=countrycl,
            title='Population for 1952'
        )
        return fig2
    else:
        hov_year = hov_data['points'][0]['x']
        dff2 = df[df.country.isin(country_chosen) & (df['year'] == hov_year)]
        fig2 = px.pie(
            data_frame=dff2,
            values='pop',
            names='country',
            color='country',
            color_discrete_map=countrycl,
            title=f'Population for: {hov_year}'
        )
        return fig2

@app.callback(
    dash.dependencies.Output('bar-graph', 'figure'),
    dash.dependencies.Input('my-graph', 'selectedData'),
    dash.dependencies.Input('dpdn2', 'value')
)
def update_bar_chart(selected_data, country_chosen):
    if selected_data:
        selected_years = [point['x'] for point in selected_data['points']]
        dff3 = df[df.country.isin(country_chosen) & df.year.isin(selected_years)]
        fig3 = px.bar(
            data_frame=dff3,
            x='year',
            y='gdpPercap',
            color='country',
            barmode='group',
            color_discrete_map=countrycl,
            title='GDP Per Capita'
        )
        return fig3
    else:
        dff3 = df[df.country.isin(country_chosen)]
        fig3 = px.bar(
            data_frame=dff3,
            x='year',
            y='gdpPercap',
            color='country',
            barmode='group',
            color_discrete_map=countrycl,
            title='GDP Per Capita for selected countries'
        )
        return fig3

if __name__ == '__main__':
    app.run_server(debug=True)




'''
GDP Per Capita คือ ผลิตภัณฑ์มวลรวมในประเทศต่อหัว หรือ GDP ต่อหัว 
เป็นตัวเลขที่บอกว่าค่าเฉลี่ยของ GDP เมื่อเทียบกับคนในประเทศแล้ว โดยเฉลี่ยคนหนึ่งคนสามารถสร้างมูลค่า GDP ขึ้นมาเท่าไหร่ 
และแน่นอนว่า GDP per capita คือ ตัวเลขที่คำนวณมาจาก ค่า GDP ÷ จำนวนประชากร

iso_alpha
The 3-letter ISO 3166-1 alpha-3 code.

iso_num
The 3-digit ISO 3166-1 numeric-3 code.

อายุคาดเฉลี่ย (Life Expectancy) : LE หรือ Life Expectancy หมายถึง
การคาดประมาณจำนวนปีโดยเฉลี่ยของการมีชีวิตอยู่ของประชากร
'''

