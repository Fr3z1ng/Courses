PRAGMA foreign_keys=on;
INSERT INTO users(id,first_name,last_name,gender,login,email,register)
VALUES(1,'Sasha','Shauro','Male','best_alex','beste@mail.ru','2020-12-12');
INSERT INTO users(id,first_name,last_name,gender,login,email,register)
VALUES(2,'Pasha','Shauro','Male','best_pasha','pavlik@mail.ru','2018-10-12');
INSERT INTO users(id,first_name,last_name,gender,login,email,register)
VALUES(3,'Tim','Smith','Male','tim_smith','smith@mail.ru','2022-12-12');
INSERT INTO category(category_id,category_title)
VALUES('1','Science');
INSERT INTO category(category_id,category_title)
VALUES('2','Sport');
INSERT INTO category(category_id,category_title)
VALUES('3','Cyber');
INSERT INTO posts(title,data_created,content,post_author_id,post_category_id)
VALUES('What is Quantum Computing?','2021-01-18','Quantum computing is a rapidly-emerging technology that harnesses the laws of quantum mechanics to solve problems too complex for classical computers',1,1);
INSERT INTO posts(title,data_created,content,post_author_id,post_category_id)
VALUES('Genius','2022-12-12','Sashka genius',2,2);
INSERT INTO posts(title,data_created,content,post_author_id,post_category_id)
VALUES('Hard','2010-10-10','Hard is not difficult',3,3);

