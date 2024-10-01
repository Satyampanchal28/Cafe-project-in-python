
menu = { 
    'Pizza': 50,
    'Pasta': 50,
    'Burger': 100,
    'Salad': 50,
    'Coffee': 80,
}


print("Welcome to Satyam Restaurant")
print("Pizza: Rs50\n Pasta: Rs50\n Burger: Rs100\n Salad: Rs50\n Coffee: Rs80")

order_total = 0

item_1 = input("Enter the name of tiem you want to order = ")
if item_1 in menu:
    order_total = order_total + menu[item_1]
    print(f"your item{item_1} has been added to your order")
else:  
    print(f"Oreded itme {item_1} is not avaialable yet")


another_order = input("Do you want to aad another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second Item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item{item_2} has been added to order")
    else:
        print(f"Ordered item{item_2} is not avaialable!")

    
print(f"The toal amount of item to pay is {order_total} ")


