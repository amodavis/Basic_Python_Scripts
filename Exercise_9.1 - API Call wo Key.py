# --------------------------------------------------------------------------------------
# File: Exercise_9.1.py
# Name: Amie Davis
# Date: 7/31/2019
# Course: DSC510 - Introduction to Programming
# Assignment Number: 9.1
#
# Purpose: Calls a web service to get Chuck Norris jokes.  Displays result.
#
# Usage: Uses API at https://api.chucknorris.io/jokes/random
#
# --------------------------------------------------------------------------------------
import requests, json

# Initializations
joke_prompt = 'Y'
joke_count = 1

# Display welcome message
print('\n')
print('Welcome to my Chuck Norris joke app.')

# Prompt for joke
while joke_prompt.upper() == 'Y':

    if joke_count == 1:
        question_prompt = 'a'
    else:
        question_prompt = 'another'

    print('\n')
    joke_prompt = input('Would you like to hear {} Chuck Norris joke?  If so, enter Y. '.format(question_prompt))
    joke_count = joke_count + 1

    # Call API for joke
    url = 'https://api.chucknorris.io/jokes/random'
    payload = ''
    headers = {'cache-control':'no-cache'}
    response = requests.request('GET',url, data=payload, headers=headers)

    # parse JSON data
    data = json.loads(response.text)

    # Format and display joke
    print('\n')
    print('Did you know...{}'.format(data['value']))