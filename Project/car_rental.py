"""5. Problem: Car Rental System
Description: Develop a Car class for a rental system, including attributes like model, color, and methods for calculating rental charges."""
class car:
    def __init__(self,car_model,car_color):
        self.car_model = car_model
        self.car_color = car_color
        self.car_rent_per_hour = 50
        
    def calculate_rent_per_hour(self):
        hour = float(input("Enter hour to calculate rent : "))
        if hour > 0:
            print(f"You worked \"{hour}hrs\"\nNow your salary is Rs{self.car_rent_per_hour*hour} ")

emp1 = car(input("Enter model of the car : "),input("Enter color of the car : "))
emp1.calculate_rent_per_hour()