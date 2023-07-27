#import
import random
from HangmanWords import words_list
from HangmanLogo import *


#print hangman logo
print(logo)
print(status[0])
print()



#choose a word from words_list randomly
chosen_word = random.choice(words_list)
for i in range(0, len(chosen_word)):
    print("_", end=" ")

#create answer
answer = []
for i in range(0, len(chosen_word)):
    answer.append("_")

print()


lives_left = 6
letters_left = len(chosen_word)

while(lives_left > 0 and letters_left > 0):
    guess = str(input("Guess a letter: "))
    guess = guess.lower()
    print()

    for i in range(0, len(chosen_word)):
        if guess in chosen_word[i]:
            if guess not in answer[i]:
                answer[i] = guess
                letters_left -= 1
    
    if guess not in chosen_word:
        lives_left -= 1

    print(answer)
    print(status[6-lives_left])

if lives_left == 0:
    print("GAME OVER")
    print(f"The word was {chosen_word}")
else:
    print("YOU WON")
