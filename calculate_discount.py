def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount and calculate the final price
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt user for input with additional context
item_name = input("Enter the name of the item: ")
original_price = float(input(f"Enter the original price of {item_name}: "))
discount_percent = float(input(f"Enter the discount percentage for {item_name}: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the result based on whether the discount was applied
if final_price == original_price:
    print(f"No discount applied. The price of {item_name} is ${final_price:.2f}.")
else:
    print(f"After applying the {discount_percent}% discount, the price of {item_name} is ${final_price:.2f}.")
