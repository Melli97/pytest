#pytest serve per due cose qui: la fixture e pytest.raises.
import pytest
 
# Importo le due cose da testare. Funziona grazie a "pythonpath = src"
# nel file pytest.ini: senza quello, Python non troverebbe il modulo "bank".
from bank import ContoBancario, SaldoInsufficiente
 
 
# ------------------------------------------
# FIXTURE: prepara qualcosa che serve a più test
# ------------------------------------------
# @pytest.fixture trasforma questa funzione in una "fixture".
# Qualsiasi test che ha un parametro chiamato "conto" riceve automaticamente
# il valore restituito da questa funzione: pytest lo collega dal nome.
# Ogni test riceve un conto NUOVO (con 100 di saldo), quindi i test
# non si influenzano a vicenda: quello che fa un test non si vede negli altri.
@pytest.fixture
def conto():
    return ContoBancario(saldo=100)
 
 
# ------------------------------------------
# TEST NORMALI: verificano che qualcosa sia vero con "assert"
# ------------------------------------------
# Pytest esegue solo le funzioni il cui nome inizia con "test_".
# Il test PASSA se arriva in fondo senza errori, FALLISCE se un assert è falso.
 
def test_deposito_aumenta_saldo(conto):
    # "conto" è la fixture: un conto con 100 di saldo.
    conto.deposita(50)
    # Controllo che il saldo sia 100 + 50 = 150.
    # Se fosse diverso, il test fallirebbe e pytest mostrerebbe i due valori.
    assert conto.saldo == 150
 
 
def test_prelievo_riduce_saldo(conto):
    conto.preleva(30)
    assert conto.saldo == 70   # 100 - 30
 
 
# ------------------------------------------
# pytest.raises: verifica che venga sollevato un ERRORE
# ------------------------------------------
# A volte il comportamento corretto è proprio "dare errore".
# Qui il test PASSA solo se dentro il blocco "with" viene sollevata
# SaldoInsufficiente. Se il codice non solleva nessun errore, il test FALLISCE.
def test_prelievo_oltre_il_saldo_solleva_errore(conto):
    with pytest.raises(SaldoInsufficiente):
        conto.preleva(500)   # 500 > 100, quindi deve dare errore
 
 
# ------------------------------------------
# parametrize: lo STESSO test con VALORI DIVERSI
# ------------------------------------------
# Invece di scrivere tre test quasi identici, ne scrivo uno solo e gli passo
# una lista di valori. Pytest lo esegue una volta per ogni valore
# e lo mostra come test separato (…[0], …[-10], …[-0.01]).
# "importo" nel decoratore deve avere lo stesso nome del parametro della funzione.
@pytest.mark.parametrize("importo", [0, -10, -0.01])
def test_deposito_non_valido(conto, importo):
    # Per ognuno di questi importi, deposita deve sollevare ValueError.
    with pytest.raises(ValueError):
        conto.deposita(importo)


@pytest.mark.parametrize("importo", [0, -1, -50])
def test_prelievo_non_valido(conto, importo):
    with pytest.raises(ValueError):
        conto.preleva(importo)

