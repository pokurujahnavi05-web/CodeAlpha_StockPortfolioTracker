
# CodeAlpha Internship
# Project: Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 190
}

# Store portfolio details
portfolio = []

total_investment = 0

print("===================================")
print("       STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("\nEnter 'done' when finished.")

# Get stock details from user
while True:
    stock_name = input("\nEnter stock name: ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock name! Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity

    total_investment += investment

    portfolio.append({
        "stock": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    print("Stock added successfully!")

# Display portfolio summary
print("\n===================================")
print("         PORTFOLIO SUMMARY")
print("===================================")

if len(portfolio) == 0:
    print("No stocks were added.")
else:
    print("\nStock\tQuantity\tPrice\tTotal")

    for item in portfolio:
        print(
            f"{item['stock']}\t"
            f"{item['quantity']}\t\t"
            f"${item['price']}\t"
            f"${item['investment']}"
        )

    print("-----------------------------------")
    print(f"Total Investment: ${total_investment}")

    # Save portfolio to text file
    with open("portfolio_report.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("======================\n\n")

        for item in portfolio:
            file.write(
                f"Stock: {item['stock']}, "
                f"Quantity: {item['quantity']}, "
                f"Price: ${item['price']}, "
                f"Investment: ${item['investment']}\n"
            )

        file.write("\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("\nPortfolio report saved successfully!")

print("\nThank you for using Stock Portfolio Tracker!")
