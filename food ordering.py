# Simulated user database
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "alice": {"password": "alice123", "role": "user"},
    "bob": {"password": "bob123", "role": "user"}
}
# Simple menu for food ordering
menu = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Sandwich": 4.99,
    "Fries": 2.99,
    "Soda": 1.99
}
order = {}
# Display food menu
def display_menu():
    print("\n------ MENU ------")
    if not menu:
        print("Menu is currently empty.")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

# Take user's order
def take_order():
    while True:
        item = input("\nEnter item to order (or 'done' to finish): ").title()
        if item.lower() == 'done':
            break
        elif item in menu:
            try:
                qty = int(input(f"Enter quantity for {item}: "))
                if item in order:
                    order[item] += qty
                else:
                    order[item] = qty
            except ValueError:
                print("❌ Invalid quantity.")
        else:
             print("❌ Item not found in menu.")
# Print receipt
def print_receipt():
    print("\n------ RECEIPT ------")
    total = 0
    for item, qty in order.items():
        subtotal = menu[item] * qty
        total += subtotal
        print(f"{item} x {qty} = ${subtotal:.2f}")
    print(f"Total Amount: ${total:.2f}")
    print("✅ Thank you for your order!")

# Admin panel to modify menu
def admin_panel():
    while True:
        print("\n🔐 Admin Panel:")
        print("1. View Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Exit Admin Panel")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            display_menu()
        elif choice == '2':
            item = input("Enter item name to add: ").title()
            try:
                price = float(input("Enter price for item: "))
                menu[item] = price
                print(f"✅ '{item}' added to the menu.")
            except ValueError:
                print("❌ Invalid price.")
        elif choice == '3':
            item = input("Enter item name to remove: ").title()
            if item in menu:
                del menu[item]
                print(f"✅ '{item}' removed from the menu.")
            else:
                print("❌ Item not found in menu.")
        elif choice == '4':
            print("Exiting Admin Panel...")
            break
        else:
            print("❌ Invalid choice.")

# Login system
def login():
    print("=== Food Ordering System Login ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print(f"✅ Login successful! Welcome, {username}.")
        return users[username]["role"]
    else:
        print("❌ Invalid credentials. Try again.")
        return None	

# Main logic
def main():
    role = login()
    if not role:
        return

    if role == "admin":
        admin_panel()
    elif role == "user":
        display_menu()
        take_order()
        print_receipt()

# Run
main()
