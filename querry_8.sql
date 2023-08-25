SELECT t.id, t.name, AVG(g.grade) AS average_grade
FROM teachers t
JOIN subjects s ON t.id = s.teacher_id
JOIN grades g ON s.id = g.subject_id
WHERE t.id = 1
GROUP BY t.id, t.name;