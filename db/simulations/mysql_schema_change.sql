-- Rename column in sales_analytics
ALTER TABLE sales_analytics CHANGE sales_count total_sales INT;
-- Split table: create new table for sales_summary
CREATE TABLE sales_summary AS SELECT product_id, SUM(total_sales) AS total FROM sales_analytics GROUP BY product_id;
