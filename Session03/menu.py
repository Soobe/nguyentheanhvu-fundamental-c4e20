#list / array

menu = ["Cơm", "Cá","Thịt bò", "Ghẹ", "Pizza", "Gà", ]
#update:
print(*menu,sep=", ")
menu[4]= "Tôm hùm"
print(*menu,sep=", '")


# print(*menu, sep=", ")  #separator
# size = len(menu)  #length
# menu.append("Ghẹ")
# print(len(menu))


# for i in range(len(menu)):
#     print(menu[i])

# for index, item in enumerate(menu):
#1     print(index + 1, item, sep="." )
#2     print("{}. {}".format(index +1, item))  //Thêm phần từ trong dấu {}

# for item in menu:
#     print(item)