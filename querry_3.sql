SELECT s.group_id, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = 1
GROUP BY s.group_id;
