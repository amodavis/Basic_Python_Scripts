# --------------------------------------------------------------------------------------
# File: Exercise_3.1.py
# Name: Amie Davis
# Date: 6/21/2019
# Course: DSC510 - Introduction to Programming
# Assignment Number: 3.1
#
# Purpose: Receives fiber installation order, calculates cost,
#          applies bulk discount, and prints receipt.
#
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

# Make sure number of fiber entered is an integer
try:
    int(num_fiber)

except:
    print('\n')
    print('ALERT: You must enter a number to the nearest foot.')

else:
    # Calculates the initial cost (in dollars) of the fiber install
    initial_cost = 0.87 * int(num_fiber)

    # Calculates bulk discount rate
    if int(num_fiber) <= 100:
        discount_rate = 0.87

    if int(num_fiber) > 100 and int(num_fiber) <= 250:
        discount_rate = 0.8

    if int(num_fiber) > 250 and int(num_fiber) <= 500:
        discount_rate = 0.7

    if int(num_fiber) > 500:
        discount_rate = 0.5

    # Calculate discounted cost
    final_cost = round(discount_rate * int(num_fiber),2)

    # Displays receipt
    print('\n')
    print('Thank you for your order.  An account specialist will contact you to schedule your installation.')
    print('\n')

    print('Receipt')
    print('Company: ', company)
    print('Amount of fiber to be installed: ', num_fiber, 'feet')

    # Formats currency to two decimals
    print('Your initial calculated cost is ${0:.2f}'.format(initial_cost))
    print('Your final cost with discount is ${0:.2f}'.format(final_cost))
    print('You saved ${0:.2f}'.format(initial_cost - final_cost))

