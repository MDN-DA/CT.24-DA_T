SELECT COUNT(*), store_city FROM store_detail
GROUP BY store_city;

CREATE TABLE store_detail_backup LIKE store_detail;
 
INSERT INTO store_detail_backup
SELECT * FROM store_detail;

-- Turn OFF Safe Mode
SET SQL_safe_updates = 0;
 
UPDATE store_detail
SET store_city = "Manchester"
WHERE store_city = "Machester";

-- Turn ON Safe Mode
-- SET SQL_safe_updates = 1;

alter table store_detail
add column store_number varchar(50),
add column store_postcode varchar(50);

select substring_index(store_address, ', ', 1)
as store_number from store_detail;

select substring_index(store_address, ', ', -1)
as store_postcode from store_detail;

update store_detail
set store_number = substring_index(store_address, ', ', 1),
store_postcode = substring_index(store_address, ', ', -1);

alter table store_detail
rename column store_number to store_door_number;

alter table store_detail
drop column store_address;

select*from store_detail
where store_postcode like 'CH%';

update store_detail
set store_postcode = upper(store_postcode);