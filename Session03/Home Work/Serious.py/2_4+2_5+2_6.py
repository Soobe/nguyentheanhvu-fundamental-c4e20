fl = [5, 7, 300, 90, 24, 50, 75]
print ("Hello my name is Mam and here are my sheep's sizes")

print(fl)

print ("Now my biggest sheep has size", max(fl), "let's shear it")


print("MONTH 1:")
print("One month has passed, now here is my flock")
newfl1 = [x+50 for x in fl]
print(newfl1)
print ("Now my biggest sheep has size", max(newfl1), "let's shear it")
print("After shearing, here is my flock")
newfl1 [newfl1.index(max(newfl1))] = 8
print(newfl1)


print("MONTH 2:")
print("Two month has passed, now here is my flock")
newfl2 = [x+50 for x in newfl1]
print(newfl2)
print ("Now my biggest sheep has size", max(newfl2), "let's shear it")
print("After shearing, here is my flock")
newfl2 [newfl2.index(max(newfl2))] = 8
print(newfl2)

print("MONTH 3:")
print("Three month has passed, now here is my flock")
newfl3 = [x+50 for x in newfl2]
print(newfl3)
print ("Now my biggest sheep has size", max(newfl3), "let's shear it")
print("After shearing, here is my flock")
newfl3 [newfl3.index(max(newfl3))] = 8
print(newfl3)

print("My flock's size in total:", sum(newfl2))
print("I would get", sum(newfl2), "* 2$ =", sum(newfl2) * 2,"$")

