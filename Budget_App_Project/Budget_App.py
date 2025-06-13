class Category:
    # Initialize a new budget category with a name and an empty ledger
    def __init__(self, category):
        self.ledger = []        # List to store all transactions (deposits/withdrawals)
        self.cat = category     # Name of the category

    # Add a deposit to the ledger with amount and optional description
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # Attempt to withdraw an amount with optional description
    # Only succeeds if there are enough funds (uses check_funds)
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    # Calculate and return the current balance by summing all amounts in the ledger
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    # Transfer funds to another Category object
    # Withdraws from this category and deposits into the other
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.cat}")
            category.deposit(amount, f"Transfer from {self.cat}")
            return True
        return False

    # Check if there are enough funds for a withdrawal or transfer
    def check_funds(self, amount):
        return self.get_balance() >= amount

    # String representation of the Category object for printing
    # Shows the title, all ledger items, and the total
    def __str__(self):
        # Build the header with the category name centered in a 30-char field, padded by '*'
        title = self.cat.center(30, "*") + "\n"

        # Prepare to accumulate each ledger line as a formatted string
        items = ""
        # Loop through each transaction entry in the ledger
        for item in self.ledger:
            # Take up to 23 chars of description, left-align within 23 spaces
            desc = item["description"][:23].ljust(23)
            # Format the amount to 2 decimal places, right-align within 7 spaces
            amt = f"{item['amount']:>7.2f}"
            # Combine description and amount, then add a newline
            items += f"{desc}{amt}\n"

        # After listing all items, append the total balance line
        total = f"Total: {self.get_balance():.2f}"
        # Return the full string: title + items + total
        return title + items + total


# Function to create a spend chart for a list of Category objects
def create_spend_chart(categories):
    # Calculate spending per category and overall total
    spend_amounts = []
    total_spent = 0
    max_name_len = 0

    for category in categories:
        # Sum only the withdrawal amounts (negative values) for this category
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spend_amounts.append(spent)
        total_spent += spent
        # Keep track of the longest category name for vertical labels
        max_name_len = max(max_name_len, len(category.cat))

    # Convert spending to percentages, rounded down to nearest 10
    percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in spend_amounts]

    # Start building the chart with its title
    chart = "Percentage spent by category\n"
    # For each row label from 100 down to 0 stepping by 10:
    for i in range(100, -1, -10):
        # Right-align the percentage label in width 3, then add the '|' separator
        chart += str(i).rjust(3) + "|"
        # For each category, place an 'o' if its percentage >= current row, else spaces
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        # Finish the row with a space and newline
        chart += " \n"

    # Add the horizontal separator line (4 spaces + dashes for each category slice)
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Build the vertical category names line by line
    for i in range(max_name_len):
        # 5-space indent to align under the chart bars
        line = "     "
        for category in categories:
            # Append the i-th character of the category name or spaces
            line += (category.cat[i] + "  ") if i < len(category.cat) else "   "
        # Append newline on all but the last label line
        chart += line + ("\n" if i < max_name_len - 1 else "")

    return chart
