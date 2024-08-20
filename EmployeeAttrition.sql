-- USE AMANDB;

-- -- Checking the data in the employeeattrition table
-- -- --------------------------------------------------------
-- SELECT * FROM EMPLOYEEATTRITION;

-- -- Column of the table
-- -- --------------------------------------------------------
-- SHOW COLUMNS FROM EMPLOYEEATTRITION;

-- ALTER TABLE employeeattrition RENAME COLUMN ï»¿Age TO AGE;

-- -- Drop Columns that we dont need
-- ALTER TABLE EMPLOYEEATTRITION DROP COLUMN OVER18,DROP COLUMN STANDARDHOURS;




-- -- Employees under attrition having 5+ years of experience
-- -- in btw the age group of 27-35
-- -- --------------------------------------------------------
-- SELECT * FROM EMPLOYEEATTRITION 
-- WHERE TotalWorkingYears>5 AND 
-- AGE BETWEEN 27 AND 35 AND 
-- ATTRITION = "Yes";

-- -- Employees having maximum and minimum salary working in different department
-- -- who recieved less than 13% salary hike
-- -- --------------------------------------------------------
-- SELECT DEPARTMENT, MIN(MONTHLYINCOME), MAX(MONTHLYINCOME)
-- FROM EMPLOYEEATTRITION
-- WHERE PERCENTSALARYHIKE <13
-- GROUP BY DEPARTMENT;

-- -- Calculatng average monthly income of all the employees who worked more
-- -- than 3 years whose education background is medical
-- -- --------------------------------------------------------
-- SELECT AVG(MONTHLYINCOME) FROM EMPLOYEEATTRITION
-- WHERE YEARSATCOMPANY > 3 AND
-- EDUCATIONFIELD = 'Medical';

-- -- Total number of male and female employees under attrition whose marital
-- -- is married and haven't recieved promotion in last 2 years
-- -- --------------------------------------------------------
-- SELECT GENDER, COUNT(EMPLOYEENUMBER) FROM EMPLOYEEATTRITION
-- WHERE MARITALSTATUS = 'Married' 
-- AND ATTRITION = "Yes"
-- AND YEARSSINCELASTPROMOTION = 2
-- GROUP BY GENDER;

-- -- Employees with max performance rating but no promotions for 4 years
-- -- and above
-- -- --------------------------------------------------------
-- SELECT * FROM EMPLOYEEATTRITION 
-- WHERE PERFORMANCERATING = (SELECT MAX(PERFORMANCERATING) FROM EMPLOYEEATTRITION)
-- AND YEARSSINCELASTPROMOTION>=4;

-- -- Who have min and max percentage salary hike
-- -- --------------------------------------------------------
-- SELECT YEARSATCOMPANY, 
-- PERFORMANCERATING, YEARSSINCELASTPROMOTION, MAX(PERCENTSALARYHIKE),
-- MIN(PERCENTSALARYHIKE) FROM EMPLOYEEATTRITION
-- GROUP BY EMPLOYEENUMBER, YEARSATCOMPANY, 
-- PERFORMANCERATING, YEARSSINCELASTPROMOTION 
-- ORDER BY MAX(PERCENTSALARYHIKE) DESC, MIN(PERCENTSALARYHIKE) ASC;

-- -- Employees working overtime but given min salary hike 
-- -- and more than 5 yrs with company
-- -- -------------------------------------------------------
-- SELECT * FROM EMPLOYEEATTRITION 
-- WHERE OVERTIME = 'Yes' AND PERCENTSALARYHIKE = (SELECT MIN(PERCENTSALARYHIKE) FROM EMPLOYEEATTRITION)
-- AND YEARSATCOMPANY > 5 AND ATTRITION = 'Yes';
