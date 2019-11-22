# --------------------------------------------------------------------------------------
# File: Exercise_5.1.py
# Name: Amie Davis
# Date: 7/4/2019
# Course: DSC510 - Introduction to Programming
# Assignment Number: 5.1
#
# Purpose: Performs mathematical operations on two numbers.
#          Calculates average on set of numbers.
#
# Usage: Reads request and numbers from user input.
#        Calculates and outputs results.
#
# Functions: performCalculation(), calculateAverage()
#
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

# Function to perform mathematical operation on two numbers
def performCalculation(p_operation):

    # Prompts users for numbers
    print('\n')
    number1 = input('Please enter your first number: ')
    number2 = input('Please enter your second number: ')

    # Converts user input into number
    try:
        float(number1)
        float(number2)

    except:
        print('\n')
        print('ALERT: You must enter a number for both inputs.')

    else:
        fl_number1 = float(number1)
        fl_number2 = float(number2)

        # Performs operation based on parameter passed
        if p_operation == '+':
            op_result = fl_number1 + fl_number2

        if p_operation == '-':
            op_result = fl_number1 - fl_number2

        if p_operation == '*':
            op_result = fl_number1 * fl_number2

        if p_operation == '/':
            op_result = fl_number1 / fl_number2

        # Displays results
        print('\n')
        print('Your calculated result is {}'.format(op_result))

# --------------------------------------------------------------------------------------

# Function to calculate average
def calculateAverage():

    # Initializes variables
    num_total = 0
    num_average = 0

    # Prompts user for amount of numbers
    print('\n')
    num_count = input('How many numbers would you like to input? ')

    # Converts user input into integer
    try:
        int(num_count)

    except:
        print('\n')
        print('ALERT: You must enter an integer.')

    else:
        i_num_count = int(num_count)

        for i in range(i_num_count):
            num_entered = input('Please enter a number: ')

            # Converts user input into a number
            try:
                float(num_entered)

            except:
                print('\n')
                print('ALERT: This process only accepts numbers.  Please start over.')
                break

            else:
                fl_num_entered = float(num_entered)

                # Calculates average
                num_total = num_total + fl_num_entered
                num_average = num_total / i_num_count

        # Displays results
        print('\n')
        print('The average of your numbers is {}'.format(num_average))

# --------------------------------------------------------------------------------------

# Main program

# Initializes variables
op_perform = ''

while op_perform != 'stop':

    # Prompts users for action to perform
    print('\n')
    print('What operation would you like to perform?')
    print('Please select from one of the following:')
    print('1 - Addition')
    print('2 - Subtraction')
    print('3 - Multiplication')
    print('4 - Division')
    print('5 - Average')
    op_perform = input('Enter number that corresponds to your selection.  Enter stop when you are done: ')

    # Calls appropriate function based on user input
    if op_perform == '1':
        performCalculation('+')

    elif op_perform == '2':
        performCalculation('-')

    elif op_perform == '3':
        performCalculation('*')

    elif op_perform == '4':
        performCalculation('/')

    elif op_perform == '5':
        calculateAverage()

    elif op_perform == 'stop':
        pass

    else:
        print('\n')
        print('ALERT: You must enter a valid response.')


