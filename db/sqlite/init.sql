-- SQLite sample schema and seed data
CREATE TABLE IF NOT EXISTS system_config (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  config_key TEXT,
  config_value TEXT
);
CREATE TABLE IF NOT EXISTS user_preferences (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  preference_key TEXT,
  preference_value TEXT
);
CREATE TABLE IF NOT EXISTS query_history (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  query_text TEXT,
  executed_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS schema_versions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  version TEXT,
  applied_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
-- Seed data
INSERT INTO system_config (config_key, config_value) VALUES
('theme', 'dark'),('language', 'en'),('timezone', 'UTC');
INSERT INTO schema_versions (version) VALUES
('v1.0'),('v1.1'),('v2.0');
-- Add 50 rows to user_preferences
WITH RECURSIVE cnt(x) AS (SELECT 1 UNION ALL SELECT x+1 FROM cnt WHERE x < 50)
INSERT INTO user_preferences (user_id, preference_key, preference_value)
SELECT x, 'notif', CASE WHEN x%2=0 THEN 'on' ELSE 'off' END FROM cnt;
-- Add 50 rows to query_history
WITH RECURSIVE cnt2(x) AS (SELECT 1 UNION ALL SELECT x+1 FROM cnt2 WHERE x < 50)
INSERT INTO query_history (user_id, query_text)
SELECT x, 'SELECT * FROM table' || x FROM cnt2;
