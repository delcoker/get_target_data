class TimePeriod:
    def __init__(self, quarter, month, month_name, year):
        self.quarter = quarter
        self.month = month
        self.monthName = month_name
        self.year = year

    def __str__(self):
        return self.__dict__

    def __repr__(self):
        return self.__dict__
