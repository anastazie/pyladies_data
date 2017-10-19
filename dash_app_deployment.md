# Nasazení aplikace Dash na externí server

[Návod na stránkách Dash](https://plot.ly/dash/deployment)

1. Vytvořte složku ve které bude aplikace. 
Pokud budete používat data z offline souborů, zkopirujte do této složky tyto soubory také.
```
mkdir moje_aplikace
```

2. Vytvořte virtuální prostředí a inicializujte verzování

```
cd moje_aplikace
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


