# Nasazení aplikace Dash na externí server

[Návod na stránkách Dash](https://plot.ly/dash/deployment)

1. Vytvořte složku ve které bude aplikace. 
Pokud budete používat data z offline souborů, zkopirujte do této složky tyto soubory také.
```
mkdir moje_aplikace
```

2. Vytvořte virtuální prostředí a inicializujte verzování

2.1. UNIX

```
cd moje-aplikace
git init                      # inicializuje prázdné git repo ve složce
virtualenv venv               # vytvoří virtuální prostředí "venv" 
source venv/bin/activate      # aktivuje virtualenv
```

2.2. Anaconda prompt

```
cd moje-aplikace
git init                      # inicializuje prázdné git repo ve složce
conda create -n venv python=3 # vytvoří virtuální prostředí "venv"
activate venv      # aktivuje virtualenv
```

*Poznámka:* `virtualenv` nainstalujte pomoci `pip install virtualenv` (UNIX). 

Pokud by příkaz `source venv/bin/activate` nefungoval, zkuste `source venv/Scripts/activate`.

3. Nainstalujte knihovny python

```
pip install dash dash-renderer dash-core-components dash-html-components plotly pandas
```

**Důležité**:  nainstalujte všechny knihovny, které potřebujete pro analýzu a vizualizaci dat, např. `xlrd`

Nainstalujte knihovnu potřebnou pro nasazení aplikace

```
pip install gunicorn
```
*Poznámka*: pokud máte Windows, neinstalujte knihovnu `gunicorn`, viz krok 10.

4. V aplikaci nastavte poměnnou `app.server`
```
import os

server = app.server
server.secret_key = os.environ.get('SECRET_KEY', 'my-secret-key')
```

5. Vytvořte soubor `.gitignore` s následujícím obsahem. 
Jedná se o lokální soubory, které nepotřebují verzování.

```
venv
*.pyc
.DS_Store
.env
```

6. Vytvořte konfigurační soubor `Procfile` s následujícím obsahem:

```
web: gunicorn app:server
```

**Důležité: `app` se musí shodovat s názvem aplikace (v tomto případě je název aplikace `app.py`). Je potřeba, aby se `Procfile` jmenoval přesně takto bez přípony, ne `Procfile.txt`.**

7. Vytvořte `requirements.txt` se seznamem potřebných knihoven pomocí následujícího příkazu:
```
pip freeze > requirements.txt
```

8. Nainstalujte Heroku a založte si účet na [Heroku](https://heroku.com)

[Návod na stránkách Heroku](https://devcenter.heroku.com/articles/heroku-cli)

```
heroku login
```

9. Vytvořte aplikace Heroku, inicializujte Git a nasaďte aplikaci

```
heroku create moje-aplikace # změňte 'moje aplikace' na unikátní název
git add . # přideá soubory do git
git commit -m 'Initial commit'
git push heroku master # nasadí kôd do heroku
heroku ps:scale web=1  # spustí aplikaci s 1 heroku "dyno"
heroku config:set SECRET_KEY=my_secret_key # vyměňte my_secret_key za náhodný řetězec
```
Vaše  aplikace bude dostupná na adrese `https://moje-aplikace.herokuapp.com`.

10. Ladění

Spusťte server lokálně
```
gunicorn app:server
```
Pokud máte problém s instalací `gunicorn` na Windows, použíjte následující příkaz.

Podívejte se na logy heroku
```
heroku logs -a app
```
Logy se také dají vidět po přihlášení na stránce [heroku](https://heroku.com) v sekci aplikace Activity -> View building log.

11. Doplnění kódu a opětovné nasazení

```
git status # prohlednout změny
git add .  # přidat všechny změny do commitu
git commit -m 'popis změny'
git push heroku master
```
