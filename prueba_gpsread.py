import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive',
    ]

creds = ServiceAccountCredentials.from_json_keyfile_name('bot-final-064b84841ced.json', scope)
client=gspread.authorize(creds)

sheet = client.open('BD para BOT').sheet1
data = sheet.col_values(7)
for links in data:
    print(links)
#print(data)
