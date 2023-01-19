import csv
from doctor_manager import DoctorManager
from patient_manager import PatientManager
from bill_manager import Bill_Manager

doctor_manage=DoctorManager()
doctor_manage.load_doctor_detail()
patient_manage=PatientManager()
patient_manage.load_patient_detail()
bill_manage=Bill_Manager()
bill_manage.load_patients_bill()

def display_all_doctors(doctors):
    for index, doctor in enumerate(doctors):
        print(f"{index + 1:2} - {doctor}")

def add_new_doctors(doctor_manage):
    doctor_first_name = input("Enter the doctor's first name --> ")
    doctor_last_name = input("Enter the doctor's last name --> ")
    doctor_id = input("Enter the doctor's Id --> ")
    doctor_specialization = input("Enter the doctor's specialization --> ")
    doctor_manage.add_new_attend_doctor(doctor_first_name, doctor_last_name, doctor_id, doctor_specialization)

def remove_doctors(doctor_manage):
    doctor_id = input("Enter the doctor's Id that you want to remove ")
    doctor_manage.remove_doctor(doctor_id)

def show_option_doctor(doctor_menu):
    doctor_sub_option = input(doctor_menu)

    if doctor_sub_option == "1":
        display_all_doctors(doctor_manage.doctors)
    elif doctor_sub_option == "2":
        add_new_doctors(doctor_manage)
    elif doctor_sub_option == "3":
        remove_doctors(doctor_manage)
    elif doctor_sub_option == "4":
        print("------Go back to the main-------")

def display_all_patients(patients):
    for index,patient in enumerate(patients):
        print(f"{index:2} - {patient}")

def add_new_patients(patient_manage):
    patient_first_name=input("Please enter the patient's first name ---> ")
    patient_last_name=input("Please enter the patient's last name ---> ")
    patient_id=input("Please enter the patient's id ---> ")
    patient_age=int(input("Please enter the patient's age ---> "))
    patient_manage.add_new_boarding_patient(patient_first_name,patient_last_name,patient_id,patient_age)

def discharge_patients(patient_manage):
    patient_id= input("Please enter the patient's Id to discharge from the hospital ---> ")
    patient_manage.discharge_patients(patient_id)
    display_all_patients(patient_manage.patients)

def show_option_patient(patient_menu):
    patient_sub_option = input(patient_menu)
    if patient_sub_option == "1":
        display_all_patients(patient_manage.patients)
    elif patient_sub_option == "2":
        add_new_patients(patient_manage)
    elif patient_sub_option == "3":
        discharge_patients(patient_manage)
    elif patient_sub_option == "4":
        print("------Go back to the main-------")
    print("")

def hospital_bill_fun():
    print("Which patient do you want to pay the bill?")
    patient_id = input("Enter the patient id to proceed\n")
    selected_patient = []

    for patient in patient_manage.patients:
        if patient.get_id() == patient_id:
            selected_patient.append(patient)

    if(selected_patient):
        for patient_data in selected_patient:
            print(patient_data)
        total_fee = 0
        medicine_fee = int(input("Medicine Fee: $"))
        doctor_fee = int(input("Doctor Fee: $"))
        room_fee = int(input("Room Fee: $"))
        total_fee = medicine_fee + doctor_fee + room_fee

        for s_patient in selected_patient:
            bill_manage.add_new_bill(s_patient.get_first_name(),s_patient.get_last_name(),s_patient.get_id(),str(medicine_fee),str(doctor_fee),str(room_fee),str(total_fee))
        print("Total Fee:",total_fee)
        print("Payment Successfull!")
    else:
        print("Your patient is not found in database!")

def save_data():
    dataset = open("patient_detail.csv", "w")
    dataset.write("first_name,last_name,patient_id,age,date_of_birth,admit_date,discharge_date\n")
    for f, b in zip(patient_manage.patients, patient_manage.date_type):
        dataset.write("{},{},{},{},{},{},{}\n".format(f.get_first_name(),f.get_last_name(),f.get_id(),f.get_age(),b.get_date_of_birth(),b.get_admit_date(),b.get_discharge_date().strip('\n')))
    print("Patient Data saved successfully!")
    dataset.close()

    dataset = open("pay_bill.csv", "w")
    dataset.write("first_name,last_name,patient_id,medicine_fee,doctor_fee,room_fee,total_fee\n")
    for index,record in enumerate(bill_manage.ledger):
        dataset.write("{},{},{},{},{},{},{}\n".format(record.get_bill_first_name(),record.get_bill_last_name(),record.get_bill_patient_id(),record.get_medicine_fee(),record.get_doctor_fee(),record.get_room_fee(),record.get_total_fee().strip('\n')))
    print("Bill Data saved successfully!")
    dataset.close()

def main():
    menu = f"1. Doctor detail\n" \
           f"2. Patient detail\n" \
           f"3. Pay bill\n" \
           f"4. Display Bill Records\n" \
           f"5. Make a exit\n" \
           f">> "
    doctor_menu = f"1. Show all doctor details\n" \
                  f"2. Add doctor details\n" \
                  f"3. Remove doctor detail\n" \
                  f"4. Go back to the main\n"
    patient_menu=f"1. Show all patient detail\n" \
                 f"2. Add the new patient\n" \
                 f"3. Discharge the patient\n" \
                 f"4. Go back to the main\n"
    option = input(menu)
    while option != "5":
        if option == "1":
            show_option_doctor(doctor_menu)
        elif option == "2":
            show_option_patient(patient_menu)
        elif option == "3":
            hospital_bill_fun()
        elif option == "4":
            print('{:5}| {:7}| {:12}| {:12}| {:12}| {:12}'.format("ID","Name","Medicine Fee","Doctor Fee","Room Fee","Total Fee"))
            for index,each_record in enumerate(bill_manage.ledger):
                print(f"{each_record}")
        print()
        option = input(menu)

    save_data()
    print("----Thank you for using my app----")


if __name__ == '__main__':
    main()
