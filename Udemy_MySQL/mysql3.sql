-- insert statement
select * from titles limit 10;
desc titles;
delete from employees where emp_no=999903;
insert into employees values (999903, '1973-3-26', 'Patricia', 'Lawrence', 'F', '1999-01-01');
insert into titles (emp_no, title, from_date) values (999903, "Senior Engineer", '1997-10-01');
select * from titles where emp_no=999903;
insert into dept_emp values (999903, 'd005', '1997-10-01', '9999-01-01');
INSERT INTO departments values ('d010', 'Business Analysis');

CREATE TABLE dept_dups
( dept_no char(4) not null,
  dept_name varchar(400) not null
);
insert into dept_dups
select * from departments;
select * from dept_dups;
commit;
update departments
set dept_name='Data Analysis' where dept_name='Business Analysis';
select * from departments;
commit;
use employees;
select COUNT(DISTINCT emp_no) from dept_emp;
select avg(salary) from salaries;
select round(avg(salary),2) from salaries where to_date>'1997-01-01';
-- preamble
ALTER TABLE dept_dups CHANGE COLUMN dept_no dept_no char(400) null;
INSERT INTO dept_dups (dept_no) values ('d010'), ('d011');
alter table dept_dups add column dept_manager varchar(255) null;
select * from dept_dups;
commit;

SELECT dept_no, dept_name, coalesce(dept_manager, dept_name, 'N/A') as name from dept_dups;

alter table dept_dups drop column dept_manager;
alter table dept_dups change column dept_no dept_no char(4) NULL;
alter table dept_dups change column dept_name dept_name varchar(200) NULL;
insert into dept_dups 
select * from departments;
insert into dept_dups (dept_name) values ('Public Relations');
select * from dept_dups;
truncate dept_dups;
insert into dept_dups 
select * from departments;
insert into dept_dups (dept_name) values ('Public Relations');

select * from dept_dups;

insert into dept_dups (dept_no) values ('d010'), ('d011');
DROP TABLE IF EXISTS dept_manager_dup;

CREATE TABLE dept_manager_dup (

  emp_no int(11) NOT NULL,

  dept_no char(4) NULL,

  from_date date NOT NULL,

  to_date date NULL

  );
INSERT INTO dept_manager_dup
select * from dept_manager;

INSERT INTO dept_manager_dup (emp_no, from_date)

VALUES (999904, '2017-01-01'),

        (999905, '2017-01-01'),

        (999906, '2017-01-01'),

        (999907, '2017-01-01');
use employees;
DELETE FROM dept_manager_dup 
WHERE
    dept_no = 'd001';

INSERT INTO dept_dups (dept_name)

VALUES ('Public Relations');

DELETE FROM dept_dups 
WHERE
    dept_no = 'd001';
 
Select * from dept_manager_dup order by dept_no;

SELECT * FROM dept_manager_dup m JOIN dept_dups d ON m.dept_no=d.dept_no order by m.dept_no;     

SELECT 
    m.dept_no, m.emp_no, d.dept_name
FROM
    dept_manager_dup m
        LEFT JOIN
    dept_dups d ON m.dept_no = d.dept_no
WHERE
    d.dept_name IS NULL
ORDER BY m.dept_no;

SELECT 
    e.emp_no, e.first_name, e.last_name, d.dept_no
FROM
    employees e
        LEFT JOIN
    dept_manager_dup d ON e.emp_no = d.emp_no
WHERE
    last_name = 'Markovitch';
use employees;
select distinct dept_name, dept_no from dept_dups;

select @@global.sql_mode;
set @@global.sql_mode := replace(@@global.sql_mode, 'ONLY_FULL_GROUP_BY', '');

select first_name, last_name, hire_date, title  from employees e 
join titles t on e.emp_no=t.emp_no
where first_name='Margareta' and last_name='Markovitch';

select e.*, d.dept_name
from employees e
cross join 
departments d
where emp_no<10011;
 select first_name, last_name, hire_date, title, dm.to_date, dp.dept_name
 from employees e join dept_manager dm on e.emp_no=dm.emp_no
 join titles t on dm.emp_no=t.emp_no
 join departments dp on dm.dept_no=dp.dept_no
 where title='Manager'
 ORDER BY e.emp_no;
 
 select gender, count(gender) from employees e join dept_manager dm on e.emp_no=dm.emp_no group by gender;
 
 -- reversing the ORDER BY clause
 SELECT 
    *
FROM
    (SELECT 
        e.emp_no,
            e.first_name,
            e.last_name,
            NULL AS dept_no,
            NULL AS from_date
    FROM
        employees e
    WHERE
        last_name = 'Denis' UNION SELECT 
        NULL AS emp_no,
            NULL AS first_name,
            NULL AS last_name,
            dm.dept_no,
            dm.from_date
    FROM
        dept_manager dm) AS a
ORDER BY - a.emp_no DESC;
-- subquery
select * from employees where emp_no in (select emp_no from dept_manager)
and hire_date between '1990-01-01' and '1995-01-01';

SELECT 
    *
FROM
    dept_manager
WHERE
    emp_no IN (SELECT 
            emp_no
        FROM
            employees
        WHERE
            hire_date BETWEEN '1990-01-01' AND '1995-01-01');
            
-- Exists
select * from employees e where exists (select * from titles t where e.emp_no=t.emp_no and title='Assistant Engineer');

select first_name, last_name, dm.dept_no, e.emp_no, dm.emp_no manager from employees e join dept_emp de on e.emp_no=de.emp_no 
join dept_manager dm on de.dept_no=dm.dept_no order by 5 desc; 

CREATE TABLE emp_manager (
	emp_no int(11) not null,
    dept_no char(4) null,
    manager_no int(11) not null
);
SELECT 
    A.*
FROM
    (SELECT 
        e.emp_no,
            MIN(dept_no) dept_no,
            (SELECT 
                    emp_no
                FROM
                    dept_manager
                WHERE
                    emp_no = 110022) AS manager_no
    FROM
        employees e
    JOIN dept_emp de ON e.emp_no = de.emp_no
    WHERE
        e.emp_no <= 10020
    GROUP BY e.emp_no
    ORDER BY e.emp_no) AS A 
UNION SELECT 
    B.*
FROM
    (SELECT 
        e.emp_no,
            MIN(dept_no) dept_no,
            (SELECT 
                    emp_no
                FROM
                    dept_manager
                WHERE
                    emp_no = 110039) AS manager_no
    FROM
        employees e
    JOIN dept_emp de ON e.emp_no = de.emp_no
    WHERE
        e.emp_no > 10020
    GROUP BY e.emp_no
    ORDER BY e.emp_no
    LIMIT 20) AS B 
UNION SELECT 
    C.*
FROM
    (SELECT 
        e.emp_no,
            MIN(dept_no) dept_no,
            (SELECT 
                    emp_no
                FROM
                    dept_manager
                WHERE
                    emp_no = 110039) AS manager_no
    FROM
        employees e
    JOIN dept_emp de ON e.emp_no = de.emp_no
    WHERE
        e.emp_no = 110022
    GROUP BY e.emp_no
    ORDER BY e.emp_no) AS C 
UNION SELECT 
    D.*
FROM
    (SELECT 
        e.emp_no,
            MIN(dept_no) dept_no,
            (SELECT 
                    emp_no
                FROM
                    dept_manager
                WHERE
                    emp_no = 110022) AS manager_no
    FROM
        employees e
    JOIN dept_emp de ON e.emp_no = de.emp_no
    WHERE
        e.emp_no = 110039
    GROUP BY e.emp_no
    ORDER BY e.emp_no) AS D;

 