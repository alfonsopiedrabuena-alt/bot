import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import requests

#datosdeselenium
PATH = '/Applications/chromedriver'
driver = webdriver.Chrome(PATH)

#datosdegoogle
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive',
    ]
creds = ServiceAccountCredentials.from_json_keyfile_name('bot-final-064b84841ced.json', scope)
client=gspread.authorize(creds)

def run():
    sitios_areas()
    driver.quit()
    print ('Terminó')

def sitios_areas():
    sheet = client.open('BD para BOT').sheet1
    data = sheet.col_values(2)
    for links in data:
        x = requests.get(links)
        #r = requests.status_code
        if x.status_code == 200:
            driver.get(links)
            print (f'la liga: {links} esta funcionando correctamente')
            continue
        else:
            pass
            return "fallaste"
        

if __name__ == '__main__':
    run()


