import re
import requests

class Cep:
    def __init__(self, cep):
        if(type(cep) != str):
            cep = str(cep)
        if Cep.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    @staticmethod
    def valida_cep(cep):
        if(len(cep) == 8):
            return True
        return False

    def formatar_cep(self):
        return re.sub(r'(\d{5})(\d{3})', r'\1-\2', self.cep)

    def busca_endereco(self):
        url_api = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        result = requests.get(url_api)
        return result.json()

    def __str__(self):
        return self.formatar_cep()