from patient import Patient

class DateType:
    def __init__(self, date_of_birth, admit_date, discharge_date):
        self.__date_of_birth = date_of_birth
        self.__admit_date = admit_date
        self.__discharge_date = discharge_date

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_admit_date(self):
        return self.__admit_date

    def get_discharge_date(self):
        return self.__discharge_date

    def __str__(self):
        output = f"Date of birth : {self.__date_of_birth}\nDate when the patient was admitted : {self.__admit_date}\n" \
                 f"Date when the patient was discharged: {self.__discharge_date}\n"
        return output





