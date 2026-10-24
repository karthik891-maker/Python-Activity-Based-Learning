balance = float(input("Opening balance: "))
count = int(input("Number of transactions: "))
records = []
accepted = rejected = 0
if balance < 0 or count < 0:
    print("Invalid opening balance or transaction count.")
else:
    for i in range(count):
        kind = input("Transaction type (D/W): ").upper()
        amount = float(input("Amount: "))
        if amount <= 0:
            status = "Rejected: amount must be positive"
            rejected += 1
        elif kind == "D":
            balance += amount
            status = "Accepted deposit"
            accepted += 1
        elif kind == "W" and amount <= balance:
            balance -= amount
            status = "Accepted withdrawal"
            accepted += 1
        else:
            status = "Rejected: invalid type or insufficient balance"
            rejected += 1
        records.append((kind, amount, status))
        print(status)
    print("Transaction summary")
    for kind, amount, status in records:
        print(kind, amount, "-", status)
    print("Final balance: {:.2f}".format(balance))
    print("Accepted:", accepted, "Rejected:", rejected)
