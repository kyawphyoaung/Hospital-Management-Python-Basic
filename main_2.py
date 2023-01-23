from classBuilding import *

pList = []
dList = []
bList = []

def enterPatientDetails():
    print("Enter patient details")
    firstName = input("Enter FirstName ")
    lastName = input("Enter LastName ")
    iD = input("Enter iD ")
    age = input("Enter age ")
    dOB = input("Enter birth date with dd,mm,yy ").split(",")
    doc = enterDoctor()
    admittedDate = input("Enter admitted date with dd,mm,yy ").split(",")
    dischargedDate = input("Enter discharged date with dd,mm,yy ").split(",")
    adddOB = Date(dOB[0],dOB[1],dOB[2])
    addadmittedDate = Date(admittedDate[0],admittedDate[1],admittedDate[2])
    adddischargedDate = Date(dischargedDate[0],dischargedDate[2],dischargedDate[2])
    addPatient = Patient(firstName, lastName, iD, age, adddOB, doc, addadmittedDate, adddischargedDate)
    print()
    addPatient.printDetails()
    return addPatient

def enterDoctor():
    print("Enter doctor details ")
    firstName = input("Enter firstName ")
    lastName = input("Enter lastName ")
    speciality = input("Enter speciality ")
    addDoctor = Doctor(firstName, lastName, speciality)
    return addDoctor

def enterMedicalBill():
    print("Enter billing details")
    patientId = input("Enter Patient id ")
    pharmacy = input("Enter Pharmacy charges ")
    doctorFee = input("Enter Doctor Fee ")
    room = input("Enter Room charges ")
    addBill = Bill(patientId, pharmacy, doctorFee, room)
    return addBill

stop = False
while not stop:
    print("""
    1.Enter patient details
    2.Print patient's medical bill
    3.Create a list of patients
    4.Create a list of doctors
    5.View list of patients
    6.View list of doctors
    7.Exit
    """)
    ans=int(input("What do you want to do?"))
    if ans==1:
        addPatient = enterPatientDetails()
        pList.append(addPatient)
        print()
        addBill = enterMedicalBill()
        bList.append(addBill)

    elif ans == 2:
        pID = int(input("Enter patient ID "))
        print("Please write patient number in order from 1")
        bList[pID - 1].printDetails()

    elif ans == 3:
        pCount = int(input("How many patient number? - "))
        for i in range(pCount):
            addPatient = enterPatientDetails()
            pList.append(addPatient)
            print()

    elif ans == 4:
        dCount = int(input("How many doctor number? - "))
        for i in range(dCount):
            addDoctor = enterDoctor()
            dList.append(addDoctor)
            print()

    elif ans == 5:
        print()
        for i in range(len(pList)):
            pList[i].printDetails()
            print()

    elif ans == 6:
        print()
        for i in range(len(dList)):
           dList[i].printDetails()
           print()
        
    elif ans == 7:
        print("Goodbye\n")
        stop = True

    elif (ans>7 or ans<1):
        print("error occured")
