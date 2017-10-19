# Nasazení aplikace Dash na externí server

[Návod na stránkách Dash](https://plot.ly/dash/deployment)

1. Vytvořte složku ve které bude aplikace. 
Pokud budete používat data z offline souborů, zkopirujte do této složky tyto soubory také.
```
mkdir moje_aplikace
```

2. Vytvořte virtuální prostředí a inicializujte verzování

```
cd moje-aplikace
git init                      # inicializuje prázdné git repo ve složce
virtualenv venv               # vytvoří virtuální prostředí "venv"
source venv/bin/activate      # aktivuje virtualenv
```

3. Nainstalujte knihovny python

```
pip install dash dash-renderer dash-core-components dash-html-components plotly pandas
```

**Důležité**:  nainstalujte všechny knihovny, které potřebujete pro analýzu a vizualizaci dat, např. `xlrd`

Nainstalujte knihovnu potřebnou pro nasazení aplikace

```
pip install gunicorn
```

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

6. Vytvořte konfigurační soubor `Procfile`

```
web: gunicorn app:server
```

**Důležité**: `app` se musí shodovat s názvem aplikace (v tomto případě je název aplikace `app.py`)

5. Vytvořte `requirements.txt` se seznamem potřebných knihoven
```
pip freeze > requirements.txt
```

6. Nainstalujte Heroku a založte si účet na [Heroku](https://heroku.com)

[Návod na stránkách Heroku](https://devcenter.heroku.com/articles/heroku-cli)

```
heroku login
```

7. Vytvořte aplikace Heroku, inicializujte Git a nasaďte aplikaci

```
heroku create moje-aplikace # změňte 'moje aplikace' na unikátní název
git add . # přideá soubory do git
git commit -m 'Initial commit'
git push heroku master # nasadí kôd do heroku
heroku ps:scale web=1  # spustí aplikaci s 1 heroku "dyno"
heroku config:set SECRET_KEY=my_secret_key # vyměňte my_secret_key za náhodný řetězec
```
Vaše  aplikace bude dostupná na adrese `https://moje-aplikace.herokuapp.com`.

8. Ladění

Spusťte server lokálně
```
gunicorn app:server
```

Podívejte se na logy heroku
```
heroku logs
```


9. Doplnění kódu a opětovné nasazení

```
git status # prohlednout změny
git add .  # přidat všechny změny do commitu
git commit -m 'popis změny'
git push heroku master
```
