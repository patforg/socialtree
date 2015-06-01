/*PG800 has a bug with capitalisations. I will post a bug report on their github soon
       - nuclearbanane
*/

create table "user"
(
       userID SERIAL PRIMARY KEY, 
       email varchar(60) PRIMARY KEY,
       userName varchar(32),
       password varchar(32), /*VERY BAD PRACTICE!!!!*/
       firstName varchar(20),
       lastName varchar(20),
       joinDate date,
       reputation integer
);


/* END */