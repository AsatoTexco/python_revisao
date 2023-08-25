def calcular_pontos(livros_comprados):
    match livros_comprados:
        case 0: 
            return 0
        case 1:
            return 5
        case 2:
            return 15
        case 3:
            return 30
        case _:
            if(livros_comprados >= 4):
                return 60
            
def escolher_brinde(pontos):
    if 20 <= pontos <= 30:
        return "Uma Ecoa OU Caneta personalizada"
    elif 35 <= pontos <= 60:
        return "Um livro (com valor máximo de R$30,00) OU Luminária de cabeceira"
    elif pontos >= 65:
        return "2 livros (com valor máximo de R$100,00) OU Powerbank"
    else:
        return "Nenhum brinde disponível"

livros_comprados = int(input("Digite o número de livros comprados: "))
pontos = calcular_pontos(livros_comprados)
brinde = escolher_brinde(pontos)

print(f"Você ganhou {pontos} pontos.")
print(f"Opções de brinde: {brinde}")
