#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Admin-User file
import json
import random as r

class Admin:
    def __init__(self):
        a=int(input("1 for add new item\n2 for edit food item\n3 for remove a food item\n4 for see all itmes"))
        if a==1:
            name = input("Enter name of the item: ")
            quantity = float(input("Enter quantity of the item: "))
            price = float(input("Enter price of the item: "))
            stock = int(input("Enter stock of the item: "))
            discount = float(input("Enter discount of the item: "))
            self.add_item(name, quantity, price, stock, discount)
        elif a==2:
            id=int(input("enter id of that item which you want to edit : "))
            self.edit_item(id)
        elif a==3:
            id=int(input("enter id of that item which you want to remove : "))
            self.remove_item(id)
        elif a==4:
            self.view_all()
        
    
    def store_item(self, name, quantity, price, stock, discount, id):
        with open("items.json", "a") as f:
            store = {
                "Item_Id": id,
                "Item_Name": name,
                "Item_Price": price,
                "Item_Stock": stock,
                "Item_Discount": discount
            }
            json.dump(store, f)
            f.write('\n')

    def add_item(self, name, quantity, price, stock, discount):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.discount = discount
        self.id = r.randint(1, 1000)
        self.store_item(self.name, self.quantity, self.price, self.stock, self.discount, self.id)
        print("Item successfully added")

    def view_all(self):
        with open("items.json", "r") as f:
            for line in f:
                data = json.loads(line)
                print(data)

    def remove_item(self, id):
        items = []
        with open("items.json", "r") as f:
            for line in f:
                item = json.loads(line)
                if item["Item_Id"] != id:
                    items.append(item)
        with open("items.json", "w") as f:
            for item in items:
                json.dump(item, f)
                f.write('\n')
            print(f"The item with ID {id} has been removed successfully.")

    def edit_item(self, id):
        with open("items.json", "r") as f:
            items = []
            for line in f:
                item = json.loads(line)
                if item["Item_Id"] == id:
                    print(f"Item with ID {item['Item_Id']} found. Choose what you want to edit:")
                    print("1. Item Name")
                    print("2. Item Price")
                    print("3. Item Stock")
                    print("4. Item Discount")
                    choice = int(input("Enter your choice (1-4): "))
                    if choice == 1:
                        new_name = input(f"Enter new name for the item {item['Item_Name']}: ")
                        item["Item_Name"] = new_name
                    elif choice == 2:
                        new_price = float(input(f"Enter new price for the item {item['Item_Price']}: "))
                        item["Item_Price"] = new_price
                    elif choice == 3:
                        new_stock = int(input(f"Enter new stock for the item {item['Item_Stock']}: "))
                        item["Item_Stock"] = new_stock
                    elif choice == 4:
                        new_discount = int(input(f"Enter new discount for the item {item['Item_Discount']}: "))
                        item["Item_Discount"] = new_discount
                    else:
                        print("Invalid choice!")
                        break
                    items.append(item)
                    print("Item updated successfully!")
                    break
            else:
                print(f"No item found with ID {id}.")
                return
        items1=[]
        with open("items.json", "r") as f:
            for line in f:
                item = json.loads(line)
                if item["Item_Id"] != id:
                    items1.append(item)
                elif item['Item_Id']==id:
                    items1.extend(items)
        with open("items.json", "w") as f:
            for item in items1:
                json.dump(item, f)
                f.write('\n')
                
