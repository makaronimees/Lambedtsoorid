###############################################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Lämbed tsõõrid
# Teema: Kasutajale meelepärase auto soovitamine
#
#
# Autorid: Kriset Laiuste, Pilleriin Sillakivi
#
# mõningane eeskuju: isiklik kogemus, online-küsitlused 
#
# Lisakommentaar (nt kasutusjuhend): 
# GitHub'ist peaks tõmbama alla kõik siin repos olevad failid 
# ja need vajadusel lahti pakkima, et importid korralikult töötaks.
#
###############################################################################
#
# Kuidas senine koostöö sujunud? 
#   Probleeme ei ole tekkinud, mõlemad oleme piisavalt panustanud.
# Kuidas on rollid jagatud? 
#   Hetkel proovime koos algvundamendi kokku panna.
# Kui palju aega projektile on kulunud? 
#   Kokku umbes 10h koos planeerimisega.
# Millised on projektiga seoses edasised plaanid ja edasiarendused? 
#   Lisame funktsionaalsuse, mis oskab tegelikult midagi soovitada.
#   Teeme ilmselt funktsiooni, mis arvutab meie loodud kordaja, mille põhjal kasutajale sobivad autod soovitatakse
#   Lisaks võiks struktuuri parandada - praegu on rõhk sellel, et asi toimiks.
#   
###############################################################################

from easygui import *

def arvuta_kordaja(remont, kesremondib, nitroeskusaal, budget):
    kordaja=0
    #motlen minigt loogikat valja
    eelarve={"Minimaalne":5, "Keskmine":6 , "Okei":7, "Suur":11, "Lõpmatu":1000}
    ns={"Ei": 7, "Jah":3, 0:0}
    remontija={"Jah": 2, "Ei":8 , "0":12}
    if remont =="Jah":
        kordaja+=remontija[kesremondib]
    else:
        #sest tak vaja uut autot kui ei taha remontida
        kordaja+=20


    kordaja+=eelarve[budget]
    kordaja+=ns[nitroeskusaal]

    return kordaja


def callback():
    msgbox("Aitäh, et usaldasite meid oma otsustusprotsessis!")
    quit()


def mida_valjastab(kordaja, ns):
    if kordaja<5:
        autod="rondid"
        aastad="Roimad"

    elif kordaja<=10:
        autod=reliable
        aastad="2003-2012"
    elif kordaja <=20:
        autod=reliable
        aasta="2008-2020"
    else:
        autod=koik_margid
        aasta="Kõik aastad"
    if kordaja> 15:
        if ns =="Klassika":
            for el in klassika:
                autod.append(el)
        elif ns == "Drift":
            for el in driftikad:
                autod.append(el)
        elif ns== "Racing":
            for el in kiiredpillid:
                autod.append(el)
    
    tekst=""
    for rida in autod:
        tekst+=rida+ ", "
    tekst+=aasta
    return tekst


jatkub=True
while jatkub:
    koik_margid = ["Audi", "Lada","BMW","Mercedes-Benz","Volkswagen","Ford","Jaguar","Škoda","Opel", "Kia", "Mazda", "Nissan", "Subaru", "Volvo"]
    reliable=["Volkswagen", "Škoda","Opel", "Kia", "Ford", "Volvo"]
    klassika = ["Audi", "BMW", "Mercedes-Benz", "Lada" , "Volkswagen", "Ford",]
    driftikad=["BMW", "Nissan", "Mazda", "Opel Omega"]
    kiiredpillid=["Subaru", "BMW", "Ford", "Audi", "Mercedes-Benz"]
    tsipalux=["Porsche", "veel midagi"]

    nimi = enterbox("Mis on su nimi?","Tere!","",True)

    kindel_ei = multchoicebox("On sul juba teada, mida kindlasti EI soovi?","Kindlad EI-d",koik_margid,None)

    #tegeleme edaspidi vaid nende autodega, millest kasutaja huvitatud on
    if kindel_ei != None:
        for mark in kindel_ei:
            koik_margid.remove(mark)
    if len(koik_margid)== 0:
        break

    budgetnupud=["Minimaalne", "Keskmine", "Okei", "Suur", "Lõpmatu"]
    budget=buttonbox("Mis on su eelarve?", choices=budgetnupud)
    if budget == "Suur":
        koik_margid+=tsipalux
    if budget == "Minimaalne":
        pass
    else:
        nitroseksuaal=buttonbox("Kas oled nitroseksuaal?", choices=["Jah", "Ei"])
        if nitroseksuaal=="Jah":
            missugunens=buttonbox("Missugune täpsemalt?", choices=["Klassika", "Drift", "Racing"])
            if missugunens == "Klassika":
                valikute_nimekiri=klassika
            elif missugunens == "Drift":
                valikute_nimekiri=driftikad
            else:
                valikute_nimekiri=kiiredpillid
    
    remondivalmis=buttonbox("Kas oled valmis remondiks?", choices=["Jah", "Ei"])
    if remondivalmis=="Ei":
        kasise="0"
        break
    else:
        kasise=buttonbox("Kas kavatsed ise teha?", choices=["Jah","Ei"])
        break

kordaja=arvuta_kordaja(remondivalmis, kasise, nitroseksuaal, budget)
valjastatav=mida_valjastab(kordaja, nitroseksuaal)
    #motlen veel mingid napunaited valja(veic ironic, kui mu enda auto isegi ülevaatuselt läbi ei saanud...)
soovitused="Meie isiklikud soovitused on vältida autosid, mida müüvad teiseringi diilerid. Pigem osta käest kätte või siis otse esindusest. Samuti tasub auto ajalugu vaadata Transpordiameti kodulehelt numbrimärgi taustakontrolli alt ning samuti sealt samast vaadata ka kindlustusjuhtumite ajalugu. Tasuks ka tähelepanu pöörata päritoluriigile, isiklikult ei ostaks kunagi autot, mis on tulnud Lätist, Leedust või Poolast, sest seal ehitatakse 'Frankensteine', ehk mitme auto juppidest kokku pandud autosid. Need autod pole enam nii struktuurselt vastupidavad ning neil võivad olla nähtamatud ning ootamatud vead."
tekst=nimi+", "+ "peaksid vaatama järgnevaud autosid: " + valjastatav + "\n"+ "\n" + soovitused
popup=msgbox(tekst)
    


