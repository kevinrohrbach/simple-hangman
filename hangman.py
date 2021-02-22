"""Simple Hangman Game."""

import time
import random
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"


"""Welcome User."""
print("\nWelcome to the Hangman Game\nDo you have the nerves?\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\nLet's play Hangman!")
time.sleep(3)


def main():
    """Define main function."""
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    response = requests.get(word_site)
    words_to_guess = response.text.splitlines()
    word = random.choice(words_to_guess)
    word = 'eventually'
    print(word)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ''


def play_loop():
    """Define game loop."""
    global play_game
    play_game = input("Do you want to play again? y= yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do you want to play again? y= yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print('Thanks for Playing! We expect you back again!')
        exit()


def hangman():
    """Initialise Hangman Conditions."""
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 6
    guess = input('This is Hangman:' + display + " Enter your Guess: \n> ")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        for n in range(word.count(guess)):
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
            index += 1
        print(display + "\n")

    elif guess in already_guessed:
        print('Try another letter.\n')

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("         \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("  ______ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("  ______ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("  ______ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 5:
            time.sleep(1)
            print("  ______ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |        \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 6:
            time.sleep(1)
            print("  ______ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was: ", already_guessed, word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()
