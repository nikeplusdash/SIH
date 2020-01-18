CREATE TABLE USER(
    id INTEGER PRIMARY KEY,
    username VARCHAR,
    email VARCHAR,
    password VARCHAR,
    time_stamp VARCHAR,
    verified INTEGER
);

CREATE TABLE ADMIN(
    id INTEGER PRIMARY KEY,
    admin_level INTEGER,
    name VARCHAR,
    password VARCHAR
);

CREATE TABLE COMPLAIN(
    id INTEGER PRIMARY KEY,
    body VARCHAR,
    category VARCHAR,
    status_id INTEGER,
    time_stamp VARCHAR
);

INSERT INTO ADMIN(admin_level,name,password) VALUES(0,"nik","1234");
INSERT INTO ADMIN(admin_level,name,password) VALUES(1,"nike","123");
INSERT INTO COMPLAIN(body,category,status_id,time_stamp) VALUES("I hate chilli paneer","Mess",0,CURRENT_TIMESTAMP);
INSERT INTO USER(username,email,password,time_stamp,verified) VALUES("niko","nik@nik.com","1234",CURRENT_TIMESTAMP,0);
INSERT INTO USER(username,email,password,time_stamp,verified) VALUES("sonu","sonu@son.com","123",CURRENT_TIMESTAMP,1);