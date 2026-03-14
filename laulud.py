import time
import slaidigeneraatorid as slaidilooja


import sys
import os
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



def extract(lauluNumber):
    with open(resource_path("laulud/" + lauluNumber + ".txt"), encoding="utf-8") as f:
        tekst = f.readlines()
        tekst = [t.replace("ő", "õ").replace("Ő", "Õ") for t in tekst]
        
    pealkiri = tekst[0].replace(lauluNumber, "")[2:].replace("\n", "").replace("\n", "")
    tekst = tekst[2:]
    salmid = [[]]
    for i in tekst:
        if i=="\n":
            salmid.append([])
            continue
        salmid[-1].append(i.replace("\n", ""))
    if salmid[-1] == []:
        salmid.pop()
    return pealkiri, salmid

def küsiKasutajalt(number, sisend):
    
    while True:
        try:
            if sisend == False:
                laul = input(number + " (nt: 291 1-2): ").split()
            else:
                laul = sisend.split()
            
            # JOELI LAULUDE VORMINDUSE PARANDUSED
            if laul[0] == ")":
                laul.remove(")")
            if laul[0] == "+":
                laul.remove("+")
            if laul[-1].endswith(";"):
                laul[-1] = laul[-1][:-1]
            
            # KRISTJANI LAULUDE VORMINDUSE PARANDUSED
            if len(laul) == 1:
                laul = laul[0].split("(")
                laul[-1] = laul[-1].replace(")", "")
                laul[-1] = laul[-1].replace(",", "")
                laul[-1] = laul[-1].replace(".", "")
                laul[0] = laul[0].replace("+", "")
            
            # EBATÕENÄOLISTE LAULUDE KONTROLL
            if laul[0] in ["419", "421", "423", "474", "475", "477", "478"]:
                print('Kas sa mõtlesid tõesti laulu "' + laul[0] + '"?')
                laul = input("Palun sisesta soovitud laulu number ja salmid uuesti: ").split()
            
            if laul[0][-1] != "A" or laul[0][-1] != "B":
                if laul[0] not in ['32', '450']:
                    try:
                        pealkiri, salmid = extract(laul[0])
                    except:
                        pealkiri, salmid = extract(laul[0]+"A")
                else:
                    raise Exception("no-song")
            else:
                pealkiri, salmid = extract(laul[0])
            if len(laul) == 1:
                print("Vale vorming!")
                time.sleep(2)
                continue
            
            if len(laul[1].split("-")) == 1:
                if len(salmid) < int(laul[1]):
                    print("Salmi number " + laul[1] + " ei eksisteeri!")
                    time.sleep(2)
                    continue
            else:
                if len(salmid) < int(laul[1].split("-")[-1]):
                    print("Salmi number " + laul[1].split("-")[-1] + " ei eksisteeri!")
                    time.sleep(2)
                    continue
            
            break
        except:
            print('Laulu "' + laul[0] + '" ei eksisteeri')
            time.sleep(2)
    
    if len(laul[1].split("-")) == 1:
        pealkiri = laul[0] + ". " + pealkiri.upper()
        return pealkiri, [laul[1], salmid[int(laul[1])-1]], laul[1]
    
    salmideNumbrid = []
    for i in range(int(laul[1].split("-")[1]) - int(laul[1].split("-")[0]) + 1):
        salmideNumbrid.append(i+int(laul[1].split("-")[0]))
    salmidearv = laul[1].replace("-", " – ")
    
    tulemusSlaidid = []
    for i in range(salmideNumbrid[-1]-salmideNumbrid[0]+1):
        tulemusSlaidid.append(str(i+salmideNumbrid[0]))
        tulemusSlaidid.append(salmid[i+salmideNumbrid[0]-1])
    
    pealkiri = laul[0] + ". " + pealkiri.upper()
    
    return pealkiri, tulemusSlaidid, salmidearv

def arvutaTekstiLaius(tekst, font_size):
    import tkinter 
    from tkinter import font as tkFont
    root = tkinter.Tk()
    dpi = root.winfo_fpixels('1i')
    root.withdraw()
    _text = tkFont.Font(family='Liberation Sans', size=font_size)
    width = _text.measure(tekst)
    cm = width * (2.54 / dpi)
    return cm

def genereeri(pealkiri, tulemusSlaidid, viimaneNumber, body, document):
    font_size = 36
    if arvutaTekstiLaius(pealkiri, font_size) > 24.5:
        while True:
            font_size -= 1
            if arvutaTekstiLaius(pealkiri, font_size) < 24.5:
                break
    slaidilooja.uusPealkiri(str(viimaneNumber+1), pealkiri, str(font_size)+"pt", body, document)
    for i in range(int(len(tulemusSlaidid)/2)):
        slaidilooja.uusSalm(str(viimaneNumber+2+i), tulemusSlaidid[i*2+1], pealkiri, "Salm "+tulemusSlaidid[i*2], body)
    
    return int(len(tulemusSlaidid)/2+viimaneNumber+1)
