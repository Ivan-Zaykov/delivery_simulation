from datetime import timedelta, datetime

from src.utils.constants import Constants
from src.utils.virtual_time import GlobalVirtualTime


class Worker:
    def __init__(self, name):
        self.name = name
        self.shift_hours = 0
        self.shift_start = None

    def start_shift(self, hours):
        self.shift_start = GlobalVirtualTime.get_current_time().time()
        self.shift_hours = hours
        print(f"`{self.name}` начал смену на {hours} часов.")

    def end_shift(self):
        salary = self.shift_hours * Constants.HOURLY_PAY
        print(f"Работник `{self.name}` закончил смену. Заработано: {salary} руб.")
        self.shift_hours = 0
        self.shift_start = None

    def is_available(self):
        current_time = GlobalVirtualTime.get_current_time().time()
        shift_end = (datetime.combine(datetime.min, self.shift_start) + timedelta(hours=self.shift_hours)).time()
        return self.shift_start <= current_time <= shift_end
