from tkinter import *


class main:
    def __init__(self):
        self.fpage()

    #################

    def player1(self):
        # artist player
        global b
        a.destroy()
        b = Tk()
        b.title("                             MUSIC PLAYER")
        b.geometry('428x446')
        r = PhotoImage(file=r"C:\Users\Acer\PycharmProjects\pldbmsrproj\background.png")
        l1 = Label(b, image=r)
        l1.place(x=0, y=0)
        l = Label(b, text='Song list', fg='black', bg='white', height=15, width=35)
        c1 = Button(b, text="pause", font='Courier 16 bold', bg='white', fg='red', width=8, bd=1, relief='ridge',
                    height=2)
        c2 = Button(b, text="play", font='Courier 16 bold', bg='white', fg='palevioletred2', width=8, bd=1,
                    relief='ridge', height=2)
        c3 = Button(b, text="stop", font='Courier 16 bold', bg='white', fg='green', width=8, bd=1, relief='ridge',
                    height=2)
        c4 = Button(b, text="previous", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2)
        c6 = Button(b, text="next", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2)

        c5 = Button(b, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1, relief='ridge',
                    height=1,command = self.artist_back)

        l.place(x=35, y=53)
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
        b.mainloop()

    def art_list(self):
        #t.destroy()
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"C:\Users\Acer\PycharmProjects\pldbmsrproj\background.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        e = Entry(a, width=50)
        a.resizable(False, False)

        c1 = Button(a, text="ARIJIT SINGH", font='Courier 16 bold', bg='white', fg='red', width=17, bd=1,
                    relief='ridge', height=2,
                    command=self.player1)
        c2 = Button(a, text="SONU NIGAM", font='Courier 16 bold', bg='white', fg='palevioletred2', width=17, bd=1,
                    relief='ridge', height=2,
                    command=self.player1)
        c3 = Button(a, text="ARMAAN MALIK", font='Courier 16 bold', bg='white', fg='green', width=17, bd=1,
                    relief='ridge', height=2,
                    command=self.player1)
        c4 = Button(a, text="SHREYA GHOSHAL", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=17, bd=1,
                    relief='ridge', height=2,
                    command=self.player1)


        c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=12, bd=1, relief='ridge',
                    height=1,
                    command=self.go_back)

        c5.place(x=10, y=10)
        e.place(x=10, y=60)
        c1.place(x=10, y=110)
        c2.place(x=10, y=190)
        c3.place(x=10, y=270)
        c4.place(x=10, y=360)
        a.mainloop()
        
    def artist_back(self):
        b.destroy()
        self.art_list()
        
    
    def art_call(self):
        t.destroy()
        self.art_list()
        
    ###################

    def player2(self):
        # language player
        global b
        a.destroy()
        b = Tk()
        b.title("                             MUSIC PLAYER")
        b.geometry('428x446')
        r = PhotoImage(file=r"C:\Users\Acer\PycharmProjects\pldbmsrproj\background.png")
        l1 = Label(b, image=r)
        l1.place(x=0, y=0)
        l = Label(b, text='Song list', fg='black', bg='white', height=15, width=35)
        c1 = Button(b, text="pause", font='Courier 16 bold', bg='white', fg='red', width=8, bd=1, relief='ridge',
                    height=2)
        c2 = Button(b, text="play", font='Courier 16 bold', bg='white', fg='palevioletred2', width=8, bd=1,
                    relief='ridge', height=2)
        c3 = Button(b, text="stop", font='Courier 16 bold', bg='white', fg='green', width=8, bd=1, relief='ridge',
                    height=2)
        c4 = Button(b, text="previous", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2)
        c6 = Button(b, text="next", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2)

        c5 = Button(b, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1, relief='ridge',
                    height=1,command = self.language_back)

        l.place(x=35, y=53)
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
        b.mainloop()

    def language_list(self):
        #t.destroy()
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"C:\Users\Acer\PycharmProjects\pldbmsrproj\background.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        e = Entry(a, width=50)
        a.resizable(False, False)

        c1 = Button(a, text="HINDI", font='Courier 16 bold', bg='white', fg='red', width=17, bd=1, relief='ridge',height=2,
                    command = self.player2)
        c2 = Button(a, text="ENGLISH", font='Courier 16 bold', bg='white', fg='palevioletred2', width=17, bd=1,relief='ridge', height=2,
                    command = self.player2)
        c3 = Button(a, text="PUNJABI", font='Courier 16 bold', bg='white', fg='green', width=17, bd=1, relief='ridge',height=2,
                    command = self.player2)
        c4 = Button(a, text="SPANISH", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=17, bd=1,relief='ridge', height=2,
                    command = self.player2)


        c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=12, bd=1, relief='ridge',height=1,
                    command=self.go_back)

        c5.place(x=10, y=10)
        e.place(x=10, y=60)
        c1.place(x=10, y=110)
        c2.place(x=10, y=190)
        c3.place(x=10, y=270)
        c4.place(x=10, y=360)

        a.mainloop()

    def language_back(self):
        b.destroy()
        self.language_list()

    def language_call(self):
        t.destroy()
        self.language_list()

    ################

    def player3(self):
        #album  player
        global b
        a.destroy()
        b = Tk()
        b.title("                             MUSIC PLAYER")
        b.geometry('428x446')
        r = PhotoImage(file=r"C:\Users\Acer\PycharmProjects\pldbmsrproj\background.png")
        l1 = Label(b, image=r)
        l1.place(x=0, y=0)
        l = Label(b, text='Song list', fg='black', bg='white', height=15, width=35)
        c1 = Button(b, text="pause", font='Courier 16 bold', bg='white', fg='red', width=8, bd=1, relief='ridge',
                    height=2)
        c2 = Button(b, text="play", font='Courier 16 bold', bg='white', fg='palevioletred2', width=8, bd=1,
                    relief='ridge', height=2)
        c3 = Button(b, text="stop", font='Courier 16 bold', bg='white', fg='green', width=8, bd=1, relief='ridge',
                    height=2)
        c4 = Button(b, text="previous", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2)
        c6 = Button(b, text="next", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2)


        c5 = Button(b, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1, relief='ridge',
                    height=1,command = self.alb_back)

        l.place(x=35, y=53)
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
        b.mainloop()

    def alb_list(self):
        #t.destroy()
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"C:\Users\Acer\PycharmProjects\pldbmsrproj\background.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        e = Entry(a, width=50)
        a.resizable(False, False)

        c1 = Button(a, text="YJHD", font='Courier 16 bold', bg='white', fg='red', width=17, bd=1, relief='ridge',
                    height=2,command = self.player3)
        c2 = Button(a, text="AASHIQI 2", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=17, bd=1,
                    relief='ridge', height=2,command = self.player3)
        c3 = Button(a, text="SOTY", font='Courier 16 bold', bg='white', fg='orchid3', width=17, bd=1, relief='ridge',
                    height=2,command = self.player3)
        c4 = Button(a, text="ROCKSTAR", font='Courier 16 bold', bg='white', fg='palevioletred3', width=17, bd=1,
                    relief='ridge', height=2,command = self.player3)


        c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=12, bd=1, relief='ridge',
                    height=1,
                    command=self.go_back)
        c5.place(x=10, y=10)
        e.place(x=10, y=60)
        c1.place(x=10, y=110)
        c2.place(x=10, y=190)
        c3.place(x=10, y=270)
        c4.place(x=10, y=360)

        a.mainloop()

    def alb_back(self):
        b.destroy()
        self.alb_list()

    def alb_call(self):
        t.destroy()
        self.alb_list()

    ##################

    def player4(self):
        #emotion player
        global b
        a.destroy()
        b = Tk()
        b.title("                             MUSIC PLAYER")
        b.geometry('428x446')
        r = PhotoImage(file=r"C:\Users\Acer\PycharmProjects\pldbmsrproj\background.png")
        l1 = Label(b, image=r)
        l1.place(x=0, y=0)
        l = Label(b, text='Song list', fg='black', bg='white', height=15, width=35)
        c1 = Button(b, text="pause", font='Courier 16 bold', bg='white', fg='red', width=8, bd=1, relief='ridge',
                    height=2)
        c2 = Button(b, text="play", font='Courier 16 bold', bg='white', fg='palevioletred2', width=8, bd=1,
                    relief='ridge', height=2)
        c3 = Button(b, text="stop", font='Courier 16 bold', bg='white', fg='green', width=8, bd=1, relief='ridge',
                    height=2)
        c4 = Button(b, text="previous", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2)
        c6 = Button(b, text="next", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                    relief='ridge', height=2)


        c5 = Button(b, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=6, bd=1, relief='ridge',
                    height=1,command = self.emotion_back)

        l.place(x=35, y=53)
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
        b.mainloop()

    def emotion_list(self):
        #t.destroy()
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"C:\Users\Acer\PycharmProjects\pldbmsrproj\background.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        e = Entry(a, width=50)
        a.resizable(False, False)

        c1 = Button(a, text="HAPPY", font='Courier 16 bold', bg='white', fg='red2', width=17, bd=1, relief='ridge',
                    height=2,command = self.player4)
        c2 = Button(a, text="SAD", font='Courier 16 bold', bg='white', fg='palevioletred2', width=17, bd=1,
                    relief='ridge', height=2,command = self.player4)
        c3 = Button(a, text="ROMANTIC", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=17, bd=1,
                    relief='ridge', height=2,command = self.player4)
        c4 = Button(a, text="LONG DRIVE", font='Courier 16 bold', bg='white', fg='coral', width=17, bd=1,
                    relief='ridge', height=2,command = self.player4)
        c6 = Button(a, text="PARTY", font='Courier 16 bold', bg='white', fg='indianred2', width=17, bd=1,
                    relief='ridge', height=2,command = self.player4)

        c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=12, bd=1, relief='ridge',
                    height=1,
                    command=self.go_back)

        c5.place(x=10, y=10)
        e.place(x=10, y=60)
        c1.place(x=10, y=90)
        c2.place(x=10, y=160)
        c3.place(x=10, y=230)
        c4.place(x=10, y=300)
        c6.place(x=10, y=370)

        a.mainloop()

    def emotion_back(self):
        b.destroy()
        self.emotion_list()

    def emotion_call(self):
        t.destroy()
        self.emotion_list()

    ##############

    def go_back(self):
        a.destroy()
        self.fpage()

    def fpage(self):
        global t
        t = Tk()
        t.title("                             MUSIC PLAYER")
        t.geometry('428x446')
        a = PhotoImage(file=r"C:\Users\Acer\PycharmProjects\pldbmsrproj\background.png")
        l = Label(t, image=a)
        l.place(x=0, y=0)

        t.resizable(False, False)
        b1 = Button(t, text="ALBUM", font='Courier 22 bold', bg='white', fg='pale violet red', width=7, bd=1,relief='ridge', height=5,
                    command=self.alb_call)
        b2 = Button(t, text="LANGUAGE", font='Courier 22 bold', bg='white', fg='steelblue4', width=7, height=5, bd=1,relief='ridge',
                    command=self.language_call)
        b3 = Button(t, text="MOOD", font='Courier 22 bold', bg='white', fg='sky blue2', width=7, height=5, bd=1, relief='ridge',
                    command=self.emotion_call)
        b4 = Button(t, text="ARTIST", font='Courier 22 bold', bg='white', fg='indian red2', width=7, height=5, bd=1,relief='ridge',
                    command=self.art_call)

        b1.place(x=10, y=10)
        b2.place(x=150, y=10)
        b4.place(x=10, y=230)
        b3.place(x=150, y=230)

        t.mainloop()


o = main()
#o.player1()
