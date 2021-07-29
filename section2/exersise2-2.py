#!/usr/bin/env python3

# exersise 2-2

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?

price = 24.95

bookstore_price = 0.4 * price

books_price = (bookstore_price * 60)

shipping_price = 3 + (0.75 * 59)

total_price = books_price + shipping_price

print(total_price)
