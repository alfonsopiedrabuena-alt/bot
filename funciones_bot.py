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
dia = '//*[@id="edit-birth"]/div[1]/div/div/div/ul/li[14]'
mes_nac = '//*[@id="edit-birth"]/div[2]/div/div/div'
mes = '//*[@id="edit-birth"]/div[2]/div/div/div/ul/li[3]'
ano_nac = '//*[@id="edit-birth"]/div[3]/div/div/div'
ano = '//*[@id="edit-birth"]/div[3]/div/div/div/ul/li[19]'
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


driver.find_element_by_xpath(nombre).send_keys('Alfonsito')
driver.find_element_by_xpath(apellido_paterno).send_keys('Piedrabuena')
driver.find_element_by_xpath(apellido_materno).send_keys('Torrecillas')
driver.find_element_by_xpath(telefono).send_keys('5539337086')
driver.find_element_by_xpath(mail_u).send_keys('alfonso.piedrabuena@tec.mx')
driver.find_element_by_xpath(dia_nac).click()
driver.find_element_by_xpath(dia).click()
driver.find_element_by_xpath(mes_nac).click()
driver.find_element_by_xpath(mes).click()
driver.find_element_by_xpath(ano_nac).click()
driver.find_element_by_xpath(ano).click()
driver.find_element_by_xpath(campus_opt).click()
driver.find_element_by_xpath(campus).click()
driver.find_element_by_xpath(fecha_opt).click()
driver.find_element_by_xpath(fecha).click()
driver.find_element_by_xpath(area_opt).click()
driver.find_element_by_xpath(area).click()
driver.find_element_by_xpath(carrera_opt).click()
driver.find_element_by_xpath(carrera).click()
driver.find_element_by_xpath(aviso_check).click()
driver.find_element_by_xpath(submit).click()
print('fin de la ejecución')

driver.close()