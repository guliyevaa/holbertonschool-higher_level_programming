from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# JSON reading function
def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)

# CSV reading function
def read_csv(file_path):
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

# SQLite reading function
def read_sqlite(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
        return products
    except Exception as e:
        print(f"Database error: {e}")
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    id_filter = request.args.get('id', type=int)

    # Validate source
    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', error="Wrong source", products=None)

    # Read data based on source
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    else:  # sql
        data = read_sqlite('products.db')
        if data is None:
            return render_template('product_display.html', error="Database error", products=None)

    # Filter by id if provided
    if id_filter:
        filtered = [product for product in data if product["id"] == id_filter]
        if not filtered:
            return render_template('product_display.html', error="Product not found", products=None)
        data = filtered

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True)
