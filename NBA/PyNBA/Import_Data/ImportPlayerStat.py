import csv

from Import_Data import ConnectDB as ConnectDBFile
from Import_Data import FormatData as FormatDataFile


class ImportPlayerStat:

    conn = None
    cursor = None
    all_seasons = []

    def __init__(self):
        self.conn = ConnectDBFile.ConnectDB.getInstance()
        self.cursor = self.conn.cursor()
        self.setAllSeasons()

    def setAllSeasons(self):
        sql = "SELECT * FROM saison"
        self.cursor.execute(sql)
        self.all_seasons = self.cursor.fetchall()
        print(self.all_seasons)

    def scrollFilesForPlayerStatAndImport(self):
        for season in self.all_seasons:
            csv_name = "../Calendrier_Resultat/" + season[1] + "/" + season[1] + "_players_total_stats.csv"
            print(csv_name)
            csv_content = list(csv.reader(open(csv_name), delimiter=','))
            self.formatAndImportPlayerStat(csv_content[1:], season)

    def selectIdTeamWithName(self, libelle_team):
        sql = "SELECT id_equipe FROM equipe WHERE libelle_equipe LIKE %s"
        val = [libelle_team]
        self.cursor.execute(sql, val)
        team = self.cursor.fetchone()
        return team[0]

    def selectIdSeasonWithLibelle(self, season_libelle):
        sql = "SELECT id_saison FROM saison WHERE annee_saison LIKE %s"
        val = [season_libelle]
        self.cursor.execute(sql, val)
        season = self.cursor.fetchone()
        return season[0]

    def formatAndImportPlayerStat(self, one_season_player_stat, season):
        for player_stat in one_season_player_stat:
            print("In progress ... {}".format(player_stat))
            libelle_team = FormatDataFile.FormatData().formatTeamLibelle(player_stat[5])

            if libelle_team != "TOT":
                id_team = self.selectIdTeamWithName(libelle_team)
                id_season = self.selectIdSeasonWithLibelle(season[1])

                print(player_stat[2], id_season, id_team, player_stat[0], player_stat[3], player_stat[4],
                      player_stat[6], player_stat[7], player_stat[8],
                      player_stat[9], player_stat[10], float(player_stat[11]),
                      player_stat[13], player_stat[12], float(player_stat[14]),
                      player_stat[16], player_stat[15], float(player_stat[17]),
                      player_stat[18],
                      player_stat[20], player_stat[19], float(player_stat[21]),
                      player_stat[22], player_stat[23], float(player_stat[24]),
                      )

                self.insertOneStat(id_team, id_season, team_stat[0], team_stat[2], team_stat[3],
                                   team_stat[4], team_stat[5], float(team_stat[6]),
                                   team_stat[8], team_stat[7], float(team_stat[9]),
                                   team_stat[11], team_stat[10], float(team_stat[12]),
                                   team_stat[14], team_stat[13], float(team_stat[15]),
                                   team_stat[16], team_stat[17], team_stat[18],
                                   team_stat[19], team_stat[20], team_stat[21],
                                   team_stat[22], team_stat[23], team_stat[24]
                                   )

    def insertOneStat(self, id_team, id_season, rank, number_match, number_minuts_play,
                      number_basket, number_basket_try, percent_basket_success,
                      number_3ptn_try, number_3ptn, percent_3ptn_succes,
                      number_2ptn_try, number_2ptn, percent_2ptn_succes,
                      number_throwfree_try, number_throwfree, percent_throwfree_succes,
                      number_offensive_rebound, number_defensive_rebound, number_rebound,
                      number_decisive_pass, number_interception, number_counter,
                      number_lost_ball, number_lack, total_point
                      ):
        sql = """
                INSERT INTO stat_equipe ( id_equipe, id_saison, classement_equipe, nbr_match, nbr_minute_joue,
                                          nbr_panier_marque, nbr_tentative_shoot, pourcentage_reussite_shoot,
                                          nbr_panier_3points_tente, nbr_panier_3points, pourcentage_reussite_3ptn,
                                          nbr_panier_2points_tente, nbr_panier_2points, pourcentage_reussite_2ptn,
                                          nbr_lancer_franc_tente, nbr_lancer_franc, pourcentage_reussite_lancer_franc,
                                          nbr_rebond_offensif, nbr_rebond_defensif, nbr_rebond_total,
                                          nbr_passe_decisive, nbr_interception, nbr_contre,
                                          nbr_ballon_perdu, nbr_faute, nbr_point_total) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        val = [id_team, id_season, rank, number_match,number_minuts_play,
               number_basket, number_basket_try, percent_basket_success,
               number_3ptn_try, number_3ptn, percent_3ptn_succes,
               number_2ptn_try, number_2ptn, percent_2ptn_succes,
               number_throwfree_try, number_throwfree, percent_throwfree_succes,
               number_offensive_rebound, number_defensive_rebound, number_rebound,
               number_decisive_pass, number_interception, number_counter,
               number_lost_ball, number_lack, total_point]
        self.cursor.execute(sql, val)
        self.conn.commit()

