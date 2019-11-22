# --------------------------------------------------------------------------------------
# File: Exercise_6.1.py
# Name: Amie Davis
# Date: 7/11/2019
# Course: DSC510 - Introduction to Programming
# Assignment Number: 6.1
#
# Purpose: Creates a list of temperatures.
#          Determines count, max, and min of temperatures entered.
#
# Usage: Reads temperatures from user input.
#
# --------------------------------------------------------------------------------------

# Initializes variables
new_temp = ''
temperatures = []

while new_temp != 'stop':

    # Prompts users for temperature
    print('\n')
    new_temp = input('Enter a temperature.  Enter stop when you are done: ')

    if new_temp == 'stop':
        break

    else:
        # Validates user input
        try:
            float(new_temp)

        except:
            print('\n')
            print('ALERT: You must enter a number.  Please re-enter or enter stop if you are finished.')

        else:
            # Converts user input into number
            float_temp = float(new_temp)

            # Creates list of temperatures entered
            temperatures.append(float_temp)

# Determines count, max, and min of values entered
num_temps = len(temperatures)
if num_temps == 1:
    print('You have entered {} temperature reading.'.format(num_temps))

else:
    print('You have entered {} temperature readings.'.format(num_temps))

if num_temps > 0:
    max_temp = max(temperatures)
    print('The largest temperature is {}.'.format(max_temp))
    min_temp = min(temperatures)
    print('The smallest temperature is {}.'.format(min_temp))