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
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': ''Cherbourg''},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Queenstown'},
                {'x': [1, 2, 3], 'y': [3, 2, 3], 'type': 'bar', 'name': 'Southampton'}
            ],
            'layout': {
                'title': 'Nástupní místo dle třídy jizdenky'
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

### HTML komponenty

`dash_html_components` obsahuje objekty pro HTML značky. V nášem případě  to jsou `html.Div()` (blokový element) a
`html.H1()` (velký nadpis).

*Poznámka*: abychom psali méně, importujeme `dash_html_components` takto: `import dash_html_components as html`

### Cvičení

Za velký nadpis přidejte odstavec (`html.P`) kde bude napsáno `Ahoj`.
 

 
## Interaktivní komponenty

Knihovna `Dash` obsahuje funkce, které dovolují jednoduše vytvářet interaktivní objekty, například grafy, interaktivní tabulky, možnosti volby a markdown.

Importujeme tyto funkce následně: `import dash_core_components as dcc`.

Místo html můžeme používat markdown (značkovací jazyk):

```
import dash_core_components as dcc

dcc.Markdown('''
# Dash a Markdown

Dash podporuje [Markdown](http://commonmark.org/help).

Markdown je jednoduchý způsob jak psát a formatovat text.
Obsahuje It includes a syntax for things like **tučný text** and *kurziva*,
[odkaz](http://commonmark.org/help), vnořený `kód`, seznamy,
citáty, atd.
''')
```

### Cvičení

Pridejte pomocí `dcc.Markdown` do `html.Div` velký nápis.

### Výber z hodnot

Tady je příklad vytvoření výběrového pole
```
import dash_core_components as dcc


dcc.Dropdown(
    options=[
        {'label': 'Cena listků podle třídy', 'value': 'fare_class'},
        {'label': 'Věk cestujících podle třídy', 'value': 'age_class'},
    ],
    value='fare_class'
)
```
`label` má hodnotu, která se zobrazí ne webové stránce, `value` je hodnota, která může být použitá pro 

*Poznámka*: pokud chete vyzkoušet výše uvedený kód, uložte ho do samostatného souboru a spusťte pomocí příkazu `python <nazev_vaseho_souboru.py>`.


Příklad přepinače - můžete vybrat jednu z hodnot.
```
import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'Histogram', 'value': 'hist'},
        {'label': 'Boxplot', 'value': 'boxplot'}
    ],
    value='hist'
)
```

### Cvičení
 
