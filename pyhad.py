from datetime import datetime, date, timedelta
from dateutil.easter import easter

def parseKuupäev(kuupäev):
    try:
        päev = datetime.strptime(kuupäev, "%d.%m.%Y")
    except:
        päev = datetime.strptime(kuupäev, "%d-%m-%Y")
    
    kuud = ['jaanuaril', 'veebruaril', 'märtsil', 'aprillil', 'mail', 'juunil', 'juulil', 'augustil', 'septembril', 'oktoobril', 'novembril', 'detsembril']
    kuupäevSõnadega = str(päev.day) + ". " + kuud[päev.month-1] + " " + str(päev.year)
    kuupäevNumbritega = päev.strftime("%d%m%Y")
    
    return kuupäevSõnadega, kuupäevNumbritega

def leiaSuuredPühad(aasta):
    ülestõusmispüha = easter(aasta, 3)
    
    pühad = [date(aasta, 1, 6), # KOLMEKUNINGAPÄEV (KRISTUSE ILMUMISPÜHA)
             ülestõusmispüha-timedelta(days=3), #SUUR NELJAPÄEV
             ülestõusmispüha-timedelta(days=2), #SUUR REEDE
             ülestõusmispüha, # 1. ÜLESTÕUSMISPÜHA
             ülestõusmispüha+timedelta(days=39), # TAEVAMINEMISPÜHA
             ülestõusmispüha+timedelta(weeks=7), # 1. NELIPÜHA
             ülestõusmispüha+timedelta(weeks=8), # KOLMAINUPÜHA
             date(aasta, 12, 25) # 1. JÕULUPÜHA
             ]
    teineKellaaeg = [date(aasta, 1, 6), # KOLMEKUNINGAPÄEV (KRISTUSE ILMUMISPÜHA)
                     ülestõusmispüha-timedelta(days=3), #SUUR NELJAPÄEV
                     ülestõusmispüha-timedelta(days=2), #SUUR REEDE
                     ]
    return pühad, teineKellaaeg

def leiaTavalised(aasta):
    
    pühad = [date(aasta, 1, 1), # UUSAASTA
             date(aasta, 12, 26), # 2. JÕULUPÜHA
             date(aasta, 12, 31) # VANAAASTAÕHTU
             ]
    teineKellaaeg = [date(aasta, 1, 1), # UUSAASTA
                     date(aasta, 12, 31) # VANAAASTAÕHTU
                     ]
    return pühad, teineKellaaeg

def paast(aasta):
    ülestõusmispüha = easter(aasta, 3)
    return ülestõusmispüha-timedelta(days=46), ülestõusmispüha

def leiaÜldAsukohad(kuupäevNumbritega):
    päev = datetime.strptime(kuupäevNumbritega, "%d%m%Y")
    aasta = päev.year
    uusKirikuaasta = datetime(aasta, 12, 24) - timedelta((datetime(aasta, 12, 24).weekday() + 1) % 7) - timedelta(weeks=3)
    if päev >= uusKirikuaasta:
        aasta += 1
    
    if aasta % 2 == 0: # Kui aasta jagub 2-ga
        if aasta % 4 == 0: # Kui aasta jagub 4-ga
            lugemine1 = "epistel"
            lugemine2 = "evangeelium"
            jutlus = "vana_testament"
        else:
            lugemine1 = "vana_testament"
            lugemine2 = "evangeelium"
            jutlus = "epistel"
    else:
        lugemine1 = "vana_testament"
        lugemine2 = "epistel"
        jutlus = "evangeelium"
    
    return lugemine1, lugemine2, jutlus
    
    
