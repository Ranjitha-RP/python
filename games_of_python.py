#quiz game in python
questions = ("what is your name:",
             "what is your age:",
             "whwre u frm:",
             "name ur fav animal:",
             "name your fav car:")

options = (('a.ranjitha','b.nav','c.banana','d.grap',),
           ('a.2','b.5','c.6','d.78',),
           ('a.manglore','b.bang','c.coorg','d.goa',),
           ('a.cat','b.dog','c.monkey','d.pig',),
           ('a.bmw','b.toyata','c.kia','d.duster',),)
answer = ('c','d','a','d','a')
guesses = []
score=0
question_num = 0

for question in questions:
    print(question)
    
    for option in options[question_num]:
        print(option)

    guess = input("enter(a,b,c,d):").lower()
    guesses.append(guess)
    if guess == answer[question_num]:
        
        print("correct!")
    else:
        print("incorrect")
        print(f"{answer[question_num]} is the correct one")
    question_num +=1

score = int (score / len(questions)*100)
score += 1
print(score)
   
    
#cocession program
menue = {"chips":120.00,
         "bear":1200.00,
         "coca":1500.00,
         "meal":150.00,
         "popcorn":123.00,
         "neam":500.00,
         }
cart = []
total = 0
print("-----MENUE-----")
for keys,values in menue.items():
    print(f"{keys}:{values:.2f}")


print("----------------")

while True:
    food = input("enter the food to buy from menue:")
    if food == "q":
        break
    elif menue.get(food) is not None:
        cart.append(food)
print(cart)
for food in cart:
    total += menue.get(food)
    print(food,end=" ")

print()
print(f"total is:{total}")






#python number guess game
import random


lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number,highest_number )
guesses = 0
is_running = True

print("python number guess game")
print(f"select a number between {lowest_number} and{highest_number}:")

while  is_running:
    guess = input("enter your guess:")
    if guess.isdigit():
        guess = int (guess)
        guesses +=1
        if guess < lowest_number or guess >highest_number:
            print("out of range")
        elif guess < answer:
            print("too low!try again")
        elif guess > answer:
            print("too high!try again")
        else:
            print(f"correct! the answer was {answer} ")
            print(f"number of guess {guesses}")
            is_running = False
        
    else:
        print("invalid")
        print(f"select a number between {lowest_number} and{highest_number}:")

import random

options = ("rock","paper","scissors")

running = True 

while running:
    player = None
    computer = random.choice(options)

    while player not in options:# not in  is a member ship operator if the option is not there in it always ask you for nxt option
        player = input("enter the choice( rock,paper,scissors): ")
    print(f"palyer:{player}")
    print(f"computer:{computer}")

    if player == computer:
        print("its a tie")
    elif player=="rock" and computer == "scissors":
        print("you win")
    elif player== "paper" and computer=="rock":
        print("you win")
    elif player== "scissors" and computer=="paper":
        print("you win")
    else:
        print("you loose")

    if not input("play again? (y/n):").lower() == "y":
        running = False
print("thank you")      


import random

# Predefined list of 5 words
words = ["apple", "mango", "grape", "lemon", "peach"]

# Choose a random secret word
secret_word = random.choice(words)
# Create a list of underscores for the word
display = ["_"] * len(secret_word)

# Number of allowed incorrect guesses
incorrect_guesses= 6

# Keep track of letters already guessed
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Main game loop
while guessed_letters > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Lives left:", incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if the guessed letter is in the secret word
    if guess in secret_word:
        for i, letter in enumerate(secret_word):
            if letter == guess:
                display[i] = guess
        print("Good guess!")
    else:
        incorrect_guesses -= 1
        print("Wrong guess!")

# End of game — win or lose
if "_" not in display:
    print("\n You guessed the word:", secret_word)
else:
    print("\n You ran out of lives. The word was:", secret_word)

 

