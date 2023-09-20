from PyInquirer import prompt
import csv

def get_expenses_from_report():
    expenses = []
    with open('expense_report.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            expenses.append(row)
    return expenses

def distribute_expenses():
    expenses = get_expenses_from_report()
    
    contributions = {}
    balances = {}
    
    for expense in expenses:
        amount = float(expense[0])
        spender = expense[2]
        involved_users = expense[3].split(', ')
        
        if spender not in contributions:
            contributions[spender] = 0
        contributions[spender] += amount
        
        for user in involved_users:
            if user not in contributions:
                contributions[user] = 0
            contributions[user] -= amount
    
    for user, contribution in contributions.items():
        balances[user] = contribution
    
    distribution = []
    for firstUser in balances:
        for secondUser in balances:
            if firstUser != secondUser:
                balance = balances[firstUser] - balances[secondUser]
                if balance > 0:
                    distribution.append(f"{firstUser} owes {balance:.2f}€ to {secondUser}")
    
    return distribution
