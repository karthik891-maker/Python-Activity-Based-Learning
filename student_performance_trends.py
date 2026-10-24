subjects = ["Python", "Mathematics", "English", "Web Development"]
first = []
latest = []
valid = True
for subject in subjects:
    a = float(input("First exam mark for " + subject + ": "))
    b = float(input("Latest exam mark for " + subject + ": "))
    if not 0 <= a <= 100 or not 0 <= b <= 100:
        valid = False
        break
    first.append(a)
    latest.append(b)
if not valid:
    print("Invalid mark. Use values from 0 to 100.")
else:
    weak = []
    for i in range(len(subjects)):
        print(subjects[i], "change:", latest[i] - first[i])
        if latest[i] < 40:
            weak.append(subjects[i])
    average = sum(latest) / len(latest)
    print("Latest average: {:.2f}".format(average))
    print("Weak subjects:", weak if weak else "None")
    print("Classification:", "Strong" if average >= 75 else "Developing")
