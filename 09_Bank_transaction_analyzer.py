# 9. Bank Transaction Analyzer (Representation & Clarity)
# Write a Python program that allows users to input a series of transactions (credits and debits). Your
# program should:
# • Record each transaction clearly.
# • Calculate and print the balance after each transaction.
# • Provide a final summary at the end.

#----------solution--------->>
def bank_transaction_analyzer():
    balance = 0  # Initial balance
    transactions = []  # List to store transaction history
    
    print("Welcome to the Bank Transaction Analyzer")
    print("You can enter 'credit' or 'debit' followed by the amount.")
    print("To stop, enter 'done'.\n")
    
    while True:
        # Get user input for transaction type and amount
        transaction = input("Enter transaction (credit/debit <amount>) or 'done' to finish: ").strip().lower()
        
        if transaction == 'done':
            break  # Exit the loop if the user is done
        
        try:
            # Split the transaction into type and amount
            transaction_type, amount = transaction.split()
            amount = float(amount)  # Convert amount to float for calculations
            
            if transaction_type == 'credit':
                balance += amount
                transactions.append(f"Credited: ${amount:.2f}")
            elif transaction_type == 'debit':
                balance -= amount
                transactions.append(f"Debited: ${amount:.2f}")
            else:
                print("Invalid transaction type. Please enter 'credit' or 'debit'.")
                continue
            
            # Display the balance after the transaction
            print(f"Balance after transaction: ${balance:.2f}\n")
        
        except ValueError:
            print("Invalid input. Please enter a valid transaction (e.g., 'credit 100' or 'debit 50').")
    
    # Final summary of transactions and balance
    print("\nTransaction Summary:")
    for transaction in transactions:
        print(transaction)
    
    print(f"\nFinal Balance: ${balance:.2f}")
    
# Run the program
bank_transaction_analyzer()
