

# CodeAlpha Stock Portfolio Tracker

## Project Description
The Stock Portfolio Tracker is a simple Python-based application developed as part of the CodeAlpha Python Internship.

This project allows users to enter stock names and quantities, calculate their total investment value using predefined stock prices, and generate a portfolio report.

## Features
- Displays available stocks and their prices.
- Allows users to enter stock names and quantities.
- Calculates individual stock investment values.
- Calculates the total investment value.
- Handles invalid stock names and quantities.
- Saves the portfolio details in a text file.

## Technologies Used
- Python 3
- Visual Studio Code

## Python Concepts Used
- Dictionaries
- Lists
- While Loop
- For Loop
- If-elif-else statements
- User Input and Output
- Exception Handling
- File Handling

## Available Stocks

| Stock Symbol | Price |
|---|---:|
| AAPL | $180 |
| TSLA | $250 |
| GOOGL | $140 |
| MSFT | $400 |
| AMZN | $190 |

## Sample Output

```text
STOCK PORTFOLIO TRACKER

Available Stocks:
AAPL : $180
TSLA : $250
GOOGL : $140
MSFT : $400
AMZN : $190

Enter stock name: AAPL
Enter quantity: 2
Stock added successfully!

Enter stock name: TSLA
Enter quantity: 3
Stock added successfully!

Enter stock name: DONE

PORTFOLIO SUMMARY

Stock   Quantity   Price   Total
AAPL    2          $180    $360
TSLA    3          $250    $750

Total Investment: $1110

Portfolio report saved successfully!
```

## How to Run the Project

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project in Visual Studio Code.
4. Run the following command in the terminal:

```bash
python CodeAlpha.py
```

5. Enter stock symbols and quantities.
6. Type `done` to finish and view the portfolio summary.

## Output File
The program automatically generates `portfolio_report.txt` containing the stock details and total investment value.

## Internship
**CodeAlpha Python Programming Internship**
