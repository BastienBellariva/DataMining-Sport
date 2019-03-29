USE d_nba;

CREATE TABLE stat_joueur(
    id_stat_joueur INT NOT NULL AUTO_INCREMENT,
    id_joueur VARCHAR(30) NOT NULL,
    id_saison INT NOT NULL,
    id_equipe INT NOT NULL,
    classement_joueur INT(4),
    poste_joueur VARCHAR(40),
    age_joueur INT(4),
    nbr_match INT(8),
    nbr_match_titulaire INT(8),
    nbr_minute_joue INT(8),
    nbr_panier_marque INT(8),
    nbr_shoot_tente INT(8),
    pourcentage_reussite_shoot FLOAT(4,2),
    nbr_panier_3ptn_tente INT(8),
    nbr_panier_3ptn INT(8),
    pourcentage_reussite_3ptn FLOAT(4,2),
    nbr_panier_2ptn_tente INT(8),
    nbr_panier_2ptn INT(8),
    pourcentage_reussite_2ptn FLOAT(4,2),
    pourcentage_effectif FLOAT(4,2),
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
    PRIMARY KEY(id_stat_joueur)
);