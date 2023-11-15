SELECT nt.id, nt.name, rc.description, rc.done, t.name as tag
FROM notes AS nt
LEFT JOIN records AS rc ON rc.note_id =  nt.id
LEFT JOIN note_m2m_tag AS nmmt ON nmmt.note = nt.id
LEFT JOIN tags AS t ON t.id = nmmt.tag
WHERE t.name = 'food'