from person import Person

class Doctor(Person):
    def __init__(self, first_name, last_name,doctor_id, specialization):
        super().__init__(first_name, last_name)
        self.__specialization = specialization
        self.__doctor_id=doctor_id

    def get_doctor_id(self):
        return self.__doctor_id

    def get_specialization(self):
        return self.__specialization

    def set_specialization(self,specialization):
        self.__specialization = specialization

    def __str__(self):
        output= f"Doctor Name: {super().__str__()}(ID-{self.__doctor_id}) Specialization: {self.__specialization}"
        return output

    def __repr__(self):
        output = self.__str__()
        return output


if __name__ == '__main__':
    # test data
    doc=Doctor("John","Cena","General")

    print(doc)