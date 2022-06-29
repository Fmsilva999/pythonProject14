import random
from time import sleep
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador >= 3:
    print('Opção Inválida!')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 20)

opcoes = [0, 1, 2]
computador = random.choice(opcoes)
if computador == 0:
    print('Computador jogou Pedra')
    if jogador == 0:
        print('Jogador jogou Pedra')
        print('-=' * 20)
        print('EMPATE')
    if jogador == 1:
        print('Jogador jogou Papel')
        print('-=' * 20)
        print('JOGADOR VENCE')
    if jogador == 2:
        print('Jogador jogou Tesoura')
        print('-=' * 20)
        print('COMPUTADOR VENCE')
elif computador == 1:
    print('Computador jogou Papel')
    if jogador == 0:
        print('Jogador jogou Pedra')
        print('-=' * 20)
        print('COMPUTADOR VENCE')
    if jogador == 1:
        print('Jogador jogou Papel')
        print('-=' * 20)
        print('EMPATE')
    if jogador == 2:
        print('Jogador jogou Tesoura')
        print('-=' * 20)
        print('JOGADOR VENCE')
else:
    print('Computador jogou Tesoura')
    if jogador == 0:
        print('Jogador jogou Pedra')
        print('-=' * 20)
        print('JOGADOR VENCE')
    if jogador == 1:
        print('Jogador jogou Papel')
        print('-=' * 20)
        print('COMPUTADOR VENCE')
    if jogador == 2:
        print('Jogador jogou Tesoura')
        print('-=' * 20)
        print('EMPATE')