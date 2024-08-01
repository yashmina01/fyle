-- Write query to get number of graded assignments for each student:
SELECT 
    assignments.student_id AS "student id", 
    COUNT(assignments.id) AS "number of graded assignments"
FROM 
    assignments 
WHERE 
    assignments.grade IS NOT NULL 
GROUP BY 
    assignments.student_id;