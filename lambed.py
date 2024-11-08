################################################
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
##################################################

from easygui import *

koik_margid = ["Audi", "Lada","BMW","Mercedes-Benz","Volkswagen","Ford","Jaguar","Škoda","Opel"]
klassika = ["Audi", "BMW", "Mercedes-Benz", "Lada" , "Volkswagen", "Ford",]

nimi = enterbox("Mis on su nimi?","Tere!","",True)
kindel_ei = multchoicebox("On sul juba teada, mida kindlasti EI soovi?","Kindlad EI-d",koik_margid,None)

#tegeleme edaspidi vaid nende autodega, millest kasutaja huvitatud on
if kindel_ei != None:
    for mark in kindel_ei:
        koik_margid.remove(mark)

#nendele, mis kasutajale meeldivad, lisame hiljem kordaja?
pigem_jah = multchoicebox("Äkki on ka teada, milliseid marke eelistad?","Pigem need",koik_margid)
