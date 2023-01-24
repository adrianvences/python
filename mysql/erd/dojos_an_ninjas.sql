SELECT * FROM dojos;
INSERT INTO users(first_name,last_name,email)
VALUES ('adrian','vences', 'adrianvences9820@gmail.com'),('elmo','puppet','elmo@seseme@gmail.com'),('sofie','delsid','sophie@cocomelon.com');
SELECT * FROM users WHERE email = ('adrianvences9820@gmail.com');
SELECT * FROM users WHERE id = 6;
UPDATE users SET last_name = 'pancakes' WHERE id =3;
DELETE FROM users WHERE id = 2;
SELECT first_name FROM users ORDER BY first_name DESC;

INSERT INTO dojos (name)
VALUES ('jiujitsu'),('boxing'),('karate');

SET SQL_SAFE_UPDATES = 0 ;
DELETE FROM dojos;

INSERT INTO dojos (name)
VALUES ('jiu'),('box'),('kar');

INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ('adrian','vences',24,5),('gen','vences',6,5),('xiomara','rivera',23,5);

SELECT * FROM ninjas;

INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ('fernanda','vences',24,6),('eric','vences',6,6),('gabby','rivera',23,6);

SELECT  dojo_id FROM ninjas WHERE id = 9;

INSERT INTO users(first_name,last_name,email)
VALUES ('bob','marley', 'bob@marley.com' ),('hulk','hogan','hulk@hogan.com'),('jimmy','hendrix','jimmy@hendrix.com'),('dwayne','johnson','dwayne@johnson.com'),('elvis','presley','elvis@presley.com');

SELECT * FROM users;


