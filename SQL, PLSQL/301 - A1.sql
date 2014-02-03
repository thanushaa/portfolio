/*

Assignment 1

Student Name: Thanusha Thaninayagam

'This Assignment represents my work
 in accordance with the Seneca Academic Policy.'
Signature: Thanusha Thaninayagam

*/

/*
1.  Write a query that produces all pairs (Two SalesPeople together) of 
    salespeople who are living in the same city(Take a close look the data and 
    you will see that Peel and Motica are both living in London) . Than all you 
    have to do is to hit the salespeople table 2 times and see that who are 
    leaving in the same city.
*/

SELECT DISTINCT s.sname "First Name", 
                sp.sname "Second Name"
FROM salespeople s
FULL OUTER JOIN salespeople sp
ON s.city = sp.city
WHERE s.sname < sp.sname;


/*
2.  Write a query that produces all pairs of orders by a given customer with the
    name and the number of that customer, and eliminates the duplicates. To 
    answer that question go to the Orders table and study the data. You will see
    that there are 3 customers who have 2 separate (pairs of) orders. Order the 
    result by cnum. (Hint: If you use only orders table you cannot get the name
    of the customer)
*/

SELECT  o.cnum, 
        cust.cname, 
        ord.cnum AS "CNUM_1", 
        o.onum AS "First Order", 
        ord.onum AS "Second Order"
FROM orders o
JOIN customers cust
ON o.cnum = cust.cnum
FULL OUTER JOIN orders ord
ON o.cnum = ord.cnum
WHERE o.onum < ord.onum
ORDER BY cnum;


/*
3.  Write a query that produces the names and the cities of all customers with 
    the same rating as Hoffman Company (We have to find the Customers whose 
    rating is the same as Hoffman’s). Build the query using Hoffman's cnum 
    rather than his rating, so it would still be usable if his rating changed.
*/

SELECT  cust.cname,
        cust.city
FROM customers cust
WHERE cust.rating = (SELECT rating
                     FROM customers
                     WHERE cnum = 2001);


/*
4.  If you look at your data in the tables of salespeople and the customers you 
    will see that some of the customers are not located in the same city of 
    their sales peoples. This is also true for the sales peoples. Write a query 
    that shows all sales people and their customers with their cities. But your 
    query should show all customers and sales people including the ones in the 
    same city.
*/

SELECT  NVL(s.sname, 'No Customer in the same city') AS "Customer Name", 
        NVL(s.city, 'No City') AS "SalesAssigneds Person City", 
        NVL(cust.cname, 'No Company in the same city') AS "Sales Person Name",
        NVL(cust.city, 'No City') AS "Customer City"
FROM salespeople s
FULL OUTER JOIN customers cust
ON s.city = cust.city
ORDER BY s.sname ASC, cust.city, cust.cname DESC;


/*
5.  If you look both Customers and Orders tables you will see that one customer 
    has not placed any order so far. Write a query and find this customer.
*/

SELECT  cust.cname AS "Customer Name", 
        NVL(TO_CHAR(ord.onum), 'No Order') AS "Order No"
FROM customers cust
FULL OUTER JOIN orders ord
ON cust.cnum = ord.cnum
ORDER BY cust.cnum;


/*
6.  Write query that shows all (Even if they have no customers assigned) 
    salespeople's total sales in amount for their customers along with their 
    customer names.
*/

SELECT  s.sname AS "Salesperson",
        NVL(cust.cname, 'No Customer') AS "Customer",
        NVL(tsum.total, 'No Order') AS "Total"
FROM salespeople s
FULL OUTER JOIN customers cust
ON s.snum = cust.snum
FULL OUTER JOIN (SELECT cnum, TO_CHAR(SUM(amt), '$99,999.99') AS Total
                 FROM orders
                 GROUP BY cnum) tsum
ON cust.cnum = tsum.cnum;


/*
7.  Write a query that uses a subquery to obtain all order for the customer 
    Cisneros Ltd. Show the amount of each order, order number and the city of 
    the customer where it comes from.
*/

SELECT  ord.onum, 
        TO_CHAR(ord.amt, '$99,999.99') AS "Order Amount",
        cust.city
