from pathlib import Path
from odfdo import *
from datetime import *
import sys

import laulud
import kirjakohad
import slaidigeneraatorid as slaidilooja
import pyhad
import uuendaja

VERSIOON = "v105"
PYTHON = False # False - selleks, et python compilida; True - selleks, et testida pythonit

# LIPPUDE HANKIMINE
import argparse
parser = argparse.ArgumentParser(prog=VERSIOON, description="Ofdo on automatiseeritud süsteem Pauluse kiriku jumalateenistuste ülekannete slaidide genereerimiseks.")
parser.add_argument('-p', '--päev', help="Genereeritava jumalateenistuse kuupäev (nt 07.12.2025)", metavar="VALIK")
parser.add_argument('-k', '--kord', help="Genereeritava jumalateenistuse slaidide soovitud kord (tavaline/suur/paast)", metavar="VALIK")
parser.add_argument('-s', '--sisend', help="Kogu nõutud sisend ühe rea kujul (eraldatud semikoolonitega)", metavar="VALIK")
argumendid = parser.parse_args()


# UUENDUSE KONTROLLIMINE
uuendaja.kontrolli_uuendusi(VERSIOON)

# JÄRGMISE TEENISTUSE ARVUTAMINE
#kuupäev = pyhad.järgmineTeenistus()
kuupäevSõnadega = "7. detsembril 2025"
kuupäevNumbritega = "07122025"
kellaaeg = "10.00"
teineKellaaeg = False
defaultkord = "tavaline"
if argumendid.päev:
    try:
        päev = datetime.strptime(argumendid.päev, "%d.%m.%Y")
    except:
        päev = datetime.strptime(argumendid.päev, "%d-%m-%Y")
    pühapäev = date(päev.year, päev.month, päev.day)
    kuupäevSõnadega, kuupäevNumbritega = pyhad.parseKuupäev(argumendid.päev)
    
    suuredPühad, teisedKellaajad = pyhad.leiaSuuredPühad(pühapäev.year)
    for i in suuredPühad:
        if i == pühapäev:
            if i in teisedKellaajad:
                teineKellaaeg = True
            defaultkord = "suur"
            break
    paastuAlgus, ülestõusmispüha = pyhad.paast(pühapäev.year)
    if paastuAlgus <= pühapäev < ülestõusmispüha:
        defaultkord = "paast"
        
    tavalised, teisedKellaajad = pyhad.leiaTavalised(pühapäev.year)
    if pühapäev in teisedKellaajad:
        teineKellaaeg = True
else:
    täna = date.today()
    pühapäev = täna + timedelta((6-täna.weekday()) % 7)
    kuupäevSõnadega, kuupäevNumbritega = pyhad.parseKuupäev(pühapäev.strftime("%d.%m.%Y")) 
    
    # KUI TULEMAS ON SUUR PÜHA
    suuredPühad, teisedKellaajad = pyhad.leiaSuuredPühad(täna.year)
    for i in suuredPühad:
        if täna <= i <= pühapäev:
            if i in teisedKellaajad:
                teineKellaaeg = True
            kuupäevSõnadega, kuupäevNumbritega = pyhad.parseKuupäev(i.strftime("%d.%m.%Y"))
            defaultkord = "suur"
            break
    # PAASTUAJA TUVASTAMINE
    paastuAlgus, ülestõusmispüha = pyhad.paast(täna.year)
    if paastuAlgus <= pühapäev < ülestõusmispüha:
        kuupäevSõnadega, kuupäevNumbritega = pyhad.parseKuupäev(pühapäev.strftime("%d.%m.%Y"))
        defaultkord = "paast"
    # KUI ON TAVALISE KORRAGA TEENISTUS, MIS POLE PÜHAPÄEVAL
    tavalised, teisedKellaajad = pyhad.leiaTavalised(täna.year)
    for i in tavalised:
        if täna <= i <= pühapäev:
            if i in teisedKellaajad:
                teineKellaaeg = True
            kuupäevSõnadega, kuupäevNumbritega = pyhad.parseKuupäev(i.strftime("%d.%m.%Y"))
            break
    

