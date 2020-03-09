from tkinter import *
class main:
    def __init__(self):
        self.fpage()

    def art_list(self):
        print("artist")
        t.destroy()
        global a
        a = Tk()
        a.configure(bg='black')
        f3 = Frame(a,bg='black')
        f3.pack(side=TOP)
        f1 = Frame(a)
        f1.pack(side=LEFT)
        f2 = Frame(a)
        f2.pack(side=RIGHT)
        e = Entry(f3,width=52)
        c1 = Button(f1, text="Arijit Singh",font='Courier 12 bold',bg='black', fg='red', width=15)
        c2 = Button(f2, text="Sonu Nigam",font='Courier 12 bold',bg='black', fg='palevioletred2', width=15)
        c3 = Button(f1, text="Armaan Malik",font='Courier 12 bold',bg='black', fg='green', width=15)
        c4 = Button(f2, text="Shreya Ghoshal",font='Courier 12 bold',bg='black', fg='deep sky blue2', width=15)
        c5 = Button(f3, text="Back",font='Courier 12 bold',bg='gray10', fg='deep pink', width=8,command = self.go_back)
        c5.pack()
        e.pack(fill=X)
        c1.pack(side=TOP)
        c2.pack(side=TOP)
        c3.pack(side=BOTTOM)
        c4.pack(side=BOTTOM)


    def song_list(self):
        print("song")
        t.destroy()
        global a
        a = Tk()
        f3 = Frame(a)
        f3.pack(side=TOP)
        e = Entry(f3)

        f1 = Frame(a)
        f1.pack(side=LEFT)
        f2 = Frame(a)
        f2.pack(side=RIGHT)
        c1 = Button(f1, text="Hindi Bollywood", fg='red', width=12)
        c2 = Button(f2, text="English", fg='black', width=12)
        c3 = Button(f1, text="Punjabi", fg='green', width=12)
        c4 = Button(f2, text="Spanish", fg='blue', width=12)
        c5 = Button(f3, text="back", fg='black', width=8, command=self.go_back)
        c5.pack()
        e.pack(side=TOP)
        c1.pack(side=TOP)
        c2.pack(side=TOP)
        c3.pack(side=BOTTOM)
        c4.pack(side=BOTTOM)


    def alb_list(self):
        print("album")
        t.destroy()
        global a
        a = Tk()
        f3 = Frame(a)
        f3.pack(side=TOP)
        e = Entry(f3)

        f1 = Frame(a)
        f1.pack(side=LEFT)
        f2 = Frame(a)
        f2.pack(side=RIGHT)
        c1 = Button(f1, text="Purpose", fg='red', width=12)
        c2 = Button(f2, text="Believe", fg='black', width=12)
        c3 = Button(f1, text="Divide", fg='green', width=12)
        c4 = Button(f2, text="Illuminate", fg='blue', width=12)
        c5 = Button(f3, text="back", fg='black', width=12, command=self.go_back)
        c5.pack()
        e.pack(side=TOP)
        c1.pack(side=TOP)
        c2.pack(side=TOP)
        c3.pack(side=BOTTOM)
        c4.pack(side=BOTTOM)


    def mood_list(self):
        print("mood")
        t.destroy()
        global a
        a = Tk()
        f3 = Frame(a)
        f3.pack(side=TOP)
        e = Entry(f3)

        f1 = Frame(a)
        f1.pack(side=LEFT)
        f2 = Frame(a)
        f2.pack(side=RIGHT)
        c1 = Button(f1, text="Happy", fg='red', width=12)
        c2 = Button(f2, text="Heart Broken", fg='black', width=12)
        c3 = Button(f1, text="In Love", fg='green', width=12)
        c4 = Button(f2, text="Party Mode", fg='blue', width=12)
        c5 = Button(f1, text="Dark", fg='pink', width=12)
        c6 = Button(f2, text="Dreamy", fg='orange', width=12)
        c7 = Button(f1, text="Meditative", fg='purple', width=12)
        c8 = Button(f2, text="Workout", fg='dark blue', width=12)
        c5 = Button(f3, text="back", fg='black', width=12, command=self.go_back)
        c5.pack()
        e.pack(side=TOP)
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
        b1 = Button(t, text="ALBUM",font='Courier 15 bold',bg='black', fg='steel blue1', width=8, height=8, command=self.alb_list)
        b2 = Button(t, text="SONG",font='Courier 15 bold',bg='black', fg='violet', width=8, height=8, command=self.song_list)
        b3 = Button(t, text="MOOD",font='Courier 15 bold',bg='black', fg='indian red1', width=8, height=8, command=self.mood_list)
        b4 = Button(t, text="ARTIST",font='Courier 15 bold',bg='black', fg='violet red1', width=8, height=8, command=self.art_list)

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=3)
        b4.grid(row=2, column=0)
        b3.grid(row=2, column=3)

        t.mainloop()

o = main()
