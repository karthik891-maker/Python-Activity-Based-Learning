names = []
totals = []
n = int(input("Number of products: "))
budget = float(input("Shopping budget (₹): "))
subtotal = 0
if n < 0 or budget < 0:
    print("Invalid input.")
else:
    for i in range(n):
        name = input("Product name: ")
        price = float(input("Unit price (₹): "))
        quantity = int(input("Quantity: "))
        if price < 0 or quantity < 0:
            print("Invalid price or quantity.")
            break
        names.append(name)
        totals.append(price * quantity)
        subtotal += price * quantity
    else:
        discount = subtotal * 0.10 if subtotal >= 2000 else 0
        final = subtotal - discount
        for i in range(len(names)):
            print(names[i], ": ₹{:.2f}".format(totals[i]))
        print("Subtotal: ₹{:.2f}".format(subtotal))
        print("Discount: ₹{:.2f}".format(discount))
        print("Final total: ₹{:.2f}".format(final))
        if final > budget:
            print("Over budget by: ₹{:.2f}".format(final - budget))
        else:
            print("Within budget; remaining: ₹{:.2f}".format(budget - final))