FROM orders ord
JOIN customers cust
ON ord.cnum = cust.cnum
WHERE ord.cnum = (SELECT cnum
                  FROM customers
                  WHERE cname = 'Cisneros Ltd.');

/*
8.  Write query that selects the total amount of sales in orders table along 
    with their name an salespeople number for each salesperson for whom this 
    total is greater than the amount of the largest order in the table.
*/

-- Inline View
SELECT  tsum.snum AS "Sales No",
        cust.cname AS "Customer",
        tsum.total AS "Total"
FROM customers cust, (SELECT snum, cnum, TO_CHAR(SUM(amt), '$99,999.99') Total
                      FROM orders
                      GROUP BY cnum, snum
                      HAVING SUM(amt) > ALL (SELECT MAX(amt)
                                             FROM orders
                                             GROUP BY cnum)) tsum
WHERE tsum.cnum = cust.cnum;


-- Correlated Subquery
SELECT  tsum.snum AS "Sales No",
        cust.cname AS "Customer Name",
        TO_CHAR(tsum.total, '$99,999.99') AS "Total"
FROM customers cust, (SELECT snum, cnum, SUM(amt) Total
                      FROM orders
                      GROUP BY cnum, snum) tsum
WHERE tsum.cnum = cust.cnum
AND tsum.total > ALL (SELECT MAX(amt)
                 FROM orders
                 GROUP BY cnum);
                   
                   
/*
9.  Write a select command using correlated subquery that select the names and 
    numbers of all customers with rating equal to the maximum for their city.
*/

-- Correlated Subquery
SELECT  cust.cnum AS "Customer No",
        cust.cname AS "Customer Name"
FROM customers cust
WHERE cust.rating = (SELECT MAX(rating)
                     FROM customers
                     WHERE cust.city = city
                     GROUP BY city);

-- Inline View
SELECT  cust.cnum AS "Customer No",
        cust.cname AS "Customer Name"
FROM customers cust, (SELECT city, MAX(rating) Rating
                      FROM customers
                      GROUP BY city) mrate
WHERE cust.city = mrate.city
AND cust.rating = mrate.rating;


/*
10. Write two queries that select all salespeople(By name and number)
    who have customers in their cities who they do not service, one using a
    join one a correlated subquery. Which solution is more elegant?
    Hint : One way to do this is to find all customers not serviced by a given 
    salesperson and see if any of them are in his or her city.
*/

-- Correlated Subquery
SELECT  s.snum AS "Sales No",
        s.sname AS "Salesperson"
FROM salespeople s
WHERE s.city = (SELECT city
                FROM customers
                WHERE snum <> s.snum
                AND city = s.city
                GROUP BY city);

-- Inline View
SELECT  s.snum AS "Sales No",
        s.sname AS "Salesperson"
FROM salespeople s, (SELECT city, snum
                     FROM customers
                     GROUP BY city, snum) cty
WHERE s.city = cty.city
AND s.snum <> cty.snum;


/*

11. Write a query that lists each order number followed by the name of the 
    customer who made the order.

*/

SELECT  ord.onum AS "Order No",
        cust.cname AS "Customer"
FROM orders ord
JOIN customers cust
ON ord.cnum = cust.cnum;


/*
12. Write a query that gives the names of both the salesperson and the customer 
    for each order after the order number. Order the output first customer (ASC)
    name and then sales person name.
*/

SELECT  ord.onum AS "Order No",
        cust.cname AS "Customer",
        s.sname AS "Salesperson"
FROM orders ord
JOIN customers cust
ON ord.cnum = cust.cnum
JOIN salespeople s
ON ord.snum = s.snum
ORDER BY cust.cname ASC, s.sname;


/*
13. Write a query that produces ALL customers serviced BY salespeople WITH a 
    commission above 12%. Output the customer's name, salesperson name and the 
    salesperson's rate OF commission. (All customers are served by at least one
    Salespeople)
*/

SELECT  cust.cname AS "Customer",
        s.sname AS "Salesperson",
        s.comm AS "Sales Rate of Commission"
