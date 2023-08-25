import random
def jogo(dif):
    match dif:
        case 1:
            aleatorio = random.randint(1,5)
        case 2:
            aleatorio = random.randint(1,25)
        case 3:
            aleatorio = random.randint(1,125)
        case 4:
            aleatorio = random.randint(1,999)
    return aleatorio
print("\033[7;31;34mJogo da Sorte\033[m")
while True:
    while True:
        try:
            op = int(input("\n\n[1] Iniciar jogo\n[0] Sair\n"))
            break
        except:
            print("Insira um valor válido")
            continue 
    match op:
        case 0:
            print("Até mais!")
            break
        case 1:
            while True:
                try:
                    dificuldade = int(input("\n\n[1] Nivel Fácil\n[2] Nivel Médio\n[3] Dificil\n[4] ABSOLUTAMENTE IMPOSSIVEL\n[0] desistir\n"))
                    if(dificuldade >= 0 and dificuldade <= 4):

                        match dificuldade:
                            case 0:
                                print("Esperava mais...")
                                break
                        num = int(input("Tente a sorte\nescolha um número: "))
                        rand = jogo(dificuldade)
                        if(num == rand):
                            print("\033[7;31;32mParabénss! Você ganhou!!!\033[m")
                        else:
                            print("\033[7;31;31mNão foi dessa vez :/\033[m")
                        while True:
                            try:
                                op = int(input("\033[7;31;32m[1] Continuar\n[0] Sair\n\033[m"))
                                break
                            except:
                                print("Digite algo valido")
                                continue
                        match op:
                            case 0:
                                break
                            case 1:
                                while True:
                                    num = int(input("Insira um numero: "))
                                    if(num == rand):
                                        print("\033[7;31;32mParabénss! Você ganhou!!!\033[m")
                                        break
                                    else:
                                        print("\033[7;31;31mVocê errou, tente outro número :\033[m")
                                        continue
                    break 
                except:
                    print("Insira um valor válido")
                    break
        
