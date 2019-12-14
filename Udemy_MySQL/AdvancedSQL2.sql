-- dates
select date_format(sysdate(), '%Y-%m-%d');
select str_to_date('15-Dec-09', '%d-%b-%y') as date;
select extract(year_month from sysdate());
select dayofmonth(sysdate());

-- 12/14/2019
use employees;
-- recap of functions

drop procedure if exists my_proc;
delimiter $$
create procedure my_proc(in p_parmt1 int, in parmt2 int, out var1 decimal(10,2))
begin
select avg(salary) into var1 from salaries s where s.emp_no=p_parmt1 or s.emp_no=parmt2;
end$$
delimiter ;
set @my_var=0.0;
call my_proc(13300, 10333, @my_var);
select @my_var;

select avg(salary) from salaries where emp_no=13300 or emp_no=10333;

drop function if exists my_func;
DELIMITER $$
create function my_func(p_1 INT, p_2 INT) RETURNS DECIMAL(10,2)
deterministic
Begin
declare new_var decimal(10,2);
select avg(salary) into new_var from salaries where emp_no in (p_1, p_2);
return new_var;
end$$
delimiter ;

select my_func(13300, 10333);

-- triggers

drop trigger if exists date_check;

Delimiter $$
create trigger date_check
before insert on employees
for each row
begin
if new.hire_date>date_format(sysdate(),'%Y-%m-%d') then
	set new.hire_date=date_format(sysdate(),'%Y-%m-%d');
    end if;
end$$

delimiter ;

INSERT employees VALUES ('999904', '1970-01-31', 'John', 'Johnson', 'M', '2025-01-01');  
SELECT 
    *
FROM
    employees
ORDER BY emp_no DESC;

-- index
show index from employees;

select * from salaries where salary>89000;

create index i_salary on salaries(salary);

select * from salaries where salary>89000;

alter table salaries
drop index i_salary;

-- case statements
select e.first_name, e.last_name, 
case
when dm.emp_no is not null then 'Manager' else 'Employee' end as is_manager
from employees e left join dept_manager dm on e.emp_no=dm.emp_no
order by 3 desc;

select first_name, last_name, if(gender='M', 'Male', 'Female') as gender from employees;
select *, IF(difference>30000, 'higher', 'lower') high from
(SELECT
    e.emp_no, e.first_name, e.last_name, max(salary)-min(salary) difference
FROM
    employees e
        JOIN
    salaries s ON e.emp_no = s.emp_no
        JOIN
    dept_manager dm ON e.emp_no = dm.emp_no
    group by 1 order by 4 desc) as d;
    
SELECT e.emp_no, e.first_name, e.last_name,
case 
	when max(to_date)<sysdate() then 'not working anymore' else 'is still employed' end as current

from employees e join dept_emp de on e.emp_no=de.emp_no 
group by de.emp_no limit 100;    -- grouping by de table ensures we get the latest date for each employee.

