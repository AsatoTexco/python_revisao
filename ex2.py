cardapio = "1-Bife\n2-Lasanha\n3-pizza\n4-Espaguete\n5-sorvete"
alimentos = ("Bife","Lasanha","Pizza","Espaguente","Sorvete")
preco = (20,10,31,51,22)

print(cardapio)
while True:
        try:
            prato = int(input("Escolha o numero do seu prato\n"))
            if(prato > 0 and prato <= len(alimentos)):
                break
            else:
                print("digite um valor valido")
                continue
        except:
            print("digite um valor valido")
            continue

while True:
        try:
            gorjeta = int(input("Deseja pagar a gorjeta?(1-Sim/0-nao)\n"))
            if(gorjeta == 1 or gorjeta == 0):
                 break
            else:
                 continue
        except:
            print("digite um valor valido")
            continue

if(gorjeta == 1):
     valor_prato = preco[prato-1] + preco[prato-1] * 0.10
else:
     valor_prato = preco[prato-1]
print(valor_prato)
