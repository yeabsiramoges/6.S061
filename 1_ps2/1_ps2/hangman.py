# Problem Set 2, hangman.py
# Name: Yeabsira Moges
# Collaborators: 
# Time spent: 2 hours

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for c in secret_word:
        if c not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    s = ""
    for c in secret_word:
        s += (c if c in letters_guessed else "*")
    return s


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    a_unicode = ord("a")
    z_unicode = ord("z")
    all_lowercase = ""
    for c in range(a_unicode, z_unicode+1):
        if chr(c) not in letters_guessed:
            all_lowercase += chr(c)
    return all_lowercase

def choose_letter(secret_word, available_letters):
    choose_from = ""
    for c in available_letters:
        if c in secret_word and c not in choose_from:
            choose_from += c
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '$'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol $, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    num_guesses_left = 10
    letters_guessed = []
    vowels = ['a','e','i','o','u']
    while num_guesses_left > 0 and not has_player_won(secret_word, letters_guessed):
        print("--------------")
        print(f"You have {num_guesses_left} guesses left.")
        print(get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ")
        if with_help and letter == "$":
                if num_guesses_left > 3:
                    num_guesses_left -= 3
                    revealed_letter = choose_letter(secret_word, get_available_letters(letters_guessed))
                    letters_guessed.append(revealed_letter)
                    print(f"Letter revealed: {revealed_letter}")
                    print(get_word_progress(secret_word, letters_guessed))
                else:
                    print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")
        elif len(letter) == 1 and ord(letter.lower()) >= 97:
            n_letter = chr(ord(letter.lower()))
            if n_letter in secret_word and n_letter not in letters_guessed:
                letters_guessed.append(n_letter)
                print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
            elif n_letter in secret_word and n_letter in letters_guessed:
                letters_guessed.append(n_letter)
                print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
            elif n_letter not in secret_word and n_letter in vowels:
                letters_guessed.append(n_letter)
                num_guesses_left -= 2
                print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
            else:
                letters_guessed.append(n_letter)
                num_guesses_left -= 1
                print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
        else:
            print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
    print("--------------")
    if has_player_won(secret_word, letters_guessed):
        print("Congratulations, you won!")
        total_score = (num_guesses_left + 3 * len(set(secret_word))) + (4*len(secret_word))
        print(f"Your total score for this game is: {total_score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    #secret_word = choose_word(wordlist)
    #secret_word = "wildcard"
    #with_help = True
    #hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "$" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

