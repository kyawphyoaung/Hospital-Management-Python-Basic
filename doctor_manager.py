from doctor import Doctor


class DoctorManager:
    def __init__(self):
        self.doctors = []

    def load_doctor_detail(self):
        with open("doctor_detail.csv") as doctor_file:
            doctor_file.readline()
            for line in doctor_file.readlines():
                doctor_data = line.split(",")
                doctor_first_name = doctor_data[0]
                doctor_last_name = doctor_data[1]
                doctor_id = doctor_data[2]
                doctor_specialization = doctor_data[3]
                new_doctor = Doctor(doctor_first_name, doctor_last_name, doctor_id, doctor_specialization)
                self.doctors.append(new_doctor)

    def add_new_attend_doctor(self, doctor_first_name, doctor_last_name, doctor_id, doctor_specialization):
        if self.existing_doctor(doctor_id):
            print("\nThis doctor Id is already taken.")
            return False
        else:
            new_attend_doctor = Doctor(doctor_first_name, doctor_last_name, doctor_id, doctor_specialization)
            self.doctors.append(new_attend_doctor)
            return True

    def existing_doctor(self, doctor_id):
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                return True
        return False

    def remove_doctor(self, doctor_id):
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                self.doctors.remove(doctor)
                return True
        return False
