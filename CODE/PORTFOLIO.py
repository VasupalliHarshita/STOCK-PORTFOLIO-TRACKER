
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# Total investment
total_investment = 0

# Number of different stocks
while True:
    try:
        n = int(input("\nHow many different stocks do you own? "))
        if n > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid number.")

# Open text file
file = open("portfolio.txt", "w")

file.write("STOCK PORTFOLIO REPORT\n")
file.write("======================\n\n")

# Loop for stock entries
for i in range(n):

    print(f"\nStock {i + 1}")

    stock = input("Enter Stock Name: ").upper()

    if stock not in stock_prices:
        print("Stock not available.")
        file.write(f"{stock} : Not Available\n")
        continue

    # Quantity input
    while True:
        try:
            quantity = int(input("Enter Quantity: "))
            if quantity > 0:
                break
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a valid quantity.")

    # Calculate investment
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"Investment in {stock}: ${investment}")

    file.write(
        f"Stock: {stock}, Price: ${stock_prices[stock]}, "
        f"Quantity: {quantity}, Investment: ${investment}\n"
    )

# Display total investment
print("\n===================================")
print(f"Total Investment: ${total_investment}")
print("===================================")

# Save total investment
file.write("\n======================\n")
file.write(f"Total Investment: ${total_investment}\n")

file.close()

print("\nPortfolio saved successfully in 'portfolio.txt'")