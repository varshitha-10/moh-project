-- PostgreSQL sample schema and seed data
CREATE TABLE IF NOT EXISTS customers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS orders (
  id SERIAL PRIMARY KEY,
  customer_id INT REFERENCES customers(id),
  product_id INT,
  order_date DATE,
  quantity INT
);
CREATE TABLE IF NOT EXISTS products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  category_id INT,
  price NUMERIC(10,2)
);
CREATE TABLE IF NOT EXISTS inventory (
  id SERIAL PRIMARY KEY,
  product_id INT REFERENCES products(id),
  stock INT
);
CREATE TABLE IF NOT EXISTS suppliers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  contact VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100)
);

-- Seed data
INSERT INTO categories (name) VALUES
('Electronics'),('Books'),('Clothing'),('Home'),('Toys'),('Sports');
INSERT INTO suppliers (name, contact) VALUES
('Acme Corp', 'acme@example.com'),('BookWorld', 'books@example.com'),('Fashionista', 'fashion@example.com'),('HomeGoods', 'home@example.com'),('ToyBox', 'toys@example.com'),('Sportify', 'sports@example.com');
INSERT INTO products (name, category_id, price) VALUES
('Laptop', 1, 999.99),('Smartphone', 1, 599.99),('Novel', 2, 19.99),('T-shirt', 3, 14.99),('Sofa', 4, 499.99),('Action Figure', 5, 24.99),('Basketball', 6, 29.99);
INSERT INTO customers (name, email) VALUES
('Alice Smith', 'alice@example.com'),('Bob Jones', 'bob@example.com'),('Carol Lee', 'carol@example.com'),('David Kim', 'david@example.com'),('Eva Green', 'eva@example.com');
-- Add more customers up to 50
DO $$
DECLARE i INT := 6;
BEGIN
  WHILE i <= 50 LOOP
    INSERT INTO customers (name, email) VALUES ('Customer ' || i, 'customer' || i || '@example.com');
    i := i + 1;
  END LOOP;
END$$;
-- Orders and inventory
INSERT INTO orders (customer_id, product_id, order_date, quantity) VALUES
(1,1,'2025-08-01',1),(2,2,'2025-08-02',2),(3,3,'2025-08-03',1),(4,4,'2025-08-04',3),(5,5,'2025-08-05',1);
-- Add more orders up to 50
DO $$
DECLARE i INT := 6;
BEGIN
  WHILE i <= 50 LOOP
    INSERT INTO orders (customer_id, product_id, order_date, quantity) VALUES (i, (i % 7) + 1, '2025-08-' || (i % 28 + 1), (i % 5) + 1);
    i := i + 1;
  END LOOP;
END$$;
INSERT INTO inventory (product_id, stock) VALUES (1, 100),(2, 150),(3, 200),(4, 80),(5, 60),(6, 120),(7, 90);
