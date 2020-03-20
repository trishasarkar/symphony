import sqlite3

c = sqlite3.connect("emotionplayer.db")
cr=c.cursor()

def create():
    cr.execute("CREATE TABLE if not exists song(s_id INTEGER PRIMARY KEY,s_name TEXT,s_lang TEXT )")
    cr.execute("CREATE TABLE if not exists emotion(e_id INTEGER PRIMARY KEY,e_name TEXT )")
    cr.execute("CREATE TABLE if not exists album(al_id INTEGER PRIMARY KEY,al_name TEXT )")
    cr.execute("CREATE TABLE if not exists artist(art_id INTEGER PRIMARY KEY,art_name TEXT )")
    cr.execute("CREATE TABLE if not exists songart(s_id INTEGER , art_id INTEGER )")
    cr.execute("CREATE TABLE if not exists songalb(s_id INTEGER , al_id INTEGER )")
    cr.execute("CREATE TABLE if not exists songemo(s_id INTEGER , e_id INTEGER )")
    c.commit()
    cr.close()
    c.close()
#create()
