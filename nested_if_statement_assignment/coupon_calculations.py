"""docstring
This program is for creating order pricing."""

# Start


def calculate_price(price, cash_coupon, percent_coupon):
    # Tax variables
    tax = 1.06

    # Shipping variables
    shipping_10 = 5.95
    shipping_10to30 = 7.69
    shipping_30to50 = 11.95
    shipping_50up = 0

    # Calculation of price
    if price 


    # Return total price to whatever called the function
    return total_price
    # pass


def main():
    purchase_amount = input()
    cash_c = input()
    percent_c = input()
    price = calculate_price(purchase_amount, cash_c, percent_c)

    # pass


if __name__ == '__main__':
    main()
