-- Malaika Tariq
-- April 20, 2026
SHOW DATABASES;
USE northwind;
SHOW TABLES;

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'northwind'
AND table_type = 'BASE TABLE';
  
-- Example 1:
SELECT ProductName, UnitPrice
FROM Products;

-- Example 2:
SELECT * FROM Products;

-- Example 3: Rename columns ProductName, UnitPrice, and UnitsInStock as Product, Price(USD) and Stock for clarity.
SELECT ProductName AS 'Product', 
UnitPrice AS 'Price(USD)', 
UnitsInstock AS 'Stock'
FROM Products;

-- Example 4:
SELECT CompanyName, City, Country
FROM Customers
Where Country = 'Germany';

-- Example 5: Retrieve all Productname and UnitPrice from the Product table, where Unitprice is greater than 50.
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > 50;

-- Example 6: Retrieve all the OrderID, CustomerID, ShipCountry and Freight from the Orders table for all orders shipped to France.
SELECT OrderId, CustomerID, Shipcountry, Freight 
FROM Orders
WHERE ShipCountry = 'France';

-- Example:
SELECT ProductName, UnitsInStock, ReorderLevel
FROM Products
WHERE UnitsInStock < ReorderLevel;

-- Example:
SELECT OrderID, Freight
FROM Orders
WHERE Freight >= 100;

-- Example:
SELECT ProductName, UnitPrice, UnitsInStock
FROM Products
WHERE UnitPrice > 20 AND UnitsInStock > 50;

-- Example:
SELECT CompanyName, Country 
FROM Customers
WHERE Country = 'UK' OR Country = 'Ireland';

-- Example:
SELECT CategoryID, UnitPrice
FROM Products
WHERE (CategoryID = 1 OR CategoryID = 2) 
AND UnitPrice < 20;

-- Example 13: Retrieve all company names, and country names other than the USA.
SELECT CompanyName, Country
FROM Customers
WHERE NOT Country = 'U.S.A';

-- Example:
SELECT ProductName
FROM Products
WHERE NOT Discontinued = 1;

-- Example:
SELECT CompanyName, Country 
From Customers
WHERE Country IN ('France', 'Germany', 'Spain');

-- Example:
SELECT ProductName, SupplierID 
FROM Products
WHERE SupplierID NOT IN (1, 2, 3);

-- Example:
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice BETWEEN 10 AND 20;

-- Example:
SELECT ProductName, Unitprice
FROM Products 
WHERE UnitPrice < 10 OR Unitprice > 20;

-- Example:
SELECT OrderID, CustomerID, ShipRegion
FROM orders
WHERE ShipRegion IS NULL;

-- Example:
SELECT LastName, FirstName
FROM employees
WHERE Region IS NOT NULL;

-- Example:
SELECT CompanyName
FROM Customers
WHERE CompanyName LIKE 'A%';

USE northwind;

-- Example 24: Retrieves OrderID, CustomerID, OrderDate for all orders with a shipped date of '1997-01-01'
SELECT OrderID, CustomerID, OrderDate
FROM orders
WHERE OrderDate = '1997-01-01';

-- Example:
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

-- Example 31: returns unique countries.
SELECT DISTINCT Country
FROM Customers
ORDER BY Country;

-- Example 32: Returns each unique pairing of Country and City - if two customers share the same city, that city appears only once.
SELECT DISTINCT Country, City
FROM Customers
ORDER BY Country, City;

-- Example 33: Returns Full Name from First and last 
SELECT CONCAT(FirstName,' ', LastName) AS 'Full Name',
	   Title
FROM Employees;

-- Example 36: 
SELECT ProductName,
UnitPrice AS 'Original Price',
UnitPrice * 0.9 AS '10% Discount Price'
FROM products;

-- JOINS
USE northwind;

-- Example 1: Return OrderID, Customer and OrderDate. Limit to 5 records
SELECT 
o.OrderID,
o.OrderDate,
c.CompanyName AS 'Customer'
FROM orders o
JOIN Customers c
ON o.CustomerID = c.CustomerID
ORDER BY o.OrderDate DESC
LIMIT 5;

-- Example 2: Return OrderID CompanyName and OrderDate with a Limit of 5. Orders Joined to Customers
SELECT OrderID, CompanyName, OrderDate
FROM Orders
JOIN Customers
USING (CustomerID)
ORDER BY OrderDate
LIMIT 5;

-- Example 3: Return ProductName, CategoryName and UnitPrice with the Limit of 6. Products with Their Category Names
SELECT p.ProductName,
	   p.UnitPrice,
       c.CategoryName
FROM products p
INNER JOIN categories c
USING (CategoryID)
ORDER BY c.CategoryName, p.ProductName
LIMIT 6;

-- Example 5: Return all Customers including those with No Orders
-- Customers with zero orders will show 0 in Order Count 
SELECT 
      c.CompanyName,
      COUNT(o.OrderID) AS 'Order Count'
FROM Customers c
LEFT JOIN orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.CompanyName
ORDER BY `Order Count` ASC
LIMIT 5;
















































  
  


