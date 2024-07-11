class GuessChecker:
    def __init__(self, secret_number):
        self.secret_number = secret_number

    def check_guess(self, user_guess):
        result = ''
        correct_position = [False] * len(self.secret_number)
        digit_position = [False] * len(self.secret_number)

        for i, digit in enumerate(user_guess):
            if digit == self.secret_number[i]:
                result += '+'
                correct_position[i] = True
                digit_position[i] = True

        for i, digit in enumerate(user_guess):
            if digit != self.secret_number[i] and digit in self.secret_number:
                for j, encrypted_digit in enumerate(self.secret_number):
                    if digit == encrypted_digit and not correct_position[j] and not digit_position[j]:
                        result += '-'
                        digit_position[j] = True
                        break
        return result
