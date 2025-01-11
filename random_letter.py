# Generate a random letter from the alphabet. No letter is used twice.

import random
import time

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Let me pick a random letter for you...")
time.sleep(2)
print() # to insert a line of white space
input("...press [ENTER] to get your first letter")


while len(letters) >= 1:
    random.shuffle(letters)
    print()
    print("Your random letter is:", letters.pop(0))
    time.sleep(3)
    input("Press [ENTER] to get the next letter")


print()    
print("no letters left")
