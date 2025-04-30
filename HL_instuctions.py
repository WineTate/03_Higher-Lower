# function go here

# Check that user have entered a valid
# Option based on a list

def string_checker(question, valid_ans=('yes', 'no')):
    """Checks users enter and answer from a list"""

    error = f"please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does enter something that is valid
        print(error)
        print()


# Displays instructions

def instructions():
    print('''
    
    ***   Instructions   ***

To begin, choose the number of rounds and either customise the game parameters 
or with the default game (where the secret number will be between 1 and 100).

then choose how many you wanna go for or press <enter> for infinite mode.

your goal is to try and guess the secret number without running out of guess
 
Good Luck!

''')


# Main routine

print()
print("⬆️⬆️⬆️ Welcome to Higher or Lower ⬇️⬇️⬇️")
print()

# loop for testing purposes

# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker("Do you want to see the instructions?")

# display the instructions if user wants to see them
if want_instructions == "yes":
    instructions()

print("program continues")
