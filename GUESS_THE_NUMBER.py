#GUESS THE NUMBER 
import random
def guess(x):# In this function we have to guess the number 
    random_number=random.randint(1,x)# x is the range
    guess=0# we initialize guess with zero because 
           #initial guess must not be equal to random num(before input)
           #so we initialized with zero which will never be equal to num >1
    while guess!=random_number:
        guess=int(input(f'Guess a number between 1 and {x}:'))
        if guess<random_number:
            print("Sorry, guess again.Your guess is Too low")
        elif guess>random_number:
            print("Sorry, guess again.Your guess is Too high")
    #we continue till we get a right guess 
    #if guess is equal to random_number loop will break
    #And prints the output
    print(f"yes!,Congrats.You have guessed the right number {guess}")
def computer_guess(x):#In this function computer will guess your random number
    print("I Started game:")#Here I means computer
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is {guess} correct(C),too high(H),too low(L):').lower()#if user enters
        if(feedback=='c'):
            break
        elif(feedback=='h'):
            high=guess-1
        elif feedback=='l':
            low=guess+1
        else:
            print("please enter right feedback")
    print(f"yes,I Guess the right number {guess}")
        
computer_guess(10)   
guess(10)