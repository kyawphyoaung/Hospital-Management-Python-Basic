from patient import Patient
from date_type import DateType
from doctor import Doctor
from doctor_manager import DoctorManager

class PatientManager:
    def __init__(self):
        self.patients = []
        self.date_type = []
        self.patients_name = []

    def load_patient_detail(self):
        doctor_manage=DoctorManager()
        doctor_manage.load_doctor_detail()
        with open("patient_detail.csv") as patient_file:
            patient_file.readline()
            for line in patient_file.readlines():
                patient_data = line.split(",")
                patient_first_name = patient_data[0]
                patient_last_name = patient_data[1]
                patient_id = patient_data[2]
                patient_age = patient_data[3]
                for doctor in doctor_manage.doctors:
                    if doctor.get_first_name() == patient_data[4] and doctor.get_last_name() == patient_data[5]:
                        attending_physician = doctor
                doB = patient_data[6].split("/")
                date_of_birth = DateType(doB[0],doB[1],doB[2])
                admission_date = patient_data[7].split("/")
                admit_date = DateType(admission_date[0],admission_date[1],admission_date[2])
                discharge = patient_data[8].split("/")
                discharge_date = DateType(discharge[0],discharge[1],discharge[2])
                new_patient = Patient(patient_first_name, patient_last_name, patient_id, patient_age, date_of_birth,attending_physician, admit_date, discharge_date)
                self.patients.append(new_patient)

    def add_new_boarding_patient(self, patient_first_name, patient_last_name, patient_id, patient_age,patient_dob,admit_date,discharge_date):
        if self.existing_patient(patient_id):
            print("\n This patient ID is already at the hospital or is already taken. ")
            return False
        else:
            #Onboarding patient haven't assigned physician,admit date and discharge date yet!
            null_doctor = Doctor("null","null","null","null")
            new_boarding_patient = Patient(patient_first_name, patient_last_name, patient_id, patient_age,patient_dob,null_doctor, admit_date, discharge_date)
            self.patients.append(new_boarding_patient)
            return True

    def existing_patient(self, patient_id):
        for patient in self.patients:
            if patient.get_id() == patient_id:
                return True
        return False

    def discharge_patients(self, patient_id,discharge_date):
        discharge = discharge_date.split(",")
        for patient in self.patients:
            if patient.get_id() == patient_id:
                patient.set_discharge_date(DateType(discharge[0],discharge[1],discharge[2]))
        
        return

    def attending_physician(self,patient_id,attending_physician):
        for patient in self.patients:
            if patient.get_id() == patient_id:
                patient.set_attending_physician(attending_physician)
                print(patient)
        return
