__author__ = 'ufli'

# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import sys

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter
        else:
            word += '_'
    return word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = string.lowercase
    letters = []
    for letter in alphabet:
        if letter not in lettersGuessed:
            letters.append(letter)
    return letters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'The secret word contains ' + str(len(secretWord)) + ' letters\n'
    lettersGuessed = []
    lettersTried = []
    win = False
    gueses_left = 8

    while gueses_left > 0:
        letter = raw_input("Enter the letter, please: ")
        while letter in lettersTried:
            print 'You have already tried this letter! Please, try another one!'
            letter = raw_input("Enter the letter, please: ")
        lettersTried.append(letter)
        lettersGuessed.append(letter)

        if letter in secretWord:
            if isWordGuessed(secretWord, lettersGuessed):
                print 'Congratulations! You won! The secret word was ' + secretWord
                win = True
                break
            print 'Yeah! You have ' + str(gueses_left) + ' guesses left'
        else:
            gueses_left -= 1
            print 'No! You still have ' + str(gueses_left) + ' guesses'


        print getGuessedWord(secretWord, lettersGuessed)
        print getAvailableLetters(lettersGuessed)
        print '\n'

    if not win:
        print 'Game over!'

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
