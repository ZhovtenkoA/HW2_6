SELECT s.id, s.name
FROM subjects s
JOIN grades g ON s.id = g.subject_id
WHERE g.student_id = 1;