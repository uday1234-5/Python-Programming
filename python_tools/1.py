#question 1 : Bridge Toll Management System

vehicle = {}

while True:
    print("1. Add Vehicle Entry")
    print("2. Display Vehicle Entries")
    print("3. Calculate Total Toll Entries")
    print("4. Search Vehicle by number")
    print("5. Exist")
    print("*"*60)
    choice = input("Enter your choice : ")
    
    
    if choice == "1":
        number = input("Enter Vehicle Number : ")
        type = input("Enter Vehicle Type (Car/Truck/Bus) : ")
        toll = input("Enter Toll amount : ")
        vehicle[number] = {"Type":type,"Toll amount":toll}
        print(vehicle)
        print("Your entry is added to the toll management system.")
        print("*"*60)
    elif choice == "2":
        if vehicle:
            print("number \t\t type\t\tamount")
            print("-"*60)
            for x,y in vehicle.items():
                print(f"{x}\t\t{y['Type']}\t\t{y['Toll amount']}")
        else:
            print("no vehicle is found")
        print("*"*60)
    elif choice == "3":
        if number in vehicle:
            detail = vehicle[number]
            z = 0
            for x,y in vehicle.items():
                z += int(detail['Toll amount'])
            print(f"Vehicle total Toll amount : {z}")
        print("*"*60)         
        
    elif choice == "4":
        number = input("Enter vehicle number to search for a vehicle.")
        if number in vehicle:
            detail = vehicle[number]
            print(f"Vehicle Type : {detail['Type']}")
            print(f"Vehicle Toll amount : {detail['Toll amount']}")
        else:
            print(f"Your vehicle is not found by this number({x})")   
        print("*"*60)      
    elif choice == "5":
        print("Exist the program")
        break
    else:
        print("Invalid choice!! please enter the choice from 1 to 5")