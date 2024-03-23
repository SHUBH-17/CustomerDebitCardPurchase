-- Create database in RDS
Create Database Sales;

--Inside Sales DB
Use Sales;

-- Create table command
CREATE TABLE customer_transaction (
    customer_id INT,
    debit_card_number VARCHAR(255),
    bank_name VARCHAR(255),
    total_amount_spend INT,
    PRIMARY KEY (customer_id)
);
