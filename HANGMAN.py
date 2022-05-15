#HANGMAN-it is a game of guessing letters of a word which is randomly picked from dictonary
import random
words=["naidu","saladi","nagamani","nani"]
choice=random.choice(words)
#print(choice)
s=[i for i in choice]
rletter=random.choice(s)
#print(s)
lst=['_']*len(choice)
used=[]
for i in range(len(choice)):
    if choice[i]==rletter:
        lst[i]=rletter
print("clue letter is:",rletter)
print(*lst)
while(lst!=s):
    guess=input("enter your guess:")
    if(guess in lst):
        print(f"you already guessed the letter {guess}")
        print(*lst)
        
    elif(guess in s):
        for i in range(len(s)):
            if s[i]==guess:
                lst[i]=guess
        print(*lst)
    elif(guess in used ):
        print(f"You already used this letter {guess}")
        print(*lst)
    else:
        used.append(guess)
        print(f"Try again,your letter {guess} is not in word")
        print(*lst)
print("yes!you won the game")       
    
        