# --------------------------------------------------------------------------------------
# File: Exercise_2.1.py
# Name: Amie Davis
# Date: 6/13/2019
# Course: DSC510 - Introduction to Programming
# Assignment Number: 2.1
# Purpose: Receives fiber installation order, calculates cost, and prints receipt.
# Usage: Reads company and order in feet from user.
#        Outputs order receipt.
# --------------------------------------------------------------------------------------

# Displays welcome message
print('\n')
print('Welcome to the Fiber Optic Cable Ordering Tool!')
print('\n')

# Retrieves company name
company = input('Please enter your Company Name: ')

# Retrieves amount of fiber to order
num_fiber = input('Please enter the amount of fiber optic cable to be installed (in feet): ')

# Only calculate if valid digits entered
if num_fiber.isdigit():

    # Calculates the cost (in dollars) of the fiber install
    cost = 0.87 * int(num_fiber)

    # Displays receipt
    print('\n')
    print('Thank you for your order.  An account specialist will contact you to schedule your installation.')
    print('\n')

    print('Receipt')
    print('Company: ', company)
    print('Amount of fiber to be installed: ', num_fiber, 'feet')
    print('Your calculated total cost is $', cost)

# Show error message if non-digit entered
else:
    print('\n')
    print('ALERT: You must enter a number to the nearest foot.')
