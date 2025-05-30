def calculate_due_amount(total_bill, amount_paid):
    if amount_paid >= total_bill:
        return 0  # No due amount if the bill is fully paid
    else:
        return total_bill - amount_paid  # Calculate the remaining due amount

# Input from the user
try:
    total_bill = float(input("Enter the total bill amount: "))
    amount_paid = float(input("Enter the amount paid by the customer: "))

    # Calculate due amount
    due_amount = calculate_due_amount(total_bill, amount_paid)

    # Display the result
    if due_amount == 0:
        print("The bill is fully paid. No due amount.")
    else:
        print(f"The due amount is: ₹{due_amount:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values for the bill and payment.")