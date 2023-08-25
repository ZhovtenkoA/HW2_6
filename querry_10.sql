SELECT s.id, s.name
FROM subjects s
JOIN grades g ON s.id = g.subject_id
JOIN students st ON g.student_id = st.id
WHERE st.id = 1 AND s.teacher_id = 1;
