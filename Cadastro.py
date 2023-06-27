from Cpf import Cpf
from Email import Email
from Telefone import Telefone
from Cep import Cep
from Endereco import Endereco

class Cadastro:
    def __init__(self, nome, cpf, email, telefone, cep, numero):
        self.nome = nome
        self.cpf = Cpf(cpf)
        self.email = Email(email)
        self.telefone = Telefone(telefone)
        self.cep = Cep(cep)
        self.endereco = Endereco(cep, numero)
        self.numero = numero

    def get_numero(self):
        return self.numero

    def __str__(self):
        return 'nome: {}' \
               '\ncpf: {}' \
               '\nemail: {}' \
               '\ntelefone: {}' \
               '\ncep: {}' \
               '\nendereco: {}'.format( self.nome, self.cpf, self.email, self.telefone, self.cep, self.endereco )