import csv

from Import_Data import ConnectDB as ConnectDBFile
from Import_Data import FormatData as FormatDataFile


class ImportMatchStat:

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

    def scrollFilesForMatchStatAndImport(self):
        for season in self.all_seasons:
            csv_name = "../Calendrier_Resultat/" + season[1] + "/" + season[1] + "_results.csv"
            print(csv_name)
            csv_content = list(csv.reader(open(csv_name), delimiter=';'))
            self.formatAndImportMatchStat(csv_content[1:], season)

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

    def formatProlongation(self, prolongation):
        if prolongation == "OT":
            return True
        else:
            return False

    def formatAndImportMatchStat(self, one_season_match_stat, season):
        for match_stat in one_season_match_stat:
            print("In progress ... {}".format(match_stat))
            date_match = FormatDataFile.FormatData().formatDateMatch(match_stat[0])
            day_of_week = FormatDataFile.FormatData().formatDayMatch(match_stat[0])
            id_season = self.selectIdSeasonWithLibelle(season[1])
            id_home_team = self.selectIdTeamWithName(match_stat[3])
            id_visitor_team = self.selectIdTeamWithName(match_stat[1])
            prolongation = self.formatProlongation(match_stat[5])

            self.insertOneStat(date_match, day_of_week, id_season, id_home_team, id_visitor_team, match_stat[4], match_stat[2], prolongation)

    def insertOneStat(self, date_match, day_of_week, id_season, id_home_team, id_visitor_team, home_points, visitor_points, prolongation):
        sql = """
                INSERT INTO match_nba ( date_match,
                                        jour_semaine,
                                        id_saison,
                                        id_equipe_domicile,
                                        id_equipe_visiteur,
                                        points_domicile,
                                        points_visiteur,
                                        prolongation) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
        val = [date_match, day_of_week, id_season, id_home_team, id_visitor_team, home_points, visitor_points, prolongation]
        self.cursor.execute(sql, val)
        self.conn.commit()

