
class Constants:
    TIME_СOMPRESSION_RATIO = 1/1000
    ORDER_ASSEMBLY_TIME = 45
    ONE_MINUTE = 60
    # Ед.расст-я / сек
    COURIER_SPEED = 1/30
    HOURLY_PAY = 300

    @staticmethod
    def oneMinute():
        return Constants.ONE_MINUTE * Constants.TIME_СOMPRESSION_RATIO

    @staticmethod
    def orderAssemblyTime():
        return Constants.ORDER_ASSEMBLY_TIME * Constants.TIME_СOMPRESSION_RATIO

    @staticmethod
    def courierSpeed():
        return Constants.COURIER_SPEED / Constants.TIME_СOMPRESSION_RATIO
