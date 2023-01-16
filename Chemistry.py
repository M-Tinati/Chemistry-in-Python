# Chemistry in Python
# It reads the weight of water in liters and counts the number of its molecules

# m = The weight of a molecule
# l = The weight of one liter of water
# w = Weight of water in liters
# number = Number of water molecules

w = int(input("Enter liter of water : "))
m = 4.5e-24
l = 305
number = (w * l) / m
print("Number of water molecules = ", number)
