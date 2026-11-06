fee = int(input("Enter time of parking in hours: "))
if fee>1 and fee<2:
    print(f'You are obligated to pay f 5 pln for {fee} hours of parking')
elif fee>=3 and fee<6:
        print(f'You are obligated to pay f 15 pln for {fee} hours of parking')
elif fee>=6:
      print(f'You are obligated to pay f 20 pln for {fee} hours of parking')
else:
      print("Your parking was free!")
