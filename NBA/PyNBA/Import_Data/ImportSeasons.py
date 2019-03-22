from Import_Data import ConnectDB as ConnectDBFile


class ImportSeasons:

    seasons = ['2008-2009',
               '2009-2010',
               '2010-2011',
               '2011-2012',
               '2012-2013',
               '2013-2014',
               '2014-2015',
               '2015-2016',
               '2016-2017',
               '2017-2018',
               '2018-2019']

    def __init__(self):
        self.conn = ConnectDBFile.ConnectDB.getInstance()
        print(self.conn)
        self.cursor = self.conn.cursor()

    def insertOneSeason(self, saison):
        sql = "INSERT INTO saison (annee_saison) VALUES (%s)"
        val = [saison]
        self.cursor.execute(sql, val)
        self.conn.commit()

    def importAllSeasons(self):
        for season in self.seasons:
            self.insertOneSeason(season)
