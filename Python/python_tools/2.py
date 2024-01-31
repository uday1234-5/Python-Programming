product = {}

while True:
    print("1. Add Product:")
    print("2. Display Product Catalog:")
    print("3. Update Product Quantity:")
    print("4. Search Product by ID:")
    print("5. Calculate Total Cost:")
    print("6. Remove Product by ID:")
    print("7. Exit")
    
    choice = input("Enter your choice(1-7) : ")
    
    
    if choice == "1":
        number = input("Enter product id : ")
        type = input("Enter Product name : ")
        toll = input("Enter Quantity : ")
        product[number] = {"Type":type,"Quantity":toll}
        print(product)
        print("Your product is added to the Online Shopping Management System.")
        print("*"*60)
    
    elif choice == "2":
        
        if product:
            print("Id \t\t Name\t\tQuantity")
            print("-"*60)
            for x,y in product.items():
                print(f"{x}\t\t{y['Type']}\t\t{y['Quantity']}")
        else:
            print("no product is found")
        print("*"*60)
    elif choice == "4":
        number = input("Enter product id to search for a product.")
        if number in product:
            detail = product[number]
            print(f"Product name : {detail['Type']}")
            print(f"Quantity : {detail['Quantity']}")
        else:
            print(f"Your product is not found by this id({x})")   
        print("*"*60)  
    
    elif choice == "6":
        id = input("Enter book ID to remove: ")

        if id in product:
            del product[id]
            print("product removed successfully!")
        else:
            print("product not found in the Online Shopping Management System!")
    
    
    
    
    elif choice == "7":
        print("Exist the program")
        break
    else:
        print("Invalid choice!! please enter the choice from 1 to 5")               
                    
       
        
    
    