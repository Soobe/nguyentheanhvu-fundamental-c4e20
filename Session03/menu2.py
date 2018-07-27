favs = ["netflix", "teaching", "death note"]

print("Hi there,here you favorite things so far")
print("* "* 10)

for index, fav in enumerate(favs):
    print("{}. {}".format(index + 1 ,fav))

print("* "* 10)

pos = int(input("Position you want to update : ")

update_fav = (input("Your replacing fav: "))

favs[pos -1] = update_fav

print("Hi there,here you favorite things so far")
print("* "* 10)

for index, fav in enumerate(favs):
    print("{}. {}".format(index + 1 ,fav))

print("* "* 10)
