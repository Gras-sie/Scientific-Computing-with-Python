# Expense Tracker using Lambda Functions
# This program demonstrates the use of functional programming concepts in Python

# Function to add a new expense to our list of dictionaries
# Each expense is stored as a dictionary with 'amount' and 'category' keys
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
# Function to display all expenses in a formatted way
# Demonstrates string formatting and dictionary access
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
# Function using lambda and map to calculate total expenses
# map() applies the lambda function to each expense in the list
# lambda creates an anonymous function that extracts the amount from each expense
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
# Function using lambda with filter to get expenses of a specific category
# filter() creates an iterator of expenses that match the category
# lambda provides the filtering condition
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

# Main program loop implementing a command-line interface
def main():
    # Initialize empty list to store expenses
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        # Handle user input and execute corresponding functions
        if choice == '1':
            # Add new expense
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            # Display all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            # Show total using our lambda and map implementation
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            # Filter and display expenses by category using lambda and filter
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            # Exit the program
            print('Exiting the program.')
            break

main()
# This code is a simple expense tracker that allows users to add expenses, list all expenses, show total expenses, and filter expenses by category.
# It uses a list of dictionaries to store the expenses, where each dictionary contains the amount and category of an expense.
# The program runs in a loop until the user chooses to exit.
