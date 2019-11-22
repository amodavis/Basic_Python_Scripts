# --------------------------------------------------------------------------------------
# File: Exercise_4.1.py
# Name: Amie Davis
# Date: 6/27/2019
# Course: DSC510 - Introduction to Programming
# Assignment Number: 4.1
#
# Purpose: Receives fiber installation order, determines rate,
#          calculates cost, and prints receipt.
#
# Usage: Reads company and order in feet from user.
#        Outputs order receipt.
#
# Methods Imported: datetime
# --------------------------------------------------------------------------------------

# Import external methods
import datetime

# Displays welcome message
print('\n')
print('Welcome to the Fiber Optic Cable Ordering Tool!')
print('\n')

# Retrieves company name
company = input('Please enter your Company Name: ')

# Retrieves amount of fiber to order
num_fiber = input('Please enter the amount of fiber optic cable to be installed (in feet): ')

# Function to determine discount
def get_cost(feet, price):
    cost = feet * price
    return cost

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
        rate = 0.87

    if int(num_fiber) > 100 and int(num_fiber) <= 250:
        rate = 0.8

    if int(num_fiber) > 250 and int(num_fiber) <= 500:
        rate = 0.7

    if int(num_fiber) > 500:
        rate = 0.5

    # Calculate discounted cost
    final_cost = get_cost(int(num_fiber),rate)

    # Displays receipt
    print('\n')
    print('Thank you for your order.  An account specialist will contact you to schedule your installation.')
    print('\n')

    # Get timestamp
    timestamp = datetime.datetime.today()

    print('RECEIPT')
    print('\n')
    print('Date: ', timestamp.strftime('%m/%d/%y'))
    print('Company: ', company)
    print('Amount of fiber to be installed: ', num_fiber, 'feet')

    # Formats currency to two deciamls
    print('Your initial calculated cost is ${0:.2f}.'.format(initial_cost))
    print('Your final cost with discount is ${0:.2f}.'.format(final_cost))
    print('You saved ${0:.2f} with your bulk discount.'.format(initial_cost - final_cost))
