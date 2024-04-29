import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By  #para hacer el control del bots By es para hacer una busqueda
from selenium.webdriver.chrome.service import Service  #Es para conectarme
from selenium.webdriver.chrome.options import Options #es para seleccionar

#SOLO LOS DE WEBDRIVERMANAGER

from webdriver_manager.chrome import ChromeDriverManager

def bot_login():
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--Window-size=1020,1200")
    navegador = webdriver.Chrome(service=s, options=options)
    navegador.get("https://www.airbnb.mx/")
    time.sleep(15)

    titulos=navegador.find_elements(By.XPATH, '//div[@data-testid="listing-card-title"]')
    dire=navegador.find_elements(By.XPATH,'//div[@data-testid="listing-card-subtitle"]')
    fec=navegador.find_elements(By.XPATH,'//div[@data-testid="listing-card-subtitle"]')
    pre=navegador.find_elements(By.XPATH,'//div[@data-testid="price-availability-row"]')
    cal=navegador.find_elements(By.XPATH,'//span[@class="r4a59j5 atm_h_1h6ojuz atm_9s_1txwivl atm_7l_jt7fhx atm_84_evh4rp dir dir-ltr"]')


    all_info={
        "titulo/":[],
        "Direccion/":[],
        "Fecha/":[],
        "precio/":[],
        "Calificacion/":[]

    }


    for titulos in titulos:
        all_info["titulo/"].append(titulos.text)
        print(titulos.text)
    for dirreccion in dire:
        all_info["Direccion/"].append(dirreccion.text)
        print(dirreccion.text)
    for fecha in fec:
        all_info["Fecha/"].append(fecha.text)
        print(fecha.text)

    for precio in pre:
        all_info["precio/"].append(precio.text)
        print(precio.text)

    for cali in cal:
        all_info["Calificacion/"].append(cali.text)
        print(cali.text)

    if not cali:
        all_info["Calificacion/"].append("Calificación promedio: 0.0 de 5")



    df = pd.DataFrame(all_info)
    print(df)
    df.to_csv("DataSet/airbnb.csv")



if __name__ == "__main__":
    bot_login()