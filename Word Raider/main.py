import random
from words import words

word = random.choice(words).lower()
print(word)
print(f"This word has {len(word)} letters")

hint1 = input("Want a hint (Y/n): ").lower()
if hint1 == "y":
    print(f"ok, the first letter of this word is '{word[0]}'")
elif hint1 == "n":
    print("ok, good luck")
count = 3
turn_took = 0

while True:
    answer1 = input("Enter the correct word: ").lower().strip()
    if answer1 == word and turn_took == 1:
        print(f"Damn you guessed the answer in just {turn_took} turn...")
        break
    elif answer1 != word:
        print("That's wrong answer, try again!!")
        count -= 1
        turn_took += 1
        if count == 0:
            hint2 = (input("It seems like you are struggling, want another hint(Y/n): ")).lower()
            if hint2 == "y":
                print(f"last letter of the word is '{word[-1]}'")
            elif hint2 == "n":
                print("ok then, all the best")
    else:
        print(f"LOL...Loser, you took {turn_took} turns to solve the question 😂😂😂")
        break
