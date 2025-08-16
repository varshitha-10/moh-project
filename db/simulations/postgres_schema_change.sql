-- Rename column in products
ALTER TABLE products RENAME COLUMN name TO product_name;
-- Split table: create new table for product_pricing
CREATE TABLE product_pricing AS SELECT id AS product_id, price FROM products;
ALTER TABLE products DROP COLUMN price;
-- Add row-level security
ALTER TABLE customers ENABLE ROW LEVEL SECURITY;
CREATE POLICY customer_isolation ON customers USING (email = current_user);
