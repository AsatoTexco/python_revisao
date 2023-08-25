def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord(key) % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a' + shift)) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A' + shift)) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord(key) % 26
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a' - shift)) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A' - shift)) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    option = input("Escolha 'e' para criptografar ou 'd' para descriptografar: ")
    if option != 'e' and option != 'd':
        print("Opção inválida.")
        return

    input_file = input("Digite o nome do arquivo de entrada: ")
    output_file = input("Digite o nome do arquivo de saída: ")
    key = input("Digite a chave de criptografia (uma letra): ")

    try:
        with open(input_file, 'r') as f:
            content = f.read()
        
        if option == 'e':
            encrypted_content = encrypt(content, key)
            with open(output_file, 'w') as f:
                f.write(encrypted_content)
            print("Arquivo criptografado com sucesso.")
        else:
            decrypted_content = decrypt(content, key)
            with open(output_file, 'w') as f:
                f.write(decrypted_content)
            print("Arquivo descriptografado com sucesso.")
    
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
