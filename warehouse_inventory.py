items = []
n = int(input("Number of products: "))
for i in range(n):
    name = input("Product name: ")
    opening = int(input("Opening stock: "))
    received = int(input("Received: "))
    dispatched = int(input("Dispatched: "))
    physical = int(input("Physical closing stock: "))
    target = int(input("Target stock: "))
    if min(opening, received, dispatched, physical, target) < 0 or dispatched > opening + received:
        print("Invalid quantities; record skipped.")
    else:
        items.append((name, opening, received, dispatched, physical, target))
for name, opening, received, dispatched, physical, target in items:
    expected = opening + received - dispatched
    print(name, "expected:", expected, "physical:", physical)
    print("Discrepancy:", physical - expected)
    print("Replenishment:", max(0, target - physical))
