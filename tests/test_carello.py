import pytest
 
# Importo la classe da testare (funziona grazie a "pythonpath = src" in pytest.ini)
from carrello import Carrello
 
 
# ------------------------------------------
# FIXTURE: un carrello vuoto e nuovo per ogni test
# ------------------------------------------
# Ogni test che ha un parametro chiamato "carrello" riceve un oggetto Carrello()
# appena creato. Così un test non "sporca" il carrello di un altro.
@pytest.fixture
def carrello():
    return Carrello()
 
 
# ------------------------------------------
# TEST SEMPLICE: stato iniziale
# ------------------------------------------
def test_carrello_vuoto_ha_totale_zero(carrello):
    # Un carrello appena creato non ha articoli, quindi il totale deve essere 0.
    # sum() di una lista vuota dà 0: è un caso limite da verificare sempre.
    assert carrello.totale() == 0
 
 
# ------------------------------------------
# PARAMETRIZE con più parametri
# ------------------------------------------
# I nomi sono dentro UNA stringa, separati da virgola: "prezzo, quantita, atteso".
# Ogni tupla della lista è un caso di test, con i valori NELLO STESSO ORDINE dei nomi.
# Pytest esegue il test 3 volte, e ogni volta mette i valori nei parametri
# prezzo, quantita e atteso della funzione.
@pytest.mark.parametrize("prezzo, quantita, atteso", [
    (10, 1, 10),     # 10 x 1 = 10
    (10, 3, 30),     # 10 x 3 = 30
    (2.5, 4, 10),    # 2.5 x 4 = 10
])
def test_totale_con_un_articolo(carrello, prezzo, quantita, atteso):
    carrello.aggiungi("penna", prezzo, quantita)
    assert carrello.totale() == atteso