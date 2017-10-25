import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.H1(id='big-title'),
    dcc.Input(id='input-text', value='Máme skvělý den', type="text"),
    html.Div(id='display-text')
])

@app.callback(
    Output(component_id='big-title', component_property='children'),
    [Input(component_id='input-text', component_property='value')]
)

def update_output_h1(input_value):
    return 'Zprava dne: "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server()
