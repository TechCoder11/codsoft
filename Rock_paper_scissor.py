import random
print("Let's play ROCK-SCISSOR-PAPER Game")
while True:
    u=input("Enter your choice amongst rock,paper,scissor:")
    l=['paper','rock','scissor']
    c=random.choice(l)
    print("Computer's choice:",c)
    if u=='rock' and c=='scissor':
        print("Congrats!! You Won")
    elif u=='rock' and c=='paper':
         print("You lose")
    elif u=='rock' and c=='rock':
        print("It's a tie")
    elif u=='paper' and c=='rock':
        print("Congrats!! You Won")
    elif u=='paper' and c=='scissor':
        print("You lose")
    elif u=='paper' and c=='paper':
        print("It's a tie")    
    elif u=='scissor' and c=='rock':
        print("You lose")
    elif u=='scissor' and c=='paper':
        print("Congrats!! You Won")
    elif u=='scissor' and c=='scissor':
        print("It's a tie")
    else:
         print("Enter the correct spelling with all lowercase letters")
    Again=input("Do you want to play again?\nIf yes type y, if no type n:")
    if Again.lower()!="y":
        print("Well Played")
        break
    