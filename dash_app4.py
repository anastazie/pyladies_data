import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash'),

    html.Div(children='''
        Data o Titaniku
    '''),

    dcc.Graph(
        id='example-graph',

    ),
    dcc.Dropdown(
        options=[
            {'label': 'Cena listků podle třídy', 'value': 'fare_class'},
            {'label': 'Věk cestujících podle třídy', 'value': 'age_class'},
        ],
        value='fare_class'
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Histogram', 'value': 'hist'},
            {'label': 'Boxplot', 'value': 'boxplot'}
        ],
        value='hist',
        id='radio-input'
    )
])

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    [Input(component_id='radio-input', component_property='value')]
)

def update_figure(plot_type):
    plot_function = go.Histogram if plot_type == 'hist' else go.Box
    trace1 = plot_function(x = [1, 2, 3], name = 'Cherbourg')
    trace2 = plot_function(x = [5, 12, 3], name = 'Queenstown')
    trace3 = plot_function(x = [5, 12, 3], name = 'Southampton')

    data = [trace1, trace2, trace3]

    figure={
        'data': data,
        'layout': {
            'title': 'Nástupní místo dle třídy jizdenky',
            'xaxis':{
                'title': 'třída jízdenky'
            }
        },

    }
    return figure
if __name__ == '__main__':
    app.run_server()