FROM salespeople s
JOIN customers cust
ON cust.snum = s.snum
WHERE s.comm > 0.12;


/*
14. Write a query that calculates the amount of the salesperson's commission 
    (Commission amount will be calculated by multiplying commissions and total 
    amounts sold) on each order by a customer with a customer rating above 100.
    Format Commission amount and give a column alias.
*/

SELECT  ord.onum AS "Order No",
        NVL(cust.cname, 'No Customer') AS "Customer",
        s.sname "Salesperson",
        TO_CHAR(NVL(ROUND(ord.amt * s.comm, 2), 0), '$99,999.99') AS "Commission Amount"
FROM salespeople s
JOIN customers cust
ON s.snum = cust.snum
JOIN orders ord
ON cust.cnum = ord.cnum
WHERE cust.rating > 100;


/*
15. Write a query that uses the EXISTS operator to extract all salespeople who 
    have customers with a rating of 300.
*/

SELECT  s.snum AS "Sales No", 
        s.sname AS "Salesperson"
FROM salespeople s
WHERE EXISTS (SELECT snum
              FROM customers
              WHERE s.snum = snum
              AND rating = 300);
              

/*
16. How could you solve above problem with a join?
*/

SELECT  s.snum AS "Sales No",
        s.sname AS "Salesperson"
FROM salespeople s
JOIN customers cust
ON s.snum = cust.snum
WHERE cust.rating = 300;


/*
17. Write a query using the EXISTS operator that selects all salespeople with 
    customers located in their cities who are not assigned to them.
*/

SELECT  s.snum AS "Sales No", 
        s.sname AS "Salesperson"
FROM salespeople s
WHERE EXISTS (SELECT *
              FROM customers
              WHERE s.city = city
              AND s.snum <> snum);
              

/*
18. Write a query that extracts from the customers table every customer assigned
    to a salesperson that currently has at least one other customer (besides the
    customer being selected) with orders in the orders table.
    Hint: This is similar in structure to our three-level subquery example.
*/


SELECT  s.snum AS "Sales No",
        s.sname AS "Salesperson",
        cust.cname AS "Customer"
FROM customers cust
JOIN salespeople s
ON cust.snum = s.snum
JOIN (SELECT snum, COUNT(cnum) Total
      FROM customers
      GROUP BY snum) t
ON t.snum = s.snum
AND t.total > 1
ORDER BY s.snum;


/*
19. Write a query that produces the names and ratings of all customers who
    have above-average orders.
*/

-- Total amount of each customer greater than average orders
SELECT  cust.cname AS "Customer",
        cust.rating AS "Customer Rating"
FROM customers cust, (SELECT cnum, SUM(amt) Total
                      FROM orders
                      GROUP BY cnum) tsum
WHERE cust.cnum = tsum.cnum
AND tsum.total > (SELECT AVG(amt)
                  FROM orders);
             
             
/*
20. Create a complex view based on 2 tables (Customers and orders) by giving 
    aliases for each column you selected. Your view should show AVG, MAX and MIN
    of sales amounts based on each customer. These are the column list that you
    have to select;
    - Custemer ID : Helping column
    - Customer name : Helping column
    - MAX, MIN and AVG of sales amount.
    - Conditions :
      o Do not select customers living in Toronto.
      o Do not select MIN sales amount less than 50.
      o Order by Average Amount.
*/

CREATE VIEW custsts AS
SELECT  cust.cnum AS "Customer No",
        cust.cname AS "Customer Name",
        TO_CHAR(csts.maxamt, '$99,999.99') AS "Max Amt",
        TO_CHAR(csts.minamt, '$99,999.99') AS "Min Amt",
        TO_CHAR(csts.avgamt, '$99,999.99') AS "Avg Amt"
FROM customers cust, (SELECT cnum, MAX(amt) Maxamt, MIN(amt) Minamt, AVG(amt) Avgamt
                      FROM orders
                      GROUP BY cnum
                      ORDER BY AVG(amt)) csts 
WHERE cust.cnum = csts.cnum
AND csts.minamt > 50
AND cust.city <> 'Toronto';