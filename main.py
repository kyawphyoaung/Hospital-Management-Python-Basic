from doctor_manager import DoctorManager
from patient_manager import PatientManager

doctor_manage=DoctorManager()
doctor_manage.load_doctor_detail()
patient_manage=PatientManager()
patient_manage.load_patient_detail()

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

# def hospital_bill_func():
    

def main():
    menu = f"1. Doctor detail\n" \
           f"2. Patient detail\n" \
           f"3. Pay bill\n" \
           f"4. Make a exit\n" \
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
    while option != "4":
        if option == "1":
            show_option_doctor(doctor_menu)
        elif option == "2":
            show_option_patient(patient_menu)
        elif option == "3":
            # hospital_bill_func()
            print("Which patient do you want to pay the bill?")
            patient_id = input("Enter the patient id to proceed\n")
            for patient in patient_manage.patients:
                if patient.get_id() == patient_id:
                    print(patient)

        print()
        option = input(menu)
    print("----Thank you for using my app----")


if __name__ == '__main__':
    main()
