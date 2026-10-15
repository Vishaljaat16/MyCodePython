show databases;
use bankdatapractice;
show tables;

select * from deposit;
-- Understanding CASE clause --
SELECT actno, cname, bname, amount, 
	CASE 
		WHEN amount < 5000 THEN amount + 1111
	ELSE amount
	END AS updated_amount
FROM deposit;

SELECT actno, cname, amount,
	CASE
		WHEN amount = 1000 THEN 2001
        WHEN amount = 2000 THEN 3001
        WHEN amount >= 5000 THEN 4900
	ELSE amount
    END AS Updated_amont
FROM deposit;

SELECT actno, cname, amount, 
	CASE 
		WHEN amount = 1000 THEN 2001
        WHEN amount = 2000 THEN 3001
        WHEN amount = 3000 THEN 4001
        When amount >= 5000 THEN 4900
	ELSE amount
    END AS updated_amout
FROM deposit
ORDER BY amount;


-- EXISTS --

SELECT cname 
FROM deposit
WHERE EXISTS ( select cname from borrow where borrow.cname = deposit.cname);

SELECT d1.*
FROM deposit d1 
WHERE EXISTS ( select cname from deposit d2 where d2.cname <> d1.cname);


-- WITH Context ( CTE ) -- 

with avg_amount_cte(average_amount) as ( select avg(amount) from deposit)
select cname, amount from deposit where amount > (select average_amount from avg_amount_cte);

WITH cte1(cname,bname) AS ( select cname, bname from deposit),
	cte2(cname,bname) AS ( select cname, bname from borrow)
SELECT * from cte1
UNION 
SELECT * from cte2;


-- window function on EMPLOYEES -- 

SELECT EmpName, Department, Salary, SUM(Salary) OVER (PARTITION BY Department) AS DeptTotal FROM Employees;
SELECT *, ROW_NUMBER() OVER( ORDER BY Salary DESC) AS RowNumber FROM Employees;
SELECT *, ROW_NUMBER() OVER (PARTITION BY Department ORDER BY Salary DESC) AS DeptRowNo FROM Employees;
SELECT *, RANK() OVER ( ORDER BY Salary DESC) AS RankSeq FROM Employees;
SELECT *, DENSE_RANK() OVER( ORDER BY Salary DESC) AS RankSeq FROM Employees;
SELECT *, DENSE_RANK() OVER( ORDER BY Department DESC) AS RankSeq FROM Employees;


SELECT 
    EmpName,
    Department,
    Salary,
    -- Total sales for the entire department
    SUM(Salary) OVER (PARTITION BY department) AS dept_total,
    
    -- Average sale in the department
    AVG(Salary) OVER (PARTITION BY department) AS dept_avg,
    
    -- The highest and lowest single sale in that department
    MAX(Salary) OVER (PARTITION BY department) AS dept_highest,
    MIN(Salary) OVER (PARTITION BY department) AS dept_lowest,
    
    -- Running total of sales over time per department
    SUM(Salary) OVER (PARTITION BY department ORDER BY JoiningDate) AS dept_running_total
FROM Employees;

SElECT EmpName, Salary,
ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num,
RANK() OVER (ORDER BY salary DESC) AS standard_rank,
DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_ranking,
PERCENT_RANK() OVER (ORDER BY salary DESC) AS pct_rank,
NTILE(3) OVER (ORDER BY salary DESC) AS performance_tier
FROM Employees;


