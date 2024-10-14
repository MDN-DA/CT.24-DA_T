
CREATE TABLE store_detail (
store_id INT PRIMARY KEY,
store_city VARCHAR(255),
store_address VARCHAR(255),
area_manager_id INT,
seat_capacity INT
); 

CREATE TABLE payment_bands (
    band_id INT PRIMARY KEY, 
    band_title VARCHAR(255), 
    hourly_amount DECIMAL(10,2)
); 

CREATE TABLE employee_detail (
employee_id INT PRIMARY KEY, 
first_name VARCHAR(255), 
last_name VARCHAR(255),  
date_of_birth DATE,
active BOOLEAN, 
main_store_id INT,
float_store_id INT,
base_pay_band INT,
weekly_hours DECIMAL(4,2),
fire_officer BOOLEAN,
first_aid_officer BOOLEAN,
keyholder BOOLEAN,
alarm_responder BOOLEAN
); 

INSERT INTO employee_detail VALUES
(1000, "Jon", "Flannagan", "1987-11-02",1,1,1,1,42,1,1,1,1),
(1008, "Noah", "Lopez", "1983-04-17",1,1,1,1,42,1,1,1,1),
(1013, "William", "Brown", "1966-08-30",1,1,1,1,42,1,1,1,1),
(1028, "Matthew", "Jones", "1956-07-25",1,1,1,1,42,1,1,1,1),
(1038, "Asuman", "Buruk", "1991-06-09",1,2,11,2,40,1,1,1,1),
(1004, "Liam", "Gonzalez", "1982-11-28",1,3,3,2,42,1,1,1,1),
(1010, "Mia", "Kim", "1978-12-10",1,4,4,2,40,1,1,1,1),
(1021, "Harper", "Park", "1977-04-02",1,5,5,2,46,1,1,1,1),
(1045, "Alex", "Blanco", "1995-07-13",1,6,6,2,35,1,1,1,1),
(1034, "Lucas", "Torres", "1954-02-08",1,7,7,2,40,1,1,1,1),
(1005, "Olivia", "Lee", "1986-07-04",1,8,8,2,30,1,1,1,1),
(1011, "Juan", "Rubio", "1974-06-05",1,9,9,2,32,1,1,1,1),
(1001, "Emily", "Smith", "1988-09-15",1,10,10,2,42,1,1,1,1),
(1006, "Ethan", "Nguyen", "1984-10-31",1,11,1,2,48,1,1,1,1),
(1002, "Daniel", "Martinez", "1985-05-20",1,12,12,2,37.5,1,1,1,1),
(1044, "Ima", "Fredrikson", "1995-07-13",1,13,13,2,37.5,1,1,1,1),
(1016, "Evelyn", "Roby", "1958-11-13",0,2,6,3,0,0,0,0,0),
(1029, "Sofia", "Hussain", "1960-12-22",1,4,4,3,37.5,0,0,1,1),
(1041, "Emma", "Taylor", "1995-07-13",1,5,5,3,35,1,0,1,1),
(1012, "Xiu", "Wang", "1979-02-14",1,7,10,3,32,0,0,1,1),
(1015, "Benjamin", "Jones", "1969-07-17",1,8,13,3,30,1,1,1,1),
(1018, "Layla", "Njoroge", "1962-05-23",1,10,7,3,37.5,0,0,1,1),
(1020, "Avery", "Ramirez", "1968-12-26",1,11,1,3,37.5,1,1,1,1),
(1014, "Amelia", "Garcia", "1972-10-25",1,12,12,3,30,0,1,1,0),
(1017, "Oliver", "Cheung", "1957-03-07",1,13,13,3,30,1,1,1,1),
(1022, "Mohammed", "Rafiq", "1959-01-29",1,3,3,4,37.5,0,0,1,0),
(1036, "Chloe", "Pham", "1974-04-26",0,4,4,4,0,0,0,0,0),
(1025, "Abigail", "Manley", "1973-02-04",1,2,11,5,20,0,1,0,0),
(1039, "Mia", "Jones", "1994-10-03",1,2,6,5,20,0,0,0,0),
(1003, "Sophia", "Chen", "1990-03-12",1,4,3,5,20,0,1,0,0),
(1042, "Hayley", "Stevenson", "1995-07-13",1,5,5,5,12,0,0,0,0),
(1043, "Charlie", "Griffiths", "1995-07-13",1,5,12,5,12,0,0,0,0),
(1007, "Ava", "Gomez", "1995-01-19",1,6,6,5,20,0,0,0,0),
(1027, "Elizabeth", "Wiggins", "1967-04-06",1,6,2,5,20,1,0,0,0),
(1019, "Azizi", "Wambui", "1955-09-09",1,7,10,5,24,0,0,0,0),
(1033, "Grace", "Avila", "1963-11-16",1,7,13,5,20,0,0,0,0),
(1024, "Alexander", "O'Reily", "1971-08-18",1,8,9,5,15,1,1,1,1),
(1023, "Sophie", "Jonestone", "1961-06-20",1,9,8,5,28,0,1,0,0),
(1031, "Madison", "Brownlee", "1987-03-04",1,10,10,5,18,0,0,0,0),
(1030, "Jacob", "Wong", "1981-09-10",1,11,6,5,20,1,0,0,0),
(1040, "Noah", "Garcia", "1988-07-27",1,11,2,5,20,0,1,0,0),
(1026, "Leon", "Bai", "1964-10-12",1,12,5,5,28,0,0,0,0),
(1032, "Elijah", "Tompkins", "1970-05-28",1,13,8,5,16,0,0,0,0),
(1051, "Olu", "Mwangi", "2005-07-13",1,2,11,6,12,0,1,0,0),
(1037, "Liam", "Salah", "2006-01-14",1,3,7,6,8,0,0,0,0),
(1009, "Isabella", "Hernandez", "2003-08-22",1,4,4,6,20,0,0,0,0),
(1035, "Avery", "Smith", "2005-08-01",1,9,13,6,8,0,0,0,0)
;

