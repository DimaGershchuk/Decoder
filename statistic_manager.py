class StatisticsManager:
    def __init__(self):
        self.total_wins = 0
        self.total_losses = 0
        self.easy_wins = 0
        self.easy_losses = 0
        self.hard_wins = 0
        self.hard_losses = 0

    def record_win(self, difficulty):
        self.total_wins += 1
        if difficulty == 'Простий':
            self.easy_wins += 1
        elif difficulty == 'Складний':
            self.hard_wins += 1

    def record_loss(self, difficulty):
        self.total_losses += 1
        if difficulty == 'Простий':
            self.easy_losses += 1
        elif difficulty == 'Складний':
            self.hard_losses += 1

    def print_statistics(self):
        print("\nЗагальна статистика:")
        print(f"Всього перемог: {self.total_wins}")
        print(f"Всього поразок: {self.total_losses}")
        print("\nСтатистика за рівнем складності:")
        print("Простий:")
        print(f"Перемог: {self.easy_wins}")
        print(f"Поразок: {self.easy_losses}")
        print("Складний:")
        print(f"Перемог: {self.hard_wins}")
        print(f"Поразок: {self.hard_losses}")
