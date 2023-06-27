import re

class Telefone:

    def __init__(self, telefone):
        self.telefone = self.formatar_telefone(Telefone.validate(telefone))

    @staticmethod
    def validate(telefone):
        if (len(telefone) != 11):
            raise ValueError("Telefone inválido")
        return telefone

    def formatar_telefone(self, telefone):
        padrao = r"(\d{2})(\d{1})(\d{4})(\d{4})"
        formato = r"(\1) \2 \3-\4"
        telefone_formatado = re.sub(padrao, formato, telefone)
        return telefone_formatado

    def __str__(self):
        return self.telefone