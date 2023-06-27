from Cep import Cep

class Endereco:

    def __init__(self, cep, numero):
        self.endereco = Cep(cep).busca_endereco()
        self.rua = self.endereco["logradouro"]
        self.bairro = self.endereco["bairro"]
        self.cidade = self.endereco["localidade"]
        self.estado = self.endereco["uf"]
        self.numero = numero
    def __str__(self):
        return f'{ self.rua }, { self.numero } - { self.bairro } - { self.cidade } - { self.estado }'