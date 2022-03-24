CREATE TABLE notebookUsersData (
	id SERIAL REFERENCES mainNoteAppUsers(id) ,
	created text,
	lastLogin text,
	timesLogin int DEFAULT 0,
	timesEdited int DEFAULT 0
);