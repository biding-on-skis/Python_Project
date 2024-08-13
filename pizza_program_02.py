import time

def num_checker(question, low, high):
    while True:
        error = f"Enter a valid option"
        try:
            user_response = int(input(question))
            if low <= user_response <= high:
                return user_response
            else:
                print(error)
        except ValueError:
            print(error)


def string_checker(question, valid_ans):
    error = f"Enter a valid option from {valid_ans}"
    while True:

        user_response = input(question).lower()
        for item in valid_ans:
            if item == user_response or user_response == item[0]:
                return item
        print(error)


def not_blank(question):
    error = "Please give a valid answer"
    while True:
        user_name = input(question)
        if user_name != '':
            return user_name
        else:
            print(error)


def calculate_price(pizza_order_size, drink_size, delivery):
    pizza_prices = {'small': 4.99, 'medium': 7.99, 'large': 12.99}
    drink_prices = {'bottle': 5.50, 'can': 3.30}

    # Calculate pizza cost
    pizza_cost = sum(pizza_prices[size] for size in pizza_order_size)

    # Calculate drink cost if drink_size is not 'none'
    drink_cost = 0
    if drink_size != 'none':
        drink_cost = drink_prices[drink_size]

    # Add $6 surcharge for delivery
    if delivery == "delivery":
        return pizza_cost + drink_cost + 6.60
    else:
        return pizza_cost + drink_cost


# set maximum number of tickets below
MAX_PIZZA = 5

# Variables
yes_no = ["yes", "no"]
deliv_option = ["delivery", "pick up"]
size_option = ["large", "medium", "small"]
size_drink = ["can", "bottle"]

pizza_order = []
pizza_order_size = []
drink_order = []
drink_size = 'none'  # Initialize with a placeholder value

# Welcome message
print("<---Welcome to Puppet Pizzaria--->")
print()

# instructions question
want_instruc = string_checker("Would you like to read the instuctions: ", yes_no)

if want_instruc == "yes":
    print('''
|-----Instructions-----|
-When answering a question you can put the first letter of
 the word and it will go through as correct

-The code will ask for your name, phone number, address (if clicked delivery), 
 pizza flavour, size, drink and drink size.
    ''')

delivery = string_checker("Is this order to pick or delivery? ", deliv_option)

if delivery == "delivery":
    print("There is a $6 surcharge for delivery")

    # Ask for name and details
    print()
    name = not_blank("Enter your name: ")

    # Ask for phone number
    print()
    phone_num = num_checker("Enter your phone number: ", 0, 9999999999)

    # Ask for address
    print()
    address = not_blank("Enter your address: ")

else:
    # Ask for name and details
    name = not_blank("Enter your name: ")
    # Ask for phone number
    phone_num = num_checker("Enter your phone number: ", 0, 9999999999)

# Time wait
time.sleep(.5)

# Do you want the Menu?
print()
want_menu = string_checker(f"Hello {name}, would you like the menu? ", yes_no)

if want_menu == "yes":
    print('''\n
|-----------------MENU------------------|  
----------------------------------------|                        
Gourmet:                         Num id |
Lamb Kebab                          1   |
Crispy BBQ Pork Belly               2   | 
Chicken Bacon & Aoli                3   |
Smokehouse Meat lover               4   |
Peri-Peri Chicken                   5   |
The Lot                             6   |
----------------------------------------|                                    
Traditional:                            |
Philly Cheese steak                 7   |
Supreme                             8   |
Double Bacon Cheeseburger           9   |
Butter Chicken                      10  |
BBQ Meat lovers                     11  |
Chicken Supreme                     12  |
----------------------------------------|
Value:                                  |
Cheesy Garlic Pizza                 13  |
Pepperoni                           14  |
Ham Cheese                          15  |
Simply Cheese                       16  |
Hawaiian                            17  |
Mega Pepperoni                      18  |
----------------------------------------|
Small | Medium | Large  |
$4.99 | $7.99  | $12.99 |
------|--------|--------|
''')

keep_going = "yes"

# While loop for user to keep adding to their pizza order
while keep_going == "yes":
    # Pizza id question
    pizza_num_id = num_checker("Enter the pizza number: ", 1, 18)
    pizza_order.append(pizza_num_id)

    # Ask for size
    size = string_checker("What Size | Small | Medium | Large |: ", size_option)
    pizza_order_size.append(size)

    print(f"Great! You have selected a {size} pizza with id {pizza_num_id}")

    print()
    keep_going = string_checker("Do you want to order another pizza? ", yes_no)

print(f"You have ordered the following: {pizza_order} with the sizes: {pizza_order_size}")

# Price summary for food
total_price = calculate_price(pizza_order_size, 'none', delivery)  # Use 'none' for initial calculation
print(f"Your order so far costs = ${total_price:.2f} (including delivery)")

# Time wait
time.sleep(1)

# Would you like the drink menu question
want_menu = string_checker(f"{name}, would you like the drink menu? ", yes_no)

if want_menu == "yes":
    # Drink menu
    print('''\n
    |--------Drink Menu--------|
    |--------------------------|
    | DRINKS            NUM ID |
    | Lift                1    |        
    | Fanta               2    |
    | Coke                3    | 
    | L & P               4    | 
    | Sprite              5    | 
    |--------------------------| 
    | CAN  | BOTTLE |
    | 3.30 |  5.50  |
    |------|--------|
    ''')

    keep_going = "yes"

    # While loop for user to keep adding to their drink order
    while keep_going == "yes":
        # Drink selection question
        drink_num_id = num_checker("Enter the drink number: ", 1, 6)
        drink_order.append(drink_num_id)

        # Drink size (bottle or can)
        drink_size = string_checker("What Size | Bottle (1.5L) | Can (330mL) |: ", size_drink)

        print(f"Great! You have selected a {drink_size} drink with id {drink_num_id}")

        # loop question yes/no
        keep_going = string_checker("Do you want to order another drink? ", yes_no)

    time.sleep(3)

    print(f"You have ordered the following drinks with IDs: {drink_order}")

# Time wait
time.sleep(2)

# Order price calculator (including drink if selected)
total_price = calculate_price(pizza_order_size, drink_size, delivery)
print(f"Your final order costs = ${total_price:.2f} (including delivery)")

# Time wait
time.sleep(1)

# pizza ready message
print("Your pizza will be ready from 10 to 20 minutes")
print("dont touch the keyboard")

# Time wait
time.sleep(3)

# Loading bar simulation

time.sleep(1)

loading_steps = [

   "               ⣠⣤⣶⣶⣦⣄⣀",
   "⠀            ⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀",
   "⠀    ⠀       ⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀",
   "      ⠀   ⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀",
   "⠀ ⠀       ⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀",
   " ⠀     ⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇",
   "⠀⠀    ⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇",
   "⠀⠀   ⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀",
   "⠀  ⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁⠀⠀⠀⠀⠀",
   "  ⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀",
   " ⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀",
   " ⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀",
   " ⠈⠓⠾⠇⠀⠀⠀⠀"

]
for step in loading_steps:
    print(step)
    time.sleep(1)

# pizza ready message
print("\nding!")
time.sleep(1)
print("Your pizza(s) is ready, enjoy")

# Time wait
time.sleep(2)
