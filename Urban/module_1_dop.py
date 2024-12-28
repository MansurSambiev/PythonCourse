grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = []
gpa = {}
avg_grades = []

for student in students:
    sorted_students.append(student)
sorted_students.sort()

for i in range(5):
    avg_grades.append(sum(grades[i])/len(grades[i]))

gpa = dict(zip(sorted_students, avg_grades))
print(gpa)