import words
import random
import display_utility

def check_word(secret, guess):
    """The function takes in two string inputs, a secret word for the Wordle game and a guess input by the user, each with a length of 5 
    and returns a list filled with 5 strings that are colors."""
    
    color_list = ["grey", "grey", "grey", "grey", "grey"]

    #implements all of the "green" in the list
    for guess_char in range(len(guess)):
        for secret_char in range(len(secret)):
            if guess[guess_char] == secret[secret_char]:
                #if the index value of the letters match, then color_list is modified with "green"
                if guess_char == secret_char:
                    color_list[guess_char] = "green"
    
    #used to contain the occurences of each letter in secret
    dupe_dict = {}

    for x in range(len(secret)):
        #if the dictionary already has the key, it increments the value by 1
        if secret[x] in dupe_dict:
            dupe_dict[secret[x]] = dupe_dict[secret[x]] + 1
        #else a new key is added into the dictionary with a value of 1
        else:
            dupe_dict[secret[x]] = 1
    
    
    for check_yellow in range(len(color_list)):
        if color_list[check_yellow] == "grey":
            for secret_char in range(len(secret)):
                #checks if two letters in guess and secret match at any time
                if guess[check_yellow] == secret[secret_char]:
                    if color_list[secret_char] != "green":
                        #checks if the occurences of the letter in secret is not less than the occurences in guess
                        if dupe_dict[secret[secret_char]] != 0:
                            color_list[check_yellow] = "yellow"
                            #reduces the occurences of the letter by one to make sure there is no excess for future iterations
                            dupe_dict[secret[secret_char]] = dupe_dict[secret[secret_char]] - 1

    return color_list




def known_word(clues):
    """Takes in a list of guesses taken(strings) and clues recieved(list of strings) 
    and outputs a string that contains known letters of the secret word"""

    known_list = ["_", "_", "_", "_", "_"]
    guess_list = []
    known = ""

    for check in range(len(clues)):
        for letters in clues[check][0]:
                guess_list.append(letters)
        for colors in range(len(clues[check][1])):
            if clues[check][1][colors] == 'green':
                #adds the letter in the guess_list at the same index as "green" into known_list
                known_list[colors] = guess_list[colors]
        guess_list = []

    #takes each character in the known_list and makes one string
    for x in known_list:
        known = known + x.upper()
    return known





def no_letters(clues):
    """Takes in a list of guesses taken(strings) and clues recieved(list of strings) 
    and outputs a string that contains all letters that are "grey"""
    temp_list = []
    grey_str = ""
    gy_check = 0

    for go in range(len(clues)):
        for check_grey in range(len(clues[go][1])):
            #checks if the value at the index is equal to "grey"
            if clues[go][1][check_grey] == "grey":
                #checks if there is a green or yellow version of the letter
                for i in range(len(clues)):
                    for gy in range(len(clues[i][1])):
                        if clues[i][0][gy] == clues[go][0][check_grey]:
                            if clues[i][1][gy] == "green" or clues[i][1][gy] == "yellow":
                                #used to track if there is a green or yellow version of the letter
                                gy_check = 1
                if gy_check != 1:
                    #adds the letter in to temp_list
                    temp_list.append(clues[go][0][check_grey])
                gy_check = 0
    
    #loops through temp_list and makes each letter uppercase
    for i in range(len(temp_list)):
        temp_list[i] = temp_list[i].upper()

    
    #sorts the list in alphabetical order (A to Z)
    temp_list = insertion_sort(temp_list)
    
    #used as a tracker to see if a grey letter repeats itself
    checker = 0


    #checks if there are an duplicates in the list
    for x in temp_list:
        for y in grey_str:
            if x == y:
                checker = 1
        if checker != 1:
            grey_str = grey_str + x
        checker = 0

    return grey_str




def insertion_sort(list):
    """ Takes in a list and returns a sorted list that is in alphabetical order."""
    temp = list
    for i in range(1, len(temp)):
        k = i
        while k > 0 and temp[k] < temp[k - 1]:
            temp[k], temp[k - 1] = temp[k-1], temp[k]
            k -= 1
    return temp
            




def yes_letters(clues):
    """ Takes in a list of guesses taken(strings) and clues recieved(list of strings) 
    and outputs a string that contains all letters that are "green" or "yellow". """

    temp = []
    yg_str = ""

    #finds the letters that are "green" or "yellow"
    for go in range(len(clues)):
        for check in range(len(clues[go][1])):
            if clues[go][1][check] == "green" or clues[go][1][check] == "yellow":
                temp.append(clues[go][0][check])
    
    #loops through temp_list and makes each letter uppercase
    for i in range(len(temp)):
        temp[i] = temp[i].upper()
    
    
    #sorts the list in alphabetical order form A to Z
    temp = insertion_sort(temp)


    #used as a tracker to see if a green/yellow letter repeats itself
    checker = 0

    #checks for duplicates in the list
    for x in temp:
        for y in yg_str:
            if x == y:
                checker = 1
        if checker != 1:
            yg_str = yg_str + x
        checker = 0

    return yg_str


def isValid(guess):
    """ Takes in a string an returns a boolean value"""
    #checks if the guess word is valid (valid if it is in the word list)
    checking = 0
    for i in words.words:
        if guess == i:
            checking = 1
    if checking == 1:
        return True
    return False
    

def visual(list):
    """Takes in a string and a list and returns nothing."""
    #store each letter of the string into a seperate indexes in a list
    #store the seperated letter lists into one list
    letter_list = []
    word_list = []
    for x in range(len(list)):
        for y in list[x][0]:
            letter_list.append(y)
        word_list.append(letter_list)
        letter_list = []
    
    #matches each letter with a visual color representation and prints it out
    for i in range(len(list)):
        for k in range(len(list[i][1])):
            if list[i][1][k] == "green":
                display_utility.green(word_list[i][k].upper())
            elif list[i][1][k] == "yellow":
                display_utility.yellow(word_list[i][k].upper())
            else:
                display_utility.grey(word_list[i][k].upper())
        if i < len(list) - 1:
            print()







if __name__ == "__main__":

    secret_word = words.words[random.randint(0, len(words.words))]
    print("Known:", known_word(""))
    print("Green/Yellow Letters: ")
    print("Grey Letters: ")
    count = 0
    list = []
    #used to track if the correct word has already been guessed
    track = 0
    i = 0
    while i < 6:
        #checks whether or not the secret word has already been guessed
        if track != 1:
            guess = input("> ")
        #checks if the guess is a word from the word list
        if isValid(guess):
            colors = check_word(secret_word, guess)
            tup = (guess.upper(), colors)
            list.append(tup)
            #the secret word was guessed
            if guess == secret_word and track == 0:
                visual(list)
                print()
                print("Answer:", secret_word.upper())
                track = 1
            #the guess was innacurate
            if i < 5 and track != 1:
                visual(list)
                print()
                print("Known:", known_word(list))
                print("Green/Yellow:", yes_letters(list))
                print("Grey Letters:", no_letters(list))
        else:
            i = i - 1
        i += 1
    #if the secret word was never guessed after six attempts
    if track == 0:
        visual(list)
        print()
        print("Answer:", secret_word.upper())
    




    


    

