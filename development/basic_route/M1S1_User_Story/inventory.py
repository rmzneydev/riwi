# Variable definitions
name = ""
price = 0.0
quantity = 0

# Request data from the user
name = input("Enter product name: ")

# Boolean variable to determine if the input data is valid
valid_value = False 

# Loop to validate that the price entered by the user is a decimal number
while not valid_value:
    try:
        price = float(input("Enter the price: "))
        valid_value = True
    except ValueError:
        print("You did not enter a valid price!")

valid_value = False

# Loop to validate that the quantity entered by the user is an integer
while not valid_value:
    try:
        quantity = int(input("Enter the quantity: "))
        valid_value = True
    except ValueError:
        print("You did not enter a valid quantity!")

# Perform mathematical operation
total_cost = price * quantity

# Print result
print("Product: " + name + " | Price: ", price, " | Quantity: ", quantity, " | Total: ", total_cost)

# General program description
# This program is a simple inventory script that allows the user to enter a product's name, its price, and the quantity. 
# Then, it calculates the total inventory cost for that product and displays it to the user. 
# The program also includes validation to ensure that the entered price and quantity are valid numbers.