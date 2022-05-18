-- 1 задание
SELECT * FROM auto WHERE make ='Toyota' AND model='Camry' ORDER BY DESC year;

-- 2 задание
SELECT DISTINCT first_name FROM call_center ORDER BY DESC first_name LIMIT 10;

-- 3 задание
UPDATE auto SET make='Mercedes' TO 'Mersus';

-- 4 задание

DELETE * FROM drivers WHERE first_name ='Азамат' AND last_name='Азаматов';

-- 5 задание

SELECT COUNT(first_name) FROM drivers WHERE experience > 10 AND gender='female';


-- 6 задание
SELECT AVG(experience) FROM drivers WHERE date_of_birth > '1975-10-10';

-- 7 задание
SELECT * FROM drivers JOIN auto ON drivers.id_car = auto.id;

-- 8 задание

SELECT COUNT('Toyota'), COUNT('BMW'), COUNT('Mercedes') FROM auto ORDER BY DESC;