korrad = ['tavaline', 'suur', 'paast']
korrad_välja_kirjutatud = ['', 'suurel pühal, ', 'paastuajal, ']
if argumendid.kord and argumendid.kord in korrad:
    kord = argumendid.kord
else:
    kord = defaultkord

print("\n************************************************************")
print("Jumalateenistus " + korrad_välja_kirjutatud[korrad.index(kord)] + kuupäevSõnadega)
print("************************************************************\n")

# SLAIDI TEGEMISEKS VAJALIKUD ANDMED
if PYTHON:
    TARGET_DIR = Path()
else:
    TARGET_DIR = Path(sys.executable).resolve().parent
TARGET = kuupäevNumbritega + " Jumalateenistus (Ofdo).odp"
STIILID = "stiilid.odp"
STIILID_DIR = Path(__file__).parent
viimaneNumber = 0
document = Document("presentation")
body = document.body
body.clear()
style_document = Document(STIILID_DIR / STIILID)
document.delete_styles()
document.merge_styles_from(style_document)



# KASUTAJALT ANDMETE KÜSIMINE
if teineKellaaeg:
    kellaaeg = input("!!! Jumalateenistuse alguskellaaeg (nt: 16.00): ")

if argumendid.sisend:
    sisend = argumendid.sisend.split(";")
else:
    sisend = [False, False, False, False, False, False, False, False, False, False]
laul1pealkiri, laul1sõnad, laul1salmidearv = laulud.küsiKasutajalt("1. laulmine ehk alguslaul", sisend[0])
laul2pealkiri, laul2sõnad, laul2salmidearv = laulud.küsiKasutajalt("2. laulmine ehk päeva laul", sisend[1])
laul3pealkiri, laul3sõnad, laul3salmidearv = laulud.küsiKasutajalt("3. laulmine ehk koguduselaul", sisend[2])
laul4pealkiri, laul4sõnad, laul4salmidearv = laulud.küsiKasutajalt("4. laulmine ehk mälestuslaul", sisend[3])
laul5pealkiri, laul5sõnad, laul5salmidearv = laulud.küsiKasutajalt("5. laulmine ehk palvelaul", sisend[4])
laul6pealkiri, laul6sõnad, laul6salmidearv = laulud.küsiKasutajalt("6. laulmine ehk lõpulaul", sisend[5])

lugemine1, salmiNumbrid1, lugemine1viide, lugemine1üldasukoht = kirjakohad.kontrolli("1. lugemine: ", sisend[6])
lugemine2, salmiNumbrid2, lugemine2viide, lugemine2üldasukoht = kirjakohad.kontrolli("2. lugemine: ", sisend[7])
lugemine3, salmiNumbrid3, lugemine3viide, lugemine3üldasukoht = kirjakohad.kontrolli("3. lugemine (jutluse aluseks): ", sisend[8])
pihtLugemine, pihtNumbrid, pihtViide, pihtÜldasukoht = kirjakohad.kontrolli("Pihisalm (pole kohustuslik): ", sisend[9], True)

# Kui laul2 ja laul3 on samad, siis pole vaja laulunumbrit esilehel mitu korda panna
laul3tekstid = [laul3pealkiri.split(".")[0], laul3salmidearv]
if laul2pealkiri == laul3pealkiri:
    laul3tekstid = [laul3salmidearv]

if sisend[0] == False:
    jutlustaja = input("Jutlustas (koos tiitliga, nt õp): ").split()
    if len(jutlustaja) == 0:
        jutlustaja = ['', '']
    if len(jutlustaja) == 1:
        jutlustaja = [jutlustaja[0], '']
    orelil = input("Orelil: ")
    kaamerad = input("Kaameraid juhtis: ") + " "
    heli = input("Heli eest vastutas: ") + " "
    slaiditegija = input("Slaide liigutas: ") + " "
    vöörmünder1 = input("1. vöörmünder: ")
    vöörmünder2 = input("2. vöörmünder: ")
else:
    jutlustaja = ['++', '+++']
    orelil = "+++"
    kaamerad = "+++"
    heli = "+++"
    slaiditegija = "+++"
    vöörmünder1 = "+++"
    vöörmünder2 = "+++"


