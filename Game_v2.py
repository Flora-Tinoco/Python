# Projeto 1 - Desenvolvimento do Game em Python- Versão 1

#Import
import random
from os import system, name

#Função para limpar a tela em cada execução- ela serve para, ao final do jogo, caso eu deseje jogar novamente, ela limpe a tela e eu possa jogar com tudo limpinho
def limpatela():
	#windows
	if name =='nt':
		_ = system('cls')

	#mac ou linux
	else:
		_ = system('clear')

# Função que desenha a forca na tela
def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]


#Função
def game():

    limpatela()

    print('bem vindo ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')

    #Lista de palavras do jogo []
    palavras = ['banana','kiwi','abacate','morango','guabiroba','uva']

    # Escolhe randomicamente uma palavra
    palavra = random.choice (palavras)

    #List comprehension
    letras_descobertas = ['_' for letra in palavra]

    #Número de chances
    chances= 6

    #Lista para letras erradas
    letras_erradas = []
	 # loop enquanto o número de tentativas for maior que zero
    while chances > 0:

        #print
        print(display_hangman(chances))
        print(" ".join(letras_descobertas))
        print("\nChances restantes:" , chances)
        print("Letras erradas:", " ".join(letras_erradas))

        #tentativa
        tentativa= input("\nDigite uma letra:").lower()

        # Condicional
        if tentativa in letras_erradas:
            print("Você já tentou essa letra. Escolha outra!")
            continue

        #Condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index +=1
        else:
            chances -=1
            letras_erradas.append(tentativa)
         #Condicional
        if "_" not in letras_descobertas:
            print("\n Parabéns, você venceu!! A palavra era:",palavra)
            break

    #Condicional
    if "_" in letras_descobertas:
        print("\n Você perdeu, a palavra era:", palavra)

# Bloco main
if __name__=="__main__":
    game()
    print("\n Obrigada por jogar, volte sempre! :D \n")    