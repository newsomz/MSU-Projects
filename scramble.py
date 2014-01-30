def scramble_text():
    """(file) -> file

    Scramble the text in input_file and save results to output_file

    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    #Read the file one line at a time
    for line in input_file:
    #Use string split method to extract a list of words, all the words in a line
        line_list = line.split(' ')
        scrambled_line = ''
    
    #Process each word such that:
        for word in line_list:
            scrambled_word = scramble_word(word)
            scrambled_line = scrambled_line + scrambled_word + ' '
        #print(scrambled_line)
        #Output the revised text file to a new file
        output_file.write(scrambled_line)

    print("Your text was scrambled and saved to: " + output_filename)


def scramble_word(word):
    """(str) -> str

    Return a scrambled version of the word for words > 3 letters. The first/last letters and punctuation 
    remain the same. The middle letters are scrambled.

    >>> scramble_word('brother')
    'btrhoer'
    >>> scramble_word('and')
    'and'
    >>> scramble_word('angrier!')
    'aignrer!'
    """

    import random
    #Set alphabet to determine if word has punctuation
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    #Set iterators
    list_word = []
    middle_list = []

    #Only scramble word if word is > 3 letters
    if len(word) > 3:
        for letter in word:
            list_word.append(letter)
        #print(list_word)

        #Keep first letter of the word the same
        first_letter = list_word.pop(0)
        #print('First letter: ' + first_letter)

        #Keep last letter of the word the same
        last_letter = list_word.pop(-1)
        #print('Last letter: ' + last_letter)

        #If last letter is punctuation, keep actual last letter, need to fix in case there are 3 !!!
        if last_letter not in alphabet:
            last_letter = list_word.pop(-1) + last_letter
            #print('Last letter: ' + last_letter)

        #print(list_word)

        #Scramble the middle of the word
        random.shuffle(list_word)

        #print(list_word)
        #Create string from scramblelist
        middle = ''
        for letter in list_word:
            middle = middle + letter

        #Return scrambled word
        return first_letter + middle + last_letter

    #Otherwise return word unscrambled
    else:
        return word


#Open a file for reading. Prompt user for the file name
input_filename = input("Please enter the file name of the file you would like to scramble: ")
input_file = open(input_filename, 'r')

output_filename = input("Please enter the file name where you will save your scrambled file: ")
output_file = open(output_filename, 'w')

scramble_text()

#Prompt the user for a new file name
