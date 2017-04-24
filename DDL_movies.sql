CREATE DATABASE CS404_Movies;

CREATE TABLE client
(
	u_id INT AUTO_INCREMENT,
	first_n VARCHAR(20),
	last_n VARCHAR(20),
	phone CHAR(10),
	PRIMARY KEY(u_id)
);

CREATE TABLE card
(
	c_number CHAR(16) ,
	c_u_id INT NOT NULL REFERENCES client(u_id),
	PRIMARY KEY(c_number)
);

CREATE TABLE email
(
	email VARCHAR(40),
	e_u_id INT REFERENCES client(u_id),
	PRIMARY KEY(email, e_u_id)
);

CREATE TABLE r_type
(
	r_id INT AUTO_INCREMENT,
    type_s VARCHAR(50),
    PRIMARY KEY (r_id)
);

CREATE TABLE genra
(
	g_id INT AUTO_INCREMENT,
    genra_s VARCHAR(50),
    PRIMARY KEY (g_id)
);

CREATE TABLE rating
(
	r_id INT AUTO_INCREMENT,
    rating_s VARCHAR(50),
    PRIMARY KEY (r_id)
);

CREATE TABLE r_format
(
	f_id INT AUTO_INCREMENT,
    format_s VARCHAR(50),
    PRIMARY KEY (f_id)
);

CREATE TABLE resource
(
	r_id INT AUTO_INCREMENT,
    title VARCHAR(50),
    type_id INT REFERENCES r_type(t_id),
    genre_id INT REFERENCES genre(g_id),
    rating_id INT REFERENCES rating(r_id),
    format_id INT REFERENCES r_format(f_id), 
    runtime INT,
    PRIMARY KEY(r_id)
);

CREATE TABLE checked_out
(
	resource INT REFERENCES resource(r_id),
	card_num CHAR(16) NOT NULL REFERENCES card(c_number),
	c_date DATE NOT NULL,
    PRIMARY KEY (resource)
);