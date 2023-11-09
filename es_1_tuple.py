prezzi_prodotti= (
    ("mele","lunedi",1.0),
    ("mele","martedi",1.2),
    ("mele","mercoledi",1.1),
    ("banana","lunedi",0.8),
    ("banana","martedi",0.9),
    ("banana","mercoledi",0.7),
)

def prezzoMedio(prezzi_prodotti,prodottoRicercato,giornoRicercato):
    prezzoMedio=0
    cont=0
    for prodotto, giorno, prezzo in prezzi_prodotti:
        if prodottoRicercato==prodotto and giornoRicercato==giorno:
            cont+=1
            prezzoMedio+=prezzo
        if cont>0:
            return prezzoMedio/cont

prodottoRicercato=input("Inserisci il prodotto da ricercare")
giornoRicercato=input("Inserisci il giorno da cercare")

if(prezzoMedio(prezzi_prodotti,prodottoRicercato,giornoRicercato)==None):
    print("Errore nell' input")
else:
    print("Il prezzo medio di",prodottoRicercato,"di",giornoRicercato,"è di:",prezzoMedio(prezzi_prodotti,prodottoRicercato,giornoRicercato))
