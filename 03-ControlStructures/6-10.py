dog_age = int(input("Enter the dog's age: "))
human_dog_age = 0
if dog_age>2:
    human_dog_age = human_dog_age + 21
    dog_age1 = dog_age - 2
    human_dog_age = human_dog_age + dog_age1*4
    print(f"Your dog is {human_dog_age} years old")
else:
    human_dog_age = dog_age*10.5
    print(f"Your dog is {human_dog_age} years old")