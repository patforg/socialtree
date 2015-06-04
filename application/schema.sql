/*PG800 has a bug with capitalisations. I will post a bug report on their github soon
       - nuclearbanane
*/

CREATE TABLE "users"
(
  userid serial NOT NULL,
  email varchar(60) NOT NULL,
  username varchar(32) NOT NULL,
  password varchar(32),
  firstname varchar(20),
  lastname varchar(20),
  joindate date,
  CONSTRAINT user_pkey PRIMARY KEY (userid, email, username)
)


/* END */