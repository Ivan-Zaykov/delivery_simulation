from datetime import timedelta, datetime


class VirtualTime:
    def __init__(self, start_time):
        self.current_time = start_time  # Текущее виртуальное время

    def advance_time(self, minutes):
        """Продвигает виртуальное время вперёд на указанное количество минут."""
        self.current_time += timedelta(minutes=minutes)

    def get_current_time(self):
        """Возвращает текущее виртуальное время."""
        return self.current_time


# Глобальный объект виртуального времени
GlobalVirtualTime = VirtualTime(datetime(2025, 1, 10, 8, 0))
