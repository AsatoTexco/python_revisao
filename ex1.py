# 1- O usuário deverá escolher uma opção de acordo com o último número da placa do carro e mostre uma mensagem dizendo em que dia da semana não poderá circular. 

# 1- 2 “Não Circular2ª Feira” 

# 3 - 4 “Não Circular 3ª Feira” 

# 5 - 6 “Não Circular 4ª Feira” 

# 7- 8 “Não Circular 5ª Feira” 

# 9 - 0 “Não Circular 6ª Feira” 

def validar(placa):
    
    num =  placa[-1]  
    
    if(num == "1" or num == "2"):
        dia = 'Segunda'
    elif(num == "3" or num == "4"):
        dia = 'Terça'
    elif(num == "5" or num == "6"):
        dia = 'Quarta'
    elif(num == "7" or num == "8"):
        dia = "Quinta"
    elif(num == "9" or num == "0" ):
        dia = "Sexta"

    return "Não pode circular na "+dia+" feira"


while True:
    while True:
        try:
            op = int(input("1 - Validar placa\n0 - sair"))
            break
        except:
            print("digite um valor valido")
            continue

    if(op == 0):
        break
    elif(op == 1):
        placa = input("Insira sua placa: ")
        
        print(validar(placa))

