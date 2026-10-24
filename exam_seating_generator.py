rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
students = input("Enter roll numbers separated by spaces: ").split()
if rows <= 0 or cols <= 0:
    print("Rows and columns must be positive.")
else:
    seats = [["--" for c in range(cols)] for r in range(rows)]
    reserved_count = int(input("Number of reserved seats: "))
    for i in range(reserved_count):
        r = int(input("Reserved row: ")) - 1
        c = int(input("Reserved column: ")) - 1
        if 0 <= r < rows and 0 <= c < cols:
            seats[r][c] = "RES"
    index = 0
    for r in range(rows):
        for c in range(cols):
            if seats[r][c] == "--" and index < len(students):
                seats[r][c] = students[index]
                index += 1
    for r in range(rows):
        print("Row", r + 1, ":", " | ".join(seats[r]))
    print("Unallocated roll numbers:", students[index:] if index < len(students) else "None")
