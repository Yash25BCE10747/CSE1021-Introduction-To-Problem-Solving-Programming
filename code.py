# Online Shopping Cart System

products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Headphones", "price": 1500},
    3: {"name": "Mouse", "price": 700},
    4: {"name": "Keyboard", "price": 1200}
}

cart = {}

def show_products():
    print("\nAvailable Products:")
    for pid, info in products.items():
        print(pid, "-", info["name"], "₹", info["price"])

def add_to_cart():
    pid = int(input("Enter product id to add: "))
    if pid in products:
        cart[pid] = cart.get(pid, 0) + 1
        print("Added to cart.")
    else:
        print("Invalid product ID.")

def remove_from_cart():
    pid = int(input("Enter product id to remove: "))
    if pid in cart:
        del cart[pid]
        print("Removed from cart.")
    else:
        print("Item not in cart.")

def view_cart():
    if not cart:
        print("\nCart is empty.")
        return
    print("\nYour Cart:")
    total = 0
    for pid, qty in cart.items():
        price = products[pid]["price"]
        print(products[pid]["name"], "x", qty, "=", price * qty)
        total += price * qty
    print("Total Amount: ₹", total)

def main():
    while True:
        print("\n1. Show Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice.")

main()
