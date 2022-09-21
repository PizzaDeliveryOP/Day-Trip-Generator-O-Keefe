import random
#(5 points): As a developer, I want to make at least three commits with descriptive messages 
#(5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
#These lists define the available options for each category of the Day Trip 
#This is a series of lists that define options for each of the categories for the user story
destination_list = ["Earth", "Mars", "Pluto", "Mercury"]
restaurant_list = ["McDonalds", "Fogo de Chao","Goodberry"]
mode_of_transportation_list = ["Spelljammer", "Space Swine", "Planeswalking"]
entertainment_list = ["Bother a Dragon", "Depose a democratically elected government","'Accidentally' invent gunpowder"]
list_of_accepted_values = ["yes, no"]
#(5 points): As a developer, I want to store my final day trip selections in a Dictionary, 
#       with a unique key value pair for each piece of the day trip. 
#This is the Day Trip Dictionary that stores the user selected value for each piece of the day trip. 
#Dictionary that retains each of the user inputs.
day_trip_dictionary ={"destination": '', "restaurant": '', "mode_of_transportation": '', "entertainment": ''}
#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
mode_of_transportation_guess = random.choice(mode_of_transportation_list)
#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
entertainment_guess = random.choice(entertainment_list)
# def choose_list_option(list_to_choose_from, key_to_set_on_dictionary, message_phrase):
#This function block asks the user for input on which Destination they would like
def choose_destination():
    temp_destinations_list = list(destination_list)
    #(5 points): As a user, I want a destination to be randomly selected for my day trip. 
    destination_guess = random.choice(temp_destinations_list)
    while True:
        user_input = get_validate_user_input(['yes', 'no'], f"Would you like to go to: {destination_guess}?")
        if len(destination_list) == 0:
            choose_destination()
        if user_input == 'yes':
            day_trip_dictionary["destination"] = destination_guess
            break
        elif user_input == 'no': 
            temp_destinations_list.remove(destination_guess)
            destination_guess = random.choice(temp_destinations_list) 
#This function asks the user which restaurant they would like
def choose_restaurant():
    temp_restaurants_list = list(restaurant_list)
#(5 points): As a user, I want a restaurant to be randomly selected for my day trip
    restaurant_guess = random.choice(temp_restaurants_list)
    while True:
        user_input = get_validate_user_input(['yes', 'no'], f"Would you like to eat at: {restaurant_guess}?")
        if len(temp_restaurants_list) == 0:
            choose_restaurant()
        if user_input == 'yes':
            day_trip_dictionary["restaurant"] = restaurant_guess
            break
        elif user_input == 'no': 
            temp_restaurants_list.remove(restaurant_guess)
            restaurant_guess = random.choice(temp_restaurants_list) 
#This function asks the user which mode of transportation they would like
def choose_mode_of_transportation():
    temp_mode_of_transportation_list = list(mode_of_transportation_list)
    #(5 points): As a user, I want a destination to be randomly selected for my day trip. 
    destination_guess = random.choice(temp_mode_of_transportation_list)
    while True:
        user_input = get_validate_user_input(['yes', 'no'], f"Would you like to use: {mode_of_transportation_guess} to travel?")
        if len(destination_list) == 0:
            choose_mode_of_transportation
        if user_input == 'yes':
            day_trip_dictionary["mode_of_transportation"] = mode_of_transportation_guess
            break
        elif user_input == 'no': 
            temp_mode_of_transportation_list.remove(destination_guess)
            destination_guess = random.choice(temp_mode_of_transportation_list) 
#This function asks the user which entertainment they would like
def choose_entertainment():
    temp_entertainment_list = list(entertainment_list)
    #(5 points): As a user, I want a destination to be randomly selected for my day trip. 
    destination_guess = random.choice(temp_entertainment_list)
    while True:
        user_input = get_validate_user_input(['yes', 'no'], f"Would you like to: {destination_guess} for your entertainment?")
        if len(temp_entertainment_list) == 0:
            choose_entertainment()
        if user_input == 'yes':
            day_trip_dictionary["destination"] = destination_guess
            break
        elif user_input == 'no': 
            temp_entertainment_list.remove(destination_guess)
            destination_guess = random.choice(temp_entertainment_list) 
#This function helps sanitize user inputs
def get_validate_user_input(list_of_excepted_values, message_to_prompt):
    user_input = input(message_to_prompt).lower()
    if user_input in list_of_excepted_values:
        return user_input
    else:
        print(f'I did not quite catch that. Please input {list_of_excepted_values} with regards to the query.')
        return get_validate_user_input()
#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, 
#       and/or form of entertainment if I don’t like one or more of those things.
#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
#This function confirms user inputs and repeats the asking input loop if the user is unsatisfied
#(10  points): As a user, I want to display my completed trip in the console
def confirm_day_trip():
    day_trip = (f'For your trip, you are going to {day_trip_dictionary["destination"]} and will be travelling via {mode_of_transportation_guess}. Once you arrive, you can eat at {restaurant_guess}, and afterwords enjoy {entertainment_guess}')
    print(day_trip)
    confirm_choice = input('Please enter Yes or No to confirm your Day Trip:')
    while True:  
        if confirm_choice == "Yes":
            day_trip = (f'For your trip, you are going to {day_trip_dictionary["destination"]} and will be travelling via {mode_of_transportation_guess}. Once you arrive, you can eat at {restaurant_guess}, and afterwords enjoy {entertainment_guess}')
            print(day_trip)
            break
        if confirm_choice == "No":
            print("Sorry that did not work out for you, let's try that again.")
            user_input_loop()
            break
#This defines the User Input loop that asks about each of the sections of the user story.
def user_input_loop():
    choose_destination()
    choose_restaurant()
    choose_mode_of_transportation()
    choose_entertainment()
    confirm_day_trip()
user_input_loop()
#(5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. 
#Remember, each function should do just one thing!   

    

