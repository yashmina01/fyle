-- Write query to get number of graded assignments for each student:
SELECT student_id AS "student id", 
       COUNT(*) AS "number of graded assignments" 
FROM assignments 
WHERE state = 'GRADED' 
GROUP BY student_id;
