import mysql.connector
import json

# Inserting the JSON data into MySQL Workbench

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host='localhost',
        user="root",
        password="1234",
        database="quickbuy"
    )
    cursor = connection.cursor()
    print("Successfully connected to the database")
    
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
    exit()

try:
    # Load JSON file
    with open("products.json", 'r', encoding="utf-8") as file:
        data = json.load(file)
    print("JSON file loaded successfully")
except Exception as err:
    print(f"Error opening JSON file: {err}")
    exit()

try:
    # Insert data into MySQL
    for item in data:
        sql = """
            INSERT INTO quickbuy.products 
            (id, title, description, category, price, discount_percentage, rating, stock, tags, brand, sku, weight, dimensions, 
            warranty_information, shipping_information, availability_status, reviews, return_policy, minimum_order_quantity, 
            meta, images, thumbnail)
            VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        values = (
            item.get("id", None),  # Safely get value or None
            item.get("title", None),
            item.get("description", None),
            item.get("category", None),
            item.get("price", None),
            item.get("discountPercentage", None),
            item.get("rating", None),
            item.get("stock", None),
            json.dumps(item.get("tags", [])),  # Convert list to JSON string, default to empty list
            item.get("brand", None),  # Use get to avoid KeyError
            item.get("sku", None),
            item.get("weight", None),
            json.dumps(item.get("dimensions", {})),  # Convert dictionary to JSON string, default to empty dict
            item.get("warrantyInformation", None),
            item.get("shippingInformation", None),
            item.get("availabilityStatus", None),
            json.dumps(item.get("reviews", [])),  # Convert list of objects to JSON string, default to empty list
            item.get("returnPolicy", None),
            item.get("minimumOrderQuantity", None),
            json.dumps(item.get("meta", {})),  # Convert dictionary to JSON string, default to empty dict
            json.dumps(item.get("images", [])),  # Convert list to JSON string, default to empty list
            item.get("thumbnail", None)
        )

        cursor.execute(sql, values)

    # Commit once after all the inserts
    connection.commit()

    print("Data inserted successfully!")

except mysql.connector.Error as err:
    print(f"Error inserting data into MySQL: {err}")
    connection.rollback()

finally:
    # Always close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed")
