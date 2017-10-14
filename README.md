# Kurz "Datová analýza pomocí Pythonu" - Pyladies 2017


## Informace ke kurzu datové analýzy Pyladies

Kurz bude probíhat v Akademii CZ NIC ([Milešovská 1136/5, Praha 3](https://mapy.cz/s/22d5n)) každý čtvrtek od 5.10 do 2.11 od 18 do 20 hodin.

### Rozvrh
| Datum | Téma|
|-------|--------|
| 5.10.2017 | Získání dat |
| 12.10.2017 | Čištění dat |
| 19.10.2017 |	Grafy |
| 26.10.2017 |	Interaktivní aplikace |
| 2.11.2017 | Obhajoba projektu |

## Instalace

Pro kurz můžete používat Python 3.5 nebo 3.6

### Windows

1. Nainstalujte anacondu 4.4.0 [32-bit](https://repo.continuum.io/archive/Anaconda3-4.4.0-Windows-x86.exe) nebo [64-bit](https://repo.continuum.io/archive/Anaconda3-4.4.0-Windows-x86_64.exe).

1. Nainstalujte GitBash pomocí následujícícho příkazu v Anaconda prompt. GiBash se objeví ve startovním menu
`conda install git`

### Linux, MacOS

1. Nainstalujte python
    1. Ubuntu, Debian
    `sudo apt install python3 python3-pip`
    1. MacOS
    `brew install python3`
    Pozn. pokud nemate brew, nainstalujte ho, viz [navod](https://brew.sh/)
    

1. Nainstalujte pandas
`pip3 install pandas`

1. Nainstalujte Jupyter Notebook
`pip3 install jupyter`

## Spuštění Jupyter Notebooku

### Windows

Protože máte python nainstalovaný pomocí Anacondy, program na spuštění Jupyter notebooku by měl byt v podsložce Anaconda.

### Linux, MacOS

Spustíte Jupyter Notebook pomocí příkazu `jupyter notebook`

## Instalace knihoven

### Anaconda

1. Do `Anaconda prompt`

```
conda install pandas
conda install requests
conda install jupyter
conda install xlrd
pip install plotly
pip install dash
pip install dash-core-components
pip install dash-html-components
pip install dash-renderer
```

### Pip


```
pip install pandas
pip install requests
pip install jupyter
pip install xlrd
pip install plotly
pip install dash
pip install dash-core-components
pip install dash-html-components
pip install dash-renderer
```

Pozn. Je možné, že budete muset použít sudo (např. `sudo pip install pandas`). Pokud máte i Python2, použijte `pip3`

### Kontrola instalace

Po instalaci zkontrolujte verze dle `requirements.txt`.

## Program

1. Úvod. Získání dat 
    - [Přednáška](https://docs.google.com/presentation/d/1a4jWMLkExi0yS4-PvnwJhvME-9DvIOs3592phCzJuuY/edit?usp=sharing)
    - [JupyterNotebook](https://github.com/anastazie/pyladies_data/blob/master/1_pyladies_data.ipynb)

1. Čištění dat 
    - [Přednáška](https://docs.google.com/presentation/d/1Eqz0zh4jK2fFMU0O2GQ2ryoAqfv_J4wL2QBZHlaizOc/edit?usp=sharing)
    - [JupyterNotebook](https://github.com/anastazie/pyladies_data/blob/master/2_pyladies_data.ipynb)

1. Grafy
    - [Přednáška](https://docs.google.com/presentation/d/162lNlIfFa91JXlxn49Idl7vSTv0U1yFi6nGJaTdb2CY/edit?usp=sharing)

1. Interaktivní aplikace 

1. Obhajoba projektu
    - [Informace](https://docs.google.com/presentation/d/1HLYrwprlPZuB2_e1Czo6WDplzqLF0k_ll-cN4p9vTOA/edit?usp=sharing)


