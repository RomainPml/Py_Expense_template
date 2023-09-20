from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"username",
        "message":"New User - Name:"
    }
]

def add_user():
    infos = prompt(user_questions)

    username = infos["username"]

    with open('user_report.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username])
    print(infos)
    return