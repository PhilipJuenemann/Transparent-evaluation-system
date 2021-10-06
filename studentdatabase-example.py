n = int(input("Please enter number of students:"))

all_students = []

for i in range(0, n):
    stud_name = input('Enter the name of student: ')
    print(stud_name)

    mark1 = int(input('Enter the marks in subject 1: '))
    print(int(mark1))

    mark2 = int(input('Enter the marks in subject 2: '))
    print(int(mark2))

    mark3 = int(input('Enter the marks in subject 3: '))
    print(int(mark3))

    total = mark1 + mark2 + mark3
    print("Total is: ", int(total))

    average = int(total) / 3
    print("Average is :", average)

    all_students.append({
                            'Name': stud_name,
                            'Mark1': mark1,
                            'Mark2': mark2,
                            'Mark3': mark3,
                            'Total': total,
                            'Average': average
                            })