# GENEREERIMINE
tiitel = ['EELK Tartu Pauluse kogudus', 'Jumalateenistus algab kell ' + kellaaeg]
lauludtekstid = ['Tänased laulud:',
                 [laul1pealkiri.split(".")[0], laul1salmidearv],
                 [laul2pealkiri.split(".")[0], laul2salmidearv],
                 laul3tekstid,
                 ["†", laul4pealkiri.split(".")[0], laul4salmidearv],
                 [laul5pealkiri.split(".")[0], laul5salmidearv],
                 [laul6pealkiri.split(".")[0], laul6salmidearv]]
lugemised = ['Kirjakohad:', 'Lektsioonid:', lugemine1viide, lugemine2viide, 'Jutlus:', lugemine3viide]
slaidilooja.avaleht(str(viimaneNumber+1), tiitel, lauludtekstid, lugemised, body)  
viimaneNumber += 1

# ALGUSLAUL
viimaneNumber = laulud.genereeri(laul1pealkiri, laul1sõnad, viimaneNumber, body)

# LITURGIA
liturgia = ["Nõnda kui alguses oli, nüüdki on ja jääb", "igavesest ajast igavesti. Aamen."]
slaidilooja.kahereaTekst(str(viimaneNumber+1), liturgia, body)
viimaneNumber += 1

#PIHT
if pihtLugemine == "" and pihtNumbrid == "" and pihtViide == "":
    slaidilooja.lugemisePealkiri(str(viimaneNumber), ["Piht:", "+++"], body)
    slaidid = [['+++']]
else:
    slaidilooja.lugemisePealkiri(str(viimaneNumber), ["Piht:", pihtViide], body)
    slaidid, viimaneRida = kirjakohad.arvutaVormindus(pihtLugemine, pihtNumbrid, False)
viimaneNumber += 1
for i in slaidid:
    slaidilooja.kolmereaTekst(str(slaidid.index(i)+1+viimaneNumber), "".join(i), body)
viimaneNumber += len(slaidid)



#PATUTUNNISTUS
slaidilooja.pealkiriMeile(str(viimaneNumber+1), "Patutunnistus", body)
viimaneNumber += 1
patutunnistus = ['Kõigeväeline Jumal, halastaja Isa! Mina, vaene patune inimene, tunnistan Sinule oma patud üles, mis mina mõtte, sõna ja teoga olen teinud ',
                 'ja millega mina Sinu viha ja Sinu nuhtluse ajalikult ja igavesti küll olen ära teeninud. Aga minul on nende pärast väga kahju ja mina kahetsen neid südamest ',
                 'ja palun Sind Sinu isaliku halastuse ja Sinu armsa Poja Jeesuse Kristuse, meie Õnnistegija kibeda kannatamise ja surma pärast: Ole Sa mulle, patusele inimesele, ',
                 'armuline ja halasta mu peale, anna mulle andeks kõik minu patud ja anna mulle armust Püha Vaimu väge, et ma oma elu saaksin parandada!']
for i in patutunnistus:
    slaidilooja.kolmereaTekst(str(patutunnistus.index(i)+1+viimaneNumber), i, body)
viimaneNumber += len(patutunnistus)


# LITURGIA
liturgia = ["Issand, halasta! Kristus, halasta! ", "Issand, halasta!"]
slaidilooja.kahereaTekst(str(viimaneNumber+1), liturgia, body)
viimaneNumber += 1

if kord == "paast":
    liturgia = ["Oh süüta Tall, oh Jeesus, Sind risti küljes surmati!", "Suur oli Sinu kannatus, ehk Sind küll kurjast põlati."]
    slaidilooja.kahereaTekst(str(viimaneNumber+1), liturgia, body)
    viimaneNumber += 1
    
    liturgia = ["Kõik patud Sina kandsid ja ennast päästjaks andsid.", "Meil' anna armu, oh Jeesus! Meil' anna rahu, oh Jeesus!"]
    slaidilooja.kahereaTekst(str(viimaneNumber+1), liturgia, body)
    viimaneNumber += 1
