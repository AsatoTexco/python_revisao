import time
from Produto import *
from Cliente import *
produtos_atual = []
produtos_escolhidos = {}
print("\n\n\n\n=======  Supermercado =======")
while True:
    count = 1
    total = 0
    while True:
        try:
            op = int(input("\n\n1 - Cadastrar Produto\n2 - Vender\n3 - Visualizar Produtos\n0 - Sair\n"))
            break
        except:
            print("Insira um valor válido")
            continue
    match op:
        case 0:
            print("Até mais!")
            break
        case 1:
            print("Cadastrar Produto")
            while True:
                try:
                    nome = input("Nome: ")
                    qnt =  int(input("Quantidade: "))
                    preco = float(input("Preço: "))
                    break
                except:
                    print("\nInsira um valor válido")
                    continue
            produto = Produto(nome,qnt,preco)
            produto.cadastrar()
            print("Sucesso!")
        case 2:
            total = 0
            print("Cadastrar Cliente")
            email = input("Email: ")
            nome = input("Nome: ")
            cep = input("cep: ")
            cpf = input("cpf: ")
            endereco = input("endereco: ")
            cliente = Cliente(nome,cep,cpf,endereco)
            cliente.cadastrar(email=email)
            produtos_escolhidos = {}
            produtos_atual = []
            while True:
                count = 1
                for i in Produto.todos_produtos:
                    print(f"{count} - {i}  {Produto.todos_produtos[i]['quantidade']} restantes R$ {Produto.todos_produtos[i]['preco']}")
                    if(i not in produtos_atual):
                        produtos_atual.append(i)
                    count += 1
                while True:
                    try:
                        op = int(input("Escolha os produtos que deseja comprar(0 - sair)\n"))
                        break
                    except:
                        print("Insira um valor válido")
                        continue
                match op:
                    case 0:
                        break
                    case _:
                        if(op > 0 and op <= len(produtos_atual) and Produto.todos_produtos[produtos_atual[op - 1]]['quantidade'] > 0):
                            escolhido = produtos_atual[op - 1]
                            while True:
                                    while True:
                                        try:
                                            qnt = int(input((f"quantidade desejada de {escolhido}: ")))
                                            break
                                        except:
                                            print("Insira um valor válido")
                                            continue
                                    if(qnt <= Produto.todos_produtos[escolhido]['quantidade']):
                                        qnt_escolhido = qnt
                                        qnt_atualizada = Produto.todos_produtos[escolhido]['quantidade'] - qnt_escolhido
                                        Produto.todos_produtos[escolhido]['quantidade'] = qnt_atualizada
                                        preco_escolhido = Produto.todos_produtos[escolhido]['preco']
                                        total += preco_escolhido * qnt_escolhido 
                                        # quebrado aqui 
                                        if(escolhido in produtos_escolhidos):
                                            produtos_escolhidos[escolhido]['qnt_escolhida'] += qnt
                                        else:
                                            produtos_escolhidos[escolhido] = {'qnt_escolhida':qnt}
                                        print("===== Sacola =====")
                                        total = 0
                                        for i in produtos_escolhidos:
                                            valor_atual = Produto.todos_produtos[i]['preco'] * produtos_escolhidos[i]['qnt_escolhida']
                                            print(f"{i} R$ {valor_atual} x{produtos_escolhidos[i]['qnt_escolhida']} ")
                                            total += valor_atual
                                        print("subtotal: R$",total)
                                        break
                                    else:
                                        print("Não há produtos suficientes")
                                        continue
                            while True:
                                try:
                                    op = int(input("\n\nDeseja adicionar mais itens?(1 - Sim/0 - Não)"))
                                    break
                                except:
                                    print("Insira um valor válido")
                                    continue
                            match op:
                                case 0:
                                    print(f"\n\nTotal: R$ {total}")
                                    while True:
                                        try:

                                            metodo_pagamento = int(input("Selecione a forma de pagamento\n1 - Pix\n2 - Dinheiro\n0 - cancelar compra\n"))
                                            break
                                        except:
                                            print("Insira um valor válido")
                                            continue
                                    match metodo_pagamento:
                                        case 0:
                                            produtos_escolhidos = {}
                                            qnt_atualizada = Produto.todos_produtos[escolhido]['quantidade'] + qnt_escolhido
                                            Produto.todos_produtos[escolhido]['quantidade'] = qnt_atualizada
                                        case 1:
                                            # pix 
                                            print("\n\nEnvie o pix para a seguinte chave\n67992743524")
                                            time.sleep(3)
                                            print("\n\nCompra validada com Sucesso!\nVolte sempre!!!\n\n")
                                        case 2:
                                            while True:
                                                while True:
                                                    try:
                                                        dinheiro_pagamento = float(input("Insira o valor em R$: "))
                                                        break
                                                    except:
                                                        print("Insira um valor válido")
                                                        continue
                                                if(dinheiro_pagamento == total):
                                                    print("\n\nObrigado pela preferência, volte sempre!")
                                                    break
                                                elif(dinheiro_pagamento > total):
                                                    troco_pagamento = dinheiro_pagamento - total
                                                    print(f"Troco: R$ {troco_pagamento}\n\nObrigado pela preferência, volte sempre!")
                                                    break
                                                else:
                                                    print("Insira valor suficiente")
                                                    continue
                                    break
                                case 1:
                                    
                                    continue
                        else:
                             
                            print("Insira um número valido")
                            continue
        case 3:
            count = 1
            print("\n\n=====  Produtos  =====")
            for i in Produto.todos_produtos:
                print(f"{count} - {i}  {Produto.todos_produtos[i]['quantidade']} restantes R$ {Produto.todos_produtos[i]['preco']}")
                if(i not in produtos_atual):
                    produtos_atual.append(i)
                count += 1