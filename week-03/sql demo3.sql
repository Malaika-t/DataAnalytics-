-- Malaika Tariq
-- April 20, 2026
SHOW DATABASES;

USE northwind;
SHOW TABLES;
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'northwind'
AND table_type = 'BASE TABLE';
    
SELECT ProductName, UnitPrice
FROM Products;

SELECT * FROM Products;

SELECT ProductName AS 'Product', 
UnitPrice AS 'Price(USD)', 
UnitsInstock AS 'Stock'
FROM Products;

SELECT CompanyName, City, Country
FROM Customers
Where Country = 'Germany';

SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > 50;

SELECT OrderId, CustomerID, Shipcountry, Freight 
FROM Orders
WHERE ShipCountry = 'France';

SELECT ProductName, UnitsInStock, ReorderLevel
FROM Products
WHERE UnitsInStock < ReorderLevel;

SELECT OrderID, Freight
FROM Orders
WHERE Freight >= 100;

SELECT ProductName, UnitPrice, UnitsInStock
FROM Products
WHERE UnitPrice > 20 AND UnitsInStock > 50;

SELECT CompanyName, Country 
FROM Customers
WHERE Country = 'UK' OR Country = 'Ireland';

SELECT CategoryID, UnitPrice
FROM Products
WHERE (CategoryID = 1 OR CategoryID = 2) 
AND UnitPrice < 20;

SELECT CompanyName, Country
FROM Customers
WHERE NOT Country = 'U.S.A';

SELECT ProductName
FROM Products
WHERE NOT Discontinued = 1;

SELECT CompanyName, Country 
From Customers
WHERE Country IN ('France', 'Germany', 'Spain');

SELECT ProductName, SupplierID 
FROM Products
WHERE SupplierID NOT IN (1, 2, 3);

SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice BETWEEN 10 AND 20;

SELECT ProductName, Unitprice
FROM Products 
WHERE UnitPrice < 10 OR Unitprice > 20;

SELECT OrderID, CustomerID, ShipRegion
FROM orders
WHERE ShipRegion IS NULL;

SELECT LastName, FirstName
FROM employees
WHERE Region IS NOT NULL;

SELECT CompanyName
FROM Customers
WHERE CompanyName LIKE 'A%';

USE northwind;

SELECT OrderID, CustomerID, OrderDate
FROM orders
WHERE OrderDate = '1997-01-01';

SELECT OrderID, OrderDate
FROM orders
WHERE YEAR (OrderDate) = 1997
AND MONTH (OrderDate) =6;

-- Example 27:
SELECT ProductName, UnitPrice
FROM products
ORDER BY UnitPrice DESC;

-- Example 28:
SELECT Companyname, City, Country
FROM customers
ORDER BY Country ASC, CompanyName ASC;

-- Example 29:
SELECT ProductName, UnitPrice
FROM products
ORDER BY UnitPrice DESC
LIMIT 5;

-- Example 30: Retrieves products and prices for rows 6 through 10 and skips the first 5 rows.
SELECT Productname, UnitPrice
FROM products
LIMIT 5 OFFSET 5;

-- Example 36: 
SELECT ProductName,
UnitPrice AS 'Original Price',
UnitPrice * 0.9 AS '10% Discount Price'
FROM products;












































  
  