else:
    liturgia = ["Ja maa peal rahu ja inimestest hea meel, hea meel.", " "]
    slaidilooja.kahereaTekst(str(viimaneNumber+1), liturgia, body)
    viimaneNumber += 1

    liturgia = ["Au, kiitus olgu igavest' Kolmainu Jumalale, ", "et Tema suurest heldusest meid avitanud jälle."]
    slaidilooja.kahereaTekst(str(viimaneNumber+1), liturgia, body)
    viimaneNumber += 1

    liturgia = ["Meist hea meel on Jumalal, suur rahupõlv on taeva all,", "kõik vaen on otsa saanud."]
    slaidilooja.kahereaTekst(str(viimaneNumber+1), liturgia, body)
    viimaneNumber += 1

slaidilooja.ühereaTekst(str(viimaneNumber+1), "Ja sinu vaimuga!", body)
viimaneNumber += 1



# LEKTSIOON 1
slaidilooja.lugemisePealkiri(str(viimaneNumber+1), ["Lektsioon:", lugemine1viide], body)
viimaneNumber += 1
slaidid, viimaneRida = kirjakohad.arvutaVormindus(lugemine1, salmiNumbrid1)
viimaneNumber = kirjakohad.slaididele(slaidid, viimaneRida, viimaneNumber, body)

slaidilooja.ühereaTekst(str(viimaneNumber+1), "Tänu olgu Jumalale!", body)
viimaneNumber += 1


# LEKTSIOON 2
slaidilooja.lugemisePealkiri(str(viimaneNumber+1), ["Lektsioon:", lugemine2viide], body)
viimaneNumber += 1

if lugemine2üldasukoht == "evangeelium" and kord != "paast":
    slaidilooja.kahereaTekst(str(viimaneNumber+1), ["Halleluuja! Halleluuja! Halleluuja!", ""], body)
    viimaneNumber += 1

slaidid, viimaneRida = kirjakohad.arvutaVormindus(lugemine2, salmiNumbrid2)
viimaneNumber = kirjakohad.slaididele(slaidid, viimaneRida, viimaneNumber, body)

if lugemine2üldasukoht == "evangeelium":
    slaidilooja.ühereaTekst(str(viimaneNumber+1), "Kiitus olgu Sulle, oh Kristus!", body)
    viimaneNumber += 1
else:
    slaidilooja.ühereaTekst(str(viimaneNumber+1), "Tänu olgu Jumalale!", body)
    viimaneNumber += 1


#USUTUNNISTUS
if kord == "suur":
    slaidilooja.pealkiriMeile(str(viimaneNumber+1), "Nikaia usutunnistus", body)
    viimaneNumber += 1
    usutunnistus = ['Meie usume ühteainsasse Jumalasse, kõigeväelisse Isasse, taeva ja maa, kõige nähtava ja nähtamatu Loojasse. ',
                    'Ja ühteainsasse Issandasse Jeesusesse Kristusesse, Jumala ainusündinud Pojasse, kes Isast on sündinud enne kõiki aegu, ',
                    'Jumal Jumalast, valgus valgusest, tõeline Jumal tõelisest Jumalast, sündinud, mitte loodud, olemuselt ühtne Isaga, kelle läbi kõik on loodud; ',
                    'kes on meie, inimeste pärast ning meie õndsuseks alla tulnud taevast ning lihaks saanud Püha Vaimu läbi neitsist Maarjast ja inimeseks saanud, ',
                    'Pontius Pilaatuse ajal ka meie eest risti löödud, kannatanud ja maha maetud ning kolmandal päeval üles tõusnud pühade kirjade järgi ja üles läinud taeva,',
                    'istub Isa paremal käel ja tuleb taas kirkuses kohut mõistma elavate ja surnute üle; Tema riigile ei tule otsa. Meie usume Pühasse Vaimusse, ',
                    'Issandasse ja Elavakstegijasse, kes lähtub Isast ja Pojast, keda Isa ja Pojaga üheskoos kummardatakse ja austatakse; kes on rääkinud prohvetite kaudu. ',
                    'Meie usume ühtainust püha, kristlikku ja apostlikku kirikut. Meie tunnistame ühtainust ristimist pattude andeksandmiseks ',
                    'ja ootame surnute ülestõusmist ning tulevase ajastu elu.']
