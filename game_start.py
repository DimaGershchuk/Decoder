from hello_and_rules import hello_words, rules
from game_functionality import Game


class Menu:
    def __init__(self):
        self.game = Game()

    def show_menu_start(self):
        print(hello_words)
        while True:
            start = input("Виберіть один з чотирьох варіантів : Старт, Правила, Статистика, Вихід : ")

            if start == 'Старт':
                self.game.start()
                continue
            elif start == 'Правила':
                print(rules)
            elif start == 'Вихід':
                print("Прощавайте, до зустрічі!")
                break
            else:
                print("Ви ввели непередбачену команду. Будь ласка, виберіть одну з перерахованих команд")
                continue


if __name__ == "__main__":
    menu = Menu()
    menu.show_menu_start()