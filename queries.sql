SELECT * FROM students;

SELECT std_name,std_mail
FROM students;

SELECT *
FROM students
WHERE std_age > 20;

SELECT *
FROM students
WHERE std_gender='Female';

SELECT *
FROM students
ORDER BY std_age DESC;

SELECT *
FROM marks
ORDER BY marks DESC
LIMIT 5;

SELECT s.*
FROM students s
JOIN departments d
ON s.std_dept_id=d.dept_id
WHERE d.dept_name='CSE';

SELECT *
FROM teachers
WHERE salary > 50000;

SELECT *
FROM courses
WHERE fees BETWEEN 10000 AND 30000;

UPDATE students
SET std_mail='newmail@gmail.com'
WHERE std_id=1;

UPDATE teachers
SET salary = salary * 1.10;

DELETE FROM students
WHERE std_id=20;

SELECT COUNT(*)
FROM students;

SELECT AVG(salary)
FROM teachers;

SELECT MAX(marks)
FROM marks;

SELECT MIN(fees)
FROM courses;

SELECT std_dept_id,
COUNT(*)
FROM students
GROUP BY std_dept_id;

SELECT subject,
AVG(marks)
FROM marks
GROUP BY subject;

SELECT course_id,
COUNT(std_id)
FROM enrollments
GROUP BY course_id;

SELECT std_dept_id,
COUNT(*)
FROM students
GROUP BY std_dept_id
HAVING COUNT(*) > 5;
