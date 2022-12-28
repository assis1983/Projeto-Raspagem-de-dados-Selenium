import time
import sqlite3
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

conexao = sqlite3.connect('banco_info')
cursor = conexao.cursor()
sql = 'insert into noticias (titulo, data, descricao) values(?, ?, ?)'
navegador = Chrome(service=Service(ChromeDriverManager().install()))
navegador.get('http://raspagem.herokuapp.com/noticias/')
link = navegador.find_element(By.LINK_TEXT, 'Entretenimento')
link.click()
time.sleep(2)
for noticia in navegador.find_elements(By.CSS_SELECTOR, 'div.position-relative'):
    titulo = noticia.find_element(By.TAG_NAME, 'h3').text
    data = noticia.find_element(By.CSS_SELECTOR, 'div.text-muted').text
    descricao = noticia.find_element(By.TAG_NAME, 'p').text
    valores = [titulo, data, descricao]
    cursor.execute(sql, valores)
link = navegador.find_element(By.LINK_TEXT, 'Esportes')
link.click()
time.sleep(2)
for noticia in navegador.find_elements(By.CSS_SELECTOR, 'div.position-relative'):
    titulo = noticia.find_element(By.TAG_NAME, 'h3').text
    data = noticia.find_element(By.CSS_SELECTOR, 'div.text-muted').text
    descricao = noticia.find_element(By.TAG_NAME, 'p').text
    valores = [titulo, data, descricao]
    cursor.execute(sql, valores)
link = navegador.find_element(By.LINK_TEXT, 'Política')
link.click()
time.sleep(2)
for noticia in navegador.find_elements(By.CSS_SELECTOR, 'div.position-relative'):
    titulo = noticia.find_element(By.TAG_NAME, 'h3').text
    data = noticia.find_element(By.CSS_SELECTOR, 'div.text-muted').text
    descricao = noticia.find_element(By.TAG_NAME, 'p').text
    valores = [titulo, data, descricao]
    cursor.execute(sql, valores)
navegador.close
conexao.commit()
conexao.close