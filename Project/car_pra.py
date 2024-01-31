class car:
    def __init__(self,maker,name,model,year,price):
        self.maker = maker
        self.name = name
        self.model = model
        self.year = year
        self.price = price
        self.available = True
        
    def display_car(self):
        return f'''
    Maker : {self.maker}
    Name : {self.name}
    Model : {self.model}
    Year : {self.year}
    Price : {self.price}'''
    
class dealership:
    def __init__(self,name):
        self.name = name 
        self.inventory = []
    
    def add_car_to_inventory(self,car):
        self.inventory.append(car)
        
    def display_available_car(self):
        for car in self.inventory:
            count = 1
            if car.available:
                print(count)
                print(car.display_car)
                count += 1
    def sell_car(self,cname,num):
        if num>0 and num <= len(self.inventory) and self.inventory[num-1].available :
            return self.inventory[num-1]
            
    
    
car1 = car('Hyundai','Creta','Knightkingdom',2023,1800000)
car2 = car('BMW','competition','M3',2017,30000000)
car3 = car('Tata','Nano','Zero',2012,114000)
# print(car1.display_car())

d1 = dealership("Uday Kushwah")
print(d1.add_car_to_inventory(car1))
print(d1.add_car_to_inventory(car1))
print(d1.add_car_to_inventory(car1))