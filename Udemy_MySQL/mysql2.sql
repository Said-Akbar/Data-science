use employees;
SELECT 
    *
FROM
    employees
LIMIT 5;
SELECT 
    dept_no
FROM
    departments;
SELECT 
    *
FROM
    departments;
-- where clause
SELECT 
    *
FROM
    employees
WHERE
    first_name = 'Elvis';
-- and operator
SELECT 
    *
FROM
    employees
WHERE
    first_name = 'Kellie' AND gender = 'F';
-- or operator
SELECT 
    *
FROM
    employees
WHERE
    first_name = 'Kellie'
        OR first_name = 'Aruna';
-- operator precedence: Retrieve a list with all female employees whose first name is either Kellie or Aruna.
SELECT 
    *
FROM
    employees
WHERE
    (first_name = 'Kellie'
        OR first_name = 'Aruna')
        AND gender = 'F';
-- IN operator
SELECT 
    *
FROM
    employees
WHERE
    first_name IN ('Denis' , 'Elvis');   
    
SELECT 
    *
FROM
    employees
WHERE
    first_name NOT IN ('John' , 'Mark', 'Jacob');
-- like operator
SELECT * FROM employees where first_name like 'Mark%';
SELECT * from employees where hire_date like '2000%';
SELECT * FROM employees where emp_no like '1000_';
SELECT * FROM employees WHERE first_name like 'Jack%';
SELECT * FROM employees WHERE first_name not like 'Jack%';
-- between and
SELECT * FROM salaries where salary between 66000 and 70000;
select * from employees where emp_no not between 10004 and 100012;
select * from departments where dept_no between 'd003' and 'd006';
select * from employees where first_name != 'Mark';
select * from employees where first_name <> 'Mark';
select distinct gender, count(*) from employees group by gender;
-- DISTINCT
select count(distinct first_name, last_name) from employees;
select count(*) from employees;
select * from employees order by first_name, last_name;

select salary, count(salary) from salaries where salary>80000
group by 1 order by 1;
-- where vs having
select emp_no, AVG(salary) from salaries group by emp_no having avg(salary)>120000;
SELECT *, AVG(salary) FROM salaries WHERE salary > 120000 GROUP BY emp_no ORDER BY emp_no;

SELECT 
    emp_no, COUNT(emp_no) AS contracts
FROM
    dept_emp
WHERE
    from_date > '2000-01-01'
GROUP BY emp_no
HAVING contracts > 1
order by emp_no desc;

-- show top 10 salaries. (rank is extra here. Used just to rank salaries)
select rank() over(order by salary desc) as ranking, salary from  
(select emp_no, salary from salaries order by salary desc limit 10) as ll;

    