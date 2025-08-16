-- MySQL sample schema and seed data
CREATE TABLE IF NOT EXISTS sales_analytics (
  id INT AUTO_INCREMENT PRIMARY KEY,
  product_id INT,
  sales_count INT,
  sales_date DATE
);
CREATE TABLE IF NOT EXISTS customer_segments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  segment_name VARCHAR(100),
  description TEXT
);
CREATE TABLE IF NOT EXISTS product_performance (
  id INT AUTO_INCREMENT PRIMARY KEY,
  product_id INT,
  rating FLOAT,
  review_count INT
);
CREATE TABLE IF NOT EXISTS regional_data (
  id INT AUTO_INCREMENT PRIMARY KEY,
  region VARCHAR(100),
  sales INT
);
-- Seed data
INSERT INTO customer_segments (segment_name, description) VALUES
('Premium', 'High value customers'),('Standard', 'Regular customers'),('Budget', 'Price sensitive customers');
INSERT INTO regional_data (region, sales) VALUES
('North', 1000),('South', 800),('East', 1200),('West', 900);
-- Add 50 rows to sales_analytics
SET @i = 1;
WHILE @i <= 50 DO
  INSERT INTO sales_analytics (product_id, sales_count, sales_date) VALUES ((@i % 7) + 1, (@i % 10) + 1, DATE_ADD('2025-08-01', INTERVAL @i DAY));
  SET @i = @i + 1;
END WHILE;
-- Add 50 rows to product_performance
SET @i = 1;
WHILE @i <= 50 DO
  INSERT INTO product_performance (product_id, rating, review_count) VALUES ((@i % 7) + 1, ROUND(RAND()*5,2), (@i % 100) + 1);
  SET @i = @i + 1;
END WHILE;
