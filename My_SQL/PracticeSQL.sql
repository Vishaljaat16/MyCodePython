create database School_Data;
use School_Data;
create table student_data (
	id INT primary key,
	name varchar(50),
    class varchar(50),
    marks decimal(10,2));
    
insert into student_data
(id, name, class, marks)
values
(1, "Vishal", "12th", 88),
(2, "Ravi", "11th", 89),
(3, "Rahul", "Btech", 78),
(4, "Ram", "8th", 84);

select * from students_data;

alter table student_data add column pass_or_fail bool;
alter table student_data rename to students_data; 
alter table students_data modify column name varchar(100);
alter table students_data drop column pass_or_fail;
alter table students_data rename column name to student_name;
alter table students_data add constraint CHK_marks check (marks >= 0 and marks <= 100);

desc students_data;

create table students_data_subtable as
select id, student_name from students_data;
select * from students_data_subtable;

show tables;

select * from student_data where pass_or_fail is not True;
select * from student_data where pass_or_fail is not False;
select distinct class from student_data;
select * from student_data where marks not in (80,90,70);

select * from student_data order by student_name ASC;
select * from student_data order by 2 desc, 1 asc;
select class, sum(marks) as total_marks from student_data group by class;
select class, avg(marks) as total_marks from student_data group by class;
select class, sum(marks) as total_marks from student_data where class = '12th' order by class;



insert into Deposit (actno, cname, bname, amount, adate)
values (100, 'Anil', 'VRCE', 1000, '1-mar-2005'),(101, 'Sunil','Ajni', 5000, '4-jan-2006'),
(102, 'Mehul', 'karolbagh', 3500, '17-nov-2005'), (104, 'Madhuri', 'Chandani', 1200, '17-dec-2006'),
(105, 'Pramod', 'M.G road', 3000, '27-mar-2006'), (106, 'Sandip', 'Andheri', 2000, '31-mar-2006'),
(107, 'Shivani','Virar', 1000, '5-sep-2005'),(108,'Kranti', 'Nehru place', 5000, '2-jul-2005'),
(109, 'Naren', 'Powai', 7000, '10-aug-2005');



 select cname from deposit d
join branch b on b.bname = d.bname
join customer c on c.cname = d.cname
where b.city = (select city from customer where cname = 'Sunil');




select concat('Vishal', ' ', 'Jaat') as fullname;
select length('Vishal Jaat') as namelength;
select char_length('Vishal Jaat') as namelength;
select upper("vishal jaat") as uppercase;
select lower('VISHAL JAAT') as lowercase;
select replace('Vishal Unknown', 'unknown', 'Jaat') as replacevalue;
select replace('Vishal Unknown', 'Unknown', 'Jaat') as replacevalue;
select substr('Vishal Jaat', 1, 5) as subsrtingexample;
select left('Vishal Jaat', 6) as leftstring;
select right('Vishal Jaat',4) as rightstring;
select instr('Vishal Jaat', 'Jaat') as substringPosition;
select trim(' ' from ' Hello World ') as TrimmedString;
select reverse('Vishal') as ReversedString;
select rtrim('Vishal   ');
select space(7);
select ascii('V');
select concat_ws('_', 'Vishal', 'Jaat');
select format(0.981 * 100, 'N2') + '%' as PercentOutput;
select locate('Jaat', 'Vishal Jaat Vishal Jaat Vishal Jaat', 1);
select locate('Jaat', 'Vishal Jaat Vishal Jaat Vishal Jaat', 3);
select lpad('Vishal', 10, 'JAAT');
select lpad('Vishal', 8, 'JAAT');
select position('i' in 'Vishal Jaat');
select position('V' in 'Vishal Jaat');
select repeat('JAAT', 10);
select rpad('Vishal', 10, 'JAAT');
select strcmp('vishal', 'vishal');




SELECT ABS(-25);
SELECT CEIL(12.34);
SELECT FLOOR(12.98);
SELECT ROUND(15.6789, 2);
SELECT TRUNCATE(12.98765, 2);
SELECT MOD(10, 3);
SELECT POWER(2, 3);
SELECT SQRT(16);
SELECT EXP(1);
SELECT LOG(100);
SELECT LOG(2,100);
SELECT RAND();





-- joins -- 
select * from employees;
select * from departments;
select * from employees e join departments d on d.dept_id = e.dept_id;
select * from employees e inner join departments d on d.dept_id = e.dept_id;
select * from employees e left join departments d on d.dept_id = e.dept_id;
select * from employees e right join departments d on d.dept_id = e.dept_id;

select * from employees e left join departments d on d.dept_id = e.dept_id
UNION
select * from employees e right join departments d on d.dept_id = e.dept_id;

select * from employees  natural join departments;


-- case --

SELECT first_name, department_id, salary,
       CASE department_id 
           WHEN 50 THEN 1.5 * salary
           WHEN 12 THEN 2.0 * salary
           ELSE salary
       END AS "REVISED SALARY"
FROM Employee;

select coalesce(last_name, '-NA-') from employee;
select greatest( 10000, 25000, 16000) as High_salary;
SELECT IFNULL(1, 0) FROM dual;
SELECT IFNULL(NULL, 10) FROM dual;
SELECT LEAST('XYZ', 'xyz') FROM dual;


--  Procedure -- 
insert into proCustomer (customer_id, customer_name, contact_number, country)
values (1, 'Vishal Jaat', '9993342671', 'India'),(2, 'James Smith','5552345678','Canada'), (3,'William Brown','5553456789','Sri Lanka'),(4,'Emily Davis','5554567890','Australia');

use bankdatapractice;
DELIMITER //

CREATE PROCEDURE get_customers_by_country(
    IN p_country VARCHAR(50)
)
BEGIN
    SELECT customer_name, contact_number
    FROM procustomer
    WHERE country = p_country;
END //

DELIMITER ;

CALL get_customers_by_country('Sri Lanka');


-- IF THEN ELIF ELSE --
DELIMITER //

CREATE PROCEDURE geekdemo(IN num1 INT)
BEGIN
    IF num1 < 5000 THEN
        SELECT 'Input is less than 5000.' AS message;
    ELSE
        SELECT 'Input is 5000 or greater.' AS message;
    END IF;
END //

DELIMITER ;

call geekdemo(59999);