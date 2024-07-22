# Personal Finance Manager

Personal Finance Manager is a Python application designed to help users manage their personal finances by tracking income and expenses. The application allows users to add, view, and analyze their financial transactions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [License](#license)

## Features

- **Add Transactions**: Add income and expense transactions with descriptions.
- **View Transactions**: Display a list of all transactions.
- **Analyze Spending**: Provide an analysis of spending habits over time.
- **CSV Storage**: Store transaction data in a CSV file for persistence.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AnushkaJainFirst/personal_finance_manager.git
   cd personal_finance_manager

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv\Scripts\activate

3. **Install the required packages**:
    pip install pandas matplotlib

## Usage

1. **Run the application**:
    ```bash
    python main.py

2. **Interact with the application**:

    ### Add a Transaction:
    Select option 1 to add a new transaction. You will be prompted to enter the transaction type (income/expense), amount, and description.

    ### View Transactions:
    Select option 2 to view all transactions. The list of transactions will be displayed in the terminal.

    ### Analyze Spending:
    Select option 3 to analyze spending. A spending analysis will be displayed, showing insights into your financial habits.

    ### Exit the application:
    Select option 4 to exit the application.

## Files

- **main.py**: The main script to run the application.
- **finance_manager.py**: Contains the `FinanceManager` class which handles all financial operations.
- **data/transactions.csv**: The CSV file where all transactions are stored.
- **README.md**: This file.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## Licence
This project is licensed under the MIT License.



