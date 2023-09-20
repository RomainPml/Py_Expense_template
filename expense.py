from PyInquirer import prompt, Separator
import csv

def read_users():
    users = []
    with open('user_report.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            users.extend(row)
    return users



def generate_expense_questions(users):
    choices = [{"name": user, "checked": True} for user in users]

    expense_questions = [
        {
            "type": "input",
            "name": "amount",
            "message": "New Expense - Total Amount: ",
        },
        {
            "type": "input",
            "name": "label",
            "message": "New Expense - Label: ",
        },
        {
            "type": "list",
            "name": "spender",
            "message": "Select Spender: ",
            "choices": choices,
        },
        {
            "type": "checkbox",  # Use "checkbox" type for selecting multiple involved users
            "name": "involved_users",
            "message": "Select Involved Users: ",
            "choices": [Separator("=== Users ===")] + choices,
        },
    ]

    return expense_questions

def new_expense():
    users = read_users()
    expense_questions = generate_expense_questions(users)

    infos = prompt(expense_questions)

    amount = float(infos["amount"])
    label = infos["label"]
    spender = infos["spender"]
    involved_users = infos["involved_users"]
    
    involved_users_str = ", ".join(involved_users)

    with open('expense_report.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow([amount, label, spender, involved_users_str])

    print("Expense Added!")
    return True
