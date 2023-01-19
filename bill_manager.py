from hospital_bill import HospitalBill

class Bill_Manager:
    def __init__(self):
        self.ledger = []

    def load_patients_bill(self):
        with open("pay_bill.csv") as bill_file:
            bill_file.readline()
            for line in bill_file.readlines():
                bill_ledger = line.split(",")
                patient_first_name = bill_ledger[0]
                patient_last_name = bill_ledger[1]
                patient_id = bill_ledger[2]
                medicine_fee = bill_ledger[3]
                doctor_fee = bill_ledger[4]
                room_fee = bill_ledger[5]
                total_fee = bill_ledger[6]
                new_hospital_bill = HospitalBill(patient_first_name, patient_last_name, patient_id,medicine_fee,doctor_fee,room_fee,total_fee)
                self.ledger.append(new_hospital_bill)

    def add_new_bill(self, patient_first_name, patient_last_name, patient_id,medicine_fee,doctor_fee,room_fee,total_fee):
        new_bill = HospitalBill(patient_first_name, patient_last_name, patient_id,medicine_fee,doctor_fee,room_fee,total_fee)
        self.ledger.append(new_bill)