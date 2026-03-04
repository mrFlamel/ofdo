import xml.etree.ElementTree as ET
import slaidigeneraatorid as slaidilooja
import time
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

tree = ET.parse(resource_path('piibel.xml'))
piibel = tree.getroot()

vanaTestament = [
    ["1Ms", "1Mo"], ["2Ms", "2Mo"], ["3Ms", "3Mo"], ["4Ms", "4Mo"], ["5Ms", "5Mo"],
    ["Jos"], ["Km", "Kht"], ["Rt"], ["1Sm"], ["2Sm"],
    ["1Kn"], ["2Kn"], ["1Aj"], ["2Aj"], ["Esr"],
    ["Ne", "Neh"], ["Est"], ["Ii", "Ib"], ["Ps"], ["Õp"],
    ["Kg"], ["Ül"], ["Js", "Jes"], ["Jr", "Jer"], ["Nl", "Nt"],
    ["Hs", "Hes"], ["Tn"], ["Ho", "Hos"], ["Jl"], ["Am"],
    ["Ob"], ["Jn"], ["Mi", "Mik"], ["Na"], ["Ha", "Hab"],
    ["Sf"], ["Hg"], ["Sk"], ["Ml"]
    ]
evangeelium = [
    ["Mt"], ["Mk", "Mrk"], ["Lk"], ["Jh"]
    ]
epistel = [
    ["Ap", "Apt"], ["Rm"], ["1Kr", "1Kor"], ["2Kr", "2Kor"], ["Gl", "Gal"],
    ["Ef"], ["Fl", "Fp"], ["Kl"], ["1Ts", "1Tes"], ["2Ts", "2Tes"],
    ["1Tm", "1Tim"], ["2Tm", "2Tim"], ["Tt"], ["Fm"], ["Hb"], ["Jk"],
    ["1Pt"], ["2Pt"], ["1Jh"], ["2Jh"], ["3Jh"],
    ["Jd"], ["Ilm"]
    ]

ülaindeks = {
    '1': "¹", '2': "²", '3': "³", '4': "⁴", '5': "⁵", '6': "⁶", '7': "⁷", '8': "⁸", '9': "⁹", '0': "⁰"}

def ava(otsitav):
    #print(root[1][3][0][0].text)
    
    raamat = otsitav.split()[0]
    vahemik = "".join(otsitav.split()[1:])
    üldine_asukoht = ""
    
    # Ignoreeri a/b salme
    vahemik = vahemik.replace("a", "")
    vahemik = vahemik.replace("b", "")
    
    testament = None
    raamatuNumber = None
    for i in vanaTestament:
        for l in i:
            if l == raamat:
                testament = 0
                raamatuNumber = vanaTestament.index(i)
                üldine_asukoht = "vana_testament"
                break
    for i in evangeelium:
        for l in i:
            if l == raamat:
                testament = 1
                raamatuNumber = evangeelium.index(i)
                üldine_asukoht = "evangeelium"
                break
    for i in epistel:
        for l in i:
            if l == raamat:
                testament = 1
                raamatuNumber = 4 + epistel.index(i)
                üldine_asukoht = "epistel"
                break
    if testament == None:
        raise Exception("Tundmatu piibliraamatu lühend " + raamat)
    
    peatükk = vahemik.split(":")[0]
    if peatükk == vahemik:
        peatükk = vahemik.split(",")[0]
        if peatükk == vahemik:
            raise Exception("Vale vorming!")
        salmid = ",".join(vahemik.split(",")[1:])
    else:
        salmid = "".join(vahemik.split(":")[1:])
    
    
    
    salmiList = []
    tempNumber = ""
    onVahemik = False
    for i in salmid:
        try:
            int(i)
            tempNumber += i
        except:
            pass
        if i == "-":
            salmiList.append(int(tempNumber))
            tempNumber = ""
            onVahemik = True
        if i == ",":
            if onVahemik:
                onVahemik = False
                for i in range(int(tempNumber) - salmiList[-1]):
                    salmiList.append(salmiList[-1]+1)
                tempNumber = ""
            else:
                salmiList.append(int(tempNumber))
                tempNumber = ""
    if onVahemik:
        for i in range(int(tempNumber) - salmiList[-1]):
            salmiList.append(salmiList[-1]+1)
        tempNumber = ""
    if tempNumber != "":
        salmiList.append(int(tempNumber))
    arvutatavTulemus = []
    #indeksid = []
    for i in salmiList:
        #Konverteeri number ülaindeksisse
        number = ""
        for l in str(i):
            number += ülaindeks[l]
        arvutatavTulemus.append(number)
        #indeksid.append(number)
        
        try:
            arvutatavTulemus.append(piibel[testament][raamatuNumber][int(peatükk)-1][i-1].text)
        except:
            raise Exception("Peatükki " + peatükk + " ja/või salmi " + str(i) + " ei eksisteeri...")
    
    # Muuda ' -> "
    for index, i in enumerate(arvutatavTulemus):
        if "'" in i:
            arvutatavTulemus[index] = i.replace("'", '”')   
    
    return arvutatavTulemus, salmiList, üldine_asukoht


