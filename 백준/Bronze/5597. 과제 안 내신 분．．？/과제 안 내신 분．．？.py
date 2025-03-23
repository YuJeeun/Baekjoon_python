all_students = set(range(1, 31))
submitted_students = set(int(input()) for _ in range(28))
missing_students = sorted(all_students - submitted_students)
for student in missing_students:
    print(student)
