students = ["Student 1", "Student 2", "Student 3"]
subjects = ["Python", "Mathematics", "English", "Web Development"]
marks = []
for student in students:
    row = []
    print("Marks for", student)
    for subject in subjects:
        row.append(float(input(subject + " (0-100): ")))
    marks.append(row)
totals = []
for i in range(len(students)):
    total = sum(marks[i])
    totals.append(total)
    print(students[i], "total:", total, "average:", "{:.2f}".format(total / len(subjects)))
best = max(totals)
print("Top performer(s):")
for i in range(len(students)):
    if totals[i] == best:
        print(students[i], "with", best)
print("Subject averages:")
for c in range(len(subjects)):
    total = 0
    for r in range(len(students)):
        total += marks[r][c]
    average = total / len(students)
    print(subjects[c], "{:.2f}".format(average))
    if average < 50:
        print("Warning: low average in", subjects[c])
