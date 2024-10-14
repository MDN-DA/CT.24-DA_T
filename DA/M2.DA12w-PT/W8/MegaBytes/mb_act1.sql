select*from employee_detail
where first_aid_officer;
-- select count(first_aid_officer), first_aid_officer
-- from employee_detail;

select*from employee_detail
where first_aid_officer and base_pay_band not like '2';

select count(store_city), store_city
from store_detail
group by store_city;

select*from employee_detail
where base_pay_band =6;

select count(main_store_id), main_store_id
from employee_detail
group by main_store_id
