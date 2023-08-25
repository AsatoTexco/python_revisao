from Banco import *

usuarios = {
    "arthur@gmail.com":{
                        "senha":"arthur123",
                        "nome":"Arthur",
                        "saldo":1000
                        },

    "luiz@gmail.com":{
                        "senha":"luiz23",
                        "nome":"Luiz",
                        "saldo":5000
                        },

    "frantz@gmail.com":{
                        "senha":"frantz123",
                        "nome":"Frantz",
                        "saldo":8000
                        },

    "enilda@gmail.com":{
                        "senha":"enilda123",
                        "nome":"Enilda",
                        "saldo":12000
                        }
}


while True:
    while True:
        try:
            op = int(input("1 - Logar\n0 - Sair\n"))
            if(op == 1 or op == 0):
                break
            else:
                print("Insira um valor valido!")
                continue
        except:
            print("digite um valor valido")
            continue
    if(op == 0):
        print("Até mais :)")
        break
    elif(op == 1):
        email = input("Email: ")
        if(email in usuarios): 
            senha = input("Senha: ")
            if(senha == usuarios[email]["senha"]):
                print("Logado com sucesso!")      
                banco = Banco(usuarios[email]['nome'],usuarios[email]['saldo'])
                banco.msgHello()
            else:
                print("Senha incorreta, Tente novamente")
                continue
            while True:
                while True:
                    try:
                        op = int(input("1 - Exibir Saldo\n2 - Sacar\n3 - Depositar\n4 - Extrato\n0 - Sair da conta\n"))
                        break
                    except:
                        print("digite um valor valido")
                        continue
                match op:
                    case 0:
                        break
                    case 1:
                         print("Seu saldo atual é de: R$", banco.getSaldo())
                    case 2:
                        while True:
                            try:
                                valor = int(input("Insira o valor que deseja sacar: "))
                                if(valor > banco.getSaldo()):
                                    print(f"Insira um valor menor que o seu saldo de R$ {banco.getSaldo()}")
                                    continue
                                else:
                                
                                    banco.saque(valor)
                                    print(f"Saque efetuado com sucesso!\nSaldo Atual: R$ {banco.getSaldo()}")

                                    break
                            except:
                                print("digite um valor valido")
                                continue
                    case 3:
                        while True:
                            try:
                                valor = int(input("Insira o valor que deseja Depositar: "))
                                banco.deposito(valor)
                                print(f"Depósito efetuado com sucesso!\nSaldo atual: {banco.getSaldo()}") 
                                break
                                
                            except:
                                print("digite um valor valido")
                                continue
                    case 4:
                        banco.getExtrato()
        else:
            print("Email Inválido")
            continue
  
        
    
# banco = Banco(nome,saldo)


     

