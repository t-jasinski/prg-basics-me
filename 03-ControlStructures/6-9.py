name = str(input("Enter name: "))
lenght_name = len(name)
print(lenght_name)
last_letter = name[(lenght_name) - 1 ]
if last_letter == 'a':
    print(f"{name} is a woman")
else:
    print(f"{name} is a man")