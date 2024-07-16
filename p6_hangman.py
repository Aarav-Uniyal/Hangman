import p6_1_hangman_art
import p6_2_hangman_words
import random

print(p6_1_hangman_art.logo)

chosen_word=random.choice(p6_2_hangman_words.word_list)
display=[]
for i in range(len(chosen_word)):
    display.append('_')

game_over=False
life=6
while not game_over:
    if life==0:
        game_over=True
        print("YOU LOSE.")
        print(f"The word was {chosen_word}.")
    if '_' not in display:
        game_over=True
        print("YOU WIN!")

    guess=input("Guess the letter: ").lower()

    if guess in display:
         print(f"You've already guessed {guess}.")
   
    for j in range(len(chosen_word)):
        letter=chosen_word[j]
        if letter==guess:
            display[j]=letter

    if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            life-=1
            
    
    print(f"{' '.join(display)}")
    print(p6_1_hangman_art.stages[life])
