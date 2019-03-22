import mysql.connector


class ConnectDB:

    __instance = None
    _user = "bastien"
    _password = "root"
    _host = "10.211.55.5"
    _database = "d_nba"

    @staticmethod
    def getInstance():
        if ConnectDB.__instance is None:
            ConnectDB()
        return ConnectDB.__instance

    def __init__(self):
        if ConnectDB.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            try:
                ConnectDB.__instance = mysql.connector.connect(user=self._user, password=self._password,
                                                               host=self._host,
                                                               database=self._database)
            except:
               print("Erreur de connexion BDD")
