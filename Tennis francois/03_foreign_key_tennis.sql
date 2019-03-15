USE d_tennis;

ALTER TABLE match_stat ADD FOREIGN KEY(id_comment_match)
    REFERENCES comment_match (id_comment_match);

ALTER TABLE match_stat ADD FOREIGN KEY(id_location)
    REFERENCES location (id_location);

ALTER TABLE match_stat ADD FOREIGN KEY(id_looser)
    REFERENCES players (id_player);

ALTER TABLE match_stat ADD FOREIGN KEY(id_winner)
    REFERENCES players (id_player);

ALTER TABLE match_stat ADD FOREIGN KEY(id_round)
    REFERENCES round (id_round);

ALTER TABLE match_stat ADD FOREIGN KEY(id_surface)
    REFERENCES surface (id_surface);

ALTER TABLE match_stat ADD FOREIGN KEY(id_tournament)
    REFERENCES tournament (id_tournament);

ALTER TABLE match_stat ADD FOREIGN KEY(id_serie)
    REFERENCES series (id_serie);