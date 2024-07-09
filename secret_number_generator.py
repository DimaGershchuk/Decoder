import random


class SecretNumberGenerator:
    def __init__(self):
        self.secret_number = ''

    def generate_number(self):
        self.secret_number = ''.join([str(random.randint(1, 6)) for _ in range(4)])
        #  self.secret_number = '6543'
        return self.secret_number
