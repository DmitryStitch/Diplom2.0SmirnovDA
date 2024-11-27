import sqlite3
from Diplom_bot.Price import *
from Diplom_bot.text import *
from Diplom_bot.Image import *

connection = sqlite3.connect("magazin.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Sklad(
id INTEGER PRIMARY KEY,
Product TEXT NOT NULL,
Opisanie TEXT ,
Price INTEGER ,
Image TEXT

)
''')

cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelNBot, NBotinki, priceNBot, "Imeges/Bot_New.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelNKr, NKreplen, priceNKr, "Imeges/Kr_New.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelNSnow, NSnoubord, priceNKr, "Imeges/Snow_New.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelMBot_Park, MBot_Park, priceMBot_Park, "Imeges/Bot_Med_Univ.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelMKr_Park, MKr_Park, priceMKr_Park, "Imeges/Kr_Med_Univ.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelMSnow_Park, MSnow_Park, priceMSnow_Park, "Imeges/Snow_Med_Univ.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelMBot_Freestyle, MBot_Freestyle, priceMBot_Freestyle, "Imeges/Bot_Med_Freestyle.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelMKr_Freestyle, MKr_Freestyle, priceMKr_Freestyle, "Imeges/Kr_Med_Freestyle.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelMSnow_Freestyle, MSnow_Freestyle, priceMSnow_Freestyle, "Imeges/Snow_Med_Freestyle.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelMBot_Freeride, MBot_Freeride , priceMBot_Freeride, "Imeges/Bot_Med_Freeride.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelMKr_Freeride, MKr_Freeride, priceMKr_Freeride, "Imeges/Kr_Med_Freeride.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelMSnow_Freeride, MSnow_Freeride, priceMSnow_Freeride, "Imeges/Snow_Med_Freeride.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelProBot_Park, ProBot_Park, priceProBot_Park, "Imeges/Bot_Pro_Uni.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelProKr_Park, ProKr_Park, priceProKr_Park, "Imeges/Krep_Pro_Uni.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelProSnow_Park, ProSnow_Park, priceProSnow_Park, "Imeges/Snow_Pro_Uni.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelProBot_Freestyle, ProBot_Freestyle, priceProBot_Freestyle, "Imeges/Bot_pro_freestyle.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelProKr_Freestyle, ProKr_Freestyle, priceProKr_Freestyle, "Imeges/Krep_Pro_Freestyle.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelProSnow_Freestyle, ProSnow_Freestyle, priceProSnow_Freestyle, "Imeges/Snow_Pro_Freestyle.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelProBot_Freeride, ProBot_Freeride, priceProBot_Freeride, "Imeges/Bot_Pro_Freeride.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelProKr_Freeride, ProKr_Freeride, priceProKr_Freeride, "Imeges/Krep_Pro_Freeride.jpg"))
cursor.execute(" INSERT INTO Sklad (product, opisanie, price, Image) VALUES (?, ?, ?, ?)",(ModelProSnow_Freeride, ProSnow_Freeride, priceProSnow_Freeride, "Imeges/Snow_Pro_Freeride.jpg"))

# def get_product(sklad_file = "magazin.db"):
#     connection = sqlite3.connect(sklad_file)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM Sklad")
#     sklad = cursor.fetchall()
#     conn.close
    
def get_product(product_name):
    connection = sqlite3.connect('magazin.db')
    cursor = connection.cursor()
    cursor.execute("SELECT opisanie, price, image FROM Sklad WHERE product = ?", (product_name,))
    result = cursor.fetchone()
    connection.close()
    if result:
        opisanie, price, image_path = result
        return {'name': product_name, 'opisanie': opisanie, 'price': price, 'image_path': image_path}

connection.commit()
connection.close()