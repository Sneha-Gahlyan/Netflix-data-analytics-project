-- =====================================================
-- Netflix Data Analytics Project
-- SQL Server (SSMS)
-- =====================================================

-- Total customers 
SELECT
COUNT(*) as Total_Customers
FROM dbo.Netflix_Customers;


-- Total active customers
SELECT
COUNT(*) as Active_Customers
FROM dbo.Netflix_Customers
WHERE Account_Status = 'Active';

-- Customers by Subscription plan
SELECT 
Subscription_Plan,
count(*) as Customers
FROM Netflix_Customers
GROUP BY Subscription_Plan
ORDER BY Customers desc;


-- Revenue by Subscription Plan 
SELECT 
Subscription_Plan,
SUM(Customer_Revenue) as Revenue
FROM Netflix_Customers
GROUP BY Subscription_Plan
ORDER BY Revenue desc;

-- Popular Genre 
SELECT 
Genre,
COUNT(*) AS Views
FROM Netflix_Customers
GROUP BY Genre 
ORDER BY Views DESC;

-- Country wise customers
SELECT 
Country,
COUNT(DISTINCT Customer_ID) AS Customers
FROM Netflix_Customers
GROUP BY Country
ORDER BY Customers DESC;


--Device usage
SELECT 
Device,
COUNT(*) AS Users
FROM Netflix_Customers
GROUP BY Device
ORDER BY Users

-- Average watch hours by plan
SELECT 
Subscription_Plan,
ROUND(AVG(Watch_Hours),2) AS Avg_Watch_Hours
FROM Netflix_Customers
GROUP BY Subscription_Plan

-- Top 10 customers by Revenue
SELECT TOP 10 
Customer_Name,
Customer_Revenue
FROM Netflix_Customers
ORDER BY Customer_Revenue DESC

-- Movie vs TV Shows
SELECT 
Content_Type,
COUNT(*) AS Total
FROM Netflix_Customers
GROUP BY Content_Type

-- Avg rating by genre
SELECT 
Genre,
ROUND(AVG(Avg_Rating),2) AS Avg_Rating
FROM Netflix_Customers
GROUP BY Genre 
ORDER BY Avg_Rating DESC;


-- Account status
SELECT 
Account_Status,
COUNT(*) AS Customers
FROM Netflix_Customers
GROUP BY Account_Status;
