import re
from hint_manager import HintManager
from secret_number_generator import SecretNumberGenerator
from guess_checker import GuessChecker


class Game:
    def __init__(self):
        self.secret_number = ''
        self.hints_manager = None
        self.attempts = 0

    def start(self):
        generator = SecretNumberGenerator()
        self.secret_number = generator.generate_number()
        self.hints_manager = HintManager(self.secret_number)
        self.attempts = self.difficulty_choose()

        self.play_game()

    def difficulty_choose(self):
        while True:
            difficulty_guess = input("Оберіть рівень складності, Простий чи Складний : ")
            if difficulty_guess == 'Простий':
                self.hints_manager.hints_left = 3
                return 5
            elif difficulty_guess == 'Складний':
                self.hints_manager.hints_left = 2
                return 3
            else:
                print("Некоректне значення, введіть один з запропонованих рівней складності ")

    def play_game(self):
        while self.attempts > 0:

            user_guess = input("Введіть число або введіть 'Вихід' для закінчення гри : ")

            if user_guess == 'Вихід':
                print("Гра завершена. Дякуємо за гру!")
                break

            if re.fullmatch(r'[1-6]{4}', user_guess):
                checker = GuessChecker(self.secret_number)
                result = checker.check_guess(user_guess)
                print(f"Результат : {result}")

                if result == '++++':
                    print(f"Ви вгадали число {self.secret_number} та перемогли!!")
                    break

                else:
                    self.attempts -= 1
                    print(f"Залишилось спроб : {self.attempts}")

                    if self.attempts > 0 and self.hints_manager.hints_left > 0:
                        while True:
                            use_hint = input("Хочете використати підказку? Введіть Так або Ні: ")

                            if use_hint == 'Так':
                                self.hints_manager.provide_hint()
                                break
                            elif use_hint == 'Ні':
                                break
                            else:
                                print("Ви ввели некоректне значення, введіть 'Так' або 'Ні'.")

                if self.attempts == 0:
                    print(f"У вас не залишилось спроб. Ви програли, таємниче число : {self.secret_number}. Розпочніть гру знову!")
                    continue
            else:
                print("Ви ввели некоректне значення, введіть число з 4 цифр від 1 до 6")




