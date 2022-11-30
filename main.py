from tkinter import *
import sqlite3
import pygame
import re

connect = sqlite3.connect('emotionplayer.db')
cursor = connect.cursor()
global index
index = 0


class main:
    global jo, jo1, jo2, jo3, index, va
    jo = []
    jo1 = []
    jo2 = []
    jo3 = []

    def __init__(self):
        self.fpage()

    #################
    # Basic Player Functions

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

    ##################

    def player1(self):
        # artist player

        global b
        global va
        a.destroy()
        b = Tk()
        b.title("                             SYMPHONY")
        b.geometry('500x446')
        r = PhotoImage(file=r"background.png")
        l1 = Label(b, image=r)
        l1.place(x=0, y=0)
    
        li = Listbox(b, width=32, height=12)
        jo2.reverse()
        for c in jo2:
            li.insert(0, c)

        def select(evt):
            global index
            index = 0
            val = li.curselection()
            index = int(val[0])
            self.updatelabel()
            pygame.mixer.init()
            pygame.mixer.music.load(jo1[index])
            pygame.mixer.music.play()

        li.bind('<<ListboxSelect>>', select)

        s = Scrollbar(b, orient='vertical')
        s.pack(side=RIGHT, fill=Y)
        li.config(yscrollcommand=s.set)

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
        global va

        a = Tk()
        a.title("                                       SYMPHONY")
        a.geometry('500x446')
        r = PhotoImage(file=r"background.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        a.resizable(False, False)

        f = Frame(a,bg='black')
        f2 = Frame(a)
        e = Entry(a)
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()

        cursor.execute("Select * from artist")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[1])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        l14 = jo1.copy()
        l15 = jo2.copy()

        def select(evt):
            global index
            index = 0
            val = lb.get(lb.curselection())
            val1 = val.title()

            jo.clear()
            jo1.clear()
            jo2.clear()
            jo3.clear()

            cursor.execute(
                "Select * from song so left outer join songart s on s.s_id=so.s_id left outer join artist a on a.art_id = s.art_id where art_name=(?)",
                (val1,))
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

        global lb
        global va
        lb = Listbox(f,fg='deepskyblue4', font=('times', 13),width=22,height=15)
        lb.bind('<<ListboxSelect>>', select)
        lb.pack(side=LEFT, fill=Y)

        s = Scrollbar(f, orient='vertical')
        s.config(command=lb.yview)
        s.pack(side=RIGHT, fill=Y)

        lb.config(yscrollcommand=s.set)
        l13 = []
        for items in jo2:
            lb.insert(END, items)

        def search():
            l12 = []
            l12.clear()
            l14.clear()
            l15.clear()
            x = e.get().lower()

            for se in jo2:
                if re.search(x, se.lower()):
                    l12.append(se)

            if l12 != []:
                lb.delete(0, 'end')
            for items in l12:
                lb.insert(END, items)
                item = items.title()
                l13.append(jo2.index(item))
            for u in l13:
                l15.append(jo2[u])
                l14.append(jo1[u])

        btn1 = Button(f2, text="Back", font='Courier 12 bold', bg='white', fg='green', width=6, bd=1,
                      relief='ridge', height=1, command=self.song_back)

        b = Button(a, text="SEARCH", font='Courier 12 bold', bg='white', fg='indianred2', width=6, bd=1,
                   relief='ridge', height=1, command=search)

        btn1.bind('<Button-1>')

        btn1.pack(side=LEFT, anchor=NW)
        f2.pack(side=TOP, fill=X)
        e.pack(fill=X, pady=10)
        b.pack()
        f.pack(pady=5, padx=5, anchor=N)
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
        b.title("                             SYMPHONY")
        b.geometry('500x446')
        r = PhotoImage(file=r"background.png")
        l1 = Label(b, image=r)
        l1.place(x=0, y=0)

        li = Listbox(b, width=32, height=12)
        jo2.reverse()
        for c in jo2:
            li.insert(0, c)

        def select(evt):
            global index
            index = 0
            val = li.curselection()
            index = int(val[0])
            self.updatelabel()
            pygame.mixer.init()
            pygame.mixer.music.load(jo1[index])
            pygame.mixer.music.play()

        li.bind('<<ListboxSelect>>', select)

        s = Scrollbar(b, orient='vertical')
        s.pack(side=RIGHT, fill=Y)
        li.config(yscrollcommand=s.set)

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
        a.title("                             SYMPHONY")
        a.geometry('500x446')
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

    #################

    def player3(self):
        # album  player
        global b
        global va
        a.destroy()
        b = Tk()
        b.title("                             SYMPHONY")
        b.geometry('500x446')
        r = PhotoImage(file=r"background.png")
        l1 = Label(b, image=r)
        l1.place(x=0, y=0)

        li = Listbox(b, width=32, height=12)
        jo2.reverse()
        for c in jo2:
            li.insert(0, c)

        def select(evt):
            global index
            index = 0
            val = li.curselection()
            index = int(val[0])
            self.updatelabel()
            pygame.mixer.init()
            pygame.mixer.music.load(jo1[index])
            pygame.mixer.music.play()

        li.bind('<<ListboxSelect>>', select)

        s = Scrollbar(b, orient='vertical')
        s.pack(side=RIGHT, fill=Y)
        li.config(yscrollcommand=s.set)

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
        global va

        a = Tk()
        a.title("                             SYMPHONY")
        a.geometry('500x446')
        r = PhotoImage(file=r"background.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        a.resizable(False, False)

        f = Frame(a)
        f2 = Frame(a)
        e = Entry(a)
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()

        cursor.execute("Select * from album")
        fet = cursor.fetchall()
        for i in fet:
            jo.append(i)
        for i in fet:
            jo1.append(i[1])
        for i in fet:
            p = i[1].title()
            jo2.append(p)
            jo3.append(p.upper())
        pygame.mixer.init()
        l14 = jo1.copy()
        l15 = jo2.copy()

        def select(evt):
            global index
            index = 0
            val = lb.get(lb.curselection())
            val1 = val.title()

            jo.clear()
            jo1.clear()
            jo2.clear()
            jo3.clear()

            cursor.execute(
                "Select * from song so left outer join album a on a.alb_id=so.alb_id where al_name=(?)", (val1,))
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

        global lb
        global va
        lb = Listbox(f, font=('times', 13),fg='deepskyblue4',height=15,width=22)
        lb.bind('<<ListboxSelect>>', select)
        lb.pack(side=LEFT, fill=Y)

        s = Scrollbar(f, orient='vertical')
        s.config(command=lb.yview)
        s.pack(side=RIGHT, fill=Y)

        lb.config(yscrollcommand=s.set)
        l13 = []
        for items in jo2:
            lb.insert(END, items)

        def search():
            l12 = []
            l12.clear()
            l14.clear()
            l15.clear()
            x = e.get().lower()

            for se in jo2:
                if re.search(x, se.lower()):
                    l12.append(se)

            if l12 != []:
                lb.delete(0, 'end')
            for items in l12:
                lb.insert(END, items)
                item = items.title()
                l13.append(jo2.index(item))
            for u in l13:
                l15.append(jo2[u])
                l14.append(jo1[u])

        btn1 = Button(f2, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1,
                      relief='ridge', height=1, command=self.song_back)

        b = Button(a, text="Search", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1,
                   relief='ridge', height=1, command=search)

        btn1.bind('<Button-1>')

        btn1.pack(side=LEFT, anchor=NW)
        f2.pack(side=TOP, fill=X)
        e.pack(fill=X, pady=10)
        b.pack()
        f.pack(pady=10, padx=30, anchor=N)
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

        cursor.execute(
            "Select * from song so left outer join songemo s on s.s_id=so.s_id left outer join emotion e on e.e_id = s.e_id where e_name='Happy'")
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

        cursor.execute(
            "Select * from song so left outer join songemo s on s.s_id=so.s_id left outer join emotion e on e.e_id = s.e_id where e_name='Sad'")
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

        cursor.execute(
            "Select * from song so left outer join songemo s on s.s_id=so.s_id left outer join emotion e on e.e_id = s.e_id where e_name='Romantic'")
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

        cursor.execute(
            "Select * from song so left outer join songemo s on s.s_id=so.s_id left outer join emotion e on e.e_id = s.e_id where e_name='Drive Time'")
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

        cursor.execute(
            "Select * from song so left outer join songemo s on s.s_id=so.s_id left outer join emotion e on e.e_id = s.e_id where e_name='Party'")
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

    def player4(self):
        # emotion player
        global b
        global va
        a.destroy()
        b = Tk()
        b.title("                             SYMPHONY")
        b.geometry('500x446')
        r = PhotoImage(file=r"background.png")
        l1 = Label(b, image=r)
        l1.place(x=0, y=0)

        li = Listbox(b, width=32, height=10, font=('times', 13))
        jo2.reverse()
        for c in jo2:
            li.insert(0, c)

        def select(evt):
            global index
            index = 0
            val = li.curselection()
            index = int(val[0])
            self.updatelabel()
            pygame.mixer.init()
            pygame.mixer.music.load(jo1[index])
            pygame.mixer.music.play()

        li.bind('<<ListboxSelect>>', select)

        s = Scrollbar(b, orient='vertical')
        s.pack(side=RIGHT, fill=Y)
        li.config(yscrollcommand=s.set)

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
        a.title("                             SYMPHONY")
        a.geometry('500x446')
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
        global va

        a = Tk()
        a.title("                             SYMPHONY")
        a.geometry('500x446')
        r = PhotoImage(file=r"background.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        a.resizable(False, False)

        f = Frame(a)
        f2 = Frame(a)
        e = Entry(a)
        global index
        index = 0
        jo.clear()
        jo1.clear()
        jo2.clear()

        cursor.execute("Select * from song")
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
        l14 = jo1.copy()
        l15 = jo2.copy()

        def snext():
            global index
            if (index == len(l14) - 1):
                index = 0
            else:
                index += 1
            pygame.mixer.music.load(l14[index])
            pygame.mixer.music.play()

        def sprev():
            global index
            if (index == 0):
                index = len(l14) - 1
            index -= 1
            pygame.mixer.music.load(l14[index])
            pygame.mixer.music.play()

        def select(evt):
            global index
            index = 0
            val = lb.get(lb.curselection())
            val1 = val.title()
            index = l15.index(val1)
            # print(val1)
            pygame.mixer.init()
            pygame.mixer.music.load(l14[index])
            pygame.mixer.music.play()

        global lb
        global va
        lb = Listbox(f, font=('times', 13), fg='deepskyblue3')
        lb.bind('<<ListboxSelect>>', select)
        lb.pack(side=LEFT, fill=Y)

        s = Scrollbar(f, orient='vertical')
        s.config(command=lb.yview)
        s.pack(side=RIGHT, fill=Y)

        lb.config(yscrollcommand=s.set)
        l13 = []
        for items in jo2:
            lb.insert(END, items)

        def search():
            l12 = []
            l12.clear()
            l14.clear()
            l15.clear()
            x = e.get().lower()

            for se in jo2:
                if re.search(x, se.lower()):
                    l12.append(se)

            if l12 != []:
                lb.delete(0, 'end')
            for items in l12:
                lb.insert(END, items)
                item = items.title()
                l13.append(jo2.index(item))
            for u in l13:
                l15.append(jo2[u])
                l14.append(jo1[u])

        c1 = Button(a, text="Pause", font='Courier 16 bold', bg='white', fg='red', width=9, bd=1, relief='ridge',
                    height=2, command=self.pause)
        c2 = Button(a, text="Play", font='Courier 16 bold', bg='white', fg='palevioletred2', width=9, bd=1,
                    relief='ridge', height=2, command=self.play)
        c4 = Button(a, text="Previous", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=9, bd=1,
                    relief='ridge', height=2, command=sprev)
        c6 = Button(a, text="Next", font='Courier 16 bold', bg='white', fg='green', width=9, bd=1,
                    relief='ridge', height=2, command=snext)

        c5 = Button(f2, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1,
                    relief='ridge', height=1, command=self.song_back)

        b = Button(a, text="Search", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1,
                   relief='ridge', height=1, command=search)

        c2.bind('<Button-1>')
        c1.bind('<Button-1>')
        c4.bind('<Button-1>')
        c5.bind('<Button-1>')
        c6.bind('<Button-1>')
        b.bind('<Button-1>')

        c5.pack(side=LEFT, anchor=NW)
        f2.pack(side=TOP, fill=X)
        e.pack(fill=X, pady=10)
        b.pack()
        f.pack(pady=10, padx=30, anchor=N)
        c4.pack(side=LEFT)
        c2.pack(side=LEFT)
        c1.pack(side=LEFT)
        c6.pack(side=LEFT)

        a.mainloop()

    def song_back(self):
        self.stop()
        a.destroy()
        self.fpage()

    def song_call(self):
        t.destroy()
        self.song_list()

    def play_back(self):
        pass

    ##############

    def go_back(self):
        a.destroy()
        self.fpage()

    def fpage(self):
        global t
        t = Tk()
        t.title("                             SYMPHONY")
        t.geometry('500x446')
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
        b3 = Button(t, text="EMOTION", font='Courier 22 bold', bg='white', fg='sky blue2', width=8, height=3, bd=1,
                    relief='ridge',
                    command=self.emotion_call)
        b4 = Button(t, text="ARTIST", font='Courier 22 bold', bg='white', fg='indian red2', width=8, height=3, bd=1,
                    relief='ridge',
                    command=self.art_call)
        b5 = Button(t, text="SONG", font='Courier 22 bold', bg='white', fg='green', width=8, height=3, bd=1,
                    relief='ridge',
                    command=self.song_call)


        b1.place(x=10, y=10)
        b2.place(x=160, y=10)
        b4.place(x=160, y=290)
        b3.place(x=80, y=150)
        b5.place(x=10, y=290)

        t.mainloop()

o = main()