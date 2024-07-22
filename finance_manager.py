import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

class FinanceManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.transactions = []
        self.load_transactions()
    
    def load_transactions(self):
        try:
            with open(self.file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.transactions.append(row)
        except FileNotFoundError:
            print(f"{self.file_path} not found. Starting with an empty list.")
    
    def save_transactions(self):
        with open(self.file_path, mode='w', newline='') as file:
            fieldnames = ['date', 'type', 'amount', 'description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in self.transactions:
                writer.writerow(transaction)
    
    def add_transaction(self):
        date = datetime.now().strftime("%Y-%m-%d")
        type = input("Enter transaction type (income/expense): ")
        amount = input("Enter amount: ")
        description = input("Enter description: ")
        
        self.transactions.append({
            'date': date,
            'type': type,
            'amount': amount,
            'description': description
        })
        self.save_transactions()
        print("Transaction added successfully.")
    
    def view_transactions(self):
        for transaction in self.transactions:
            print(transaction)
    
    def analyze_spending(self):
        df = pd.DataFrame(self.transactions)
        df['amount'] = pd.to_numeric(df['amount'])
        expenses = df[df['type'] == 'expense']
        income = df[df['type'] == 'income']
        
        print(f"Total Income: {income['amount'].sum()}")
        print(f"Total Expenses: {expenses['amount'].sum()}")
        print(f"Net Savings: {income['amount'].sum() - expenses['amount'].sum()}")
        
        # Visualization
        expenses_by_category = expenses.groupby('description')['amount'].sum()
        expenses_by_category.plot(kind='bar')
        plt.title('Expenses by Category')
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

