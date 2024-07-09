class GuessChecker:
    def __init__(self, secret_number):
        self.secret_number = secret_number

    def check_guess(self, user_guess):
        result = ''
        correct_position = [False] * len(self.secret_number)
        digit_position = set()

        for i, digit in enumerate(user_guess):
            if digit == self.secret_number[i]:
                result += '+'
                correct_position[i] = True
                digit_position.add(i)

        for i, digit in enumerate(user_guess):
            if digit != self.secret_number and digit in self.secret_number:
                for j, encrypted_digit in enumerate(self.secret_number):
                    if digit == encrypted_digit and not correct_position[j] and j not in digit_position:
                        result += '-'
                        digit_position.add(j)
                        break
        return result
