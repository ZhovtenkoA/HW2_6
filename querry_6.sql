SELECT s.id, s.name
FROM students s
JOIN groups g ON s.group_id = g.id
WHERE g.id = 1;