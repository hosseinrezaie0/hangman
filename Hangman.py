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

