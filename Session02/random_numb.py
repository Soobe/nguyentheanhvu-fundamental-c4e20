from random import randint 

# rand_numb = randint(0, 100)

# print(rand_numb)

mood = randint(0, 100)

if mood < 30:
    print ("I feel sad")

elif mood < 60: 
    print("I feel ok")

else:
    print("oh yeah !")
    