
class Produto:
    todos_produtos = {}
    todos_produtos = {"Macarrao":{"preco":10,
                                  "quantidade":15.45,
                                  },
                       "Beterraba":{"preco":2,
                                  "quantidade":19.89,
                                  },
                        "Paçoca":{"preco":2.5,
                                  "quantidade":75.89,
                                  },
                        "Arroz 5kg":{"preco":17.99,
                                  "quantidade":125,
                                  },
                        "Massa de Pastel 300g":{"preco":6.99,
                                  "quantidade":20,
                                  },
                        "Carne kg":{"preco":28.99,
                                  "quantidade":500,
                                  },
                        "Pizza 400g":{"preco":19.89,
                                  "quantidade":337 ,
                                  },}
 
    def __init__(self,nome,qnt,preco) -> None:
        self.nome = nome
        self.qnt = qnt
        self.preco = preco
    
    def cadastrar(self):
        if(self.nome in Produto.todos_produtos):
            Produto.todos_produtos[self.nome]['quantidade'] += self.qnt
            Produto.todos_produtos[self.nome]['preco'] = self.preco
        else:
            Produto.todos_produtos[self.nome] = {"preco":self.preco,
                                                 "quantidade":self.qnt}
        return True
    
     
        