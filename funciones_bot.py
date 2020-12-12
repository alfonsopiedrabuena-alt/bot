from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import gspread
from oauth2client.service_account import ServiceAccountCredentials

PATH = '/Applications/chromedriver'
driver = webdriver.Chrome(PATH)

def run():
    sitios_areas()
    driver.quit()
    print ('Terminó')


def sitios_areas():

    sitios = {
        'Ambiente Construido':'https://tec.mx/es/ambiente-construido',
        'Ciencias Sociales':'https://tec.mx/es/ciencias-sociales',
        'Negocios':'https://tec.mx/es/negocios',
        'Estudios Creativos':'https://tec.mx/es/estudios-creativos',
        'Salud':'https://tec.mx/es/salud',
        'Ingeniería-Innovación y Transformación':'https://tec.mx/es/innovacion-y-transformacion',
        'Ingeniería-Computación y Tecnologías de Información':'https://tec.mx/es/computacion-y-tecnologias-de-informacion',
        'Ingeniería-Bioingeniería y Procesos Químicos':'https://tec.mx/es/bioingenieria-y-procesos-quimicos',
        'Ingeniería-Ciencias Aplicadas':'https://tec.mx/es/ciencias-aplicadas'
    }

    for ligas in sitios.values():
        driver.get(ligas)
        accion_bot(ligas)
        print(driver.title)
    
    return ligas

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