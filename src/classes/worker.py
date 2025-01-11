from datetime import timedelta, datetime
from abc import ABC, abstractmethod

from src.utils.constants import Constants
from src.utils.virtual_time import GlobalVirtualTime


class Worker:
    def __init__(self, name):
        self._name = name
        self._shift_hours = 0
        self._shift_start = None
        self._current_order = None

    @property
    def name(self):
        return self._name

    @property
    def current_order(self):
        return self._current_order

    @current_order.setter
    def current_order(self, current_order):
        self._current_order = current_order

    def start_shift(self, hours):
        self._shift_start = GlobalVirtualTime.get_current_time().time()
        self._shift_hours = hours
        print(f"`{self.name}` в {self._shift_start} начал смену на {hours} часов.")

    def end_shift(self):
        salary = self._shift_hours * Constants.HOURLY_PAY
        print(f"Работник `{self.name}` закончил смену. Заработано: {salary} руб.")
        self._shift_hours = 0
        self._shift_start = None

    def is_available(self):
        return self.is_on_shift() and self._current_order is None

    def is_on_shift(self):
        current_time = GlobalVirtualTime.get_current_time().time()
        shift_end = (datetime.combine(datetime.min, self._shift_start) + timedelta(hours=self._shift_hours)).time()
        return self._shift_start <= current_time <= shift_end

    @abstractmethod
    def execute_work(self):
        pass