from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

PATH = '/Applications/chromedriver'
driver = webdriver.Chrome(PATH)

def run():
    sitios_areas()
    driver.quit()
    print ('Terminó')


def sitios_areas():

    sitios = {
        "PrepaTec Aguascalientes":"https://admision.tec.mx/sesiones-informativas-prepatec/aguascalientes/refer/gon/cm/0043232/",
        "PrepaTec Estado de México":"https://admision.tec.mx/sesiones-informativas-prepatec/cdmx/refer/gon/cm/0043232/",
        "PrepaTec Santa fe":"https://admision.tec.mx/sesiones-informativas-prepatec/cdmx/refer/gon/cm/0043232/",
        "PrepaTec Ciudad de méxico":"https://admision.tec.mx/sesiones-informativas-prepatec/cdmx/refer/gon/cm/0043232/",
        "PrepaTec Esmeralda":"https://admision.tec.mx/sesiones-informativas-prepatec/cdmx/refer/gon/cm/0043232/",
        "PrepaTec Celaya":"https://admision.tec.mx/sesiones-informativas-prepatec/celaya/refer/gon/cm/0043232/",
        "PrepaTec Chiapas":"https://admision.tec.mx/sesiones-informativas-prepatec/chiapas/refer/gon/cm/0043232/",
        "PrepaTec Chihuahua":"https://admision.tec.mx/sesiones-informativas-prepatec/chihuahua/refer/gon/cm/0043232/",
        "PrepaTec Ciudad Juárez":"https://admision.tec.mx/sesiones-informativas-prepatec/juarez/refer/gon/cm/0043232/",
        "PrepaTec Ciudad Obregón":"https://admision.tec.mx/sesiones-informativas-prepatec/obregon/refer/gon/cm/0043232/",
        "PrepaTec Colima":"https://admision.tec.mx/sesiones-informativas-prepatec/colima/refer/gon/cm/0043232/",
        "PrepaTec Cuernavaca":"https://admision.tec.mx/sesiones-informativas-prepatec/cuernavaca/refer/gon/cm/0043232/",
        "PrepaTec Guadalajara":"https://admision.tec.mx/sesiones-informativas-prepatec/guadalajara/refer/gon/cm/0043232/",
        "PrepaTec Hidalgo":"https://admision.tec.mx/sesiones-informativas-prepatec/hidalgo/refer/gon/cm/0043232/",
        "PrepaTec Irapuato":"https://admision.tec.mx/sesiones-informativas-prepatec/irapuato/refer/gon/cm/0043232/",
        "PrepaTec Laguna":"https://admision.tec.mx/sesiones-informativas-prepatec/laguna/refer/gon/cm/0043232/",
        "PrepaTec León":"https://admision.tec.mx/sesiones-informativas-prepatec/leon/refer/gon/cm/0043232/",
        "PrepaTec Morelia":"https://admision.tec.mx/sesiones-informativas-prepatec/morelia/refer/gon/cm/0043232/",
        "PrepaTec Navojoa":"https://admision.tec.mx/sesiones-informativas-prepatec/navojoa/refer/gon/cm/0043232/",
        "PrepaTec Puebla":"https://admision.tec.mx/sesiones-informativas-prepatec/puebla/refer/gon/cm/0043232/",
        "PrepaTec Querétaro":"https://admision.tec.mx/sesiones-informativas-prepatec/queretaro/refer/gon/cm/0043232/",
        "PrepaTec Saltillo":"https://admision.tec.mx/sesiones-informativas-prepatec/saltillo/refer/gon/cm/0043232/",
        "PrepaTec San Luis Potosí":"https://admision.tec.mx/sesiones-informativas-prepatec/sanluis/refer/gon/cm/0043232/",
        "PrepaTec Sinaloa":"https://admision.tec.mx/sesiones-informativas-prepatec/sinaloa/refer/gon/cm/0043232/",
        "PrepaTec Sonora Norte":"https://admision.tec.mx/sesiones-informativas-prepatec/sonoranorte/refer/gon/cm/0043232/",
        "PrepaTec Tampico":"https://admision.tec.mx/sesiones-informativas-prepatec/tampico/refer/gon/cm/0043232/",
        "PrepaTec Toluca":"https://admision.tec.mx/sesiones-informativas-prepatec/toluca/refer/gon/cm/0043232/",
        "PrepaTec Zacatecas":"https://admision.tec.mx/sesiones-informativas-prepatec/zacatecas/refer/gon/cm/0043232/",
        "PrepaTec Metepec":"https://admision.tec.mx/sesiones-informativas-prepatec/toluca/refer/gon/cm/0043232/",
        "PrepaTec Santa Anita ":"https://admision.tec.mx/sesiones-informativas-prepatec/santa-anita/refer/gon/cm/0043232/",
        "PrepaTec Cumbres":"https://admision.tec.mx/sesiones-informativas-prepatec/monterrey/refer/gon/cm/0043232/",
        "PrepaTec Eugenio Garza Lagüera":"https://admision.tec.mx/sesiones-informativas-prepatec/monterrey/refer/gon/cm/0043232/",
        "PrepaTec Eugenio Garza Sada":"https://admision.tec.mx/sesiones-informativas-prepatec/monterrey/refer/gon/cm/0043232/",
        "PrepaTec Santa Catarina":"https://admision.tec.mx/sesiones-informativas-prepatec/monterrey/refer/gon/cm/0043232/",
        "PrepaTec Valle Alto":"https://admision.tec.mx/sesiones-informativas-prepatec/monterrey/refer/gon/cm/0043232/",

    }

    for ligas in sitios.values():
        driver.get(ligas)
        print(driver.title)
    
    return ligas




if __name__ == '__main__':
    run()