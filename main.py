from tkinter import *
class main:
    def __init__(self):
        self.fpage()

    def art_list(self):
        print("artist")
        t.destroy()
        global a
        a = Tk()
        a.geometry('300x200')
        a.configure(bg='black')
        a.resizable(False,False)
        f3 = Frame(a,bg='black')
        f3.pack(side=TOP,fill=X)
        f1 = Frame(a)
        f1.pack(side=LEFT)
        f2 = Frame(a)
        f2.pack(side=RIGHT)
        e = Entry(f3,width=35)
        
        c1 = Button(f1, text="Arijit Singh",font='Courier 12 bold',bg='black', fg='red', width=15)
        c2 = Button(f2, text="Sonu Nigam",font='Courier 12 bold',bg='black', fg='palevioletred2',width=15)
        c3 = Button(f1, text="Armaan Malik",font='Courier 12 bold',bg='black', fg='green',width=15)
        c4 = Button(f2, text="Shreya Ghoshal",font='Courier 12 bold',bg='black', fg='deep sky blue2', width=15)
        c5 = Button(f3, text="Back",font='Courier 12 bold',bg='gray10', fg='deep pink', width=6,command = self.go_back)
        c5.pack(anchor=W,pady=5)
        e.pack(side=BOTTOM,pady=5)
        c1.pack(side=TOP)
        c2.pack(side=TOP)
        c3.pack(side=BOTTOM)
        c4.pack(side=BOTTOM)
       


    def song_list(self):
        print("song")
        t.destroy()
        global a
        a = Tk()
        a.geometry('300x200')
        a.configure(bg='black')
        a.resizable(False,False)
        f3 = Frame(a,bg='black')
        f3.pack(side=TOP,fill=X)
        e = Entry(f3,width=35)

        f1 = Frame(a)
        f1.pack(side=LEFT)
        f2 = Frame(a)
        f2.pack(side=RIGHT)
        c1 = Button(f1, text="Hindi Bollywood",font='Courier 12 bold',bg='black', fg='red', width=15)
        c2 = Button(f2, text="English",font='Courier 12 bold',bg='black', fg='palevioletred2',width=15)
        c3 = Button(f1, text="Punjabi",font='Courier 12 bold',bg='black', fg='green',width=15)
        c4 = Button(f2, text="Spanish",font='Courier 12 bold',bg='black', fg='deep sky blue2', width=15)
        c5 = Button(f3, text="back",font='Courier 12 bold',bg='gray10', fg='deep pink', width=6, command=self.go_back)
        c5.pack(anchor=W,pady=5)
        e.pack(side=BOTTOM,pady=5)
        c1.pack(side=TOP)
        c2.pack(side=TOP)
        c3.pack(side=BOTTOM)
        c4.pack(side=BOTTOM)


    def alb_list(self):
        print("album")
        t.destroy()
        global a
        a = Tk()
        a.geometry('300x200')
        a.configure(bg='black')
        a.resizable(False,False)
        f3 = Frame(a,bg='black')
        f3.pack(side=TOP,fill=X)
        e = Entry(f3,width=35)

        f1 = Frame(a)
        f1.pack(side=LEFT)
        f2 = Frame(a)
        f2.pack(side=RIGHT)
        c1 = Button(f1, text="Purpose",font='Courier 12 bold',bg='black', fg='red', width=15)
        c2 = Button(f2, text="Believe",font='Courier 12 bold',bg='black', fg='palevioletred2',width=15)
        c3 = Button(f1, text="Divide", font='Courier 12 bold',bg='black', fg='deep sky blue2', width=15)
        c4 = Button(f2, text="Illuminate",font='Courier 12 bold',bg='black', fg='green',width=15)
        c5 = Button(f3, text="back", font='Courier 12 bold',bg='gray10', fg='deep pink', width=6,command=self.go_back)
        c5.pack(anchor=W,pady=5)
        e.pack(side=BOTTOM,pady=5)
        c1.pack(side=TOP)
        c2.pack(side=TOP)
        c3.pack(side=BOTTOM)
        c4.pack(side=BOTTOM)


    def mood_list(self):
        print("mood")
        t.destroy()
        global a
        a = Tk()
        a.geometry('300x200')
        a.configure(bg='black')
        a.resizable(False,False)
        f3 = Frame(a,bg='black')
        f3.pack(side=TOP,fill=X)
        e = Entry(f3,width=35)

        f1 = Frame(a)
        f1.pack(side=LEFT)
        f2 = Frame(a)
        f2.pack(side=RIGHT)
        c1 = Button(f1, text="Happy", font='Courier 12 bold',bg='black', fg='red', width=15)
        c2 = Button(f2, text="Heart Broken",font='Courier 12 bold',bg='black', fg='palevioletred2',width=15)
        c3 = Button(f1, text="In Love",font='Courier 12 bold',bg='black', fg='green',width=15)
        c4 = Button(f2, text="Party Mode",font='Courier 12 bold',bg='black', fg='deep sky blue2', width=15)
        c5 = Button(f1, text="Dark", font='Courier 12 bold',bg='black', fg='yellow', width=15)
        c6 = Button(f2, text="Dreamy", font='Courier 12 bold',bg='black', fg='orange', width=15)
        c7 = Button(f1, text="Meditative",font='Courier 12 bold',bg='black', fg='palevioletred2',width=15)
        c8 = Button(f2, text="Workout",font='Courier 12 bold',bg='black', fg='green',width=15)
        c9 = Button(f3, text="back", font='Courier 12 bold',bg='gray10', fg='deep pink', width=6,command=self.go_back)
        c9.pack(anchor=W,pady=5)
        e.pack(side=BOTTOM,pady=5)
        c1.pack(side=TOP)
        c2.pack(side=TOP)
        c3.pack(side=BOTTOM)
        c4.pack(side=BOTTOM)
        c5.pack(side=BOTTOM)
        c6.pack(side=BOTTOM)
        c7.pack(side=BOTTOM)
        c8.pack(side=BOTTOM)

    def go_back(self):
        a.destroy()
        self.fpage()

    def fpage(self):
        global t
        t =Tk()
        t.geometry('300x251')
        t.configure(bg='black')
        t.resizable(False,False)
        b1 = Button(t, text="ALBUM",font='Courier 15 bold',bg='black', fg='steel blue1', width=12, height=5, command=self.alb_list)
        b2 = Button(t, text="SONG",font='Courier 15 bold',bg='black', fg='violet', width=12, height=5, command=self.song_list)
        b3 = Button(t, text="MOOD",font='Courier 15 bold',bg='black', fg='indian red1', width=12, height=5, command=self.mood_list)
        b4 = Button(t, text="ARTIST",font='Courier 15 bold',bg='black', fg='violet red1', width=12, height=5, command=self.art_list)

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=3)
        b4.grid(row=2, column=0)
        b3.grid(row=2, column=3)

        t.mainloop()

o = main()
