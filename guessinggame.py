import random
print("number guessing game")
number=random.randint(1,9)
numberofchances=0
print("guess a number between 1 to 9")
while numberofchances<5:
    guess=int(input("enter your guess"))
    if guess==number:
        print("congratulation! you got it right")
        break
    elif guess<number:
        print("guess was too low ,guess a higher numberthan ",guess)
    else: 
        print("guess was too high, guess a lower number than",guess)
    numberofchances+=1
if not numberofchances<5:
    print("you lose the number was",number)