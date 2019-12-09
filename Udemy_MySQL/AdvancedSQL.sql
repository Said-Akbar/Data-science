use employees;
-- self join
-- extract the records of employees who are managers as well. (from emp_manager)
select * from emp_manager;
select distinct e1.* from emp_manager e1 join emp_manager e2 on e1.emp_no=e2.manager_no; -- show employees (e1) who are managers (e2).

-- views
create view v_avg_manager_salary as 
select avg(salary) from dept_manager dm join salaries s on dm.emp_no=s.emp_no;

-- procedures
drop procedure if exists select_employees;
DELIMITER $$
CREATE PROCEDURE select_employees()
BEGIN
SELECT * FROM employees limit 100;
END$$
DELIMITER ;

call employees.select_employees(); 

DELIMITER $$
CREATE PROCEDURE avg_salary()
BEGIN
SELECT avg(salary) from salaries;
END$$
DELIMITER ;

call avg_salary();

-- procedure with IN parameter
drop procedure if exists avg_salary_emp;
DELIMITER $$
CREATE PROCEDURE avg_salary_emp(IN p_emp_id INTEGER)
BEGIN
SELECT first_name, last_name, avg(salary)
from employees e join salaries s on e.emp_no=s.emp_no
where e.emp_no=p_emp_id group by e.emp_no;
END$$
DELIMITER ;

call avg_salary_emp(100133);

-- OUT parameter 

drop procedure if exists avg_salary_emps;
DELIMITER $$
CREATE PROCEDURE avg_salary_emps(IN p_emp_id1 INTEGER, p_emp_id2 INTEGER, OUT avg_salaries DECIMAL(10,2))
BEGIN
select avg(salary) into avg_salaries
from employees e join salaries s on e.emp_no=s.emp_no
where e.emp_no=p_emp_id1 or e.emp_no=p_emp_id2;
END$$
DELIMITER ;

set @avg_salaries=0.0;
call avg_salary_emps(10133, 13300, @avg_salaries);
select @avg_salaries;

set @v_emp_salary=0.0;
call avg_salary_emps(10133, 13300, @v_emp_salary);
select @v_emp_salary;

-- functions
use employees;
DELIMITER $$
CREATE FUNCTION my_func(EMP_ID INTEGER) RETURNS DECIMAL(10,2)
deterministic
BEGIN

DECLARE v_avg_sal DECIMAL(10,2);

select avg(salary) into v_avg_sal from salaries where emp_no=emp_id;
RETURN v_avg_sal;
END$$
DELIMITER ;

select my_func(10333);
drop function if exists emp_info;
DELIMITER $$
CREATE FUNCTION emp_info(pfirst_name VARCHAR(255), plast_name VARCHAR(255)) RETURNS decimal(10,2)
DETERMINISTIC
BEGIN
DECLARE v_salary DECIMAL(10,2);
SELECT 
    salary
INTO v_salary FROM
    employees e
        JOIN
    salaries s ON e.emp_no = s.emp_no
WHERE
    first_name = pfirst_name
        AND last_name = plast_name
        AND from_date = (SELECT 
            MAX(from_date)
        FROM
            salaries s
        WHERE
            e.emp_no = s.emp_no);
return v_salary;
END $$
DELIMITER ;

select emp_info('Aruna', 'Journel');
select from_date, salary from salaries s join employees e on s.emp_no=e.emp_no where last_name='Journel' and first_name='Aruna'
order by from_date desc limit 1;

set global my_var=3;
