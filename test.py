import gspread
import WarRoster
from oauth2client.service_account import ServiceAccountCredentials
 
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
 
# Find a workbook by name and open the sheet specified
gs = client.open("WARrTest").worksheet("SDFRoosterMI")
 
rosterData = gs.get_all_records()
matrix = WarRoster.rosterMatrix()


for row in rosterData:

    #generate a champ obj from data
    tChamp = WarRoster.champ(row["USER"], row["DATA"])
    #aRoster.addChamp(tChamp)
    matrix.addChamp(tChamp)


#print (matrix.champs.champ)
#print (matrix.users.user)

print (sorted(matrix.champs.champ["Abomination"]))
