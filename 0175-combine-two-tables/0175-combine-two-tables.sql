SELECT firstName, lastName, city, state
FROM Person as A
LEFT JOIN Address as B
ON A.personId = B.personId

