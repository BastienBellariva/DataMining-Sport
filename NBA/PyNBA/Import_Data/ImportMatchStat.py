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

