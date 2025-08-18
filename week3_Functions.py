# function to calculate the final price after applying a discount
# if the discount is 20% or more, apply the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * (100 - discount_percent) / 100
    else:
        final_price = price
    return final_price

# prompt the user for input and calculate the final price
price = float(input("Enter the original price of the item:"))
discount_percent = float(input("Enter the discount percentage:"))
if discount_percent >=20:
    print("The final price after applying the discount is:", calculate_discount(price, discount_percent))
else:
    print("With no discount applied, the final price is:", price)
    
    