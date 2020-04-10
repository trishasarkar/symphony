from tkinter import *
import sqlite3
import pygame
import re

connect = sqlite3.connect('emotionplayer.db')
cursor = connect.cursor()
global index
index = 0


class main:
    global jo, jo1, jo2, jo3,index
    jo = []
    jo1 = []
    jo2 = []
    jo3 = []


    def __init__(self):
        self.fpage()

    #################
    #Basic Player Functions

    def updatelabel(self):
        global index
        global songname
        va.set(jo3[index])

    def play(self):
        pygame.mixer.music.unpause()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        global index
        if (index == len(jo1) - 1):
            index = 0
        else:
            index += 1
        pygame.mixer.music.load(jo1[index])
        pygame.mixer.music.play()
        self.updatelabel()

    def prev(self):
        global index
        if (index == 0):
            index = len(jo1) - 1
        index -= 1
        pygame.mixer.music.load(jo1[index])
        pygame.mixer.music.play()
        self.updatelabel()

    #################

    def ars(self):
        # Arijit Singh_Player

        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute(
            "Select * from song so left outer join songart s on s.s_id=so.s_id left outer join artist a on a.art_id = s.art_id where art_name='Arijit Singh'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player1()

    def sn(self):
        # Sonu Nigam_Player

        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute(
            "Select * from song so left outer join songart s on s.s_id=so.s_id left outer join artist a on a.art_id = s.art_id where art_name='Vishal Dadlani'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player1()


    def mc(self):
        # Mohit Chauhan_Player

        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute(
            "Select * from song so left outer join songart s on s.s_id=so.s_id left outer join artist a on a.art_id = s.art_id where art_name='Mohit Chauhan'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player1()

    def sg(self):
        # Sheya Ghoshal_Player

        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute(
            "Select * from song so left outer join songart s on s.s_id=so.s_id left outer join artist a on a.art_id = s.art_id where art_name='Shreya Ghoshal'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player1()

    ##################

    def player1(self):
        # artist player

        global b
        global va
        a.destroy()
        b = Tk()
        b.title("                             MUSIC PLAYER")
        b.geometry('428x446')
        r = PhotoImage(file=r"background.png")
        l1 = Label(b, image=r)
        l1.place(x=0, y=0)

        li = Listbox(b, width=32, height=12)
        jo2.reverse()
        for c in jo2:
            li.insert(0, c)
        va = StringVar()
        songlabel = Label(b, textvariable=va, width=35)
        self.updatelabel()
        c1 = Button(b, text="pause", font='Courier 16 bold', bg='white', fg='red', width=8, bd=1, relief='ridge',
                    height=2, command=self.pause)
        c2 = Button(b, text="play", font='Courier 16 bold', bg='white', fg='palevioletred2', width=8, bd=1,
                    relief='ridge', height=2, command=self.play)
        c3 = Button(b, text="stop", font='Courier 16 bold', bg='white', fg='green', width=8, bd=1, relief='ridge',
                    height=2, command=self.stop)
        c4 = Button(b, text="previous", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2, command=self.prev)
        c6 = Button(b, text="next", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2, command=self.next)

        c5 = Button(b, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1, relief='ridge',
                    height=1, command=self.artist_back)

        songlabel.place(x=40, y=40)
        li.place(x=100, y=75)
        c5.place(x=10, y=10)
        c1.place(x=170, y=300)
        c2.place(x=50, y=300)
        c3.place(x=130, y=370)
        c4.place(x=10, y=370)
        c6.place(x=250, y=370)
        c2.bind('<Button-1>')
        c1.bind('<Button-1>')
        c3.bind('<Button-1>')
        c4.bind('<Button-1>')
        c5.bind('<Button-1>')
        pygame.mixer.music.play()
        b.mainloop()

    def art_list(self):
        # t.destroy()
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"background.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)

        a.resizable(False, False)
        c1 = Button(a, text="ARIJIT SINGH", font='Courier 16 bold', bg='white', fg='red', width=17, bd=1,
                    relief='ridge', height=2,
                    command=self.ars)
        c2 = Button(a, text="VISHAL DADLANI", font='Courier 16 bold', bg='white', fg='palevioletred2', width=17, bd=1,
                    relief='ridge', height=2,
                    command=self.sn)
        c3 = Button(a, text="MOHIT CHAUHAN", font='Courier 16 bold', bg='white', fg='green', width=17, bd=1,
                    relief='ridge', height=2,
                    command=self.mc)
        c4 = Button(a, text="SHREYA GHOSHAL", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=17, bd=1,
                    relief='ridge', height=2,
                    command=self.sg)

        c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=12, bd=1, relief='ridge',
                    height=1,
                    command=self.go_back)

        c5.place(x=10, y=10)

        c1.place(x=10, y=110)
        c2.place(x=10, y=190)
        c3.place(x=10, y=270)
        c4.place(x=10, y=360)
        a.mainloop()

    def artist_back(self):
        self.stop()
        b.destroy()
        self.art_list()

    def art_call(self):
        t.destroy()
        self.art_list()

    ####################################

    def hindi(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song where s_lang='hindi'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player2()

    def eng(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song where s_lang='english'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player2()
    def spa(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song where s_lang='spanish'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player2()


    def pun(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song where s_lang='punjabi'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player2()


    def player2(self):
        # language player
        global b
        global va
        a.destroy()
        b = Tk()
        b.title("                             MUSIC PLAYER")
        b.geometry('428x446')
        r = PhotoImage(file=r"background.png")
        l1 = Label(b, image=r)
        l1.place(x=0, y=0)

        li = Listbox(b, width=32, height=12)
        jo2.reverse()
        for c in jo2:
            li.insert(0, c)
        va = StringVar()
        songlabel = Label(b, textvariable=va, width=35)
        self.updatelabel()

        c1 = Button(b, text="pause", font='Courier 16 bold', bg='white', fg='red', width=8, bd=1, relief='ridge',
                    height=2,command=self.pause)
        c2 = Button(b, text="play", font='Courier 16 bold', bg='white', fg='palevioletred2', width=8, bd=1,
                    relief='ridge', height=2,command=self.play)
        c3 = Button(b, text="stop", font='Courier 16 bold', bg='white', fg='green', width=8, bd=1, relief='ridge',
                    height=2,command=self.stop)
        c4 = Button(b, text="previous", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2,command=self.prev)
        c6 = Button(b, text="next", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2,command=self.next)

        c5 = Button(b, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1, relief='ridge',
                    height=1, command=self.language_back)

        songlabel.place(x=40, y=40)
        li.place(x=100, y=75)
        c5.place(x=10, y=10)
        c1.place(x=170, y=300)
        c2.place(x=50, y=300)
        c3.place(x=130, y=370)
        c4.place(x=10, y=370)
        c6.place(x=250, y=370)
        c2.bind('<Button-1>')
        c1.bind('<Button-1>')
        c3.bind('<Button-1>')
        c4.bind('<Button-1>')
        c5.bind('<Button-1>')
        pygame.mixer.music.play()
        b.mainloop()



    def language_list(self):
        # t.destroy()
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"background.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        a.resizable(False, False)

        c1 = Button(a, text="HINDI", font='Courier 16 bold', bg='white', fg='red', width=17, bd=1, relief='ridge',
                    height=2,
                    command=self.hindi)
        c2 = Button(a, text="ENGLISH", font='Courier 16 bold', bg='white', fg='palevioletred2', width=17, bd=1,
                    relief='ridge', height=2,
                    command=self.eng)
        c3 = Button(a, text="PUNJABI", font='Courier 16 bold', bg='white', fg='green', width=17, bd=1, relief='ridge',
                    height=2,
                    command=self.pun)
        c4 = Button(a, text="SPANISH", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=17, bd=1,
                    relief='ridge', height=2,
                    command=self.spa)

        c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=12, bd=1, relief='ridge',
                    height=1,
                    command=self.go_back)

        c5.place(x=10, y=10)
        c1.place(x=10, y=110)
        c2.place(x=10, y=190)
        c3.place(x=10, y=270)
        c4.place(x=10, y=360)
        a.mainloop()

    def language_back(self):
        self.stop()
        b.destroy()
        self.language_list()

    def language_call(self):
        t.destroy()
        self.language_list()

    ################

    def yjhd(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song so left outer join songalb s on s.s_id=so.s_id left outer join album a on a.al_id = s.al_id where al_name='YJHD'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player3()

    def aash(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song so left outer join songalb s on s.s_id=so.s_id left outer join album a on a.al_id = s.al_id where al_name='Aashiqui 2'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player3()


    def rock(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song so left outer join songalb s on s.s_id=so.s_id left outer join album a on a.al_id = s.al_id where al_name='Rockstar'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player3()


    def soty(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song so left outer join songalb s on s.s_id=so.s_id left outer join album a on a.al_id = s.al_id where al_name='SOTY'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player3()

    #################

    def player3(self):
        # album  player
        global b
        global va
        a.destroy()
        b = Tk()
        b.title("                             MUSIC PLAYER")
        b.geometry('428x446')
        r = PhotoImage(file=r"background.png")
        l1 = Label(b, image=r)
        l1.place(x=0, y=0)

        li = Listbox(b, width=32, height=12)
        jo2.reverse()
        for c in jo2:
            li.insert(0, c)
        va = StringVar()
        songlabel = Label(b, textvariable=va, width=35)
        self.updatelabel()
        c1 = Button(b, text="pause", font='Courier 16 bold', bg='white', fg='red', width=8, bd=1, relief='ridge',
                    height=2,command=self.pause)
        c2 = Button(b, text="play", font='Courier 16 bold', bg='white', fg='palevioletred2', width=8, bd=1,
                    relief='ridge', height=2,command=self.play)
        c3 = Button(b, text="stop", font='Courier 16 bold', bg='white', fg='green', width=8, bd=1, relief='ridge',
                    height=2,command=self.stop)
        c4 = Button(b, text="previous", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2,command=self.prev)
        c6 = Button(b, text="next", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2,command=self.next)

        c5 = Button(b, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1, relief='ridge',
                    height=1, command=self.alb_back)

        songlabel.place(x=40, y=40)
        li.place(x=100, y=75)
        c5.place(x=10, y=10)
        c1.place(x=170, y=300)
        c2.place(x=50, y=300)
        c3.place(x=130, y=370)
        c4.place(x=10, y=370)
        c6.place(x=250, y=370)
        c2.bind('<Button-1>')
        c1.bind('<Button-1>')
        c3.bind('<Button-1>')
        c4.bind('<Button-1>')
        c5.bind('<Button-1>')
        pygame.mixer.music.play()
        b.mainloop()

    def alb_list(self):
        # t.destroy()
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"background.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)

        a.resizable(False, False)

        c1 = Button(a, text="YJHD", font='Courier 16 bold', bg='white', fg='red', width=17, bd=1, relief='ridge',
                    height=2, command=self.yjhd)
        c2 = Button(a, text="AASHIQI 2", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=17, bd=1,
                    relief='ridge', height=2, command=self.aash)
        c3 = Button(a, text="SOTY", font='Courier 16 bold', bg='white', fg='orchid3', width=17, bd=1, relief='ridge',
                    height=2, command=self.soty)
        c4 = Button(a, text="ROCKSTAR", font='Courier 16 bold', bg='white', fg='palevioletred3', width=17, bd=1,
                    relief='ridge', height=2, command=self.rock)

        c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=12, bd=1, relief='ridge',
                    height=1,
                    command=self.go_back)
        c5.place(x=10, y=10)

        c1.place(x=10, y=110)
        c2.place(x=10, y=190)
        c3.place(x=10, y=270)
        c4.place(x=10, y=360)

        a.mainloop()

    def alb_back(self):
        self.stop()
        b.destroy()
        self.alb_list()

    def alb_call(self):
        t.destroy()
        self.alb_list()

    ##################################

    def happy(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song so left outer join songemo s on s.s_id=so.s_id left outer join emotion e on e.e_id = s.e_id where e_name='Happy'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player4()


    def sad(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song so left outer join songemo s on s.s_id=so.s_id left outer join emotion e on e.e_id = s.e_id where e_name='Sad'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player4()


    def rom(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song so left outer join songemo s on s.s_id=so.s_id left outer join emotion e on e.e_id = s.e_id where e_name='Romantic'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player4()

    def drive(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song so left outer join songemo s on s.s_id=so.s_id left outer join emotion e on e.e_id = s.e_id where e_name='Drive Time'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player4()


    def party(self):
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()
        jo3.clear()

        cursor.execute("Select * from song so left outer join songemo s on s.s_id=so.s_id left outer join emotion e on e.e_id = s.e_id where e_name='Party'")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[3])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        pygame.mixer.music.load(jo1[index])

        self.player3()


    def player4(self):
        # emotion player
        global b
        global va
        a.destroy()
        b = Tk()
        b.title("                             MUSIC PLAYER")
        b.geometry('428x446')
        r = PhotoImage(file=r"background.png")
        l1 = Label(b, image=r)
        l1.place(x=0, y=0)

        li = Listbox(b, width=32, height=12)
        jo2.reverse()
        for c in jo2:
            li.insert(0, c)
        va = StringVar()
        songlabel = Label(b, textvariable=va, width=35)
        self.updatelabel()
        c1 = Button(b, text="pause", font='Courier 16 bold', bg='white', fg='red', width=8, bd=1, relief='ridge',
                    height=2,command=self.pause)
        c2 = Button(b, text="play", font='Courier 16 bold', bg='white', fg='palevioletred2', width=8, bd=1,
                    relief='ridge', height=2,command=self.play)
        c3 = Button(b, text="stop", font='Courier 16 bold', bg='white', fg='green', width=8, bd=1, relief='ridge',
                    height=2,command=self.stop)
        c4 = Button(b, text="previous", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2,command=self.prev)
        c6 = Button(b, text="next", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2,command=self.next)

        c5 = Button(b, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1, relief='ridge',
                    height=1, command=self.emotion_back)

        songlabel.place(x=40, y=40)
        li.place(x=100, y=75)
        c5.place(x=10, y=10)
        c1.place(x=170, y=300)
        c2.place(x=50, y=300)
        c3.place(x=130, y=370)
        c4.place(x=10, y=370)
        c6.place(x=250, y=370)
        c2.bind('<Button-1>')
        c1.bind('<Button-1>')
        c3.bind('<Button-1>')
        c4.bind('<Button-1>')
        c5.bind('<Button-1>')
        pygame.mixer.music.play()
        b.mainloop()

    def emotion_list(self):
        # t.destroy()
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"background.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        a.resizable(False, False)

        c1 = Button(a, text="HAPPY 😄", font='Courier 16 bold', bg='white', fg='red2', width=17, bd=1, relief='ridge',
                    height=2, command=self.happy)
        c2 = Button(a, text="SAD 😔", font='Courier 16 bold', bg='white', fg='palevioletred2', width=17, bd=1,
                    relief='ridge', height=2, command=self.sad)
        c3 = Button(a, text="ROMANTIC 😍", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=17, bd=1,
                    relief='ridge', height=2, command=self.rom)
        c4 = Button(a, text="LONG DRIVE 🚗", font='Courier 16 bold', bg='white', fg='coral', width=17, bd=1,
                    relief='ridge', height=2, command=self.drive)
        c6 = Button(a, text="PARTY 🎉", font='Courier 16 bold', bg='white', fg='indianred2', width=17, bd=1,
                    relief='ridge', height=2, command=self.party)

        c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=12, bd=1, relief='ridge',
                    height=1,
                    command=self.go_back)

        c5.place(x=10, y=10)
        c1.place(x=10, y=90)
        c2.place(x=10, y=160)
        c3.place(x=10, y=230)
        c4.place(x=10, y=300)
        c6.place(x=10, y=370)

        a.mainloop()

    def emotion_back(self):
        self.stop()
        b.destroy()
        self.emotion_list()

    def emotion_call(self):
        t.destroy()
        self.emotion_list()

    def song_list(self):
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"background.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        a.resizable(False, False)


        f = Frame(a)
        f1= Frame(a)
        f2=Frame(a)
        f3=Frame(a)
        e = Entry(a)
        l = ['Aasan Nahin Yahan', 'Angreji Beat', 'Aur Ho', 'Badtameez Dil', 'Balam Pichkari'
            , 'Bhula Dena', 'Chahu Mei Ya Naa', 'Daaru Desi', 'Dar Lagi Lekin', 'Despacito'
            , 'Dil Dhadakne Do', 'Dilliwaali Girlfriend', 'Ghagra', 'Hawaa Hawaa'
            , 'Hum Mar Jayenge', 'Ik Junoon', 'Ik Junoon Remix', 'Ilahi', 'Ishq Wala Love'
            , 'Jo Bhi Main', 'Kabira', 'Katiya Karun', 'Khaab', 'Khaabon Ke Parinday', 'Kukkad'
            , 'Kun Faya Kun', 'Meri Aashiqui', 'Milne Hai Mujhse Aayi', 'Nadaan Parinde'
            , 'Phir Se Ud Chala', 'Piya Aaye Na', 'Radha', 'Ratta Maar', 'Sadda Haq', 'Senorita Remix'
            , 'Senorita', 'Shape of You', 'Sheher Mein', 'Sooraj ki Baahon Mein', 'Subhanallah'
            , 'Sunn Raha Hai', 'Sunn Raha Hai Female Version', 'Tera Naam Japdi Phira'
            , 'The Disco Song', 'Tum Hi Ho Bandhu', 'Tum Hi Ho', 'Vele', 'What Do You Mean'
            , 'Yaariyan', 'High Heels', 'Dope Shope', 'Mi Gente', 'Yo x Ti Tu x Mi']

        def select(evt):
            value = str((lb.get(ACTIVE)))
            print(value)

        lb = Listbox(f, font=('times', 13))
        lb.bind('<<ListboxSelect>>', select)
        lb.pack(side=LEFT, fill=Y)

        s = Scrollbar(f, orient='vertical')
        s.config(command=lb.yview)
        s.pack(side=RIGHT, fill=Y)

        lb.config(yscrollcommand=s.set)
        for items in l:
            lb.insert(END, items)
        l1=[]
        def search():
            x=e.get().lower()
            for i in l:
                if re.search(x,i.lower()):
                    l1.append(i)
            if l1!=[]:
                lb.delete(0, 'end')
                for items in l1:
                    lb.insert(END, items)
        c1 = Button(a, text="Pause", font='Courier 16 bold', bg='white', fg='red', width=8, bd=1, relief='ridge',
                    height=2, command=self.pause)
        c2 = Button(a, text="Play", font='Courier 16 bold', bg='white', fg='palevioletred2', width=8, bd=1,
                    relief='ridge', height=2, command=self.play)
        c4 = Button(a, text="Previous", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2, command=self.prev)
        c6 = Button(a, text="Next", font='Courier 16 bold', bg='white', fg='green', width=8, bd=1,
                    relief='ridge', height=2, command=self.next)

        c5 = Button(f2, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1,
                    relief='ridge',height=1, command=self.song_back)

        b=Button(a, text="Search", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1,
                    relief='ridge',height=1,command=search)

        c2.bind('<Button-1>')
        c1.bind('<Button-1>')
        c4.bind('<Button-1>')
        c5.bind('<Button-1>')
        #pygame.mixer.music.play()


        c5.pack(side=LEFT,anchor=NW)
        f2.pack(side=TOP,fill=X)
        e.pack(fill=X,pady=10)
        b.pack()
        f.pack(pady=10,padx=30,anchor=N)
        c4.pack(side=LEFT)
        c2.pack(side=LEFT)
        c1.pack(side=LEFT)
        c6.pack(side=LEFT)

        a.mainloop()


    def play_list(self):
        pass
    def song_back(self):
        self.stop()
        a.destroy()
        self.fpage()
    def song_call(self):
        t.destroy()
        self.song_list()
    def play_back(self):
        pass
    def play_call(self):
        t.destroy()
        self.play_list()

    ##############

    def go_back(self):
        a.destroy()
        self.fpage()

    def fpage(self):
        global t
        t = Tk()
        t.title("                             MUSIC PLAYER")
        t.geometry('428x446')
        a = PhotoImage(file=r"background.png")
        l = Label(t, image=a)
        l.place(x=0, y=0)

        t.resizable(False, False)
        b1 = Button(t, text="ALBUM", font='Courier 22 bold', bg='white', fg='pale violet red', width=8, bd=1,
                    relief='ridge', height=3,
                    command=self.alb_call)
        b2 = Button(t, text="LANGUAGE", font='Courier 22 bold', bg='white', fg='steelblue4', width=8, height=3, bd=1,
                    relief='ridge',
                    command=self.language_call)
        b3 = Button(t, text="MOOD", font='Courier 22 bold', bg='white', fg='sky blue2', width=8, height=3, bd=1,
                    relief='ridge',
                    command=self.emotion_call)
        b4 = Button(t, text="ARTIST", font='Courier 22 bold', bg='white', fg='indian red2', width=8, height=3, bd=1,
                    relief='ridge',
                    command=self.art_call)
        b5= Button(t, text="SONG", font='Courier 22 bold', bg='white', fg='green', width=8, height=3, bd=1,
                    relief='ridge',
                    command=self.song_call)
        b6 = Button(t, text="PLAYLIST", font='Courier 22 bold', bg='white', fg='deep pink', width=8, height=3, bd=1,
                    relief='ridge',
                    command=self.play_call)

        b1.place(x=10, y=10)
        b2.place(x=160, y=10)
        b4.place(x=10, y=150)
        b3.place(x=160, y=150)
        b5.place(x=10, y=290)
        b6.place(x=160, y=290)

        t.mainloop()


o = main()
# o.player1()
