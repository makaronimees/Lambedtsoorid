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

def arvuta_kordaja(remont, kesremondib, nitroeskusaal, lemmik, budget):
    kordaja=0
    #motlen minigt loogikat valja
    eelarve={"Minimaalne":1, "Keskmine":2 , "Okei":3, "Suur":8, "Lõpmatu":1000}
    ns={"Ei": 0, "Jah":5}
    remontija={"Jah": 2, "Ei":8 }
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


jatkub=True
while jatkub:
    koik_margid = ["Audi", "Lada","BMW","Mercedes-Benz","Volkswagen","Ford","Jaguar","Škoda","Opel", "Kia"]
    klassika = ["Audi", "BMW", "Mercedes-Benz", "Lada" , "Volkswagen", "Ford",]
    driftikad=["BMW", "Nissan", "Mazda", "Opel Omega"]
    kiiredpillid=["Subaru", "BMW", "Ford", "Audi", "Mercedes-Benz"]
    tsipalux=["Porsche", "veel midagi"]

    nimi = enterbox("Mis on su nimi?","Tere!","",True)

    kindel_ei = multchoicebox("On sul juba teada, mida kindlasti EI soovi?","Kindlad EI-d",koik_margid,None,cancel_choice=callback())

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
        print(koik_margid)
    #huvitav kas see on nilbe sõnapruuk?
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
        break
    kasise=buttonbox("Kas kavatsed ise teha?", choices=["Jah","Ei"])


    tekst="Peaksid vaatama järgnevaud autosid: "
    #motlen veel mingid napunaited valja(veic ironic, kui mu enda auto isegi ülevaatuselt läbi ei saanud...)
    soovitused="Meie isiklikud soovitused on.."
    popup=msgbox(tekst)

