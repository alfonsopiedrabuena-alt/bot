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
        print (x.status_code)
        if x.status_code == 200:
            driver.get(links)
            print(links, x.status_code)
            #print (f'la liga: {links} esta funcionando correctamente')
            continue
            return 200, links
        elif x.status_code == 404:
            continue
            return 404, links
        elif x.status_code == 301:
            driver.get(links)
            return 300
        else:
            print('Existe un error')

if __name__ == '__main__':
    run()


