-- Rename column in user_preferences
ALTER TABLE user_preferences RENAME COLUMN preference_key TO pref_key;
-- Split table: create new table for user_notifications
CREATE TABLE user_notifications AS SELECT id AS pref_id, user_id, preference_value FROM user_preferences;
