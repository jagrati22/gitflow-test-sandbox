def calculate_discount(price, discount):
    # Testing function for GitFlow IDE refactor
    final_price = price - (price * discount)
    print("Calculating final price...")
    return final_price

result = calculate_discount(100, 0.2)
print("Result:", result)
