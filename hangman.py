import random

words_list = ["python", "code", "intern", "github", "project"]
word = random.choice(words_list)

guessed_letters = []
tries = 6

print("Hangman Game Started!")

while tries > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("You win!")
        break

    guess = input("Guess a letter: ").lower()

    # validation (ONLY required safety check)
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input")
        continue

    if guess in guessed_letters:
        print("Already guessed")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        tries -= 1
        print("Wrong! Tries left:", tries)
    else:
        print("Correct!")

if tries == 0:
    print("Game over! Word was:", word)