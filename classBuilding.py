class Person:
    
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName
        
    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def __str__(self):
        return (self.__firstName + self.__lastName)

    def printDetails(self):
        print("Name - " + self.__firstName + " " + self.__lastName)
	
class Doctor(Person):

    def __init__(self, firstName, lastName, speciality):
        Person.__init__(self, firstName, lastName)
        self.__speciality = speciality

    def setSpeciality(self, speciality):
        self.__speciality = speciality

    def getSpeciality(self):
        return self.__speciality

    def printDetails(self):
        super().printDetails()
        print("Speciality - " + self.__speciality)

class Bill:

    def __init__(self,patientiD, pharmacyCharges, doctorFee, roomCharges):
        self.__patientiD = patientiD
        self.__pharmacyCharges = pharmacyCharges
        self.__doctorFee = doctorFee
        self.__roomCharges = roomCharges

    def setpatientiD(self,patientiD):
        self.__patientiD = patientiD

    def setpharmacyCharges(self,pharmacyCharges):
        self.__pharmacyCharges = pharmacyCharges

    def setdoctorFee(self,doctorFee):
        self.__doctorFee = doctorFee

    def setroomCharges(self,roomCharges):
        self.__roomCharges = roomCharges

    def getpatientiD(self):
        return self.__patientiD

    def getpharmacyCharges(self):
        return self.__pharmacyCharges

    def getdoctorFee(self):
        return self.__doctorFee

    def getroomCharges(self):
        return self.__roomCharges

    def printDetails(self):
        print("Patient Id - " + self.__patientiD)
        print("Pharmacy Charges - " + self.__pharmacyCharges)
        print("Doctor Fee - " + self.__doctorFee)
        print("Room Charges - " + self.__roomCharges)
        total = float(self.__pharmacyCharges) + float(self.__doctorFee) + float(self.__roomCharges)
        print("Total billing amout - " + str(total))
    

class Patient(Person):

    def __init__(self, firstName, lastName, iD, age, dOB,physicianName ,admittedDate, dischargedDate):
        Person.__init__(self, firstName, lastName)
        self.__iD = iD
        self.__age = age
        self.__dOB = dOB
        self.__physicianName = physicianName
        self.__admittedDate = admittedDate
        self.__dischargedDate = dischargedDate

    def setiD(self,iD):
        self.__iD = iD

    def setage(self,age):
        self.__age = age

    def setDOB(self,dOB):
        self.__dOB = dOB

    def setPhysicianName(self, physicianName):
        self.__physicianName = physicianName

    def setAdmittedDate(self,admittedDate):
        self.__admittedDate = admittedDate

    def setDischargedDate(self,dischargedDate ):
        self.__dischargedDate = dischargedDate

    def getiD(self):
        return self.__iD

    def getage(self):
        return self.__age

    def getDOB(self):
        return self.__dOB

    def getPhysicianName(self):
        return self.__physicianName

    def getAdmittedDate(self):
        return self.__admittedDate

    def getDischargedDate(self):
        return self.__dischargedDate

    def printDetails(self):
        super().printDetails()
        print("iD:",self.__iD)
        print("age:",self.__age)
        print("dOB:",self.__dOB)
        print("physicianName:",self.__physicianName.getFirstName(),self.__physicianName.getLastName())
        print("admittedDate:",self.__admittedDate)
        print("dischargedDate:",self.__dischargedDate)


class Date:

    def __init__(self, day, month, year):               
        self.__d = day
        self.__m = month
        self.__y = year

    def setDay(self, day):
        self.__d = day

    def setMonth(self, month):
        self.__m = month

    def setYear(self,year):
        self.__y = year

    def getDay(self):
        return self.__d

    def getMonth(self):
        return self.__m

    def getYear(self):
        return self.__y

    def __str__(self):
        return (str(self.__d) + "," + str(self.__m) + "," + str(self.__y))









    
        
        


    
        
        

    
        
        
        
         

    

    

    



   

        

    


        


