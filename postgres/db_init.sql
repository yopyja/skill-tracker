CREATE TABLE IF NOT EXISTS public."User" (
	id varchar NOT NULL,
	firstname varchar NOT NULL,
	lastname varchar NOT NULL,
	email varchar NOT NULL,
	"password" varchar NOT NULL,
	prefix varchar NULL,
	lastlogin timestamp NULL,
    CONSTRAINT user_pkey PRIMARY KEY (id)
);
