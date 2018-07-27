from random  import randint
count = 0
numb = randint (0, 100)
print(numb)

playing = True
while playing:
    guess = int(input("Guess my number (0-100) ?"))
    if guess < numb:
        print("Too small :(")

    elif guess > numb:
        print("Too large :( ")

    else:
        print("Bingo  ")    
        playing =False
        break

    count += 1
    if count == 7:
        print("you lose")
        playing = False    
