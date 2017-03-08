select count(*)
from employee e
inner join address_employee ae on ae.employee_id=e.id
inner join address a on ae.address_id=a.id
-- left join income i on i.employee_id=e.id
where a.state='TX';

select state,avg(income) as income
from employee e
inner join address_employee ae on ae.employee_id=e.id
inner join address a on ae.address_id=a.id
inner join income i on i.employee_id=e.id
group by a.state;

-- highest income
select e.*,i.*
from employee e
inner join income i 
on i.employee_id=e.id
order by income desc
limit 1;

-- highest paid employee
select employee.*
from income
inner join employee on income.employee_id=employee.id 
where income = (
SELECT MAX(income) FROM income
);

SELECT MAX(income) FROM income;


-- get the addresses over 220
select a.* 
from employee e
inner join address_employee ae on ae.employee_id=e.id
inner join address a on ae.address_id=a.id
inner join income i on i.employee_id=e.id
where income>220000;

-- returns 48 records
-- check if any addresses are used more than once
select line1,city,state, count(*) 
from address group by line1,city,state
having count(*)>1;
-- no duplicates, safe to insert duplicates and use the address value to link back to employee

-- insert into address (line1,city,state,zip)
select line1,city,state,zip
from employee e
inner join address_employee ae on ae.employee_id=e.id
inner join address a on ae.address_id=a.id
left join income i on i.employee_id=e.id
where income>220000;

select count(*) from address; -- now we have 348 with 48 unlinked

-- link the unlinked back to the employees
insert into address_employee (address_id,employee_id)
select a1.id,ae.employee_id
from address a1
inner join address a2 on a1.line1=a2.line1 
	and a1.city=a2.city 
	and a1.state=a2.state 
	and a1.id<>a2.id
left join address_employee ae on ae.address_id=a2.id
where a1.id not in (select address_id from address_employee);

select a1.id,ae.employee_id
from address a1
inner join address a2 on a1.line1=a2.line1 
	and a1.city=a2.city 
	and a1.state=a2.state 
	and a1.id<>a2.id
left join address_employee ae on ae.address_id=a2.id
where a1.id not in (select address_id from address_employee);

select *
from address a1
inner join address a2 on a1.line1=a2.line1 
	and a1.city=a2.city 
	and a1.state=a2.state
	and a1.id<>a2.id
left join address_employee ae on ae.address_id=a2.id
where a1.id not in (select address_id from address_employee);


select * from employee e
inner join address_employee ae on ae.employee_id=e.id
inner join address a on a.id=ae.address_id;

update income set income=income*1.1; -- 10% raise

-- show the lowest earner
select employee.*,income
from income
inner join employee on income.employee_id=employee.id 
where income= (
SELECT MIN(income) FROM income
);

-- give them a raise
-- find the lowest with a target to update, can't update on a sub select
select * from income i1
JOIN (SELECT MIN(income) AS income FROM income) mI ON (i1.income = mI.income);

-- Do the update
UPDATE income i1
JOIN (SELECT MIN(income) AS income FROM income) mI ON (i1.income = mI.income)
SET 
    i1.income = mI.income + 5000;

select * 
from income
join (SELECT MIN(income) AS income FROM income) as mI
;

-- check for the increase
select * from income where employee_id=249;

select count(*) from employee; -- starting emp count = 300
select count(*) from employee where lastname like 'w%';  -- 15

delete from address_employee where employee_id in (select id from employee where lastname like 'W%');
delete from address where id not in (select  address_id from address_employee);
delete from income where employee_id in (select id from employee where lastname like 'W%');
delete from employee where lastname like 'W%';

select count(*)
from employee e
inner join address_employee ae on ae.employee_id=e.id
inner join address a on ae.address_id=a.id;
--  333 addresses

select sum(income)
from employee e
inner join income i on i.employee_id=e.id;
--  44768805


select count(*) from employee; -- ending emp count = 285


select * from employee;
-- delete from employee;