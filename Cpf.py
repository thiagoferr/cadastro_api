import re

class Cpf:
    def __init__(self, doc):
        doc = str(doc)
        if self.valida_cpf(doc):
            self.doc = doc
        else:
            raise ValueError("CPF Inválido!")

    def valida_cpf(self, doc):
       if len(doc) != 11:
           return False
       return True

    @staticmethod
    def cpf_formatado(doc):
        return re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', doc)

    def __str__(self):
        return Cpf.cpf_formatado(self.doc)