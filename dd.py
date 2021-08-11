for i in range (4,-1,-1):
    n=int(input("Guess the number bw 1 and 50\n"))
    if n==35:
        print("congratulations!! you the number ")
        if i==4:
            break
    elif i==0:
        print("Game Over")        
    elif i<0:
        print("you took ",i," guesses to guess")
    else:
        if n>30 and n<35:        
            print("close to the no guess a bit higher")
        elif n>35 and n<41:    
            print("close to the no guess a bit lower")
        else:
            print("try better")
        print("you have",i,"chances left")