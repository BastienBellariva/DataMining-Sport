from Import_Data import ImportPlayers, ImportSeasons


obj_import_season = ImportSeasons.ImportSeasons()
obj_import_season.importAllSeasons()

obj_import_players = ImportPlayers.ImportPlayers()
obj_import_players.scrollFilesForPlayers()
obj_import_players.importAllPlayers()


