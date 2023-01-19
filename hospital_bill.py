class HospitalBill:
    def __init__(self,medicine_fee,doctor_fee,room_fee):
        self.__medicine_fee=medicine_fee
        self.__doctor_fee=doctor_fee
        self.__room_fee=room_fee

    def get_medicine_fee(self):
        return self.__medicine_fee

    def get_doctor_fee(self):
        return self.__doctor_fee

    def get_room_fee(self):
        return self.__room_fee
