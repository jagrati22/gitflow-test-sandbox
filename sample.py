def calculate_discount(price, discount):
    # Validate payload
    if not isinstance(price, (int, float)):
        print("Error: Price must be a number.")
        return None
    if not isinstance(discount, (int, float)):
        print("Error: Discount must be a number.")
        return None

    if not (0 <= discount <= 1):
        print("Error: Discount must be between 0 and 1 (inclusive).")
        return None

    # Add try-except error handling for the calculation
    try:
        final_price = price - (price * discount)
        print("Calculating final price...")
        return final_price
    except Exception as e:
        print(f"An unexpected error occurred during calculation: {e}")
        return None

result = calculate_discount(100, 0.2)
print("Result:", result)

# Example of invalid inputs
result_invalid_price_type = calculate_discount("invalid", 0.2)
print("Result (invalid price type):", result_invalid_price_type)

result_invalid_discount_range = calculate_discount(100, 1.5)
print("Result (invalid discount range):", result_invalid_discount_range)

result_invalid_discount_type = calculate_discount(100, "invalid")
print("Result (invalid discount type):", result_invalid_discount_type)