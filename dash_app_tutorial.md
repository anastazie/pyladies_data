# Dash

## Úvod

Dash je nástroj pro vytvoření interaktivních aplikaci i reportů, který kombinuje v sobě HTML prvky a markdown.
Projekty, vytvořené v Dash lze nahrát na plotly cloud anebo na Heroku.

[Odkaz na tutoriály](https://plot.ly/dash/).

Pro vytvoření applikace Dash budeme potřebovat naimportovat `dash` knihovny.

Tady je úkázka jednoduché aplikace
```
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

Pokud pojmenujete svoji aplikaci `app.py`, spustíte ji následujícím příkazem:
```
$ python app.py
 * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 155-644-719
```
Vaše aplikace bude na adrese `http://127.0.0.1:8050/`

### Cvičení

Popište osu x u předešlého grafu.

## Komponenty `Dash`

`Dash` obsahuje 2 hlavní typy komponentů - `dash_html_components` a `dash_core_components`.

`dash_html_components` obsahuje objekty pro HTML značky. V nášem případě  to jsou `html.Div()` (blokový element) a
`html.H1()` (velký nadpis).

### Cvičení

Přidejte 
