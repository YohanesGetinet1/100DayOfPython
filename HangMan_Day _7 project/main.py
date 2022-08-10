import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
game_is_finished = False
# the amount of times you can guess for the letter
lives = len(stages) - 1
# chosen_word will be selected from word_list randomly
chosen_word = random.choice(word_list)

word_length = len(chosen_word)
# empty list to take each letters from the selected word
display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    # take input from user and keep as guess and change to lower case
    guess = input("Guess a letter: ").lower()

    # Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")
    # if the letter guessed is in the display list tell the user it's already guessed
    for position in range(word_length):
        letter = chosen_word[position]
        # this for loop check the guessed letter in the given word
        if letter == guess:
            display[position] = letter
            # if letter at the current position and the guess is same we show letter instead of "_"
    print(f"{' '.join(display)}")
    # join all the elements in the display list and turn to String

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        # this if statement check if the guess is correct or not
        #  if not it decrement 1 life each time we didn't guess correct
        if lives == 0:
            game_is_finished = True
            print("You lose.")
            # if live become zero game will end and the user lose

    if "_" not in display:
        game_is_finished = True
        print("You win.")
        # check if the user correctly guessed all letters and no more "_" in display list
        # if True the game will end and the user will win

    print(stages[lives])
# print each stage of the hangman by number of lives remaining
