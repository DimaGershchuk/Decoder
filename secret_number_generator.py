import random


class SecretNumberGenerator:
    def __init__(self):
        self.secret_number = ''

    def generate_number(self):
        self.secret_number = ''.join([str(random.randint(1, 6)) for _ in range(4)])
        #  print(f"Згенероване число для тестування: {self.secret_number}")  # Видаліть у фінальній версії
        return self.secret_number
