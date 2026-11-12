from datetime import datetime

now = datetime.now()

print("┌─────────────────────────────────────────────┐")
print("│         🥐☕ CROSSROADS CAFE 🌿🌿          │")
print("└─────────────────────────────────────────────┘")
print(f"Time: {now.strftime('%d %b %Y %I:%M %p')}")

customer_name = input("Please enter your name: ").strip()
print(f"\nWelcome, {customer_name}!")

if now.hour < 12:
    print("☀️ Good morning! Start your day with a fresh cup of coffee.")
elif now.hour < 18:
    print("🌤️ Good afternoon! Take a break and enjoy.")
else:
    print("🌙 Good evening! Relax and unwind with a warm drink.")


class Menu:
    def __init__(self):
        self.items = {
            "Hot Coffee": {"Espresso": 150, "Cappuccino": 220, "Latte": 240},
            "Cold Drinks": {"Iced Coffee": 250, "Cold Brew": 270},
            "Tea": {"Masala Tea": 100, "Green Tea": 120},
            "Pastries": {"Croissant": 180, "Blueberry Muffin": 160},
            "Donuts": {"Glazed Donut": 120, "Chocolate Donut": 140},
            "Snacks": {"Veg Sandwich": 200, "French Fries": 150},
        }

    def display_menu(self):
        print("\n📜 CROSSROADS CAFE MENU")
        print("=" * 40)
        for category, items in self.items.items():
            print(f"\n🍽️ {category}")
            print("-" * 40)
            for name, price in items.items():
                print(f"{name:<20} Rs. {price}")
        print("=" * 40)

    def find(self, query):
        """Case-insensitive lookup. Returns (name, price) or None."""
        query = query.strip().lower()
        for items in self.items.values():
            for name, price in items.items():
                if name.lower() == query:
                    return name, price
        return None


menu = Menu()
menu.display_menu()

order = input("\n🍽️ Enter dish name(s), separated by commas: ")

total = 0
not_found = []

print(f"\n🧾 ORDER FOR {customer_name.upper()}")
print("-" * 40)

for item in order.split(","):
    if not item.strip():
        continue  
    result = menu.find(item)
    if result:
        name, price = result
        print(f"✅ {name:<20} Rs. {price}")
        total += price
    else:
        not_found.append(item.strip())

print("-" * 40)
print(f"💰 Total: Rs. {total}")

if not_found:
    print(f"❌ Not on the menu: {', '.join(not_found)}")

print("\n🍩 Thank you for visiting Crossroads Cafe! Come again!")