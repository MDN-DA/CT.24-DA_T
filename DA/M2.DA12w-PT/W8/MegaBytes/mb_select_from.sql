-- Selecting information from the database
-- * is a wildcard, and means "everything" or "all"
-- this is usually written as "select column from table"
 
-- Select everything from employee_detail
-- returns all columns and rows from employee_detail
SELECT * FROM employee_detail;
 
SELECT * FROM employee_detail
WHERE base_pay_band = 2;
-- returns the weekly hours column
SELECT weekly_hours FROM employee_detail;
 
-- returns two columns; main store id and float store id;
SELECT main_store_id, float_store_id FROM employee_detail;
 
-- returns employee's first and last names
SELECT first_name, last_name FROM employee_detail;
 
SELECT * FROM employee_detail
ORDER BY first_name;
 
SELECT * FROM employee_detail
ORDER BY main_store_id DESC;
 
SELECT * FROM employee_detail
WHERE weekly_hours BETWEEN 1 AND 20
ORDER BY weekly_hours;
 
SELECT MAX(seat_capacity)
FROM store_detail;
 
SELECT store_id, store_city, seat_capacity
FROM store_detail
WHERE seat_capacity = (SELECT MAX(seat_capacity) 
FROM store_detail)
;
 
SELECT COUNT(base_pay_band), base_pay_band
FROM employee_detail
GROUP BY base_pay_band;