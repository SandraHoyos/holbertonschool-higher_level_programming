--  lists all the cities of California that can be found in the database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.i
-- database name will be passed as an argument of the mysql command

SELECT id, name
  fROM cities
 WHERE state_id = (SELECT id FROM states WHERE name = "california") GROUP BY id ORDER BY id ASC;
