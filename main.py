from tkinter import *
t=Tk()
b1=Button(t,text="Album",fg='red')
b2=Button(t,text="Song",fg='black')
b3=Button(t,text="Mood",fg='green')
b4=Button(t,text="Song",fg='blue')
b5=Button(t,text="Playlist",fg='violet')

b1.grid(row=0,column=0)
b2.grid(row=0,column=3)
b3.grid(row=1,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=3)

t.mainloop()