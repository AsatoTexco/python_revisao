# alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# letras_encrypt = []
# for i in range(len(alfabeto)):
from faker import Faker

fake = Faker()
random_name = fake.name() 
print("Nome aleatório:", random_name)
