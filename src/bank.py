class SaldoInsufficiente(Exception):
    pass

class ContoBancario:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def deposita(self, importo):
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo")
        self.saldo += importo

    def preleva(self, importo):
        if importo > self.saldo:
            raise SaldoInsufficiente("Saldo insufficiente")
        self.saldo -= importo