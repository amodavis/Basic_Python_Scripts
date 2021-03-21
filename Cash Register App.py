# --------------------------------------------------------------------------------------
# File: Exercise_10.1.py
# Name: Amie Davis
# Date: 8/8/2019
# Course: DSC510 - Introduction to Programming
# Assignment Number: 10.1
#
# Purpose: Cash Register app using Class & Methods
#
# Classes: CashRegister()
# CashRegister Methods: __init__(), additem(), getTotal(). getCount()
#
# Program Functions: main()
#
# --------------------------------------------------------------------------------------
# Cash Register class adds items and tracks total items and costs of cart.
class CashRegister:

    # dunder init method runs at each new instance of CashRegister.
    # Resets totals on each instance call.
    def __init__(self):
        self.itemCount = 0
        self.totalPrice = 0

    # additem is an instance method run each time a new item is added.
    # Adds each new item to the cart totals.
    def additem(self, price):
        print('You have added an item to your cart.')
        self.itemCount = self.itemCount + 1
        self.totalPrice = self.totalPrice + float(price)

    # getTotal returns the total cost of the cart.
    def getTotal(self):
        return self.totalPrice

    # getCount returns the total number of items in the cart.
    def getCount(self):
        return self.itemCount

    #clearCart resets variables to clear out the cart.
    def clearCart(self):
        self.itemCount = 0
        self.totalPrice = 0
        print('Your cart is now clear.')

# --------------------------------------------------------------------------------------
def main():

    # Initialize cart
    cart = CashRegister()

    # Display welcome message
    print('\n')
    print('Welcome to my store.')

    # Prompt user for new item
    print('\n')
    item_prompt = input('Would you like to enter a new item  If so, enter Y. Enter Q to quit the program.')

    while item_prompt.upper() == 'Y':

        print('\n')
        price = input('Enter the price of your item.')

        # Validate number
        try:
            float(price)
        except:
            print('\n')
            print('You must enter a valid number without a dollar sign.')

        else:
            # Add item to cart
            cart.additem(price)

            # Display running total of cart
            if cart.getCount() == 1:
                item_str = 'item'
            else:
                item_str = 'items'

            # Set locale for currency format
            locale.setlocale(locale.LC_ALL, '')

            print('You have {} {} totalling {} in your cart.'.format(cart.getCount(), item_str, locale.currency(cart.getTotal())))

        print('\n')
        item_prompt = input('Would you like to add another item?  If so, enter Y. Enter C to clear your cart and start over. Enter Q to quit when you are done.')

        # Validate response
        if item_prompt.upper() != 'Y' and item_prompt.upper() != 'C' and item_prompt.upper() != 'Q':
            print('You must enter a valid response.')
            item_prompt = input(
                'Would you like to add another item?  If so, enter Y. Enter C to clear your cart and start over. Enter Q to quit when you are done.')

        # Clear cart when prompted and start over.
        if item_prompt.upper() == 'C':
            cart.clearCart()
            print('\n')
            item_prompt = 'Y'

        # Display final totals when done with items in cart
        if item_prompt.upper() == 'Q' and cart.getCount() > 0:
            print('Thank you for shopping with us.  Your final total is {} for {} {}.'.format(locale.currency(cart.getTotal()), cart.getCount(), item_str))

    # Exit if quit before any items entered
    if item_prompt.upper() == 'Q':
        print('Please come again.')

# --------------------------------------------------------------------------------------
# Runs program
import locale

main()
