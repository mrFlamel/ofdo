from datetime import *
from dateutil.easter import *
"""
def arvutaKõikTeenistused(aasta): # tavaline, suur, paast
    kõik = []
    
    # ADVENDIAEG
    for i in range(8):
        if date(aasta-1, 12, 24-i).isoweekday() == 7:
            kõik.append([date(aasta-1, 12, 24-i)-timedelta(weeks=3), "Advendiaja 1. pühapäev", "tavaline"])
            break
    for i in range(3):
        kõik.append([kõik[-1][0]+timedelta(weeks=1), "Advendiaja "+str(2+i)+". pühapäev", "tavaline"])
    
    # JÕULUAEG
    kõik.append([date(aasta-1, 12, 24), "Jõululaupäev", "tavaline"])
    kõik.append([date(aasta-1, 12, 25), "Esimene jõulupüha", "suur"])
    kõik.append([date(aasta-1, 12, 26), "Teine jõulupüha", "suur"])
    if kõik[-4][0]+timedelta(weeks=1) < date(aasta-1, 12, 31):
        kõik.append([kõik[-1][0]+timedelta(weeks=1), "Jõuluaja 1. pühapäev", "suur"])  
    
    
    
    ülestõusmispüha = easter(aasta, 3)
    nelipühad = ülestõusmispüha + timedelta(days=49)
    
    print(ülestõusmispüha)
    print(nelipühad)
    
    return kõik
"""


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

"""
def järgmineTeenistus():
    täna = datetime.today().date()
    for i in arvutaKõikTeenistused(täna.year+1):
        print(i)
    
"""