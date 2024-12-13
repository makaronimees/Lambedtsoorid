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
    #motlen mingit loogikat valja
    eelarve={"Minimaalne":5, "Keskmine":6 , "Okei":7, "Suur":11, "Lõpmatu":1000}
    ns={"Ei": 7, "Jah":-3, 0:0}
    remontija={"Jah": 2, "Ei":8 , "0":12, 0:0}
    if remont =="Jah":
        kordaja+=remontija[kesremondib]
    else:
        #sest tal vaja uut autot kui ei taha remontida
        kordaja+=20

    kordaja+=eelarve[budget]
    kordaja+=ns[nitroeskusaal]

    return kordaja

def callback():
    msgbox("Aitäh, et usaldasite meid oma otsustusprotsessis!")
    quit()


def mida_valjastab(kordaja, ns):
    if kordaja<8:
        autod="rondid"
        aastad="Roimad"

    elif kordaja<=14:
        autod=reliable
        aastad="2003-2012"
    elif kordaja <=25:
        autod=reliable
        aastad="2008-2020"
    else:
        autod=koik_margid
        aastad="Kõik aastad"
    if kordaja> 25:
        aastad="1997-2005"
        if ns =="Klassika":
            aastad="1980-1990"
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
    tekst+=aastad
    return tekst

def x_kontroll(nimi):
    if nimi == None:
        quit()

def margi_eemaldus(mark,koik):
    for nimekiri in koik:
        if mark in nimekiri:
            nimekiri.remove(mark)

remondivalmis=0
kasise=0
nitroseksuaal=0
budget=0
koik_margid = ["Audi", "Lada","BMW","Mercedes-Benz","Volkswagen","Ford","Jaguar","Škoda","Opel", "Kia", "Mazda", "Nissan", "Subaru", "Volvo", "Fiat", "Dodge", "Ram"]
reliable=["Volkswagen", "Škoda","Opel", "Kia", "Ford", "Volvo", "Fiat"]
klassika = ["Audi", "BMW", "Mercedes-Benz", "Lada" , "Volkswagen", "Ford"]
driftikad=["BMW", "Nissan", "Mazda", "Opel Omega"]
kiiredpillid=["Subaru", "BMW", "Ford", "Audi", "Mercedes-Benz"]
tsipalux=["Porsche", "Dodge", "Ram", "Jaguar"]

koik_valikud = [koik_margid, reliable, klassika, driftikad, kiiredpillid, tsipalux]

nimi = enterbox("Mis on su nimi?","Tere!","",True)
x_kontroll(nimi)

kindel_ei = multchoicebox("On sul juba teada, mida kindlasti EI soovi?","Kindlad EI-d",koik_margid,None)

#tegeleme edaspidi vaid nende autodega, millest kasutaja huvitatud on

try:
    for mark in kindel_ei:
        margi_eemaldus(mark,koik_valikud)

except:
    pass

budgetnupud=["Minimaalne", "Keskmine", "Okei", "Suur", "Lõpmatu"]
budget=buttonbox("Mis on su eelarve?", choices=budgetnupud)
if budget == "Suur":
    koik_margid+=tsipalux
elif budget == "Minimaalne":
    headaega = "Kahjuks ei ole võimalik tänapäeval leida minimaalse eelarvega autot, mida on mõtet osta. Kui muudad oma meelt, võid meid uuesti proovida!"
    msgbox(headaega)
    quit()
else:
    nitroseksuaal=buttonbox("Kas oled nitroseksuaal?", choices=["Jah", "Ei"])
    x_kontroll(nitroseksuaal)
    if nitroseksuaal=="Jah":
        missugunens=buttonbox("Missugune täpsemalt?", choices=["Klassika", "Drift", "Racing"])
        if missugunens == "Klassika":
            valikute_nimekiri=klassika
        elif missugunens == "Drift":
            valikute_nimekiri=driftikad
        else:
            valikute_nimekiri=kiiredpillid

remondivalmis=buttonbox("Kas oled valmis remondiks?", choices=["Jah", "Ei"])
x_kontroll(remondivalmis)
if remondivalmis=="Ei":
    kasise="0"

else:
    kasise=buttonbox("Kas kavatsed ise teha?", choices=["Jah","Ei"])
    x_kontroll(kasise)

kordaja=arvuta_kordaja(remondivalmis, kasise, nitroseksuaal, budget)
valjastatav=mida_valjastab(kordaja, nitroseksuaal)
#motlen veel mingid napunaited valja(veic ironic, kui mu enda auto isegi ülevaatuselt läbi ei saanud...)
soovitused="Meie isiklikud soovitused on vältida autosid, mida müüvad teiseringi diilerid. Pigem osta käest kätte või siis otse esindusest. Samuti tasub auto ajalugu vaadata Transpordiameti kodulehelt numbrimärgi taustakontrolli alt ning samuti sealt samast vaadata ka kindlustusjuhtumite ajalugu. Tasuks ka tähelepanu pöörata päritoluriigile, isiklikult ei ostaks kunagi autot, mis on tulnud Lätist, Leedust või Poolast, sest seal ehitatakse 'Frankensteine', ehk mitme auto juppidest kokku pandud autosid. Need autod pole enam nii struktuurselt vastupidavad ning neil võivad olla nähtamatud ning ootamatud vead."
tekst=nimi+", "+ "peaksid vaatama järgnevaid autosid: " + valjastatav + "\n"+ "\n" + soovitused
popup=msgbox(tekst)



