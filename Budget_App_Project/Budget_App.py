class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        # Appends a deposit to the ledger with amount and description (default empty string)
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # Appends a withdrawal to the ledger as a negative amount if funds are sufficient
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Title line
        title = f"{self.name.center(30, '*')}\n"
        # Ledger lines
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            # Amount right-aligned, description left-aligned, total width 30
            items += f"{desc:<23}{amt:>7}\n"
        # Total line
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    # Calculate total spent per category (withdrawals only)
    spent = []
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)
    total_spent = sum(spent)
    # Calculate percentage spent per category, rounded down to nearest 10
    percents = [int((s / total_spent) * 100) // 10 * 10 for s in spent]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}|"
        for p in percents:
            chart += " o " if p >= i else "   "
        chart += " \n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Prepare category names for vertical printing
    names = [cat.name for cat in categories]
    maxlen = max(len(name) for name in names)
    for i in range(maxlen):
        chart += "     "
        for name in names:
            chart += (name[i] if i < len(name) else " ") + "  "
        if i < maxlen - 1:
            chart += "\n"
    return chart.rstrip("\n")