else:
    slaidilooja.pealkiriMeile(str(viimaneNumber+1), "Apostlik usutunnistus", body)
    viimaneNumber += 1
    usutunnistus = ['Mina usun Jumalasse, kõigeväelisse Isasse, taeva ja maa Loojasse. Ja Jeesusesse Kristusesse, Tema ainsasse Pojasse, meie Issandasse,',
                     'kes on saadud Pühast Vaimust, ilmale tulnud neitsi Maarjast, kannatanud Pontius Pilaatuse all, risti löödud, surnud ja maha maetud, alla läinud surmavalda,',
                     'kolmandal päeval üles tõusnud surnuist, üles läinud taeva, istub Jumala, oma kõigeväelise Isa paremal käel, sealt Tema tuleb kohut mõistma elavate ja surnute üle.  ',
                     'Mina usun Pühasse Vaimusse, üht püha kristlikku Kirikut, pühade osadust, pattude andeksandmist, ihu ülestõusmist ja igavest elu.']

for i in usutunnistus:
    slaidilooja.kolmereaTekst(str(usutunnistus.index(i)+1+viimaneNumber), i, body)
viimaneNumber += len(usutunnistus)


# PÄEVA LAUL
viimaneNumber = laulud.genereeri(laul2pealkiri, laul2sõnad, viimaneNumber, body)


# JUTLUSETEKST
slaidilooja.lugemisePealkiri(str(viimaneNumber+1), ["Jutlus:", lugemine3viide], body)
viimaneNumber += 1

slaidid, viimaneRida = kirjakohad.arvutaVormindus(lugemine3, salmiNumbrid3)
viimaneNumber = kirjakohad.slaididele(slaidid, viimaneRida, viimaneNumber, body)


# KANTSLISALM
viimaneNumber = laulud.genereeri(laul3pealkiri, laul3sõnad, viimaneNumber, body)


# MÄLESTUSLAUL
viimaneNumber = laulud.genereeri(laul4pealkiri, laul4sõnad, viimaneNumber, body)

# PALVELAUL
viimaneNumber = laulud.genereeri(laul5pealkiri, laul5sõnad, viimaneNumber, body)


# KIRIKUPALVE
slaidilooja.pealkiriMeile(str(viimaneNumber+1), "Kirikupalve", body)
viimaneNumber += 1

slaidilooja.ühereaTekst(str(viimaneNumber+1), "Sind, Jumal kiidame! Sind, Issand täname!", body)
viimaneNumber += 1
slaidilooja.ühereaTekst(str(viimaneNumber+1), "Kuule meid, armas Issand Jumal!", body)
viimaneNumber += 1
slaidilooja.ühereaTekst(str(viimaneNumber+1), "Aita meid, armas Issand Jumal!", body)
viimaneNumber += 1
liturgia = ["Oh Jeesus Krist, oh kuule mind, oh kuule mind!", "Ma tahan ikka kiita Sind! Aamen."]
slaidilooja.kahereaTekst(str(viimaneNumber+1), liturgia, body)
viimaneNumber += 1
slaidilooja.ühereaTekst(str(viimaneNumber+1), "Ja sinu vaimuga!", body)
viimaneNumber += 1
slaidilooja.ühereaTekst(str(viimaneNumber+1), "Meie ülendame südamed Issanda poole.", body)
viimaneNumber += 1
slaidilooja.ühereaTekst(str(viimaneNumber+1), "See on õige ja kohus.", body)
viimaneNumber += 1


# SANCTUS
slaidilooja.pealkiriMeile(str(viimaneNumber+1), "Sanctus", body)
viimaneNumber += 1

