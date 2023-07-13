import wordle
import words
import random

def filter_word_list(words, clues):
    """ Takes in a list of words in string format a
    nd a list of tuples that contain a string guess and color list representation respectively
    and returns a list of words in string format that represent hints. """
    filtered = []
    test = 0

    for i in range(len(words)):
        for x in range(len(clues)):
            #checks to see if the colors match
            if clues[x][1] == wordle.check_word(words[i], clues[x][0].lower()):
                test += 1
        #if the word corrisponds with all of the guesses, it is added into a list
        if test == len(clues):
            filtered.append(words[i])
        test = 0
    return filtered



if __name__ == "__main__":
    secret_word = words.words[random.randint(0, len(words.words))]
    count = 0
    list = []
    an_list = []
    used_clues = []
    track = 0
    i = 0
    x = 0
    five = 0
    while i < 6:
        if track != 1:
            guess = input("> ")
        #checks if the guess is valid
        if wordle.isValid(guess):
            colors = wordle.check_word(secret_word, guess)
            tup = (guess, colors)
            list.append(tup)
            #checks if the guess was the secret word
            if guess == secret_word and track == 0:
                wordle.visual(list)
                print()
                print("1 words possible:")
                print(secret_word)
                print("Answer:", secret_word.upper())
                track = 1
            #checks if the amount of guesses hasn't exceded the limit and that the correct word hasn't been guessed
            if i < 5 and track != 1:
                wordle.visual(list)
                print()
                an_list = filter_word_list(words.words, list)
                #prints all of the hints if there is 5 or less available
                if len(an_list) < 6:
                    print(len(an_list), "words possible:")
                    for y in an_list:
                        print(y)
                #prints 5 random hints from all of the possible hints
                else:
                    random.shuffle(an_list)
                    print(len(an_list), "words possible:")
                    while x < 5:
                        if str(an_list[x]) not in used_clues:
                            print(an_list[x])
                            used_clues.append(an_list[x])
                        else:
                            x = x - 1
                        x += 1
                    used_clues = []
                    x = 0

        else:
            i = i - 1
        i += 1
    #if all 6 guesses are inaccurate
    if track == 0:
        wordle.visual(list)
        print()
        an_list = filter_word_list(words.words, list)
        print(len(an_list), "words possible:")
        #prints all of the hints if there is 5 or less available
        if len(an_list) < 6:
            for y in an_list:
                print(y)
        #prints 5 random hints from all of the possible hints
        else:
            random.shuffle(an_list)
            while x < 5:
                if str(an_list[x]) not in used_clues:
                    print(an_list[x])
                    used_clues.append(an_list[x])
                else:
                    x = x - 1
                x += 1
        print("Answer:", secret_word.upper())


