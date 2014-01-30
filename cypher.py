#Prompt user for one of three commands: 'e' to encode, 'd' to decode, 'q' to quit
command = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def code(string):
    #Encode/decode string
    coded_string = ''
    for letter in string:
        #Skip letters that are not lower case, pass them through to the encoded string
        if letter not in alphabet:
            coded_string = coded_string + letter
        else:
            letter_index = alphabet.index(letter)
            coded_string = coded_string + rotated_alphabet[letter_index]
    return coded_string

while command != 'q':
    command = input('Please enter "e" to encode a string, "d" to decode a string or "q" to quit program: ')

    #encode prompts user for a string to encode & a rotation in range of 1-25
    if command == 'e':
        string = input('Please enter a string to encode: ')
        rotation = int(input('Please enter a rotation to use. Rotation should be in the range 1-25: '))

        #Print error message if user enters invalid rotation & reprompt for rotation
        while rotation < 1 or rotation > 25:
            print('Error: Please enter a valid rotation.')
            rotation = int(input('Please enter a rotation to use. Rotation should be in the range 1-25: '))

        #Rotate alphabet
        first_half = alphabet[rotation:]
        second_half = alphabet[:rotation]
        rotated_alphabet = first_half + second_half
        
        #return the encoded string
        print(code(string))

    #decode prompts user for a string to decode & a word that appears in the text
    elif command == 'd':
        string = input('Please enter a string to decode: ')
        word = input('Please enter a word that occurs in the string: ')

        decoded = False

        for x in range(0, 26):
            first_half = alphabet[x:]
            second_half = alphabet[:x]
            rotated_alphabet = first_half + second_half

            #returns the rotation needed to decode the string
            if word in code(string): 
                print(code(string))
                decoded = True

        #if no rotation is found, program should indicate no rotation found
        if decoded == False:
            print('No rotation found. Unable to crack code.')

    else:
        print('Error: Please enter a valid command.')
        
#quit ends the program and prints an exit message
if command == 'q':
    print("Thank you for using Caesar Cypher")
