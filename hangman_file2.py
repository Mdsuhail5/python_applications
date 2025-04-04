import random
import hangman_file1

print(hangman_file1.title)

chosen_word = random.choice(hangman_file1.word_list)

lives = 6
display = []
# checking
print(chosen_word)


for n in range(0, len(chosen_word)):
    display += "_"

print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter of the word : ").lower()
    for x in range(len(chosen_word)):
        if chosen_word[x] == guess:
            display[x] = guess
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}")
        print(hangman_file1.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose...")

    if "_" not in display:
        end_of_game = True
        print("You Win!")
