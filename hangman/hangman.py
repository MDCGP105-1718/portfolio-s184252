# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

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
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for c in secret_word:
        if c not in letters_guessed:
                return False
    else:
        return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []

    for c in secret_word:
        if c in letters_guessed:
            guessed_word.append(c + " ")
        else:
            guessed_word.append("_ ")

    return "".join(guessed_word)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = []

    for c in string.ascii_lowercase:
        if c not in letters_guessed:
            available_letters.append(c)

    return "".join(available_letters)

def number_unique_letters(secret_word):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    returns: number of unique letters in secret_word
    '''
    unique_letters = []
    for c in secret_word:
        if c not in unique_letters:
            unique_letters.append(c)

    return len(unique_letters)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    while guesses_remaining > 0:
        print(f"{warnings_remaining} warnings left: {'=' * warnings_remaining}")
        print(f"{guesses_remaining} guesses  left: {'=' * guesses_remaining}")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        print(f"{get_guessed_word(secret_word, letters_guessed)}")
        current_guess = input("Please guess a letter: ").lower()
        if not str.isalpha(current_guess):
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! That is not a valid letter. You used up a warning.")
            else:
                guesses_remaining -= 1
                print(f"Oops! That is not a valid letter. You used up a guess.")
        elif current_guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f"Oops! You've already guessed that letter. You used up a warning.")
            else:
                guesses_remaining -= 1
                print(f"Oops! You've already guessed that letter. You used up a guess.")
        elif current_guess in secret_word:
            letters_guessed.append(current_guess)
            if is_word_guessed(secret_word, letters_guessed):
                print(get_guessed_word(secret_word, secret_word))
                print("Congratulations! you won!")
                print(f"Your total score for this game is: {guesses_remaining * number_unique_letters(secret_word)}")
                exit()
            else:
                print("Good guess!")
        else:
            if current_guess in 'aeiou':
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            letters_guessed.append(current_guess)
            print("Oops! That letter is not in my word.")
        print("-------------------------------------------------------------------")

    print("Sorry, you ran out of guesses!")
    print(f"The word was: {get_guessed_word(secret_word, secret_word)}")
    exit()

secret_word = choose_word(wordlist)
hangman(secret_word)
