PRAGMA foreign_keys=on;
CREATE TABLE users(id INTEGER PRIMARY KEY,first_name TEXT,last_name TEXT,gender TEXT,login TEXT,email TEXT,register VARCHAR(8));
CREATE TABLE category(category_id INTEGER PRIMARY KEY,category_title TEXT);
CREATE TABLE posts(title TEXT,data_created VARCHAR(10),content VARCHAR(140),post_author_id INTEGER, post_category_id INTEGER, FOREIGN KEY (post_author_id) REFERENCES users(id) ON DELETE CASCADE, FOREIGN KEY (post_category_id) REFERENCES category(category_id) ON DELETE SET NULL);