from selenium import webdriver
from PIL import Image
import time
import schedule
import db

def screenshot(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=chrome_options, executable_path='C:/Users/joao/Documents/chromedriver.exe')
    browser.get(url)
    browser.execute_script("document.body.style.zoom='50%'")
    browser.set_window_size(1920, 1080, browser.window_handles[0])
    browser.maximize_window()
    time.sleep(5)
    browser.save_screenshot("images/screenshot.png")
    print("screenshot deu certo!")

def compress():
    image = Image.open("images/screenshot.png")
    new_image = image.resize((960,540), resample=1)
    new_image.save("images/compressed.png")
    print("foto comprimida!")

def task():
    jornal = [
        {"url":"https://g1.globo.com/", "nome":"g1"}, 
        {"url":"https://www.estadao.com.br/","nome":"estadao"}, 
        {"url":"https://www.cnnbrasil.com.br/", "nome":"cnn"}
    ]
    for j in jornal:
        screenshot(j["url"])
        compress()
        client = db.getClient()
        if client:
            db.addNoticia(client, j["nome"])
            print("noticia adicionada!")

def main():   
    schedule.every(120).minutes.do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()