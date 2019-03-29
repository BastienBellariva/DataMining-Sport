from Import_Data import ConnectDB as ConnectDBFile


conn = ConnectDBFile.ConnectDB.getInstance()
cursor = conn.cursor()

team = ".031"


print(float(team))
