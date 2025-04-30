def int_check(question):
    """Checks for an integer more than zero / <enter> for infinite"""
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)
            # check that the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0

print()
print("⬆️⬆️⬆️Welcome to Higher or Lower⬇️⬇️⬇️")
print()


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


# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker("Do you want to see the instructions?")

# display the instructions if user wants to see them
if want_instructions == "yes":

    def instructions():
        print('''

        ***   Instructions   ***

    To begin, choose the number of rounds and either customise the game parameters 
    or with the default game (where the secret number will be between 1 and 100).

    then choose how many you wanna go for or press <enter> for infinite mode.

    your goal is to try and guess the secret number without running out of guess

    Good Luck!

    ''')

# Ask user for number of rounds / infinite
num_rounds = int_check("How many rounds would you like? push <enter> for infinite: ")
print()
print(f"you chose: {num_rounds}")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop stats here
while rounds_played < num_rounds:

    # Rounds heading
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode)"
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# game loop ends here


# game history
