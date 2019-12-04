# SQL exercises from udemy course. Part 1. Creating a database
CREATE DATABASE IF NOT EXISTS Sales;
USE Sales;
CREATE TABLE IF NOT EXISTS customers
(
	customer_id int not null primary key auto_increment,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email_address VARCHAR(255),
    number_of_complaints int not null 
);
Select * from sales.customers;

DROP TABLE customers;

-- Creating new tables
CREATE TABLE IF NOT EXISTS customers
(
	customer_id int,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email_address VARCHAR(255),
    number_of_complaints int,
PRIMARY KEY (customer_id)
);
-- items
CREATE TABLE items
(
	item_code varchar(255),
    item varchar(255),
    unit_price numeric(10,2),
    company_id varchar(255),
PRIMARY KEY (item_code)
);
-- companies
CREATE TABLE companies
(
	company_id varchar(255),
    company_name varchar(255),
    headquarters_phone_number int(12),
PRIMARY KEY (company_id)
);

DROP TABLE customers, items,  companies;
ALTER TABLE customers ADD unique KEY (email_address);

DROP TABLE customers;
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email_address VARCHAR(255),
    number_of_complaints INT,
    PRIMARY KEY (customer_id)
);
ALTER TABLE customers 
ADD COLUMN gender ENUM('M', 'F') AFTER last_name;
INSERT INTO customers (first_name, last_name, gender, email_address, number_of_complaints) 
				VALUES ('John', 'Mackinley', 'M','john.mckinley@365careers.com', 0);
CREATE TABLE companies (
    company_id VARCHAR(255),
    company_name VARCHAR(255) DEFAULT 'X',
    headquarter_phone_number VARCHAR(255) UNIQUE KEY
);
DROP TABLE companies;
ALTER TABLE companies CHANGE COLUMN headquarter_phone_number headquarter_phone varchar(255) not null;
ALTER TABLE companies CHANGE COLUMN headquarter_phone headquarter_phone varchar(255) null;