from selenium import webdriver

PATH = '/Applications/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://tec.mx/es/ambiente-construido')
print(driver.title)
#driver.close()

nombre = '//*[@id="edit-nombre"]'
apellido_paterno = '//*[@id="edit-apellido-paterno"]'
apellido_materno = '//*[@id="edit-apellido-materno"]'
telefono = '//*[@id="edit-telefono"]'
mail_u = '//*[@id="edit-correo"]'
dia_nac = '/html/body/div[1]/div/div[2]/div/div/article/div[2]/div/div[12]/div/div/div[2]/div[2]/form/fieldset/div[2]/fieldset[1]/fieldset[1]/div[1]/div'
#mes_nac = 
#ano_nac = 

driver.find_element_by_xpath(nombre).send_keys('Alfonsito')
driver.find_element_by_xpath(apellido_paterno).send_keys('Piedrabuena')
driver.find_element_by_xpath(apellido_materno).send_keys('Torrecillas')
driver.find_element_by_xpath(telefono).send_keys('5539337086')
driver.find_element_by_xpath(mail_u).send_keys('alfonso.piedrabuena@tec.mx')
driver.find_element_by_xpath(dia_nac).click()

print(f'Hola {nombre}{apellido_paterno} tu teléfono es:{telefono}')

time.sleep(5)

driver.close()