-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student (
student_id serial,
first_name varchar(80),
last_name varchar(80),
birthday date,
phone varchar(20)
);

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE student ADD COLUMN middle_name varchar(80);

-- 3. Удалить колонку middle_name
ALTER TABLE student DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student RENAME COLUMN birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student ALTER COLUMN phone SET DATA TYPE varchar(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student (first_name, last_name, birthday, phone) VALUES
('Anna', 'Grey', '1990-08-24', '888-432-89-00'),
('Boris', 'Green', '2000-01-20', '888-555-00-16'),
('Jake', 'Smith', '1994-04-10', '888-555-48-00');

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE student RESTART IDENTITY;