USE d_nba;

-- Foreign keys table match_nba
ALTER TABLE match_nba ADD FOREIGN KEY(id_equipe_domicile)
    REFERENCES equipe(id_equipe);

ALTER TABLE match_nba ADD FOREIGN KEY(id_equipe_visiteur)
    REFERENCES equipe(id_equipe);


-- Foreign keys table stat_equipe
ALTER TABLE stat_equipe ADD FOREIGN KEY(id_equipe)
    REFERENCES equipe(id_equipe);

ALTER TABLE stat_equipe ADD FOREIGN KEY(id_saison)
    REFERENCES saison(id_saison);


-- Foreign keys table stat_joueur
ALTER TABLE stat_joueur ADD FOREIGN KEY(id_joueur)
    REFERENCES joueur(id_joueur);

ALTER TABLE stat_joueur ADD FOREIGN KEY(id_saison)
    REFERENCES saison(id_saison);

ALTER TABLE stat_joueur ADD FOREIGN KEY(id_equipe)
    REFERENCES equipe(id_equipe);