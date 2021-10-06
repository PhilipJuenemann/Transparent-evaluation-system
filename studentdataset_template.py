num_students = int(input('Enter number of students: '))

all_students = []

for i in range (0, num_students):

    name = input('Enter the students name: ')
    print(name)

    birthdate = float(input('Enter the students birthdate (without year): '))
    print(str(birthdate))

    student_id =  1000 * (birthdate / 2)

    student_password = student_id * (12**2 - student_id // 222)


    all_students.append({
        'Name': name,
        'Birthdate': birthdate,
        'Student-ID-Number': int(student_id),
        'Studentpassword': int(student_password)
    })

print(all_students)

