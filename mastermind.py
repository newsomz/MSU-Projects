#Prompt the administrator for a secret number that is 5 digits long without any repeated digits.
print("Welcome to mastermind.")
secret_number = input("You are the game administrator.\nPlease enter a 5 digit number that does not contain any repeated digits: ")

#Set max number of guesses
max_guesses = 7

#Check to see if secret_number is 5 digits 
def secret_format_not_ok(secret_number):
    """(str) -> bool

    >>> secret_format_not_ok(y899u)
    True
    >>> secret_format_not_ok(55678)
    False
    >>> secret_format_not_ok(34567)
    False
    """
    return len(secret_number) != 5 or not secret_number.isdigit()

#Check to see if there are any repeating digits in secret_number
def secret_no_repeating_digits(secret_number):
    """(str) -> bool

    >>> secret_no_repeating_digits(45567)
    False
    >>> secret_no_repeating_digits(45678)
    True
    """
    secret_number_list = []

    for digit in secret_number:
        if digit not in secret_number_list:
            secret_number_list.append(digit)
        else:
            return False

#Test secret_number to see if it fits specified criteria. If not, prompt admin for another secret_number
while secret_format_not_ok(secret_number) == True or secret_no_repeating_digits(secret_number) == False:
    print("Your number was not in the correct format.")
    secret_number = input("Please enter a 5 digit number that does not contain any repeated digits: ")

#Print blank lines so the game player cannot see secret_number
for blank in range (0,10):
    print('\n')

#Ask the player to guess a 5 digit number
print("This is mastermind.\n You will try to guess the exact 5 digit number entered by the game administator.\n You will have " + str(max_guesses) + " guesses to correctly guess the secret number.\n To quit the game, type quit.")

guess = input("Please enter a 5 digit number with no repeated digits: ")

#Initialize turn number
turn = 0

while secret_number != guess and turn < max_guesses - 1 and guess != 'quit':

#Check to see if players number conforms to rules
    while secret_format_not_ok(guess) == True or secret_no_repeating_digits(guess) == False:
        print("Your number was not in the correct format.")
        guess = input("Please enter a 5 digit number that does not contain any repeated digits: ")

    turn = turn + 1

#Calculate how many of the digits in the secret number also appear in the guess
    num_correct = 0

    for digit in guess:
        if digit in secret_number:
            num_correct = num_correct + 1

#Calculate how many of the guess digits are in the correct position
    num_correct_position = 0

    for digit_index in range(0, 5):
        if guess[digit_index] == secret_number[digit_index]:
            num_correct_position = num_correct_position + 1

#Report progress (# guesses, their guess, # correct digits, # digits in correct position
    print("Your guess was " + guess) 
    print("You had " + str(num_correct) + " digits correct.")
    print("You had " + str(num_correct_position) + " digits in the correct position.")
    print("That was guess number " + str(turn))

#Prompt user to guess again if guess is not correct
    guess = input("Please enter another guess: ")

#Once player guesses secret number, print out how many guesses were needed
if secret_number == guess:
    turn = turn + 1
    print("Congratulations!!! You guessed the secret number in " + str(turn) + " tries.")

#Allow player to quit game. If they quit, report they lost & # guesses
elif guess == 'quit':
    print("You chose to quit after " + str(turn) + " guesses.")

#If player exceeds maximum number of guesses, report the player lost
elif secret_number != guess:
    print("I'm sorry you did not guess the secret number in " + str(max_guesses) + " tries.")
