import csv

from Import_Data import ConnectDB as ConnectDBFile


class ImportPlayers:

    conn = None
    cursor = None
    all_seasons = []
    all_distinct_players = []

    def __init__(self):
        self.conn = ConnectDBFile.ConnectDB.getInstance()
        self.cursor = self.conn.cursor()
        self.setAllSeasons()

    def setAllSeasons(self):
        sql = "SELECT * FROM saison"
        self.cursor.execute(sql)
        self.all_seasons = self.cursor.fetchall()
        print(self.all_seasons)

    def scrollFilesForPlayers(self):
        for season in self.all_seasons:
            csv_name = "../Calendrier_Resultat/" + season[1] + "/" + season[1] + "_players_total_stats.csv"
            print(csv_name)
            csv_content = list(csv.reader(open(csv_name), delimiter=','))
            self.fillArrayPlayers(csv_content[1:])

    def fillArrayPlayers(self, season_player_stat):
        for line_stat in season_player_stat:
            tmp_array = []
            tmp_array.append(line_stat[2])
            tmp_array.append(line_stat[1])

            if tmp_array not in self.all_distinct_players:
                self.all_distinct_players.append(tmp_array)

    def insertOnePlayer(self, id_player, name_player):
        sql = "INSERT INTO joueur (id_joueur, nom_joueur) VALUES (%s, %s)"
        val = [id_player, name_player]
        self.cursor.execute(sql, val)
        self.conn.commit()

    def importAllPlayers(self):
        for player in self.all_distinct_players:
            print(player)
            self.insertOnePlayer(player[0], player[1])



