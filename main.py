
def show_menue():
    print("welcome to sadjad store")
    print("1- add")
    print("2- edit")
    print("3- delete")
    print("4- show list")
    print("5- search")
    print("6- buy")
    print("7- exit")

def add():
    product_dict={}
    product_dict["id"] = input("Please enter the product id: ")
    product_dict["name"] = input("Please enter the product Name: ")
    product_dict["price"] = input("Please enter the product Price: ")
    product_dict["count"] = input("Please enter the product Amount: ")
    products.append(product_dict)
    print("Done!" + "\n")
def edit():
    show_list()
    str = input("What product do you want to edit? please enter the id of this product: ")
    flag = False
    for product in products:
        if product["id"] == str:
            while True:
                choice = input("What field should be update? press 1 for name and press 2 for price and press 3 for amount: ")
                if choice == "1":
                    product['name'] = input("Please enter the new data: ")
                    break
                elif choice == "2":
                    product['price'] = input("Please enter the new data: ")
                    break
                elif choice == "3":
                    product['count'] = input("Please enter the new data: ")
                    break
                else:
                    print("invalid input!")
            flag = True
            print("Done!" + "\n")
            break
    if flag == False:
        print("This product does not exict.")
        print()

def delete():
    show_list()
    flag = False
    str = input("What product do you want to delete? please enter the id of this product: ")
    for product in products:
        if product['id'] == str:
            products.remove(product)
            flag = True
            print("Done!" + "\n")
            break
    if flag == False:
        print("This product does not exict.")
        print()

def show_list():
    print()
    print("ID\t\t\tName\t\tPrice\t\tAvailable")
    print("-------------------------------------------")
    for product in products:
        print(f"{product['id']}\t\t{product['name']}\t\t{product['price']}\t\t{product['count']}")
        print()

products = []

def load_data_from_database():
    file = open("database.csv", "r")
    text = file.read()
    rows = text.split("\n")
    for row in rows:
        if row:
            info = row.split(",")
            new_dict = {"id":info[0], "name":info[1], "price":info[2], "count":info[3]}
            products.append(new_dict)

def search():
    str = input("Plese enter the name for search: ")
    flag = False
    for product in products:
        if product['name'] == str:
            print("This product is exist: ")
            print("ID\t\t\tName\t\tPrice\t\tAvailable")
            print("-------------------------------------------")
            print(f"{product['id']}\t\t{product['name']}\t\t{product['price']}\t\t{product['count']}")
            print()
            flag = True
    if flag == False:
        print("This product does not exist.")
        print()


def buy():
    show_list()
    str = input("What product do you want? enter the name: ")
    flag = False
    for product in products:
        if product['name'] == str:
            num = int(input("How many?"))
            while True:
                if num > int(product["count"]):
                    num = int(input("Not available in this number. plese enter Less amount: "))
                else:
                    product["count"] = int(product["count"])
                    product["count"] -= num
                    break
            product['price'] = int(product['price'])
            print(f"This is your bill: {num} {str} and it costs {num*product['price']} toman.")
            flag = True
            print()
    if flag == False:
        print("This product does not exist.")


def save_to_database():
    with open("database.csv", "w") as file:
        for product in products:
            new_data = str(product['id']) + ',' + str(product['name']) + ',' + str(product['price']) + ',' + str(product['count'])
            file.write(new_data + "\n")
    # with open("database.csv") as file:
    #     lines = file.readlines()
    #     print(lines)
    # with open("database.csv","w"):
    #     for line in lines:



load_data_from_database()
while True:
    show_menue()
    choice = int(input("please choice from menu: "))
    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        delete()
    elif choice == 4:
        show_list()
    elif choice == 5:
        search()
    elif choice == 6:
        buy()
    elif choice == 7:
        save_to_database()
        exit()
