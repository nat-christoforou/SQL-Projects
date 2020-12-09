SELECT johnny.title FROM (SELECT * FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = 'Johnny Depp') AS johnny
INNER JOIN
(SELECT * FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = 'Helena Bonham Carter') AS helena
ON johnny.id = helena.id;