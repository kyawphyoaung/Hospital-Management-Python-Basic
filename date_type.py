from patient import Patient

class DateType:
    def __init__(self, day, month, year):
        self.__d = day
        self.__m = month
        self.__y = year

    def get_day(self):
        return self.__d

    def get_month(self):
        return self.__m

    def get_year(self):
        return self.__y

    def __str__(self):
        return (str(self.__d) + "," + str(self.__m) + "," + str(self.__y))





