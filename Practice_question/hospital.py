class Patient:
    def __init__(self,patient_id,patient_name,age,gender,contact_num):
        self.__patient_name = patient_name     #private variable
        self.__patient_id = patient_id
        self.__age = age
        self.__contact_num = contact_num
        self.__gender = gender
    def get_patient_info(self):
        return {
        "Patient_Id"  : self.__patient_id,
        "Name" : self.__patient_name,
        "Age" :self.__age ,
        "gender":self.__gender,
        "contact":self.__contact_num
        }
class Doctor:
    def __init__(self,doctor_id,name,specialist):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialist = specialist
    def get_doctor_info(self):
        return {
            "doctor_id" : self.__doctor_id,
            "Name" : self.__name,
            "specialist":self.__specialist
        }
class medical_records:
    def __init__(self):
        self.__records = {}
    def add_records(self,patient_detail,doctor_detail,disease,medication):
        self.__records[patient_detail.get_patient_info()['Patient_Id']] = {"Patient":patient_detail.get_patient_info(),
                                                                           "Doctor" : doctor_detail.get_doctor_info(),
                                                                           "Disease": disease,
                                                                           "Medication" : medication}
    
    def get_medical_record(self):
        return self.__records
#Driver Code
patient1 = Patient(1,'Ravi',23,'male','+97427962476')
patient2 = Patient(2,'Saket',34,'male','+97427876743')
patient3 = Patient(3,'Saket',54,'male','+97427000674')
# print(patient2.get_patient_info()["Name"])

# print(patient2.get_patient_info())
# print(patient1._Patient__patient_name)

doctor1 = Doctor(1,"Dr. Santosh","Cardiologist")
doctor2 = Doctor(2,"Dr. Kunal","Neurologist")

record = medical_records()
record.add_records(patient1,doctor1,'Heart Problem','Asprin')
record.add_records(patient2,doctor2,'Brain Problem','Paracetamole')
record.add_records(patient3,doctor2,'Brain Problem','cetamole')
print(record.get_medical_record())

patient_name  = input("Enter Patient Name : ")

# for x,y in record.get_medical_record().items():
#     if patient_name == y['Patient']['Name']:
#         print(y['Patient'])

for i in record.get_medical_record():
    if patient_name == record.get_medical_record()[i]['Patient']['Name']:
        print(record.get_medical_record()[i]['Patient']['Patient_Id'])