INSERT INTO store_detail VALUES
(1,"Head Office","16b, SW13 XBU", 1000, 12),
(2,"Machester","43, M39 7BF", 1000, 40),
(3,"St Helens","Unit 3, WA9 5SL", 1008, 26),
(4,"Wigan","132, WN1 7DW", 1000, 34),
(5,"Liverpool","26, L1 9LU", 1013, 40),
(6,"Manchester","Unit 34, M42 9AQ", 1000, 12),
(7,"Warrington","76, WA5 7BR", 1028, 44),
(8,"Chester","2 The Market, CH4 7QJ", 1028, 15),
(9,"New Brighton","478, ch45 4FT", 1028, 22),
(10,"Warrington","Block C, WA1 6YS", 1028, 34),
(11,"Manchester","112A, M1 1LH", 1000, 45),
(12,"Liverpool","1, L3 1HL", 1013, 26),
(13,"Chester","22, CH2 9RC", 1028, 35);

INSERT INTO payment_bands VALUES
(1, "Area Manager", 21.30),
(2, "Store Manager", 19.30),
(3, "Deputy Manager", 17.30),
(4, "Supervisor", 15.30),
(5, "Cashier", 12.30),
(6, "Cashier - 21", 10.30);

ALTER TABLE store_detail
ADD CONSTRAINT fk_area_manager_id
FOREIGN KEY (area_manager_id) REFERENCES employee_detail(employee_id);

ALTER TABLE employee_detail
ADD CONSTRAINT fk_main_store_id
FOREIGN KEY (main_store_id) REFERENCES store_detail(store_id);

ALTER TABLE employee_detail
ADD CONSTRAINT fk_float_store_id
FOREIGN KEY (float_store_id) REFERENCES store_detail(store_id);

ALTER TABLE employee_detail
ADD CONSTRAINT fk_base_pay_band
FOREIGN KEY (base_pay_band) REFERENCES payment_bands(band_id);
