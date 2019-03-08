USE tennis;

CREATE TABLE comment_match(
	id_comment_match int NOT NULL AUTO_INCREMENT,
	libelle_comment_match varchar(50) NULL,
 	PRIMARY KEY (id_comment_match) 
);

CREATE TABLE location(
	id_location int NOT NULL AUTO_INCREMENT,
	libelle_location varchar(50) NOT NULL,
	PRIMARY KEY (id_location)
);	

CREATE TABLE match_stat(
	id_match_stat int NOT NULL AUTO_INCREMENT,
	atp int NULL, -- A compléter
	wta int NULL, -- A compléter
	id_location int NOT NULL,
	id_round int NULL,
	id_tournament int NOT NULL,
	date_match datetime NOT NULL,
	id_serie int NULL,
	court varchar(50) NULL,
	id_surface int NULL,
	best_of smallint NULL,
	id_winner int NOT NULL,
	id_looser int NOT NULL,
	winner_atp_rank varchar(20) NULL,
	looser_atp_rank varchar(20) NULL,
	winner_points int NULL,
	looser_points int NULL,
	score_winner_set1 int NULL,
	score_looser_set1 int NULL,
	score_winner_set2 int NULL,
	score_looser_set2 int NULL,
	score_winner_set3 int NULL,
	score_looser_set3 int NULL,
	score_winner_set4 int NULL,
	score_looser_set4 int NULL,
	score_winner_set5 int NULL,
	score_looser_set5 int NULL,
	score_sets_winner int NULL,
	score_sets_looser int NULL,
	id_comment_match int NOT NULL,
	odd_winner float NULL,
	odd_looser float NULL,
	average_odd_winner float NULL,
	average_odd_looser float NULL,
   	PRIMARY KEY (id_match_stat) 
);

CREATE TABLE players(
	id_player int NOT NULL AUTO_INCREMENT,
	name_player varchar(50) NULL,
	genre_player int NULL,
  	PRIMARY KEY (id_player) 
);

CREATE TABLE round(
	id_round int NOT NULL AUTO_INCREMENT,
	libelle_round varchar(50) NULL,
  	PRIMARY KEY (id_round) 
);

CREATE TABLE series(
	id_serie int NOT NULL AUTO_INCREMENT,
	libelle_serie varchar(50) NULL,
	PRIMARY KEY (id_serie)
);

CREATE TABLE surface(
	id_surface int NOT NULL AUTO_INCREMENT,
	libelle_surface varchar(50) NULL,
	PRIMARY KEY (id_surface)
);

CREATE TABLE tournament(
	id_tournament int NOT NULL,
	libelle_tournament varchar(50) NOT NULL,
	type_genre int NULL,
 	PRIMARY KEY (id_tournament)
 );