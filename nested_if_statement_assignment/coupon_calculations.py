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

    # Calculation of price after coupons
    # NEED IF STATEMENT FOR COUPONS - LOGIC ERROR
    price_after_c = (float(price) - float(cash_coupon)) * (float(percent_coupon) / float(100))

    # Calculation of price after shipping
    if float(price_after_c) < float(10.00):
        price_after_s = float(price_after_c) + float(shipping_10)
    elif float(10.00) <= float(price_after_c) < float(30.00):
        price_after_s = float(price_after_c) + float(shipping_10to30)
    elif float(30.00) <= float(price_after_c) < float(50.00):
        price_after_s = float(price_after_c) + float(shipping_30to50)
    elif float(50.00) < float(price_after_c):
        price_after_s = float(price_after_c) + float(shipping_50up)
    else:
        return "Please enter a positive number for price."

    # Calculation of price after tax
    total_price = float(price_after_s) * float(tax)

    # Return total price
    return total_price
    # pass


def main():
    purchase_amount = input("Please enter the initial purchase price: ")
    cash_c = input("Please enter any cash coupons: ")
    percent_c = input("Please enter any percent coupons: ")
    price = calculate_price(purchase_amount, cash_c, percent_c)

    print(str(price))

    # pass


if __name__ == '__main__':
    main()
