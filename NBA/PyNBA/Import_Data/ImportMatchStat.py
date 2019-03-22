import csv

from Import_Data import ConnectDB as ConnectDBFile


class ImportTeams:

    conn = None
    cursor = None
    all_seasons = []
    all_match_stat = []

    def __init__(self):
        self.conn = ConnectDBFile.ConnectDB.getInstance()
        self.cursor = self.conn.cursor()
        self.setAllSeasons()

    def setAllSeasons(self):
        sql = "SELECT * FROM saison"
        self.cursor.execute(sql)
        self.all_seasons = self.cursor.fetchall()
        print(self.all_seasons)

    def scrollFilesForMatchStat(self):
        for season in self.all_seasons:
            csv_name = "../Calendrier_Resultat/" + season[1] + "/" + season[1] + "_results.csv"
            print(csv_name)
            csv_content = list(csv.reader(open(csv_name), delimiter=';'))
            self.addMatchStatOnArray(csv_content[1:])

    def addMatchStatOnArray(self, match_stat):

    def insertOneStat(self, date_match, day_of_week, id_home_team, id_visitor_team, home_points, visitor_points, ):
        sql = "INSERT INTO match_nba (libelle_equipe) VALUES (%s)"
        val = [libelle_team]
        self.cursor.execute(sql, val)
        self.conn.commit()

    def importAllMatchStat(self):
        for team in self.all_distinct_teams:
            print(team)
            self.insertOneTeam(team)

