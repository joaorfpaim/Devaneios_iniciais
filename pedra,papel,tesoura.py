import os
os.system('cls')
import random 

print('-----------Pedra,Papel,Tesoura-----------')

movimentos = ['pedra','papel','tesoura']
nome = input('Insira seu nome: ')

def jogo():
    pontopc = 0
    ponto = 0
    while True:
        movimentopc1 = random.choice(movimentos)
        movimento1 = input('(Quando quiser acabar, escreva "Exit")\nPedra, papel ou tesoura?: ').lower()

        if movimento1 == 'exit':
            break
        elif movimentopc1 == movimento1:
            os.system('cls')
            print('Empate')
            pontopc += 1
            ponto += 1
        elif movimentopc1 == ('pedra' and movimento1 == 'tesoura') or (movimentopc1 == 'tesoura' and movimento1 == 'papel') \
            or (movimentopc1 == 'papel' and movimento1 == 'pedra'):
            os.system('cls')
            print('O pc ganhou.')
            pontopc += 1

        elif (movimento1 == 'pedra' and movimentopc1 == 'tesoura')  or (movimento1 == 'tesoura' and movimentopc1 == 'papel') \
            or (movimento1 == 'papel' and movimentopc1 == 'pedra'):
            os.system('cls')
            print('Você ganhou.')
            ponto += 1
        
        else:
            os.system('cls')
            print('Entrada inválida.')
        print(f'{nome}: {ponto} PC: {pontopc}')
        
jogo()
