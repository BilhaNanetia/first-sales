import datetime
import json

class SalesRecord:
    def __init__(self):
        self.sales = {}

    def add_sale(self, item, quantity, price):
        date = datetime.date.today().isoformat()
        if date not in self.sales:
            self.sales[date] = []
        self.sales[date].append({"item": item, "quantity": quantity, "price": price})

    def get_daily_total(self, date):
        if date in self.sales:
            return sum(sale["quantity"] * sale["price"] for sale in self.sales[date])
        return 0

    def get_daily_sales(self, date):
        if date in self.sales:
            return self.sales[date]
        return []

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.sales, f)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                self.sales = json.load(f)
        except FileNotFoundError:
            print("No existing file found. Starting with an empty record.")

    def format_currency(self, amount):
        return f"KES {amount:,.2f}"

def main():
    record = SalesRecord()
    filename = "sales_record.json"
    record.load_from_file(filename)

    while True:
        print("\n1. Add Sale")
        print("2. Get Daily Total")
        print("3. View Daily Sales")
        print("4. Save and Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item (in KES): "))
            record.add_sale(item, quantity, price)
            print("Sale added successfully!")

        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            total = record.get_daily_total(date)
            print(f"Total sales for {date}: {record.format_currency(total)}")

        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            daily_sales = record.get_daily_sales(date)
            if daily_sales:
                print(f"\nSales for {date}:")
                for i, sale in enumerate(daily_sales, 1):
                    print(f"{i}. Item: {sale['item']}, Quantity: {sale['quantity']}, Price: {record.format_currency(sale['price'])}")
            else:
                print(f"No sales recorded for {date}")

        elif choice == '4':
            record.save_to_file(filename)
            print("Sales record saved. Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()