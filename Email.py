import re

class Email:
    def __init__(self, email):
        self.email = Email.validate(email)

    @staticmethod
    def validate(email: str = '') -> str:
        pattern = "\w{5,50}@\w{3,10}.\w{2,3}"
        email = re.search(pattern, email)
        return email.group()

    def __str__(self):
        return self.email