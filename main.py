import csv
from datetime import date
from doctor_manager import DoctorManager
from patient_manager import PatientManager
from bill_manager import Bill_Manager
from date_type import DateType

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
    print('{:5}| {:14}| {:12}| {:4}| {:14}| {:12}| {:12}'.format("ID","Name","DateofBirth","Age","Physician","Admit Date","Dicharge Date"))
    for index,patient in enumerate(patients):
        print(patient)

def add_new_patients(patient_manage):
    patient_first_name=input("Please enter the patient's first name ---> ")
    patient_last_name=input("Please enter the patient's last name ---> ")
    patient_id=input("Please enter the patient's id ---> ")
    input_dOB = input("Enter birth date with dd,mm,yyyy --->").split(",")
    patient_dOB = DateType(input_dOB[0],input_dOB[1],input_dOB[2])
    # Patient Age calculation
    today = date.today()
    admit_date= DateType(today.day,today.month,today.year)
    discharge_date = DateType("00","00","0000")
    patient_age = today.year - int(input_dOB[2]) - ((today.month, today.day) < (int(input_dOB[1]), int(input_dOB[0])))
    patient_manage.add_new_boarding_patient(patient_first_name,patient_last_name,patient_id,patient_age,patient_dOB,admit_date,discharge_date)

def discharge_patients(patient_manage):
    patient_id= input("Please enter the patient's Id to discharge from the hospital ---> ")
    for patient in patient_manage.patients:
        if patient.get_id() == patient_id:
            print(patient)
    print("Do you want to discharge today or orther date?\n")
    print("1. Today\n")
    print("2. Input Date\n")
    discharge_opt = input(">>")
    if(discharge_opt == 1):
        today = date.today()
        discharge_date = today.day+","+today.month+","+today.year
        patient_manage.discharge_patients(patient_id,discharge_date)
    elif(discharge_opt == 2):
        dicharge_date = input("Enter discharge date with dd,mm,yyyy --->")
        patient_manage.discharge_patients(patient_id,dicharge_date)
    else:
        print("Your input is wrong!")

    display_all_patients(patient_manage.patients)

def show_option_patient(patient_menu):
    patient_sub_option = input(patient_menu)
    if patient_sub_option == "1":
        display_all_patients(patient_manage.patients)
    elif patient_sub_option == "2":
        add_new_patients(patient_manage)
    elif patient_sub_option == "3":
        #Assign Doctor
        print("Assign Doctor")
    elif patient_sub_option == "4":
        discharge_patients(patient_manage)
    elif patient_sub_option == "5":
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
    dataset.write("first_name,last_name,patient_id,age,date_of_birth,A.P_fname,A.P_lname,admit_date,discharge_date\n")
    for f in zip(patient_manage.patients):
        attending_physician = f[0].get_attending_physician()
        a_p_f_n = attending_physician.get_first_name()
        a_p_l_n = attending_physician.get_last_name()

        doB = f[0].get_date_of_birth()
        dob_format = doB.__str__().replace(",","/")

        admit_date = f[0].get_admit_date()
        admit_date_format = admit_date.__str__().replace(",","/")

        dicharge_date = f[0].get_discharge_date()
        dicharge_date_format = dicharge_date.__str__().replace(",","/").strip("\n")
        
        dataset.write("{},{},{},{},{},{},{},{},{}\n".format(f[0].get_first_name(),f[0].get_last_name(),f[0].get_id(),f[0].get_age(),a_p_f_n,a_p_l_n,dob_format,admit_date_format,dicharge_date_format))
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
                  f"4. Go back to the main\n" \
                  f">>"
    patient_menu=f"1. Show all patient detail\n" \
                 f"2. Add the new patient\n" \
                 f"3. Assign Doctor\n" \
                 f"4. Discharge the patient\n" \
                 f"5. Go back to the main\n" \
                 f">>"
    option = input(menu)
    while option != "5":
        if option == "1":
            show_option_doctor(doctor_menu)
        elif option == "2":
            show_option_patient(patient_menu)
        elif option == "3":
            hospital_bill_fun()
        elif option == "4":
            for index,each_record in enumerate(bill_manage.ledger):
                print(f"{each_record}")
        print()
        option = input(menu)

    save_data()
    print("----Thank you for using my app----")


if __name__ == '__main__':
    main()
