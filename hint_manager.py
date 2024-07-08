class HintManager:
    def __init__(self, secret_number):
        self.secret_number = secret_number
        self.hints_left = 0

    def provide_hint(self):
        if self.hints_left > 0:
            while True:
                try:
                    hint_position = int(input("Введіть позицію (1-4) для якої хочете використати підказку : "))
                    if 1 <= hint_position <= 4:
                        print(f"Підказка : на позиції {hint_position} цифра {self.secret_number[hint_position - 1]}")
                        self.hints_left -= 1
                        print(f"Підказок залишилось : {self.hints_left}")
                        break
                    else:
                        print("Ви ввели не коректне значення, введіть від 1 до 4")

                except (IndexError, ValueError):
                    print("Ви ввели не коректне значення, введіть від 1 до 4")
        else:
            print("Підказок не залишилось")
