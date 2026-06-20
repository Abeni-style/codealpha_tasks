stocks_data = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140
}

total = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock (or 'done'): ").upper()

    if stock == "DONE":
        break

    if stock in stocks_data:
        qty = int(input("Quantity: "))
        total += stocks_data[stock] * qty
        print("Added")
    else:
        print("Not found")

print("Total value:", total)