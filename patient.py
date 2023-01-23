from person import Person

class Patient(Person):
    def __init__(self, first_name, last_name, patient_id, age, date_of_birth,admit_date,discharge_date):
        super().__init__(first_name, last_name)
        self.__patient_id = patient_id
        self.__age = age
        self.__date_of_birth = date_of_birth
        self.__admit_date = admit_date
        self.__discharge_date = discharge_date

    def get_id(self):
        return self.__patient_id

    def get_age(self):
        return self.__age

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_admit_date(self):
        return self.__admit_date

    def get_discharge_date(self):
        return self.__discharge_date

    def __str__(self):
        output = f"Patient is {super().__str__()}(Id-{self.__patient_id}) Age is {self.__age} "
        return output


"""attending_physician_name = DoctorManager()
attending_physician_name.load_doctor_detail()


def display_all_doctors(doctors):
    for doctor in range(doctors):
        print(f"Attending Doctor Name is {doctor}")

if __name__ == '__main__':
    patient1=Patient("Harry","potter",attending_physician_name,"C001",30)
    print(patient1)"""
