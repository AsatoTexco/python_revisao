class Banco:
    def __init__(self,nome,saldo):
        self.saldo = saldo
        self.nome = nome
        self.extrato = []
    
    def msgHello(self):
        print("=====  Bem-Vindo Sr. "+self.nome+"  =====")
 

    def getSaldo(self):
        return self.saldo

    def saque(self,valor):
        if(valor > self.saldo):
            return False
        else: 
            self.saldo = self.saldo - valor
            valorstr = str(valor)
            self.extrato.append("- R$"+valorstr)
            print(2)
            return True
    
    def deposito(self,valor):
        self.saldo = self.saldo + valor
        valorstr = str(valor)
        self.extrato.append("+ R$"+valorstr)
        return self.saldo
    
    def getExtrato(self):
        # print(self.extrato)
        print("=== Extrato ===")
        for i in self.extrato:
            print(i)