def poolita(poolitatavRida):
    
    # ARVUTAB LISTI TÄHTEDE ARVU
    def count(countList):
        counted = 0
        for i in countList:
            if type(i) == int:
                counted = counted + str(i).count("") - 1
            else:
                counted = counted + i.count("") - 1
        return counted
    
    def poolitaMärgiJärgi(märk, rida, lubatudLõikamiseAla):
        for index, i in enumerate(reversed(poolitatavRida)):
            if type(i) == str:
                if märk in i:
                    tempPooleks = i.split(märk)
                    if (count([tempPooleks[1]] + poolitatavRida[len(poolitatavRida)-index:]) / reapikkus) < lubatudLõikamiseAla:
                        tagasi1 = poolitatavRida[:len(poolitatavRida)-index-1] + [tempPooleks[0] + märk]
                        tagasi2 = [" ".join(tempPooleks[1:])] + poolitatavRida[len(poolitatavRida)-index:]
                        return tagasi1, tagasi2
    
    
    esimenePool = []
    teinePool = []
    reapikkus = count(poolitatavRida)
    lubatudLõikamiseAla = 0.7
    
    # KUI SAAB ÜHE SALMI LÕIGATA JÄRGMISELE SLAIDIDLE
    for index, i in enumerate(reversed(poolitatavRida)):
        if type(i) == int:
            if (count(poolitatavRida[len(poolitatavRida)-index-1:]) / reapikkus) < lubatudLõikamiseAla:
                return poolitatavRida[:len(poolitatavRida)-index-1], poolitatavRida[len(poolitatavRida)-index-1:]
            else:
                break
    
    # POOLITAMINE KOOLONIST
    try:
        tagasi1, tagasi2 = poolitaMärgiJärgi(": ", poolitatavRida, lubatudLõikamiseAla)
        return tagasi1, tagasi2
    except:
        pass
    
    # POOLITAMINE DIALOOGI LÕPETAVAST PUNKTIST
    try:
        tagasi1, tagasi2 = poolitaMärgiJärgi('."', poolitatavRida, lubatudLõikamiseAla)
        return tagasi1, tagasi2
    except:
        pass
    
    # POOLITAMINE PUNKTIST
    try:
        tagasi1, tagasi2 = poolitaMärgiJärgi(". ", poolitatavRida, lubatudLõikamiseAla)
        return tagasi1, tagasi2
    except:
        pass
    
    # POOLITAMINE HÜÜUMÄRGIST
    try:
        tagasi1, tagasi2 = poolitaMärgiJärgi("! ", poolitatavRida, lubatudLõikamiseAla)
        return tagasi1, tagasi2
    except:
        pass
    
    # POOLITAMINE KÜSIMÄRGIST
    try:
        tagasi1, tagasi2 = poolitaMärgiJärgi("? ", poolitatavRida, lubatudLõikamiseAla)
        return tagasi1, tagasi2
    except:
        pass
    
    # POOLITAMINE SEMIKOOLONIST
    try:
        tagasi1, tagasi2 = poolitaMärgiJärgi("; ", poolitatavRida, lubatudLõikamiseAla)
        return tagasi1, tagasi2
    except:
        pass
    
    # POOLITAMINE MÕTTEKRIIPSUST
    try:
        tagasi1, tagasi2 = poolitaMärgiJärgi(" - ", poolitatavRida, lubatudLõikamiseAla)
        return tagasi1, tagasi2
    except:
        pass
    
    # POOLITAMINE KOMAGA SIDESÕNA JUUREST
    sidesõnad = [', et', ', sest', ', aga', ', vaid', ', kuid', ', ent', ', kuna', ', siis', ', kes', ', mistõttu', ', mispärast']
    for index, i in enumerate(reversed(poolitatavRida)):
        if type(i) == str:
            variant = max((item for item in sidesõnad if item in i),
                          key=lambda item: i.rfind(item),
                          default=None)
            if variant:
                tempPooleks = i.split(variant)
                tagasi1 = poolitatavRida[:len(poolitatavRida)-index-1] + [variant.join(tempPooleks[:-1])+", "]
                tagasi2 = [variant.replace(", ","")+tempPooleks[-1]] + poolitatavRida[len(poolitatavRida)-index:]
                return tagasi1, tagasi2
            
    
    # POOLITAMINE SEKUNDAARSE SIDESÕNA JUUREST
    sekundaarsed_sidesõnad = [' ja', ' ning']
    for index, i in enumerate(reversed(poolitatavRida)):
        if type(i) == str:
            variant = max((item for item in sekundaarsed_sidesõnad if item in i),
                          key=lambda item: i.rfind(item),
                          default=None)
            if variant:
                tempPooleks = i.split(variant)
                tagasi1 = poolitatavRida[:len(poolitatavRida)-index-1] + [variant.join(tempPooleks[:-1])+" "]
                tagasi2 = [variant.replace(" ","")+tempPooleks[-1]] + poolitatavRida[len(poolitatavRida)-index:]
                return tagasi1, tagasi2
    
    
    # KASUTAJALT KÜSIMINE
    järjeKord = 0
    tempNumbriteta = ""
    tempIlus = ""
    tempList = []
    for i in poolitatavRida:
        if type(i) == str:
            tempNumbriteta += i
            tempIlus += i.split()[0]
            tempList.append(i.split()[0])
            for l in i.split()[1:]:
                järjeKord += 1
                tempIlus = tempIlus + " [" + str(järjeKord) + "] " + l
                tempList.append(l)
        elif type(i) == int:
            järjeKord += 1
            tempNumbriteta += str(i)
            tempIlus = tempIlus + " [" + str(järjeKord) + "] " + str(i)
            tempList.append(i)
    
    print('\nMillisest kohast peaks poolitama järgnevat rida:')
    print('"' + tempNumbriteta + '"')
    print('Valikud:')
    print(tempIlus)
    poolitamisKoht = input("-> ")
    
    while True:
        try:
            sisend = int(poolitamisKoht)
            if sisend >= len(tempList):
                raise Exception("too-big-number")
            break
        except:
            print("Number on vigane!")
            poolitamisKoht = input("-> ")
    
    # KUI NUMBER ON TOHUTU SUUR, SIIS JÄTA ÜLDSE POOLITAMATA
    #if int(poolitamisKoht) >= len(tempList):
    #    esimenePool = poolitatavRida
    #    teinePool = [""]
    #    return esimenePool, teinePool
    
    esimenePool = []
    teinePool = []
    esimessePoolde = True
    if type(tempList[0]) == str:
        esimenePool.append("")
    if type(tempList[int(poolitamisKoht)]) == str:
        teinePool.append("")
        
    for index, i in enumerate(tempList):
        if index == int(poolitamisKoht):
            esimessePoolde = False
        if type(i) == int:
            if esimessePoolde:
                esimenePool.append(i)
                esimenePool.append("")
                continue
            else:
                teinePool.append(i)
                teinePool.append("")
                continue
        
        if esimessePoolde:
            esimenePool[-1] = esimenePool[-1] + i + " "
        else:
            teinePool[-1] = teinePool[-1] + i + " "
    
    if esimenePool[-1] == "":
        esimenePool.pop()
    elif teinePool[-1] == "":
        teinePool.pop()
    
    
    return esimenePool, teinePool


