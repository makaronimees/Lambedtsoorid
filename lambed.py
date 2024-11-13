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
#   Selleks peame ilmselt lisama funktsioone ning rohkem andmeid ja kordajaid.
#   Lisaks võiks struktuuri parandada - praegu on rõhk sellel, et asi toimiks.
#   Teeme ilmselt funktsiooni, mis arvutab meie loodud kordaja, mille põhjal kasutajale sobivad autod soovitatakse
###############################################################################

from easygui import *


jatkub=True
while jatkub:
    koik_margid = ["Audi", "Lada","BMW","Mercedes-Benz","Volkswagen","Ford","Jaguar","Škoda","Opel", "Kia"]
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
        #hiljem kõik jatkub false asendada mingi head aega sõnumiga?
        jatkub=False

    #nendele, mis kasutajale meeldivad, lisame hiljem kordaja? et suurema tõenäosusega neid soovitada
    pigem_jah = multchoicebox("Äkki on ka teada, milliseid marke eelistad?","Pigem need",koik_margid)

    budgetnupud=["Minimaalne", "Keskmine", "Okei", "Suur", "Lõpmatu"]
    budget=buttonbox("Mis on su eelarve?", choices=budgetnupud)
    if budget == "Suur":
        valikudlisa=tsipalux
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
        jatkub=False
    kasise=buttonbox("Kas kavatsed ise teha?", choices=["Jah","Ei"])
    jatkub=False


tekst="Peaksid vaatama järgnevaud autosid: "
#motlen veel mingid napunaited valja(veic ironic, kui mu enda auto isegi ülevaatuselt läbi ei saanud...)
soovitused="Meie isiklikud soovitused on.."
popup=msgbox(tekst)