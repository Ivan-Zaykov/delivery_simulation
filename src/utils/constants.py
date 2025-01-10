
class Constants:
    TIME_COMPRESSION_RATIO = 1 / 1000
    ORDER_ASSEMBLY_TIME = 45
    SECONDS_PER_MINUTE = 60
    # Ед.расст-я / сек
    COURIER_SPEED = 1/30
    HOURLY_PAY = 300
    MINUTES_PER_HOUR = 60

    @staticmethod
    def oneMinute():
        return Constants.SECONDS_PER_MINUTE * Constants.TIME_COMPRESSION_RATIO

    @staticmethod
    def orderAssemblyTime():
        return Constants.ORDER_ASSEMBLY_TIME * Constants.TIME_COMPRESSION_RATIO

    @staticmethod
    def courierSpeed():
        return Constants.COURIER_SPEED / Constants.TIME_COMPRESSION_RATIO
