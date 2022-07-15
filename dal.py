#Arquivo para criação de métodos de classe para simular aplicação no banco de dados

from model import Cliente


class ClienteDal:

    @classmethod
    def salvar(cls, cliente: Cliente):
        with open('Clientes.txt', 'a') as arq:
            arq.write(f'\n{"Nome: ":<20} {cliente.nome}\n{"Idade: ":<20} {cliente.idade}\n{"Genero: ":<20} {cliente.genero}\n{"="*40}')

    @classmethod
    def ler(cls):
        with open('Clientes.txt', 'r') as arq:
            print(arq.read())