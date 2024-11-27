from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from database import database_connection
from datetime import datetime, date
import pyautogui as tempo_carregamento



service = Service(r"C:\Windows\System32\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\chrome-win64\chrome.exe"
options.add_argument(r"user-data-dir=C:\whatappcache")
options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(service=service, options=options)
nome_grupo = "Financeiro neno e nena"
lista_dict = []
connection, cursor = database_connection()

# Acessar o WhatsApp Webs
driver.get("https://web.whatsapp.com")




try:
    elemento_caixa_busca = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[3]/div/div[1]/div/div[2]/div[2]/div/div/p'))
    )
    elemento_caixa_busca.send_keys(nome_grupo)
    
    tempo_carregamento.sleep(5)
    
    elemento_grupo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[3]/div/div[3]/div[1]/div/div/div[1]/div/div/div/div[2]'))
    )
    
    elemento_grupo.click()
    
    #Até o momento consegui apenas acessar o grupo
    elemento_chat = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[4]/div/div[3]/div/div[2]/div[2]/div[2]/div/div'))
    )
    
    container_mensagens = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div[4]/div/div[3]/div/div[2]/div[2]'))
    )
    
    #Váriável que recebe lista de WebElements do container de mensagens do whatsapp
    mensagens = container_mensagens.find_elements(By.XPATH, ".//div[@role='row']")
    lista_texto = [row.text.split('\n') for row in mensagens]
    
    
    def verifica_ultima_coleta(cursor):           
        try:
            query = "SELECT TOP 1 ID_COLETA FROM TB_MENSAGENS_COLETADAS ORDER BY ID_COLETA DESC"
            cursor.execute(query)
        except (ValueError, TypeError) as error:
            print(f"{e}")
        
        retono_query = cursor.fetchone()
        return retono_query[0] if retono_query else 0
     
    # Processar cada sublista
    for sublista in lista_texto:
        # Verificar se a sublista tem exatamente 10 elementos
        if len(sublista) == 10:
            # Criar o dicionário para a sublista atual
            dados = {
                'ID mensagem': sublista[0],
                'Data compra': sublista[1],
                'Valor': sublista[2],
                'Desc': sublista[3],
                'Local': sublista[4],
                'Forma': sublista[5],
                'Parcelamento': sublista[6],
                'QTD': sublista[7],
                'Categoria': sublista[8],
                'Hora': sublista[9]
            }
            # Adicionar o dicionário à lista principal
            lista_dict.append(dados)

    id_ultima_coleta = verifica_ultima_coleta(cursor=cursor)
    for dicionarios in lista_dict:
   
        data_reg = date.today()
        
        data_compra_conv = datetime.strptime(dicionarios['Data compra'].strip(), "%d/%m/%Y").strftime("%Y-%m-%d")
        id_mensagem= int(dicionarios['ID mensagem'])
        
        
        
        if connection and cursor and id_mensagem > id_ultima_coleta:
            print(f"ID ÚLTIMA COLETA: {id_ultima_coleta}, ID MENSAGEM ATUAL: {id_mensagem}")
            categoria_map = {
            'ALIMENTAÇÃO': 100,
            'MORADIA': 200,
            'TRANSPORTE': 300,
            'SAÚDE': 400,
            'LAZER E ENTRETERIMENTO': 500,
            'COMPRAS': 600,
            'GASTOS OCASIONAIS': 700,
            'INVESTIMENTOS E APLICAÇÕES': 800,
            'PAGAMENTO FATURA': 900,
            'EDUCAÇÃO': 1000,
            'OUTROS': 1100
            }
            forma_pagamento_map = {
            'CARTÃO DE CRÉDITO': 100,
            'CARTÃO DE DÉBITO': 200,
            'DINHEIRO': 300,
            'PIX': 400,
            'SALDO DA CONTA': 500
            }
            
            
            cursor.execute(
                'INSERT INTO TB_MENSAGENS_COLETADAS (ID_COLETA, DATA_COLETA, DATA_GASTO, DESCRICAO) VALUES (?, ?, ?, ?)',
                (
                id_mensagem,
                data_reg, 
                data_compra_conv,                  
                dicionarios['Desc'].strip(), 
                )
            )
            
            
            cursor.execute(
                'INSERT INTO TB_REG_FINANC (DATA_REGISTRO, DATA_GASTO, VALOR, DESCRICAO, LOCAL_GASTO, PARCELAMENTO, N_PARCELAS, IDCATEGORIA, IDFORMA_PAGAMENTO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (data_reg, 
                 data_compra_conv, 
                 dicionarios['Valor'].strip(), 
                 dicionarios['Desc'].strip(), 
                 dicionarios['Local'].strip(), 
                 dicionarios['Parcelamento'].strip(),
                 dicionarios['QTD'].strip(),
                 categoria_map.get(dicionarios['Categoria'].strip().upper(), None),
                 forma_pagamento_map.get(dicionarios['Forma'].strip().upper(), None))
            )
            
        else:
            print(f"Não há mensagens a serem coletadas! Ultima coleta realizada ID: {id_ultima_coleta}")
            
    connection.commit()
    connection.close()
    
except Exception as e:
    print(f"Erro ao localizar o elemento: {e}")
finally:
    driver.quit()
    


