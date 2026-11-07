if washing_product == 'j' or washing_product == 'J':
    washing_time += 40
    washing_product = 'Jacket'
elif washing_product == 'u' or washing_product == 'U':
    if washing_product == 'u' or washing_product == 'U':
        washing_time += 70
        washing_product = 'Underwear'
elif washing_product == 's' or washing_product == 'S':
    if washing_product == 's' or washing_product == 'S':
        washing_time += 20
        washing_product = 'Shoes'
else:
    print("Invalid input. Please enter 'j', 'u', or 's'.")