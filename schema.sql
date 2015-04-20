DROP TABLE jobs;
CREATE TABLE jobs(
	id integer primary key autoincrement, 
	job varchar(32), 
	address varchar(64), 
	phone varchar(32), 
	notes varchar(512), 
	lastUpdated bigint
);