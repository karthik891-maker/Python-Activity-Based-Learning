conducted = int(input("Classes conducted: "))
attended = int(input("Classes attended: "))
target = float(input("Required attendance percentage: "))
if conducted < 0 or attended < 0 or attended > conducted or not 0 <= target <= 100:
    print("Invalid input.")
elif conducted == 0:
    print("Attendance percentage is unavailable.")
else:
    current = attended / conducted * 100
    future = 0
    while (attended + future) / (conducted + future) * 100 < target:
        future += 1
    print("Current attendance: {:.2f}%".format(current))
    print("Minimum classes to attend:", future)
    print("Attendance afterwards: {:.2f}%".format((attended + future) / (conducted + future) * 100))
