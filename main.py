from PyInquirer import prompt
from examples import custom_style_2
from expense import new_expense
from user import add_user
from balance import distribute_expenses

def main():
    while True:
        options = [
            {
                "type": "list",
                "name": "menu",
                "message": "Expense Tracker v0.1",
                "choices": ["New Expense", "Show Status", "New User", "Quit"],
            }
        ]

        choice = prompt(options)["menu"]

        if choice == "New Expense":
            new_expense()
        elif choice == "Show Status":
            status_report = distribute_expenses()
            if status_report:
                print("Status Report:")
                for line in status_report:
                    print(line)
            else:
                print("No expenses found.")
        elif choice == "New User":
            add_user()
        elif choice == "Quit":
            break

main()