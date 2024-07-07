class GuessChecker:
    def __init__(self,secret_number):
        self.secret_number = secret_number

    def check_guess(self, user_guess):
        result = ''
        digit_position = set()
        for i, digit in enumerate(user_guess):
            if digit == self.secret_number[i]:
                result += '+'
                digit_position.add(i)
            elif digit in self.secret_number:
                for j, encrypted_digit in enumerate(self.secret_number):
                    if digit == encrypted_digit and encrypted_digit not in digit_position:
                        result += '-'
                        digit_position.add(encrypted_digit)
                        break
        return result
