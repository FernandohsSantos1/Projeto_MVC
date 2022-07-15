#Arquivo onde ocorre as regras de negocio, back-end;
from dal import ClienteDal
from model import Cliente

class ClienteController:
    
    @classmethod
    def cadastrar(cls, cliente: Cliente):
        
        if not len(cliente.nome)>2:
            
            mensagem = 'Nome inválido!'
            return mensagem 
        
        if cliente.idade < 10 or cliente.idade > 100:
               
            mensagem = 'Idade inválida!'
            return mensagem
        
        if cliente.genero not in ['Masculino', 'Feminino', 'masculino', 'feminino','M','F']:
            
            mensagem = 'Genero inválido!'
            return mensagem

        mensagem = 'Cliente salvo com sucesso'
        ClienteDal.salvar(cliente)
        
        return mensagem