# Lab 2:

def display_mailing_label(name, address, city, state, zip):
    print(f"{name}\n{address}\n{city}, {state} {zip}")

def add_numbers(*args):
    result = sum(args)
    numbers_str = "+".join(str(n) for n in args)
    print(f"{numbers_str} = {result}")

def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")
    change = amount_paid - total_due
    if change >= 0:
        print(f"Change Due: ${change:.2f}")
    else:
        print(f"Remaining Balance: ${abs(change):.2f}")

# 5a:
display_mailing_label("Sarah John", "123 Main St", "Wilmington", "DE", "10101")
display_mailing_label("Harry Smith", "456 Augustine St", "Chicago", "IL", "20202")

# 5b:
add_numbers(4)
add_numbers(5, 6)
add_numbers(1, 2, 4, 7)

# 5c:
display_receipt(50.00, 60.00)  # overpay
display_receipt(50.00, 50.00)  # exact
display_receipt(50.00, 40.00)  # underpay