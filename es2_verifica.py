tupla_vendite = (
        (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
        (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
        (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
        (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
        (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
        (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
        (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
        (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
                )
scelta=0

def mediaGlobale(tupla_vendite):
    media=0
    cont=0
    for reparto, *altro in tupla_vendite:
        for prodotto, *metodoPagamento in altro:
            for metodo, pagamento in metodoPagamento:
                media+=pagamento
                cont+=1
    return (media/cont)

def media(tupla_vendite, categoriaRic, metPagamentoRic):
    media=0
    cont=0
    for reparto, *altro in tupla_vendite:
        if (reparto[1]==categoriaRic):
            for prodotto, *metodoPagamento in altro:
                for metodo, pagamento in metodoPagamento:
                    if (metodo==metPagamentoRic):
                        media+=pagamento
                        cont+=1
    if cont>0:
        return (media/cont)
    else:
        return -1
    
def venditaMax(tupla_vendite):
    max=0
    prodotti=[]
    for reparto, *altro in tupla_vendite:
        for prodotto, *metodoPagamento in altro:
            for metodo, pagamento in metodoPagamento:
                if (max<pagamento):
                    max=pagamento
            for metodo, pagamento in metodoPagamento:
                if (max==pagamento):
                    prodotti.append(prodotto)
    return (max, prodotto)

def venditaMin(tupla_vendite):
    min=999
    for reparto, *altro in tupla_vendite:
        if (reparto[0]=="RepartoA"):
            for prodotto, *metodoPagamento in altro:
                for metodo, pagamento in metodoPagamento:
                    if (pagamento<min):
                        min=pagamento
    return min

def venditaPer(tupla_vendite):
    tot=0
    totRepartoA=0
    totRepartoB=0
    for reparto, *altro in tupla_vendite:
        if (reparto[0]=="RepartoA"):
            for prodotto, *metodoPagamento in altro:
                for metodo, pagamento in metodoPagamento:
                    totRepartoA+=pagamento
        else:
            for prodotto, *metodoPagamento in altro:
                for metodo, pagamento in metodoPagamento:
                    totRepartoB+=pagamento
    for reparto, *altro in tupla_vendite:
        for prodotto, *metodoPagamento in altro:
            for metodo, pagamento in metodoPagamento:
                tot+=pagamento
    return (("RepartoA",(totRepartoA/tot)*100),("RepartoA",(totRepartoB/tot)*100))

while scelta!=6:
    scelta=int(input("\n1)Importo medio delle vendite\n2)Media di una tipologia di pagamento x\n3)Vendita di valore max\n4)Vendita min nel reparto A\n5)Percentuale delle vendite per reparto rispetto al totale\n6)Esci\n"))
    if (scelta==1):
        print("La media totale delle vendite è:",mediaGlobale(tupla_vendite))
    elif (scelta==2):
        categoriaRic=input("Inserisci la categoria da ricercare: ")
        metPagamentoRic=input("Inserisci il metodo di pagamento: ")
        if (media(tupla_vendite, categoriaRic, metPagamentoRic)==-1):
            print("Errore nell' input")
        else:
            print(f"La media delle vendite della categotia {categoriaRic} con la tipologia di pagamento in {metPagamentoRic} è:",media(tupla_vendite, categoriaRic, metPagamentoRic))
    elif (scelta==3):
            print("La vendita max equivale a",venditaMax(tupla_vendite)[0],"dei prodotti:",venditaMax(tupla_vendite)[1])
    elif (scelta==4):
            print("La vendita minore del reparto A è:",venditaMin(tupla_vendite))
    elif (scelta==5):
            print("La percentuale delle vendite del",venditaPer(tupla_vendite)[0][0],"è:",venditaPer(tupla_vendite)[0][1])
            print("La percentuale delle vendite del",venditaPer(tupla_vendite)[1][0],"è:",venditaPer(tupla_vendite)[1][1])