slaidilooja.ühereaTekst(str(viimaneNumber+1), "Püha, püha, püha on meie Jumal, me Issand Seebaot.", body)
viimaneNumber += 1
slaidilooja.ühereaTekst(str(viimaneNumber+1), "Taevas ja maa, taevas ja maa on täis Tema au!", body)
viimaneNumber += 1
liturgia = ["Hoosianna kõrges! Kiidetud olgu, kes tuleb ", "Issanda nimel. Hoosianna kõrges!"]
slaidilooja.kahereaTekst(str(viimaneNumber+1), liturgia, body)
viimaneNumber += 1


# MEIE ISA PALVE
slaidilooja.pealkiriMeile(str(viimaneNumber+1), "Meie Isa Palve", body)
viimaneNumber += 1
meieisapalve = ['Meie Isa, kes Sa oled taevas! Pühitsetud olgu Sinu nimi. Sinu riik tulgu. Sinu tahtmine sündigu nagu taevas, nõnda ka maa peal.',
                 'Meie igapäevast leiba anna meile tänapäev. Ja anna meile andeks meie võlad, nagu meiegi andeks anname oma võlglastele. Ja ära saada meid kiusatusse, ']
for i in meieisapalve:
    slaidilooja.kolmereaTekst(str(meieisapalve.index(i)+1+viimaneNumber), i, body)
viimaneNumber += len(meieisapalve)
liturgia = ['vaid päästa meid ära kurjast.', ['♪ Sest Sinu päralt on riik ja vägi ja au igavesti. ', 'Aamen.']]
slaidilooja.liturgiaKollane(str(viimaneNumber+1), liturgia, body)
viimaneNumber += 1


# AGNUS DEI
slaidilooja.pealkiriMeile(str(viimaneNumber+1), "Agnus Dei", body)
viimaneNumber += 1
liturgia = ["Kristus, Jumala Tall, kes maailma patud kannad,", "halasta meie peale!"]
slaidilooja.kahereaTekst(str(viimaneNumber+1), liturgia, body)
viimaneNumber += 1
liturgia = ["Kristus, Jumala Tall, kes maailma patud kannad,", "halasta meie peale!"]
slaidilooja.kahereaTekst(str(viimaneNumber+1), liturgia, body)
viimaneNumber += 1
liturgia = ["Kristus, Jumala Tall, kes maailma patud kannad,", "anna meile oma rahu!"]
slaidilooja.kahereaTekst(str(viimaneNumber+1), liturgia, body)
viimaneNumber += 1


# HALLELUUJA
if kord == "paast":
    slaidilooja.ühereaTekst(str(viimaneNumber+1), "Ja Tema heldus kestab igavesti.", body)
    viimaneNumber += 1
else:
    slaidilooja.ühereaTekst(str(viimaneNumber+1), "Ja Tema heldus kestab igavesti. Halleluuja!", body)
    viimaneNumber += 1


# LÕPULAUL
viimaneNumber = laulud.genereeri(laul6pealkiri, laul6sõnad, viimaneNumber, body)

# LÕPUSOOV
tekst = ['Issanda Jeesuse Kristuse arm,', 'Jumala armastus ja Püha Vaimu osadus olgu teie kõikidega!']
slaidilooja.lõpuSoov(str(viimaneNumber+1), tekst, body)
viimaneNumber += 1

# TIITRID
tiitel = "Jumalateenistus " + kuupäevSõnadega
peategijad = [['Jutlustas: '+jutlustaja[0]+' ', " ".join(jutlustaja[1:])], ['Kaasa teenisid: ++ ', '+++ ', 'ja'], ['++ ', '+++'], ['Orelil: ', orelil], ['Piiblitekste lugesid: ', '+++ ', 'ja ', '+++']]
tehnikatiim = ['Ülekande tõid teieni:', [kaamerad, '– kaamerad'], [heli, '– heli'], [slaiditegija, '– slaidid']]
vöörmündrid = ['Vöörmündrid:', vöörmünder1, vöörmünder2]
lõpusoov = "Täname südamest! Uute kohtumisteni!"
slaidilooja.lõpuTiitrid(str(viimaneNumber+1), tiitel, peategijad, tehnikatiim, vöörmündrid, lõpusoov, body)



document.save(TARGET_DIR / TARGET, pretty=True)

print("************************************************************\n")
print("Ofdo " + VERSIOON)