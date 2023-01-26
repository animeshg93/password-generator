import random
from hangmanPics import HANGMAN_PICS

with open("words.txt", 'r') as textfile:
    words = textfile.read().splitlines()


def createWordFreqMap(word):
    dict = {}
    index = 0
    for letter in word:
        if dict.get(letter) is None:
            indexList = [index]
            dict[letter] = indexList
        else:
            dict.get(letter).append(index)
        index += 1
    return dict


def gameLogic(word, guess, freqMap, guessed_letters):
    hidden = "-" * len(word)
    while guess < len(HANGMAN_PICS) - 1 and '-' in hidden:
        print(HANGMAN_PICS[guess])
        print(f"The word for you to guess is {hidden}")
        letter = input("Please guess your letter: ").lower()

        while letter in guessed_letters:
            letter = input("That letter has been already guessed. Please try again: ").lower()

        if letter in freqMap:
            indices = freqMap.get(letter)
            hiddenList = list(hidden)
            for index in indices:
                hiddenList[index] = letter
            hidden = "".join(hiddenList)
        else:
            guess += 1
            guessed_letters.append(letter)

    if guess < len(HANGMAN_PICS) - 1:
        print(f"Congratulations, you guessed the correct word. The word was \"{word}\"")
    else:
        print(HANGMAN_PICS[guess])
        print(f"Sorry, the correct word was {word}")


def startGame():
    word = "".join(random.choice(words)).lower()
    guessed_letters = []
    guess = 0
    # print(word)
    freqMap = createWordFreqMap(word)

    print("Hello, welcome to Hangman.")
    gameLogic(word, guess, freqMap, guessed_letters)


startGame()
