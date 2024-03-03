def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

price = float(input("Enter the price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if final_price == price:
    print(f"No discount applied. Final price: ${final_price}")
else:
    print(f"Discount applied. Final price after discount: ${final_price}")
