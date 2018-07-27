# for i in range(4):
#     for j in range(6):
#         print("*", end=" ")
#     print()

# print("Hello", end=" ")
# print("Word")

for i in range(10):
    for j in range(10):
        if j <= 10 - i -1:
            print(" ", end=" ")
        else:   
            print("*", end=" ")
    print()