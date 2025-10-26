-- PostgreSQL initialization script
-- This script runs when the database is first created

-- Create a sample table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);

-- Insert sample data (optional)
-- INSERT INTO users (username, email) VALUES ('admin', 'admin@example.com');

-- Create additional schemas if needed
-- CREATE SCHEMA IF NOT EXISTS app_schema;
