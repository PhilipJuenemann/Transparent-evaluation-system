import pandas as pd
import string
import random

characters = list(string.ascii_letters + string.digits)
numbers = list(string.digits)
num_students = int(input('Enter number of students: '))

all_students = []
for i in range(0, num_students):

    username = input('Enter the students name: ')
    print(username)

    id_length = 5
    random.shuffle(numbers)
    id = []
    for i in range(id_length):
        id.append((random.choice(numbers)))
    random.shuffle(id)
    id = ("".join(id))

    password_length = 8
    random.shuffle(characters)
    password = []
    for i in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = ("".join(password))

    all_students.append({
        'Username': username,
        'ID-Number': id,
        'Studentpassword': password
    })

print(all_students)

df = pd.DataFrame(all_students)
df.to_csv('student.csv')