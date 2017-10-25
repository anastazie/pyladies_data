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

Přidejte popisek osy x u předešlého grafu ('třída jízdenky').

## Komponenty `Dash`

`Dash` obsahuje 2 hlavní typy komponentů - `dash_html_components` a `dash_core_components`.

### HTML komponenty

`dash_html_components` obsahuje objekty pro HTML značky. V nášem případě  to jsou `html.Div()` (blokový element) a
`html.H1()` (velký nadpis).

*Poznámka*: abychom psali méně, importujeme `dash_html_components` takto: `import dash_html_components as html`

### Cvičení

Za velký nadpis přidejte odstavec (`html.P`) kde bude napsáno `Popis dat tady.`.
 

 
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

Pridejte pomocí `dcc.Markdown` do `html.Div` místo `html.P` odkaz na [dokumentaci k datem](https://www.kaggle.com/c/titanic/data).

### Výber z hodnot

Tady je příklad vytvoření výběrového pole
```
import dash_core_components as dcc


dcc.Dropdown(
    options=[
        {'label': 'Možnost A', 'value': 'val_a'},
        {'label': 'Možnost B', 'value': 'val_b'},
    ],
    value='val_a'
)
```
`label` má hodnotu, která se zobrazí ne webové stránce, `value` je hodnota, která může být použitá pro 

*Poznámka*: pokud chete vyzkoušet výše uvedený kód, uložte ho do samostatného souboru a spusťte pomocí příkazu `python <nazev_vaseho_souboru.py>`.


Příklad přepinače - můžete vybrat jednu z hodnot.
```
import dash_core_components as dcc

dcc.RadioItems(
    options=[
        {'label': 'Tato možnost', 'value': 'variant1'},
        {'label': 'Nebo tato', 'value': 'variant2'}
    ],
    value='variant'
)
```

Další možnosti jsou [tady](https://plot.ly/dash/dash-core-components).


### Cvičení

Do své aplikace přidejte výběrové pole s možnostmi: 'Cena listků podle třídy' a 'Věk cestujících podle třídy' (hodnoty 'fare_class' a 'age_class').
Poté přijdete přepináč s možnostmi: 'Histogram' a 'Boxplot' (hodnoty 'hist' a 'boxplot').

## Dekoratory

Dekorátor je funkce, která obaluje jinou funkci. V nášem případe se jedná o `@app.callback`, která říká, že pokud se vstup do této funkce změní, má se zavolat funkce, která je definována níže.

Tady je příklad:

```
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input-text'', value='initial value', type="text"),
    html.Div(id='display-text')
])

@app.callback(
    Output(component_id='display-text', component_property='children'),
    [Input(component_id='input-text', component_property='value')]
)

def update_output_div(input_value):
    return 'Napsali jste "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server()

```
POkud napišemé cokoliv do okénka (`dcc.Input`), změní se vstupní data do `@app.callback` (`Input(component_id='input-text', component_property='value')`). Proto se zavolá funkce a `html.Div` s id `display-text` zobrazí text, který jsme zadali do okénka, protože tak je definována funkce `update_output_div`.
 
### Cvičení

Upravte výše uvedený kod:
1. Vložte nadpis (`html.H1`) před `dcc.Input` a pojmenujte jeho id 'big-title'
2. Předělejte `app.callback` aby aktualizoval nadpis, ne `html.Div`
3. Předělejte funkci `update_output_div` na `update_output_h1` aby varcela 'Zprava dne:' a text, který jste zadali


