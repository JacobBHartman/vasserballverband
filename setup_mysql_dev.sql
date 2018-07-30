-- Set up the new database vbvb_dev_db and add user vbvb_dev
CREATE DATABASE IF NOT EXISTS vbvb_dev_db;
CREATE USER IF NOT EXISTS 'vbvb_dev'@'localhost' IDENTIFIED BY 'password';
-- Grant all privileges for vbvb_dev on vbvb_dev_db.
GRANT ALL ON vbvb_dev_db.* TO 'vbvb_dev'@'localhost';
-- Grant select privilege on performance_schema database to vbvb_dev.
GRANT SELECT ON performance_schema.* TO 'vbvb_dev'@'localhost';
