#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 18:17:11 2017

@author: nasta
"""

import dash
import dash.dependencies
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.graph_objs as go


app = dash.Dash()


OPTIONS = {
        'birth': 'Počet narození a potratů', 
        'mom_age': 'Průměrný věk prvorodičky',
        'bride_groom_age': 'Průměrný věk ženicha a nevěsty',
        'marriage': 'Počet svateb a rozvodů',
}


app.layout = html.Div(children = [
    dcc.Markdown('''
## Česká republika v číslech 1989 - 2016
                  
Podle dat [Českého statistického úřadu](https://www.czso.cz/csu/czso/ceska-republika-od-roku-1989-v-cislech-w0i9dxmghn)
    '''),
    dcc.Graph(
        id = 'example-graph',
        figure = {
            'data': [],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    html.Label('Dropdown'),
    dcc.Dropdown(
        id = 'chooser',
        options = [{'label': label, 'value': key} for key, label in OPTIONS.items()],
        value = 'birth'
    )
])
    
@app.callback(
    dash.dependencies.Output(component_id='example-graph', component_property='figure'),
    [dash.dependencies.Input(component_id='chooser', component_property='value')],
)
def update_graph(choice):
    figure = {
            'data': [],
            'layout': go.Layout(title = OPTIONS[choice])
    }
    
    if choice == 'birth':
        data_baby = pd.read_csv('data_baby.csv')
        figure['data'] = [
                {'x': data_baby.columns[1:], 'y': data_baby.iloc[0], 'type': 'line', 'name': 'Narození'},
                {'x': data_baby.columns[1:], 'y': data_baby.iloc[2], 'type': 'line', 'name': 'Umělé potraty'},
        ]
        
    elif choice == 'mom_age':
        data_baby = pd.read_csv('data_baby.csv')
        figure['data'] = [
                {'x': data_baby.columns[1:], 'y': data_baby.iloc[1], 'type': 'bar', 'name': 'Věk prvorodičky'}
                ]
        figure['layout'].yaxis = dict(range=[20, 35])
        
    elif choice == 'bride_groom_age':
        data_marriage = pd.read_csv('data_marriage.csv')
        figure['data'] = [
                {'x': data_marriage.columns[1:], 'y': data_marriage.iloc[1], 'type': 'bar', 'name': 'Věk ženichů'},
                {'x': data_marriage.columns[1:], 'y': data_marriage.iloc[2], 'type': 'bar', 'name': 'Věk nevěst'},
                ]
        figure['layout'].yaxis = dict(range=[20, 35])
        
    elif choice == 'marriage':
        data_marriage = pd.read_csv('data_marriage.csv')
        figure['data'] = [
                {'x': data_marriage.columns[1:], 'y': data_marriage.iloc[0], 'type': 'bar', 'name': 'Svatby'},
                {'x': data_marriage.columns[1:], 'y': data_marriage.iloc[3], 'type': 'bar', 'name': 'Rozvody'},
                ]
        
        
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)