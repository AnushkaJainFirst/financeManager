from finance_manager import FinanceManager

def main():
    fm = FinanceManager('data/transactions.csv')
    
    while True:
        print("\nPersonal Finance Management System")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Analyze Spending")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            fm.add_transaction()
        elif choice == '2':
            fm.view_transactions()
        elif choice == '3':
            fm.analyze_spending()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



