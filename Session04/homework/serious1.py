name = input("Your full name:")
lower_name = name.lower()

words = lower_name.split()
space = " "
print("Updated:",(space.join(words)).title())
