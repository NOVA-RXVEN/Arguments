def calculateBill(b, tp):
    total = b* (1 + (0.01 * tp ))
    return total

bill = int(input("Enter the bill amount: "))
tipPerc = float(input("Enter the Tip Percentage: "))

total = calculateBill(bill, tipPerc)

print(f"Total Tip : {total-bill}")
print(f"\n\nTotal bill with tip : {total}")