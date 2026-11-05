###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
h = int(input('c='))
vol = a*b*h
surface = a*b*2 + a*h*2 + b*h*2
print(f"cuboid with sides {a,b,h} has volume of {vol}")
print(f"and surface of the cuboid is {surface}")