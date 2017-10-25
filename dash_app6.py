import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash'),

    html.Div(children='''
        Data o Titaniku
    '''),

    dcc.Graph(
        id='results-graph',

    ),
    dcc.Dropdown(
        options=[
            {'label': 'Cena listků podle třídy', 'value': 'fare_class'},
            {'label': 'Věk cestujících podle třídy', 'value': 'age_class'},
        ],
        value='fare_class',
        id='plot-dropdown'
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Histogram', 'value': 'hist'},
            {'label': 'Boxplot', 'value': 'boxplot'}
        ],
        value='hist',
        id='plot-type'
    )
])

@app.callback(
    Output(component_id='results-graph', component_property='figure'),
    [Input(component_id='plot-dropdown', component_property='value'), Input(component_id='plot-type', component_property='value')]
)
def update_figure(data, plot_type):
    if data == 'fare_class':
        first = titanic[titanic.pclass == 1].fare
        second = titanic[titanic.pclass == 2].fare
        third = titanic[titanic.pclass == 3].fare

    else:
        first = titanic[titanic.pclass == 1].age
        second = titanic[titanic.pclass == 2].age
        third = titanic[titanic.pclass == 3].age
    plot_function = go.Histogram if plot_type == 'hist' else go.Box
    trace1 = plot_function(x = first, opacity = 0.75, name = 'První třída')
    trace2 = plot_function(x = second, opacity = 0.75, name = 'Druhá třída')
    trace3 = plot_function(x = third, opacity = 0.75, name = 'Třetí třída')

    data = [trace1, trace2, trace3]

    figure={
        'data': data,
        'layout': {}
    }
    return figure

titanic = pd.read_excel('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.xls')

if __name__ == '__main__':
    app.run_server()
