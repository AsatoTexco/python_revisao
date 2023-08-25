class Cliente:
    
    todos_clientes = {}
    # todos_clientes = {"arthur@gmail.com":{"nome":"arthur",
    #                                       "cep":"79220100",
    #                                       "cpf":"87228551290",
    #                                       "endereco":"Rua da esquerda, 255",
    #                                       "produtos_comprados": {"Macarrão":{"preco":2.99,
    #                                                                          "qnt_comprada":25}
    #                                                             }}}
                               

    def __init__(self,nome,cep,cpf,endereco):

        self.nome = nome
        self.cep = cep
        self.cpf = cpf
        self.endereco = endereco

    def cadastrar(self,email):

        if(email in Cliente.todos_clientes):
            return False
        else:
            Cliente.todos_clientes[email] = {
                "nome":self.nome,
                "cep":self.cep,
                "cpf":self.cpf,
                "endereco":self.endereco,
                "produtos_comprados":{}
            }
            return True
        
    def pagar(self):
        print("pagar")

        