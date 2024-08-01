-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(*) AS "number of grade A's by the teacher who has graded the most assignments"
FROM assignments
JOIN teachers ON assignments.teacher_id = teachers.id
WHERE assignments.grade = 'A'
GROUP BY teachers.id
ORDER BY COUNT(*) DESC
LIMIT 1;