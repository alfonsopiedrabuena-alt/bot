from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import gspread
from oauth2client.service_account import ServiceAccountCredentials

PATH = '/Applications/chromedriver'
driver = webdriver.Chrome(PATH)

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
    sheet = client.open('BD para BOT')
    #la siguiente linea de código sirve para revisar que hoja estaré jalando. Esto debería de ser una variable a llenar de acuerdo la necesidad, incluso un parámetro.
    worksheet = sheet.get_worksheet(1)
    data = worksheet.col_values(2)
    for links in data:
        driver.get(links)
        accion_bot(links)
        print(links)

def  accion_bot(ligas):
    nombre = '//*[@id="edit-nombre"]'
    apellido_paterno = '//*[@id="edit-apellido-paterno"]'
    apellido_materno = '//*[@id="edit-apellido-materno"]'
    telefono = '//*[@id="edit-telefono"]'
    mail_u = '//*[@id="edit-correo"]'
    dia_nac = '//*[@id="edit-birth"]/div[1]/div/div/div'
    dia = '//*[@id="edit-birth"]/div[1]/div/div/div/ul/li[2]'
    mes_nac = '//*[@id="edit-birth"]/div[2]/div/div/div'
    mes = '//*[@id="edit-birth"]/div[2]/div/div/div/ul/li[2]'
    ano_nac = '//*[@id="edit-birth"]/div[3]/div/div/div'
    ano = '//*[@id="edit-birth"]/div[3]/div/div/div/ul/li[2]'
    campus_opt = '//*[@id="edit-block-3"]/div[1]/div/div'
    campus = '//*[@id="edit-block-3"]/div[1]/div/div/ul/li[5]'
    fecha_opt = '//*[@id="edit-block-3"]/div[2]/div/div'
    fecha = '//*[@id="edit-block-3"]/div[2]/div/div/ul/li[3]'
    area_opt = '//*[@id="edit-block-3"]/div[3]/div/div'
    area = '//*[@id="edit-block-3"]/div[3]/div/div/ul/li[5]'
    carrera_opt = '//*[@id="edit-block-3"]/div[4]/div/div'
    carrera = '//*[@id="edit-block-3"]/div[4]/div/div/ul/li[2]'
    aviso_check = '//*[@id="edit-copy"]'
    aviso = '//*[@id="edit-copy"]'
    submit = '//*[@id="edit-submit"]'
    driver.find_element_by_xpath(nombre).send_keys('Alfonso')
    driver.find_element_by_xpath(apellido_paterno).send_keys('Piedrabuena')
    driver.find_element_by_xpath(apellido_materno).send_keys('Torrecillas')
    driver.find_element_by_xpath(telefono).send_keys('5539337086')
    driver.find_element_by_xpath(mail_u).send_keys('alfonso.piedrabuena@tec.mx')

    x = 1
    y = 1

    try:
        lista = [dia_nac,dia,mes_nac,mes,ano_nac,ano,campus_opt,campus,fecha_opt,fecha,area_opt,area,carrera_opt,carrera,aviso_check,submit]
        for elementos in lista:
            driver.find_element_by_xpath(elementos).click()
        print('ejecución correcta')
        return x
    except:
        print(f'El error sucedió en: '+ ligas)
        return y


if __name__ == '__main__':
    run()