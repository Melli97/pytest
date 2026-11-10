import pytest
from bank import ContoBancario, SaldoInsufficiente

@pytest.fixture
def conto():
    return ContoBancario(saldo=100)

def test_deposito_aumenta_saldo(conto):
    conto.deposita(50)
    assert conto.saldo == 150

def test_prelievo_riduce_saldo(conto):
    conto.preleva(30)
    assert conto.saldo == 70

def test_prelievo_oltre_il_saldo_solleva_errore(conto):
    with pytest.raises(SaldoInsufficiente):
        conto.preleva(500)

@pytest.mark.parametrize("importo", [0, -10, -0.01])
def test_deposito_non_valido(conto, importo):
    with pytest.raises(ValueError):
        conto.deposita(importo)