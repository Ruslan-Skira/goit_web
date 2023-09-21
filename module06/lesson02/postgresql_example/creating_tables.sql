CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(30),
  email VARCHAR(30),
  password VARCHAR(30),
  age TINYINT UNSIGNED,  /*age smallint Postgresql*/
  gender_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (gender_id) REFERENCES genders (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

INSERT INTO contacts (id, name, email, phone, favorite, user_id)
VALUES (1, 'Allen Raymond', 'nulla.ante@vestibul.co.uk', '(992) 914-3792', false, 1), 
(2, 'Chaim Lewis', 'dui.in@egetlacus.ca', '(294) 840-6685', true, 1),
(3, 'Kennedy Lane', 'mattis.Cras@nonenimMauris.net', '(542) 451-7038', true, 2),
(4, 'Wylie Pope', 'est@utquamvel.net', '(692) 802-2949', false, 2),
(5, 'Cyrus Jackson', 'nibh@semsempererat.com', '(501) 472-5218', false, null);