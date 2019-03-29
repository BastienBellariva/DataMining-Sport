from Import_Data import ImportPlayers, ImportSeasons, ImportTeams, ImportMatchStat, ImportTeamStat


obj_import_season = ImportSeasons.ImportSeasons()
obj_import_season.importAllSeasons()

obj_import_players = ImportPlayers.ImportPlayers()
obj_import_players.scrollFilesForPlayers()
obj_import_players.importAllPlayers()

obj_import_teams = ImportTeams.ImportTeams()
obj_import_teams.scrollFilesForTeams()
obj_import_teams.importAllTeams()

obj_import_match = ImportMatchStat.ImportMatchStat()
obj_import_match.scrollFilesForMatchStatAndImport()

obj_import_team_stat = ImportTeamStat.ImportTeamStat()
obj_import_team_stat.scrollFilesForTeamStatAndImport()



