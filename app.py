import dash
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
        figure={
            'data': [
                go.Bar(x = [1, 2, 3], y = [4, 1, 2], name ='Cherbourg'),
                go.Bar(x = [1, 2, 3], y = [2, 4, 5], name = 'Queenstown'),
                go.Bar(x = [1, 2, 3], y = [3, 2, 3], name = 'Southampton')
            ],
            'layout': {
                'title': 'Nástupní místo dle třídy jizdenky'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server()
