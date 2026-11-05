price = float(input("Enter Price: "))
discount = float(input("Enter discount %: "))
red = price * discount/100
p_d = price - red
print(f"Prince with discount: {p_d}")
print(f"Reduction: {float(red)}")