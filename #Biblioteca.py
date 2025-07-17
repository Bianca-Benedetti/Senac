#Biblioteca
import random
# Gera um numero secreto aleatóreo entre 1  e 10
numero_secreto = random.randint(1, 10)
#Ler o palpite da tela
palpite =int(input("Digite um palpite: "))
#Compara se o palpite e igual ao numero secreto
if(palpite == numero_secreto):
    print("Parabens voce acertou!")
else:
    print("Tente outra vez!")
    #Numero secreto
    print("O numero secreto e",numero_secreto)