def slaididele(slaidid, viimaneRida, viimaneNumber, body):
    for i in slaidid:
        if type(i[0]) == int:
            salmi_number = True
        else:
            salmi_number = False
        if i == slaidid[-1]: # Kui praegune slaid on viimane slaid kirjakohas
            slaidilooja.lugemiseTekst(str(viimaneNumber + 1 + slaidid.index(i)), i, salmi_number, viimaneRida, body)
        else:
            slaidilooja.lugemiseTekst(str(viimaneNumber + 1 + slaidid.index(i)), i, salmi_number, 2, body) # viimaneRida=2 ehk kõik kolm rida on kasutuses
    return viimaneNumber + len(slaidid)




def arvutaVormindus(lugemine, salmiNumbrid, numbritega=True):#Ps 22,8-10 Jh 16,23-27
    import tkinter 
    from tkinter import font as tkFont
    root = tkinter.Tk()
    dpi = root.winfo_fpixels('1i')
    root.withdraw()
    text = tkFont.Font(family='Liberation Sans', size=28)
    
    slaidid = []
    slaididPraeguneRida = []
    ridaArvutamiseks = "" # Ajutine tekst rea laiuse arvutamiseks
    ainultTekst = "" # Praegune rida ainult teksti kujul
    praeguneRida = 0
    onNumber = True
    
    slaidid.append([]) # Uus slaid
    for i in lugemine:
        if onNumber:
            if numbritega:
                slaididPraeguneRida.append(salmiNumbrid[int(lugemine.index(i)/2)])
                ridaArvutamiseks += i
            onNumber = False
        else:
            onNumber = True
            slaididPraeguneRida.append("")
            
            for word in i.split():
                width = text.measure(ridaArvutamiseks + word + " ")
                cm = width * (2.54 / dpi)
                
                if cm > 24.95:
                    
                    if praeguneRida == 2:
                        
                        # POOLITA KOOS JÄRGMISE SLAIDI SÕNAGA
                        tempRidaPoolitamiseks = list(slaididPraeguneRida)
                        if type(tempRidaPoolitamiseks[-1]) == str:
                            tempRidaPoolitamiseks[-1] = tempRidaPoolitamiseks[-1] + word + " "
                        else:
                            tempRidaPoolitamiseks.append(word + " ")
                        esimenePool, teinePool = poolita(tempRidaPoolitamiseks)
                        # KUI PROGRAMM TAHAKS JÄTA JÄRGMISE SLAIDI SÕNA ESIMESSE POOLDE
                        if teinePool == [""]:
                            esimenePool, teinePool = poolita(slaididPraeguneRida)
                            if type(teinePool[-1]) == str:
                                teinePool[-1] = teinePool[-1] + word + " "
                            else:
                                teinePool.append(word + " ")
                        
                        #print("OHHOHOO")
                        #print(slaididPraeguneRida)
                        #print(esimenePool)
                        #print(teinePool)
                        
                        if type(esimenePool[0]) == str:
                            slaidid[-1][-1] += esimenePool[0]
                            slaidid[-1] = slaidid[-1] + esimenePool[1:]
                        else:
                            slaidid[-1] = slaidid[-1] + esimenePool
                        slaididPraeguneRida = teinePool
                        
                        slaidid.append([]) # Uus slaid
                        
                        ridaArvutamiseks = ""
                        for l in slaididPraeguneRida:
                            if type(l) == int: #Konverteeri number ülaindeksisse
                                tempNumber = ""
                                for k in str(l):
                                    tempNumber += ülaindeks[k]
                                ridaArvutamiseks += tempNumber
                            else:
                                ridaArvutamiseks += l
                        
                    else:
                        if type(slaididPraeguneRida[0]) == str and len(slaidid[-1]) > 0:
                            slaidid[-1][-1] += slaididPraeguneRida[0]
                            slaidid[-1] = slaidid[-1] + slaididPraeguneRida[1:]
                        else:
                            slaidid[-1] = slaidid[-1] + slaididPraeguneRida
                        slaididPraeguneRida = [word + " "]
                        ridaArvutamiseks = word + " "
                    
                    if praeguneRida == 2:
                        praeguneRida = 0
                    else:
                        praeguneRida += 1
                    continue
                
                # Mahub kenasti ritta ära, võib sõna lisada
                ridaArvutamiseks = ridaArvutamiseks + word + " "
                slaididPraeguneRida[-1] = slaididPraeguneRida[-1] + word + " "
    
    # Kõik järelejäänused võib lisada ka slaidile
    if type(slaididPraeguneRida[0]) == str and len(slaidid[-1]) > 0:
        slaidid[-1][-1] += slaididPraeguneRida[0]
        slaidid[-1] = slaidid[-1] + slaididPraeguneRida[1:]
    else:
        slaidid[-1] = slaidid[-1] + slaididPraeguneRida
    
    
    return slaidid, praeguneRida





def kontrolli(küsimus, sisend, tühiSobib=False):
    while True:
        try:
            if sisend == False:
                asukoht = input(küsimus)
            else:
                asukoht = sisend
            if tühiSobib and asukoht == "":
                return "", "", "", ""
            
            # KRISTJANI VORMINDUSE PARANDUSED
            if asukoht.endswith("."):
                asukoht = asukoht[:-1]
        
            arvutatavTulemus, salmiList, üldine_asukoht = ava(asukoht)
            if len(asukoht.split(":")) == 1:
                asukoht = asukoht.split(",")[0]+":"+",".join(asukoht.split(",")[1:])
            else:
                pass
            
            #       [kirjakoht]        [2, 3]  Lk 1:2-3  evangeelium    
            return arvutatavTulemus, salmiList, asukoht.strip(), üldine_asukoht
        except Exception as e:
            print(e)
            time.sleep(2)