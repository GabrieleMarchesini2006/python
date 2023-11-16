pluviometriaMensile=(
    ("milano",[("gennaio",2),("febbraio",1),("maggio",4),("luglio",3)]),
    ("torino",[("gennaio",4),("febbraio",2),("maggio",1),("luglio",6)]),
    ("catanzaro",[("gennaio",0.8),("febbraio",2),("maggio",3),("luglio","N/D")]),
)

def media(pluviometriaMensile, cittaRicercata):
    cont=0
    media=0
    max=0
    min=999
    meseMax=[]
    meseMin=[]
    for citta, *lista in pluviometriaMensile:
        if cittaRicercata==citta:
            for l in lista:
                for p in l:
                    if (p[1]!="N/D"):
                        media+=p[1]
                        cont+=1
                        if (max<p[1]):
                            max=p[1]
                        if(min>p[1]):
                            min=p[1]
                for p in l:
                    if (p[1]!="N/D"):
                        if (p[1]==max):
                            meseMax.append(p[0])
                        if (p[1]==min):
                            meseMin.append(p[0])
    if cont>0:
        return ((media/cont),(max,meseMax),(min,meseMin))
    else:
        return -1

cittaRicercata=input("Inserisci una citta da ricercare: ")
if (media(pluviometriaMensile, cittaRicercata)==-1):
    print("Errore nell' input")
else:
    print(f"La media delle precipitazioni di {cittaRicercata} è:",media(pluviometriaMensile, cittaRicercata)[0])
    print(f"Il valore max di {cittaRicercata} è",media(pluviometriaMensile, cittaRicercata)[1][0],"nei mesi:",media(pluviometriaMensile, cittaRicercata)[1][1])
    print(f"Il valore min di {cittaRicercata} è",media(pluviometriaMensile, cittaRicercata)[2][0],"nei mesi:",media(pluviometriaMensile, cittaRicercata)[2][1])