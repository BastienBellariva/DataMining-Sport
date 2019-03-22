import csv

from Import_Data import ConnectDB as ConnectDBFile


class ImportTeams:

    conn = None
    cursor = None
    all_seasons = []
    all_distinct_teams = []

    def __init__(self):
        self.conn = ConnectDBFile.ConnectDB.getInstance()
        self.cursor = self.conn.cursor()
        self.setAllSeasons()

    def setAllSeasons(self):
        sql = "SELECT * FROM saison"
        self.cursor.execute(sql)
        self.all_seasons = self.cursor.fetchall()
        print(self.all_seasons)

    def scrollFilesForTeams(self):
        for season in self.all_seasons:
            csv_name = "../Calendrier_Resultat/" + season[1] + "/" + season[1] + "_team_total_stats.csv"
            print(csv_name)
            csv_content = list(csv.reader(open(csv_name), delimiter=','))
            self.fillArrayTeams(csv_content[1:])

    def fillArrayTeams(self, season_team_stat):
        for line_stat in season_team_stat:
            if line_stat[1] not in self.all_distinct_teams:
                self.all_distinct_teams.append(line_stat[1])

    def insertOneTeam(self, libelle_team):
        sql = "INSERT INTO equipe (libelle_equipe) VALUES (%s)"
        val = [libelle_team]
        self.cursor.execute(sql, val)
        self.conn.commit()

    def importAllTeams(self):
        for team in self.all_distinct_teams:
            print(team)
            self.insertOneTeam(team)

