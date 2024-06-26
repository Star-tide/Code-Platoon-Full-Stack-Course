-- psql starts database terminal
-- \l lists all databases
-- \c <db_name> Shows what DB you are connected to
-- \d lists DB connected to the DB
-- \i <script> runs the script
-- example import of data \COPY students FROM '/Users/bnesslage/Code Platoon/.venv/homeworkAssignments/postgresql/students.csv' DELIMITER ',' CSV HEADER;
-- ABSPATH for sql

DROP TABLE IF EXISTS students;
-- Serialized means it will increment
CREATE TABLE students(
    id serial PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade CHAR(1)
);

\COPY students FROM '/Users/bnesslage/Code Platoon/.venv/homeworkAssignments/postgresql/students.csv' DELIMITER ',' CSV HEADER;