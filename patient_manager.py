from patient import Patient
from date_type import DateType


class PatientManager:
    def __init__(self):
        self.patients = []
        self.date_type = []
        self.patients_name = []

    def load_patient_detail(self):
        with open("patient_detail.csv") as patient_file:
            patient_file.readline()
            for line in patient_file.readlines():
                patient_data = line.split(",")
                patient_first_name = patient_data[0]
                patient_last_name = patient_data[1]
                patient_id = patient_data[2]
                patient_age = patient_data[3]
                date_data = line.split(",")
                date_of_birth = date_data[4]
                admit_date = date_data[5]
                discharge_date = date_data[6]
                new_patient = Patient(patient_first_name, patient_last_name, patient_id, patient_age)
                new_date = DateType(date_of_birth, admit_date, discharge_date)
                self.patients.append(new_patient)
                self.patients.append(new_date)

    """def get_patient_name(self):
        with open("patient_detail.csv") as patient_file:
            patient_file.readline()
            for line in patient_file.readlines():
                patient_data = line.split(",")
                patient_first_name = patient_data[0]
                patient_last_name = patient_data[1]
                new_patient = Patient(patient_first_name, patient_last_name, patient_id, patient_age)
                new_date = DateType(date_of_birth, admit_date, discharge_date)
                self.patients.append(new_patient)
                self.patients.append(new_date)"""

    """def load_date_detail(self):
        with open("patient_detail.csv") as data_file:
            data_file.readline()
            for line in data_file.readlines():"""



    def add_new_boarding_patient(self, patient_first_name, patient_last_name, patient_id, patient_age):
        if self.existing_patient(patient_id):
            print("\n This patient ID is already at the hospital or is already taken. ")
            return False
        else:
            new_boarding_patient = Patient(patient_first_name, patient_last_name, patient_id, patient_age)
            self.patients.append(new_boarding_patient)
            return True

    def existing_patient(self, patient_id):
        for patient in self.patients:
            if patient.get_id() == patient_id:
                return True
        return False

    def discharge_patients(self, patient_id):
        for patient in self.patients:
            if patient.get_id() == patient_id:
                self.patients.remove(patient)
                return True
        return False
