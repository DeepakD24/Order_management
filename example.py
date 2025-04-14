import mysql.connector

# Step 1: Connect to MySQL and create database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",         
        password="deepak..AK",  
    )

def create_database():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS order__management")
    db.close()

# Step 2: Create tables
def create_tables():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="deepak..AK",
        database="order__management"
    )
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            CustomerID INT PRIMARY KEY,
            Name VARCHAR(100),
            Email VARCHAR(100),
            Address VARCHAR(255)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Suppliers (
            SupplierID INT PRIMARY KEY,
            Name VARCHAR(100),
            Contact VARCHAR(100)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            ProductID INT PRIMARY KEY,
            Name VARCHAR(100),
            Price DECIMAL(10,2),
            Stock INT,
            SupplierID INT,
            FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            OrderID INT PRIMARY KEY,
            CustomerID INT,
            OrderDate DATETIME,
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS OrderDetails (
            OrderDetailID INT PRIMARY KEY,
            OrderID INT,
            ProductID INT,
            Quantity INT,
            FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
            FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
        )
    """)
    db.commit()
    db.close()

# Step 3: Insert sample data
def insert_data():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="deepak..AK",
        database="order__management"
    )
    cursor = db.cursor()

    customers = [
	(1, "Jagadeesh", "22ee016@kpriet.ac.in", "123 Main St mannarai,Tiruppur"),
        (2, "Amreth", "22ee002@kpriet.ac.in", "45 Avenue Park,Erode"),
	(3, "Sadhur", "22ee046@kpriet.ac.in", "6 Gsquare,Tiruppur")
    ]
    suppliers = [
        (1, "Tech Supplier", "tech@suppliers.com"),
        (2, "Gadget Hub", "contact@gadgethub.com")
    ]
    products = [
        (1, "Laptop", 45000.00, 10, 1),
        (2, "Mouse", 5000.00, 50, 2),
        (3, "Keyboard", 5000.00, 30, 1),
	(4, "HeadPhones", 2000.00, 30, 1),

    ]
    orders = [
        (1, 1, "2025-04-13 10:00:00"),
        (2, 2, "2025-04-13 11:30:00")
    ]
    order_details = [
        (1, 1, 1, 1),
        (2, 1, 2, 2),
        (3, 2, 3, 1)
    ]

    cursor.executemany("INSERT IGNORE INTO Customers VALUES (%s, %s, %s, %s)", customers)
    cursor.executemany("INSERT IGNORE INTO Suppliers VALUES (%s, %s, %s)", suppliers)
    cursor.executemany("INSERT IGNORE INTO Products VALUES (%s, %s, %s, %s, %s)", products)
    cursor.executemany("INSERT IGNORE INTO Orders VALUES (%s, %s, %s)", orders)
    cursor.executemany("INSERT IGNORE INTO OrderDetails VALUES (%s, %s, %s, %s)", order_details)

    db.commit()
    db.close()

# Run everything
create_database()
create_tables()
insert_data()
print("✅ Database setup complete.")
