DROP TABLE IF EXISTS students;
-- Serialized means it will increment
CREATE TABLE students(
    id serial PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    subject VARCHAR(50)
);

DROP TABLE IF EXISTS subjects;

CREATE TABLE subjects(
    id serial PRIMARY KEY,
    subject VARCHAR(50)
);

DROP TABLE IF EXISTS teachers;

CREATE TABLE teachers(
    id serial PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INTEGER,
    subject VARCHAR(50)
);

\COPY students FROM '/Users/bnesslage/Code Platoon/.venv/homeworkAssignments/school_api/data/student.csv' DELIMITER ',' CSV HEADER;
\COPY subjects FROM '/Users/bnesslage/Code Platoon/.venv/homeworkAssignments/school_api/data/subjects.csv' DELIMITER ',' CSV HEADER;
\COPY teachers FROM '/Users/bnesslage/Code Platoon/.venv/homeworkAssignments/school_api/data/teachers.csv' DELIMITER ',' CSV HEADER;