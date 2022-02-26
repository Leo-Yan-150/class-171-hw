from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

print('Timezones')
for timeZone in pytz.all_timezones:
    print(timeZone)

root=Tk()
root.geometry("1200x850")
guns = ImageTk.PhotoImage(Image.open("amurica.jpeg"))
sushi = ImageTk.PhotoImage(Image.open("japan.png"))
emus = ImageTk.PhotoImage(Image.open("aussie.jpeg"))
spices = ImageTk.PhotoImage(Image.open("india.png"))
#-------india-------
ilabel=Label(root, text="India")
ilabel.place(relx=0.2,rely=0.05,anchor=CENTER)

iclock = Label(root)
iclock["image"]=spices
iclock.place(relx=0.2,rely=0.20,anchor=CENTER)

itime=Label(root)
itime.place(relx=0.2,rely=0.35,anchor=CENTER)
#------AMURICA-----
ulabel=Label(root, text="AMURICA")
ulabel.place(relx=0.7,rely=0.05,anchor=CENTER)

uclock = Label(root)
uclock["image"]=guns
uclock.place(relx=0.7,rely=0.20,anchor=CENTER)

utime=Label(root)
utime.place(relx=0.7,rely=0.35,anchor=CENTER)
#------Aussie------
alabel=Label(root, text="Australia")
alabel.place(relx=0.2,rely=0.55,anchor=CENTER)

aclock = Label(root)
aclock["image"]=emus
aclock.place(relx=0.2,rely=0.70,anchor=CENTER)

atime=Label(root)
atime.place(relx=0.2,rely=0.85,anchor=CENTER)
#------Japan------
clabel=Label(root, text="Japan")
clabel.place(relx=0.7,rely=0.55,anchor=CENTER)

cclock = Label(root)
cclock["image"]=sushi
cclock.place(relx=0.7,rely=0.70,anchor=CENTER)

ctime=Label(root)
ctime.place(relx=0.7,rely=0.85,anchor=CENTER)

class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        lt = datetime.now(home)
        ct = lt.strftime("%H:%M:%S")
        itime["text"]="Current time in India is " + ct
        itime.after(200,self.times)
class AMURICA():
    def times(self):
        home=pytz.timezone('US/Pacific')
        lt = datetime.now(home)
        ct = lt.strftime("%H:%M:%S")
        utime["text"]="Current time in AMURICA is " + ct
        utime.after(200,self.times)
class Aussie():
    def times(self):
        home=pytz.timezone('Australia/ACT')
        lt = datetime.now(home)
        ct = lt.strftime("%H:%M:%S")
        atime["text"]="Current time in Australia is " + ct
        ctime.after(200,self.times)
class Japan():
    def times(self):
        home=pytz.timezone('Asia/Tokyo')
        lt = datetime.now(home)
        ct = lt.strftime("%H:%M:%S")
        ctime["text"]="Current time in Japan is " + ct
        ctime.after(200,self.times)

objectinindia = India()
thatthinyinamurica = AMURICA()
thatemu = Aussie()
moresushi = Japan()
ibtn = Button(root, text="Show Time", command=objectinindia.times)
ibtn.place(relx=0.2, rely = 0.40, anchor=CENTER)
ubtn = Button(root, text="Show Time", command=thatthinyinamurica.times)
ubtn.place(relx=0.7, rely = 0.40, anchor=CENTER)
cbtn = Button(root, text="Show Time", command=moresushi.times)
cbtn.place(relx=0.7, rely = 0.90, anchor=CENTER)
abtn = Button(root, text="Show Time", command=thatemu.times)
abtn.place(relx=0.2, rely = 0.90, anchor=CENTER)

root.mainloop()