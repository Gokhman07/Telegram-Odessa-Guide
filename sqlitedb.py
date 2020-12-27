#from pymongo import  MongoClient
#from settings import  MONGO_DB, MONGODB_LINK
import re
import sqlite3
import emoji
def give_emoji_free_text(text):
    allchars = [str for str in text.decode('utf-8')]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text



#mdb=MongoClient(MONGODB_LINK)[MONGO_DB] #переменная для работы с базой данных MongoDB#
#cursor=conn.cursor()
#def search_place(mdb,name):
 #   place=mdb.CLUBS.find_one({"NAME":name})# поиск в коллекции clubs
  #  print(name)
   # return  place


#                                def fill_keyboard(mdb)
def search_place(name):
    
    conn=sqlite3.connect("ODESSAPLACES.db")
    cursor=conn.cursor()
    #print(cursor)
    sql_place = f"SELECT * FROM PLACES WHERE title='{name}'"
    print(sql_place)
    cursor.execute(sql_place)
    #print(cursor)
    result=cursor.fetchone()
    print(result)
    return result

def build_keyboard(title):
 
    types={'Клубы 🍹🍸':'CLUB','ТРЦ  🛍🛒':"MALL","Отели  🏩🛎":"HOTEL","Рестораны 🍷☕":"CAFE",'Религиозные места ☮':"CULT"}
    print(types['Клубы 🍹🍸'])
    conn=sqlite3.connect("ODESSAPLACES.db")
 
    cursor=conn.cursor()

    sql = f"SELECT title FROM PLACES JOIN PLACES_TYPE ON(PLACES.type_id=PLACES_TYPE.id) WHERE PLACES_TYPE.name='{types[title]}'"
    print(sql)
    cursor.execute(sql)
    
    sql_results= cursor.fetchall()
    
    result=sql_results
 
        
    
   
   
    print(result)
    return result