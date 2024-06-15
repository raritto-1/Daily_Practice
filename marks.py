if __name__ == '__main__':
    num_students = int(input("Enter the number of students: "))

    students = []

    for _ in range(num_students):
        name = input("Enter a name: ")
        grade = float(input("Enter the grade: "))
        students.append([name, grade])

    sorted_students = sorted(students, key=lambda x: (x[1], x[0]))

    second_lowest_grade = sorted_students[0][1]
    for student in sorted_students:
        if student[1] > second_lowest_grade:
            second_lowest_grade = student[1]
            break

    # Extract names of students with the second lowest grade
    second_lowest_names = [student[0] for student in sorted_students if student[1] == second_lowest_grade]

    # Print the result
    print("Students with the second lowest grade (alphabetically):")
    for name in second_lowest_names:
        print(name)