class User:
    def __init__(self):
        self.choice = int(input("Enter 1 for Place New Order\nEnter 2 for Order History\nEnter 3 for Update Profile\n"))

        if self.choice == 1:
            self.place_order()
        elif self.choice == 2:
            self.order_history()
        elif self.choice == 3:
            self.update_profile()

    def place_order(self):
        with open('items.json', 'r') as f:
            for line in f:
                item=json.loads(line)
                print(f"ID :- {item['Item_Id']} |  {item['Item_Name']} |  {item['Item_Price']}")

            items_selected = list(map(int, input("Enter the item IDs of the items you want to order: ").split()))
            total_price = 0

            print("Your selected orders are:")
            with open('items.json','r') as f:
                items=[]
                for line in f:
                    item=json.loads(line)
                    if item['Item_Id'] in items_selected:
                        quantity = int(input(f"How much quantity of {item['Item_Name']} you want: "))
                        items.append(f"{quantity} {item['Item_Name']}")
                        price = item['Item_Price'] * quantity
                        print(f"{item['Item_Name']} with price tag of {item['Item_Price']} for {quantity} quantity is: {price}")
                        total_price += price
                print(f"So total money you want to pay is : {total_price}")

            with open("user_order.json", "a") as f:
                order = {"User": username, "Items_selected": items, "Total_price": total_price}
                json.dump(order, f)
                f.write('\n')

    def order_history(self):
        with open('user_order.json', 'r') as f:
            for line in f:
                order=json.loads(line)
                if order['User'] == username:
                    print(order)

    def update_profile(self):
        with open('info_user.json', 'r') as f:
            lines = f.readlines()

        for i in range(len(lines)):
            user = json.loads(lines[i])
            if user['username'] == username:
                field = int(input("Enter 1 for update username\nEnter 2 for update phone_no\nEnter 3 for update email\nEnter 4 for update address\n"))
                if field == 1:
                    new_username = input("Enter new username: ")
                    user['username'] = new_username
                elif field == 2:
                    new_phone_no = input("Enter new phone no.: ")
                    user['phone_no'] = new_phone_no
                elif field == 3:
                    new_email = input("Enter new email id: ")
                    user['email'] = new_email
                elif field == 4:
                    new_address = input("Enter new address: ")
                    user['address'] = new_address

                lines[i] = json.dumps(user) + "\n"
            print("Updated successfully")

        with open('info_user.json', 'w') as f:
            f.writelines(lines)
      
inp=int(input("Enter 1 if you access admin\nEnter 2 if you are user: "))
if inp==2:    
    print("Welcome to User Page")
    b=int(input("Enter 1 if you already have an account\nEnter 2 if you don't have an account: "))
    with open("info_user.json",'r') as f:
        if b==1:
            username=input("Enter Username : ")
            for line in f:
                i=json.loads(line)
                if i["username"]==username:
                    password=input("Enter Your password : ")
                    if i["password"]==password:
                         print("Login Successful!")
                         user=User()
                    else:
                        print("Incorrect password")
                else:
                    print("Incorrect username, please try again")
        elif b==2:
            username=input("Enter your name : ")
            password=input("Enter your password: ")
            phone_no=input("Enter your phone no.: ")
            email=input("Enter your email id: ")
            address=input("Enter your address: ")
            h={"username":username,"password":password,'phone_no':phone_no,'email':email,'address':address}
            print("Your account created :) ")
            json.dump(h,f)
            f.write('\n')    
            
elif inp==1:
    print("Welcome to Admin Page")
    b=int(input("Enter 1 if you already have an account\nEnter 2 if you don't have an account: "))
    with open("info_admin.json",'r') as f:
        if b==1:
            username=input("Enter Username : ")
            for line in f:
                i=json.loads(line)
                if i["username"]==username:
                    password=input("Enter Password : ")
                    if i["password"]==password:
                         print("Login Successful!")
                         admin = Admin()
                         break
                    else:
                        print("incorrect password please try again")
                        break
                else:
                        print("incorrect username please try again")
                        break
        elif b==2:
            c=input("Enter your name : ")
            d=input("Enter your password: ")
            e={"username":c,"password":d}
            json.dump(e,f)
            f.write('\n')


# In[ ]:


'''
info_user.json
{"username": "Mohit K", "password": "12345", "phone_no": "8696435149", "email": "mohitk26@gmail.com", "address": "sikar"}

info_admin.json
{"username": "Mohit Krishnia", "password": "12345"}
{"username": "Mohit Krishnia", "password": "12345"}


user_order.json
{"User": "Mohit K", "Items_selected": ["2 Men T-shirt", "4 Shoes"], "Total_price": 239.94}
{"User": "Mohit K", "Items_selected": ["2 Pajama"], "Total_price": 500500}
{"User": "Mohit K", "Items_selected": ["2 Pajama"], "Total_price": 1000.0}
{"User": "Mohit K", "Items_selected": ["2 Women T-shirt"], "Total_price": 400.0}
{"User": "Mohit K", "Items_selected": ["1 Men T-shirt"], "Total_price": 19.99}

items.json
{"Item_Id": 1, "Item_Name": "Men T-shirt", "Item_Price": 19.99, "Item_Stock": 50, "Item_Discount": 10}
{"Item_Id": 3, "Item_Name": "Shoes", "Item_Price": 49.99, "Item_Stock": 20, "Item_Discount": 0}
{"Item_Id": 595, "Item_Name": "Women T-shirt", "Item_Price": 200, "Item_Stock": 100, "Item_Discount": 0}
{"Item_Id": 571, "Item_Name": "Pajama", "Item_Price": 500, "Item_Stock": 120, "Item_Discount": 0}


I check on these data for my code you can create your own data or run on my own data by firstly saving these to files before running the code

'''

