
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
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

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
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_ '
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = string.ascii_lowercase
    for letter in letters_guessed:
        available_letters = available_letters.replace(letter, '')
    return available_letters


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
    guesses_remaining = 6
    letters_guessed = []
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    
    while guesses_remaining > 0:
        print("-------------")
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()
        
        if guess in letters_guessed:
            print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        
        if is_word_guessed(secret_word, letters_guessed):
            print("-------------")
            print("Congratulations, you won!")
            break
    
    if not is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        print("Sorry, you ran out of guesses. The word was", secret_word + ".")


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for mw, ow in zip(my_word, other_word):
        if mw != '_' and mw != ow:
            return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    matches = [word for word in wordlist if match_with_gaps(my_word, word)]
    if matches:
        print("Possible word matches are:")
        print(" ".join(matches))
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    letters_guessed = []
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    
    while guesses_remaining > 0:
        print("-------------")
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()
        
        if guess == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        
        if guess in letters_guessed:
            print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        
        if is_word_guessed(secret_word, letters_guessed):
            print("-------------")
            print("Congratulations, you won!")
            break
    
    if not is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        print("Sorry, you ran out of guesses. The word was", secret_word + ".")


if __name__ == "__main__":
   
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    
