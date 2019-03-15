USE d_nba;

CREATE TABLE stat_equipe(
    id_stat_equipe INT NOT NULL AUTO_INCREMENT,
    id_equipe INT NOT NULL,
    id_saison INT NOT NULL,
    classement_equipe INT(4),
    nbr_match INT(4),
    nbr_minute_joue INT(8),
    nbr_panier_marque INT(8),
    nbr_tentative_shoot INT(8),
    pourcentage_reussite_shoot FLOAT(4,2),
    nbr_panier_3points_tente INT(8),
    nbr_panier_3points INT(8),
    pourcentage_reussite_3ptn FLOAT(4,2),
    nbr_panier_2points_tente INT(8),
    nbr_panier_2points INT(8),
    pourcentage_reussite_2ptn FLOAT(4,2),
    nbr_lancer_franc_tente INT(8),
    nbr_lancer_franc INT(8),
    pourcentage_reussite_lancer_franc FLOAT(4,2),
    nbr_rebond_offensif INT(8),
    nbr_rebond_defensif INT(8),
    nbr_rebond_total INT(8),
    nbr_passe_decisive INT(8),
    nbr_interception INT(8),
    nbr_contre INT(8),
    nbr_ballon_perdu INT(8),
    nbr_faute INT(8),
    nbr_point_total INT(8),
    PRIMARY KEY(id_stat_equipe)
);