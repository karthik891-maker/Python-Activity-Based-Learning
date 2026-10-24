days = int(input("Number of days: "))
total_prepared = total_served = 0
if days <= 0:
    print("Number of days must be positive.")
else:
    for day in range(1, days + 1):
        prepared = int(input("Meals prepared on day " + str(day) + ": "))
        served = int(input("Meals served: "))
        if prepared < 0 or served < 0 or served > prepared:
            print("Invalid counts; day not included.")
        else:
            leftovers = prepared - served
            waste = leftovers / prepared * 100 if prepared > 0 else 0
            print("Leftovers:", leftovers)
            print("Waste percentage: {:.2f}%".format(waste))
            if waste > 10:
                print("Warning: waste exceeds 10%.")
            total_prepared += prepared
            total_served += served
    left = total_prepared - total_served
    overall = left / total_prepared * 100 if total_prepared > 0 else 0
    print("Overall prepared:", total_prepared)
    print("Overall served:", total_served)
    print("Overall leftovers:", left)
    print("Overall waste percentage: {:.2f}%".format(overall))
