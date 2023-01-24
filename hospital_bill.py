class HospitalBill:
    def __init__(self,first_name,last_name,patient_id,medicine_fee,doctor_fee,room_fee,total_fee):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__patient_id = patient_id
        self.__medicine_fee=medicine_fee
        self.__doctor_fee=doctor_fee
        self.__room_fee=room_fee
        self.__total_fee=total_fee

    def get_bill_first_name(self):
        return self.__first_name

    def get_bill_last_name(self):
        return self.__last_name

    def get_bill_patient_id(self):
        return self.__patient_id

    def get_medicine_fee(self):
        return self.__medicine_fee

    def get_doctor_fee(self):
        return self.__doctor_fee

    def get_room_fee(self):
        return self.__room_fee

    def get_total_fee(self):
        return self.__total_fee

    def __str__(self):
        print('{:5}| {:7}| {:12}| {:12}| {:12}| {:12}'.format("ID","Name","Medicine Fee","Doctor Fee","Room Fee","Total Fee"))
        output = '{:5}| {:7}| {:12}| {:12}| {:12}| {:12}'.format(self.__patient_id,self.__first_name,self.__medicine_fee+"$",self.__doctor_fee+"$",self.__room_fee+"$",self.__total_fee.strip('\n')+"$")
        return output