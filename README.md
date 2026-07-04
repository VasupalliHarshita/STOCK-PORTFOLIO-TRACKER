# Stock Portfolio Tracker (Python)

## Project Overview

The **Stock Portfolio Tracker** is a simple Python console application that calculates the total value of a user's stock investments. The user enters stock names and the number of shares owned, while the program uses a predefined dictionary of stock prices to calculate the investment value.

The application also saves the investment details to a text file (`portfolio.txt`) for future reference.

This project is ideal for beginners learning Python and demonstrates the use of dictionaries, loops, conditional statements, user input, arithmetic operations, and file handling.

---

## Features

* Displays a list of available stocks and their prices.
* Accepts stock names and quantities from the user.
* Uses a predefined dictionary to store stock prices.
* Calculates the investment value for each stock.
* Calculates the total portfolio value.
* Handles invalid stock names.
* Validates quantity input to prevent errors.
* Saves the portfolio report to a text file (`portfolio.txt`).
* Console-based application requiring no external libraries.

---

## Technologies Used

* Python 3
* Built-in Python libraries only

---

## Python Concepts Used

* Variables
* Dictionary
* User Input (`input()`)
* Conditional Statements (`if-else`)
* Loops (`for`, `while`)
* Exception Handling (`try-except`)
* Arithmetic Operators
* File Handling (`open()`, `write()`, `close()`)

---

## Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_portfolio_tracker.py
├── portfolio.txt
└── README.md
```

---

## How the Program Works

1. The program stores stock prices in a Python dictionary.

2. It displays the available stocks and their prices.

3. The user enters the number of different stocks they own.

4. For each stock:

   * Enter the stock symbol.
   * Enter the quantity of shares.

5. The program checks whether the stock exists in the dictionary.

6. If the stock exists:

   * It calculates the investment value using:

   **Investment = Stock Price × Quantity**

7. The investment value is added to the total portfolio value.

8. After all entries are completed, the total investment is displayed.

9. The complete report is saved to **portfolio.txt**.

---

## Algorithm

1. Start the program.
2. Create a dictionary containing predefined stock prices.
3. Display all available stocks.
4. Initialize the total investment to 0.
5. Ask the user for the number of different stocks.
6. Repeat for each stock:

   * Read the stock name.
   * Validate the stock name.
   * Read the quantity.
   * Validate the quantity.
   * Calculate the investment value.
   * Add it to the total investment.
   * Save the details to the report file.
7. Display the total investment.
8. Save the total investment to `portfolio.txt`.
9. Close the file.
10. End the program.

---

## Sample Input

```text
How many different stocks do you own?
2

Enter Stock Name:
AAPL

Enter Quantity:
5

Enter Stock Name:
TSLA

Enter Quantity:
4
```

---

## Sample Output

```text
===================================
      STOCK PORTFOLIO TRACKER
===================================

Available Stocks:
AAPL : $180
TSLA : $250
GOOGL : $140
MSFT : $320
AMZN : $150

Stock 1
Enter Stock Name: AAPL
Enter Quantity: 5

Investment in AAPL: $900

Stock 2
Enter Stock Name: TSLA
Enter Quantity: 4

Investment in TSLA: $1000

===================================
Total Investment: $1900
===================================

Portfolio saved successfully in 'portfolio.txt'
```

---

## Example `portfolio.txt`

```text
STOCK PORTFOLIO REPORT
======================

Stock: AAPL, Price: $180, Quantity: 5, Investment: $900
Stock: TSLA, Price: $250, Quantity: 4, Investment: $1000

======================
Total Investment: $1900
```

---

## Time Complexity

* **Time Complexity:** O(n), where **n** is the number of different stocks entered by the user.
* **Space Complexity:** O(1), excluding the output file, because the stock dictionary has a fixed size.

---

## Learning Outcomes

By completing this project, you will learn how to:

* Use dictionaries to store key-value pairs.
* Accept and validate user input.
* Perform arithmetic calculations.
* Use loops to process multiple inputs.
* Apply conditional statements for decision-making.
* Handle invalid input using exception handling.
* Write data to a text file using file handling.

---

## Future Enhancements

* Fetch live stock prices using a stock market API.
* Store portfolio data in a CSV or Excel file.
* Calculate profit and loss.
* Add a graphical user interface (GUI).
* Display investment charts and graphs.
* Support buying and selling of stocks.
* Save multiple user portfolios.

---

## Author

**Harshita Vasupalli**

Engineering Student

GitHub: https://github.com/VasupalliHarshita
