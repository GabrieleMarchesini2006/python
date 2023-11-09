prezzi_prodotti= (
    ("mela", ("lunedi",1.0),("martedi",1.0),("mercoledi",1.3),("giovedi",1.3),("venerdi",1.3),("sabato",1.3))
    ("banana", ("lunedi",1.1),("martedi",1.2),("mercoledi",1.4),("giovedi",1.4),("venerdi",1.4),("sabato",1.4))
)
scelta=0

def prezzoMedioRic(prezzi_prodotti,prodottoRicercato):
    prezzoMedio=0
    cont=0
    for prodotto, *giorno in prezzi_prodotti:
        if prodotto==prodottoRicercato:
            for giorni, costo in giorno:
                prezzoMedio+=costo
                cont+=1
                if cont>0:
                    return prezzoMedio/cont

def prezzoMedio(prezzi_prodotti):
    prezzoMedio=0
    cont=0
    for prodotto, *giorno in prezzi_prodotti:
        for giorni, costo in giorno:
            prezzoMedio+=costo
            cont+=1
            if cont>0:
                return prezzoMedio/cont

def max(prezzi_prodotti, prodottoRicercato):
    max=0
    massimo=[]
    giorni=[]
    for prodotto, *giorno in prezzi_prodotti:
        if prodotto==prodottoRicercato:
            for giorni, costo in giorno:
                if costo>max:
                    max=costo
            for giorni, costo in giorno:
                if costo==max:
                    massimo.append(costo)
                    giorni.append(giorni)
        return (massimo,giorni)

def min(prezzi_prodotti, prodottoRicercato):
    min=99999999999
    minimo=[]
    giorni=[]
    prodotto=[]
    for prodotto, *giorno in prezzi_prodotti:
        for giorni, costo in giorno:
            if costo<min:
                min=costo
        for giorni, costo in giorno:
            if costo==min:
                minimo.append(costo)
                giorni.append(giorni)
                prodotto.append(prodotto)
    return (minimo,giorni,prodotto)
            
while scelta!=9:
    scelta=int(input("1.Il prezzo medio di un dato prodotto scelto dall' utente\n2.Il prezzo medio di tutti i prodotti\n3.IL prezzo massimo di un dato prodotto scelta dall' utente\n4.Il prezzo minimo di tutti i prodotti\n9.Esci"))
    if scelta==1:
        prodottoRicercato=input("Inserisci un prodotto da cercare")
        if(prezzoMedioRic(prezzi_prodotti,prodottoRicercato)==None):
            print("Errore nell' input")
        else:
            print("Il prezzo medio di",prodottoRicercato,"è di:",prezzoMedioRic(prezzi_prodotti,prodottoRicercato))

            

prodottoRicercato=input("Inserisci il prodotto da ricercare")
giornoRicercato=input("Inserisci il giorno da cercare")