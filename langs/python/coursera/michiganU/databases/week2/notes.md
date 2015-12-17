###### SQL 

```sql
CREATE TABLE Users(
name VARCHAR(128),
email VARCHAR(128)
)

INSERT INTO Users (name,email) VALUES ('Kristin', 'kf@umich.edu')

DELETE FROM Users WHERE email='fred@umich.edu'

UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'

SELECT * FROM Users 

SELECT * FROM Users WHERE email='csev@umich.edu'

SELECT * FROM Users ORDER BY email

SELECT * FROM Users ORDER BY name
```
