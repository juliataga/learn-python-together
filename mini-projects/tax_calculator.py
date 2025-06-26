print("Hello, this program takes your input for total cost, tax rate, & what % you want to tip.")
print("then calculate and print out total, total with tax, & tip amount.")

total_cost = float(input("enter total cost: "))
tax_rate = float(input("enter tax rate: "))
tip_percent = float(input("enter the tip percent: "))

total_tax = (tax_rate / 100 ) * total_cost
total_with_tax = total_tax + total_cost
total_tip = (tip_percent / 100) * total_with_tax

print("---------\nHere is what you will pay\n")
print(f"Total without tax:\t{total_cost}")
print(f"Total with tax:\t\t{total_with_tax}")
print(f"Tip ammount:\t\t{total_tip}")


print("-------\nThank you for using this program! Have a great day!")