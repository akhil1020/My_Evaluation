# 9. Bank Transaction Analyzer (Representation & Clarity)
# Write a Python program that allows users to input a series of transactions (credits and debits). Your
# program should:
# • Record each transaction clearly.
# • Calculate and print the balance after each transaction.
# • Provide a final summary at the end.

#----------solution--------->>
def bank_transaction_analyzer():
    balance = 0 
    transactions = []  
    
    print("Welcome to the Bank Transaction Analyzer")
    print("You can enter 'credit' or 'debit' followed by the amount.")
    print("To stop, enter 'done'.\n")
    
    while True:
        transaction = input("Enter transaction (credit/debit <amount>) or 'done' to finish: ").strip().lower()
        if transaction == 'done':
            break  
        
        try:

            transaction_type, amount = transaction.split()
            amount = float(amount)  
            
            if transaction_type == 'credit':
                balance += amount
                transactions.append(f"Credited: ${amount:.2f}")
            elif transaction_type == 'debit':
                balance -= amount
                transactions.append(f"Debited: ${amount:.2f}")
            else:
                print("Invalid transaction type. Please enter 'credit' or 'debit'.")
                continue
            
        
            print(f"Balance after transaction: ${balance:.2f}\n")
        
        except ValueError:
            print("Invalid input. Please enter a valid transaction (e.g., 'credit 100' or 'debit 50').")
    

    print("\nTransaction Summary:")
    for transaction in transactions:
        print(transaction)
    
    print(f"\nFinal Balance: ${balance:.2f}")
    

bank_transaction_analyzer()
