import random
from modules.hangman_words import word_list
from modules.hangman_art import stages, logo


end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)

# Creates blanks
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = str(input("Please guess a letter: ")).lower()

    if guess in display:
        print(f"You have already guessed {guess}")
    
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in this word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE!!")
    print(f"{' '.join(display)}")        

    
    if "_" not in display:
        end_of_game = True
        print("YOU WIN!!!")
    print(stages[lives])