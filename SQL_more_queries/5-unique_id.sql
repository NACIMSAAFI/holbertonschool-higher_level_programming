-- Creates the table unique_id on MySQL server.
CREATE TABLE IF NOT EXISTS id_not_null (id INT PRIMARY KEY UNIQUE NOT NULL DEFAULT 1, name  VARCHAR(256))