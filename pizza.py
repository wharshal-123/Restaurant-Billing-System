
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["WaradeCafe"]
orders = db["orders"] 

while True:

    print("\n")
    print("Welcome to Warade Cafe\n")

    name = input("Enter your Name: ")
    cont = int(input("Enter your contact No: "))

    print("***** CAFE MENU *****\n")
    print("1 - Pizza")
    print("2 - Pasta")
    print("3 - Burger")
    print("4 - Maggie")
    print("5 - Exit")

    order = int(input("Enter your choice: "))

    if order == 1:
        print("You chose Pizza.\n")
        print("PIZZA MENU\n")
        print("1 - Corn Pizza")
        print("2 - Onion Pizza")
        print("3 - Paneer Pizza")
        print("4 - Margita Pizza")

        sub = (input("Enter your choice: "))

        if sub == "Corn Pizza" or 1:
            print("\nThanks for choosing Corn Pizza.")
            print("The 1 Corn Pizza cost is 100 rupees.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Corn Pizza.")
            cost = x * 100
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Corn Pizza is {totalbill}.")
        
        elif sub ==  "Onion Pizza" or 2:
            print("\nThanks for choosing Onion Pizza.")
            print("The 1 Onion Pizza cost is 120 rupees.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Onion Pizza.")
            cost = x * 120
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Onion Pizza is {totalbill}.")
        
        elif sub == "Paneer Pizza" or 3:
            print("\nThanks for choosing Paneer Pizza.")
            print("The 1 Paneer Pizza cost is 150 rupees.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Paneer Pizza.")
            cost = x * 150
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Paneer Pizza is {totalbill}.")
        
        elif sub == "Margita Pizza" or 4:
            print("\nThanks for choosing Margita Pizza.")
            print("The 1 Margita Pizza cost is 200 rupees.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Margita Pizza.")
            cost = x * 200
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Margita Pizza is {totalbill}.")
        
        else:
            print("Sorry, we don't have this pizza.")
        
    elif order == 2:
        print("You chose Pasta\n")
        print("PASTA MENU\n")
        print("1 - Redsos Pasta")
        print("2 - Whitesos Pasta")
        print("3 - Cheese Pasta")

        sub = (input("Enter your choice: \n"))

        if sub == "Redsos Pasta" or 1:
            print("\nThanks for choosing Redsos Pasta.")
            print("The 1 Redsos Pasta cost is 50 rupees.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Redsos Pasta.")
            cost = x * 50
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Redsos Pasta is {totalbill}.")
        
        elif sub == "Whitesos Pasta" or 2:
            print("\nThanks for choosing Whitesos Pasta.")
            print("The 1 Whitesos Pasta cost is 70 rupees.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Whitesos Pasta.")
            cost = x * 70
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Whitesos Pasta is {totalbill}.")
        
        elif sub == "Cheese Pasta" or 3:
            print("\nThanks for choosing Cheese Pasta.")
            print("The 1 Cheese Pasta cost is 200 rupees.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Cheese Pasta.")
            cost = x * 200
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Cheese Pasta is {totalbill}.")
        
        else:
            print("Sorry, we don't have this pasta.")

    elif order == 3:
        print("You chose Burger")
        print("BURGER MENU\n")
        print("1 - Veg Burger")
        print("2 - Paneer Burger")
        print("3 - Aalupaty Burger")

        sub = (input("Enter your choice: "))

        if sub == "Veg Burger" or 1:
            print("\nThanks for choosing Veg Burger.")
            print("The 1 Veg Burger cost is 59 rupees.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Veg Burger.")
            cost = x * 59
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Veg Burger is {totalbill}.")
        
        elif sub == "Paneer Burger" or 2:
            print("\nThanks for choosing Paneer Burger.")
            print("The 1 Paneer Burger cost is 89 rupees.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Paneer Burger.")
            cost = x * 89
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Paneer Burger is {totalbill}.")
        
        elif sub == "Aalupaty Burger" or 3:
            print("\nThanks for choosing Aalupaty Burger.")
            print("The 1 Aalupaty Burger cost is 110 rupees.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Aalupaty Burger.")
            cost = x * 110
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Aalupaty Burger is {totalbill}.")
        
        else:
            print("Sorry, we don't have this burger.")

    elif order == 4:
        print("You chose Maggie\n")
        print("MAGGIE MENU\n")
        print("1 - Plain Maggie")
        print("2 - Cheese Maggie")
        print("3 - Veg Maggie")
    
        sub = (input("Enter your choice: "))

        if sub == "Plain Maggie" or 1:
            print("\nThanks for choosing Plain Maggie.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Plain Maggie.")
            cost = x * 60
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Plain Maggie is {totalbill}.")
        
        elif sub == "Cheese Maggie" or 2:
            print("\nThanks for choosing Cheese Maggie.")
            print("The 1 Cheese Maggie cost is 100 rupees.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Cheese Maggie(s).")
            cost = x * 100
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Cheese Maggie is {totalbill}.")
        
        elif sub == "Veg Maggie" or 3:
            print("\nThanks for choosing Veg Maggie.")
            print("The 1 Veg Maggie cost is 80 rupees.")
            x = int(input("Enter the quantity to order: "))
            print(f"You have ordered {x} Veg Maggie.")
            cost = x * 80
            gst = cost * 0.18
            totalbill = cost + gst
            print(f"The total bill of Veg Maggie is {totalbill}.")
        
        else:
            print("Sorry, we don't have this Maggie.")

    elif order == 5:
        print("Thank you for visiting Warade Cafe!")
        break

    else:
        print("Sorry, we don't have option", order)

    order_data = {
        "name":name,
        "contact":cont,
        "items": sub,
        "quantity":x,
        "cost":cost,
        "gst":gst,
        "total amount":totalbill
    }
    result = orders.insert_one(order_data)
    print("The Order is placed successfully!!\n")
    print("Thank You",name,"please visit again.")
    print("-------------////////--------------")