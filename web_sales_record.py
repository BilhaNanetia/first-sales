from flask import Flask, render_template, request, jsonify
import datetime
import json
import os

app = Flask(__name__)

class SalesRecord:
    def __init__(self):
        self.sales = {}
        self.load_from_file("sales_record.json")

    def add_sale(self, item, quantity, price):
        date = datetime.date.today().isoformat()
        if date not in self.sales:
            self.sales[date] = []
        self.sales[date].append({"item": item, "quantity": int(quantity), "price": float(price)})
        self.save_to_file("sales_record.json")

    def get_daily_total(self, date):
        if date in self.sales:
            return sum(sale["quantity"] * sale["price"] for sale in self.sales[date])
        return 0

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.sales, f)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.sales = json.load(f)
        else:
            print("No existing file found. Starting with an empty record.")

    def format_currency(self, amount):
        return f"KES {amount:,.2f}"

record = SalesRecord()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_sale', methods=['POST'])
def add_sale():
    item = request.form['item']
    quantity = request.form['quantity']
    price = request.form['price']
    record.add_sale(item, quantity, price)
    return jsonify({"message": "Sale added successfully!"})

@app.route('/get_daily_total', methods=['POST'])
def get_daily_total():
    date = request.form['date']
    total = record.get_daily_total(date)
    return jsonify({"total": record.format_currency(total)})

if __name__ == '__main__':
    app.run(debug=True)