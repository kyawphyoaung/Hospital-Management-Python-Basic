from person import Person

class Patient(Person):
    def __init__(self, first_name, last_name, patient_id, age, date_of_birth,attending_physician,admit_date,discharge_date):
        super().__init__(first_name, last_name)
        self.__patient_id = patient_id
        self.__age = age
        self.__attending_physician = attending_physician
        self.__date_of_birth = date_of_birth
        self.__admit_date = admit_date
        self.__discharge_date = discharge_date

    def get_id(self):
        return self.__patient_id

    def get_age(self):
        return self.__age

    def get_attending_physician(self):
        return self.__attending_physician

    def set_attending_physician(self,attending_physician):
        self.__attending_physician = attending_physician

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_admit_date(self):
        return self.__admit_date

    def get_discharge_date(self):
        return self.__discharge_date

    def set_discharge_date(self,discharge_date):
        self.__discharge_date = discharge_date

    def __str__(self):
        attending_physician_name = self.__attending_physician
        output = '{:5}| {:14}| {:12}| {:4}| {:14}| {:12}| {:12}'.format(self.__patient_id,super().get_name(),self.__date_of_birth.__str__(),self.__age,attending_physician_name.get_name(),self.__admit_date.__str__(),(self.__discharge_date.__str__()).strip('\n'))
        return output


"""attending_physician_name = DoctorManager()
attending_physician_name.load_doctor_detail()


def display_all_doctors(doctors):
    for doctor in range(doctors):
        print(f"Attending Doctor Name is {doctor}")

if __name__ == '__main__':
    patient1=Patient("Harry","potter",attending_physician_name,"C001",30)
    print(patient1)"""
