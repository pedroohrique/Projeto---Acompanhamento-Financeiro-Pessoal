from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pyautogui as tempo_carregamento

# Configuração do driver
service = Service(r"C:\Windows\System32\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\chrome-win64\chrome.exe"
options.add_argument(r"user-data-dir=C:\whatappcache")
options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(service=service, options=options)
nome_grupo = "Financeiro neno e nena"

# Acessar o WhatsApp Web
driver.get("https://web.whatsapp.com")


#
# Aguardar até que o elemento esteja presente
try:
    elemento = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/p'))
    )
    elemento.send_keys(nome_grupo)
    acessar_grupo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/span/span'))
    )
    acessar_grupo.send_keys(Keys.ENTER)
    print("Por favor, escaneie o QR code do WhatsApp Web. O cache será salvo para próximas execuções.")
    

# O navegador permanece aberto para você verificar o funcionamento
    input("Pressione Enter após verificar o funcionamento e escanear o QR code.")
    
except Exception as e:
    print(f"Erro ao localizar o elemento: {e}")
finally:
    driver.quit()
    
    # Aguarde para escanear o QR code na primeira vez
