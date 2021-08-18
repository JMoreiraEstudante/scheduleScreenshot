from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime
import io
from PIL import Image

load_dotenv()

def getClient():
    try: 
        client = MongoClient("mongodb+srv://"+os.getenv('DB_USER')+":"+os.getenv('DB_PASSWORD')+"@clusterestudos.neryf.mongodb.net/Estudos?retryWrites=true&w=majority")
        print("Conectado com o banco!")
        return client
    except:
        print("Não foi possível conectar com o banco")
        return False

def addNoticia(client, jornal):
    db = client.Noticias
    screenshot = db.screenshot
    image = Image.open("images/screenshot.png")
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')

    screenshotDocument = {
        "jornal" : jornal,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 
        "imagem": image_bytes.getvalue()
    }
    screenshot.insert_one(screenshotDocument)

def main():   
    client = getClient()
    if client:
        addNoticia(client)

if __name__ == "__main__":
    main()

#read the document image
'''from bson.binary import Binary
import matplotlib.pyplot as plt

image = screenshot.find_one()

pil_img = Image.open(io.BytesIO(image['imagem']))
plt.imshow(pil_img)
plt.show()'''