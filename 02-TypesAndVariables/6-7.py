###
# A program that prints a numerical representation of each letter of your name.
#
name = str(input("Type in your name: ")) # replace John with your name
lenght = len(name)
i=0
for i in range (lenght):
    print(f'The letter {name[i]} has a code {ord(name[i])}')