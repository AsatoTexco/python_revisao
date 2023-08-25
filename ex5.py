produtos = ("Sabonete","Pasta de dente","creme de alho","tomate")
preco = (20,10,25,5)
escolhidos = []
total = 0

print("===== BEM-VINDO AO SUPERMERCADO =====")
while True:
    while True:
        try:
            op = int(input(f"escolha o que deseja comprar\n1 - {produtos[0]}\n2 - {produtos[1]}\n3 - {produtos[2]}\n4 - {produtos[3]}\n0 - fechar compra\n")) 
            break
        except:
            print("digite um valor valido")
            continue
    if(op == 0):
        break
    elif(op == 1 or op == 2 or op == 3 or op == 4):
        escolhidos.append(op - 1)
        
for i in escolhidos:
    total += preco[i]

print("Valor total da compra:",total)
while True:
    try:
        pagamento = float(input("Insira o valor do pagamento:\n"))
        if(pagamento >= total):
            break
        else:
            print("Insira um valor maior para pagar sua conta de: R$",total)
            continue
    
    except:
        print("Insira um valor valido")
        continue

troco = pagamento - total 
print("Pegue o seu troco de R$",troco)

        

    

    
