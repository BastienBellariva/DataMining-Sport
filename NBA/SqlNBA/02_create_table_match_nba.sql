USE d_nba;

CREATE TABLE match_nba(
	id_match_nba INT NOT NULL AUTO_INCREMENT,
	date_match DATE NOT NULL,
    jour_semaine VARCHAR(10) NOT NULL,
    id_saison INT NOT NULL,
    id_equipe_domicile INT NOT NULL,
    id_equipe_visiteur INT NOT NULL,
    points_domicile INT NOT NULL,
    points_visiteur INT NOT NULL,
    prolongation BOOLEAN NOT NULL,
 	PRIMARY KEY (id_match_nba) 
);