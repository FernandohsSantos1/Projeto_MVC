#Arquivo que gera a interface, ou seja, o que é exibido ao usuário e com que ele pode interagir

from dal import ClienteDal
from controller import ClienteController
from model import Cliente

print('\n         Seja Bem-Vindo!\n')

while True:
    
    print('Selecione:\n   1 - Para Cadastrar\n   2 - Para Ler\n   0 - Para Sair')
    opcao = int(input())
    
    if opcao == 0:
        print('Encerrando programa...')
        break
    
    elif opcao == 1:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        genero = input('Digite seu genero: ')
        print('\n'+ClienteController.cadastrar(Cliente(nome,idade,genero))+'\n')
        

    elif opcao == 2: 
        ClienteDal.ler()
        

    else:
        print('Opção invalida! Tente novamente.\n')