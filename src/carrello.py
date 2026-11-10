class Carrello:
    def __init__(self):
        # Ogni articolo è un dizionario: nome, prezzo unitario, quantità
        self.articoli = []

    def aggiungi(self, nome, prezzo, quantita=1):
        if prezzo < 0:
            raise ValueError("Il prezzo non può essere negativo")
        if quantita <= 0:
            raise ValueError("La quantità deve essere positiva")
        self.articoli.append({"nome": nome, "prezzo": prezzo, "quantita": quantita})

    def totale(self):
        return sum(a["prezzo"] * a["quantita"] for a in self.articoli)

    def totale_scontato(self, percentuale):
        # Sconto in percentuale, da 0 a 100
        if percentuale < 0 or percentuale > 100:
            raise ValueError("Sconto non valido")
        return self.totale() * (1 - percentuale / 100)

    def rimuovi(self, nome):
        # Rimuove tutti gli articoli con quel nome
        self.articoli = [a for a in self.articoli if a["nome"] != nome]