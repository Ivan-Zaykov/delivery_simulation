from src.utils.constants import Constants


class Worker:
    def __init__(self, name):
        self.name = name
        self.is_available = True
        self.shift_hours = 0

    def start_shift(self, hours):
        self.shift_hours = hours
        print(f"{self.name} начал смену на {hours} часов.")

    def end_shift(self):
        salary = self.shift_hours * Constants.HOURLY_PAY
        print(f"Работник: {self.name} закончил смену. Заработано: {salary} руб.")
        self.shift_hours = 0
