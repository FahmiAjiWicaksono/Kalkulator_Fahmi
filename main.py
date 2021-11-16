from tkinter import *
from tkinter.font import BOLD
from tkinter.messagebox import *
import math as m
import threading
import tkinter as tk

#Variable Huruf
huruf = ('Franklin Gothic Book', 24, BOLD)


#Definisi
def hapussedikit():
    hilangsatu = LayarHitung.get()
    hilangsatu = hilangsatu[0:len(hilangsatu) - 1]
    LayarHitung.delete(0, END)
    LayarHitung.insert(0, hilangsatu)


def hapussemua():
    LayarHitung.delete(0, END)


def notiftertekan(event):
    global p
    print("Tombol tertekan")
    b = event.widget
    text = b['text']
    print(text)
    t = threading.Thread( args=(text,))
    t.start()

    if text == 'x':
        LayarHitung.insert(END, "*")
        return

    if text == '=':
        try:
            ex = LayarHitung.get()
            anser = eval(ex)
            LayarHitung.delete(0, END)
            LayarHitung.insert(0, anser)
        except Exception as e:
            print("Masukan input dengan benar")
            showerror("Peringatan","Masukan input dengan benar/pastikan input terisi")
        return

    LayarHitung.insert(END, text)


# Pengaturan jendela
jendela = Tk()
jendela.title('Kalkulator Fahmi')
jendela.geometry('435x440')
jendela.config(bg='#FFFFFF')


# Nama Label
kepala = Label(jendela, text='Kalkulator Fahmi', font=huruf, underline=0, bg='#FFFFFF', fg='#272533')
kepala.pack(side=TOP)

# Layar hitung
LayarHitung = Entry(jendela, font=huruf,bg='#ECA527', justify=CENTER)
LayarHitung.pack(side=TOP, pady=10, fill=X, padx=10)

# Tombol 
Tombol = Frame(jendela)
Tombol.pack(side=TOP, padx=0)

# Setting Tombol
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(Tombol, text=str(temp), font=huruf, width=5, relief='ridge', activebackground='orange',
                     activeforeground='black',bg='#272533',fg='orange', highlightthickness=0 )
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind('<Button-1>', notiftertekan)

tombolnol = Button(Tombol, text='0', font=huruf, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white',bg='#272533',fg='orange', highlightthickness=0)
tombolnol.grid(row=3, column=0)

titik = Button(Tombol, text='.', font=huruf, width=5, relief='ridge', activebackground='orange',
                activeforeground='white',bg='#272533',fg='orange', highlightthickness=0)
titik.grid(row=3, column=1)

jumlah = Button(Tombol, text='=', font=huruf, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white',bg='#272533',fg='orange', highlightthickness=0)
jumlah.grid(row=3, column=2)

tambah = Button(Tombol, text='+', font=huruf, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white',bg='#272533',fg='orange', highlightthickness=0)
tambah.grid(row=0, column=3)

kurangi = Button(Tombol, text='-', font=huruf, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white',bg='#272533',fg='orange', highlightthickness=0)
kurangi.grid(row=1, column=3)

kali = Button(Tombol, text='x', font=huruf, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white',bg='#272533',fg='orange', highlightthickness=0)
kali.grid(row=2, column=3)

bagi = Button(Tombol, text='/', font=huruf, width=5, relief='ridge', activebackground='orange',
                   activeforeground='white',bg='#272533',fg='orange', highlightthickness=0)
bagi.grid(row=3, column=3)

HapusDikitBtn = Button(Tombol, text='<--', font=huruf, width=11, relief='ridge', activebackground='orange',
                  activeforeground='white', command=hapussedikit,bg='orange',fg='#272533', highlightthickness=0)
HapusDikitBtn.grid(row=4, column=0, columnspan=2)

HapusSemuaa= Button(Tombol, text='AC', font=huruf, width=11, relief='ridge', activebackground='orange',
                     activeforeground='white', command=hapussemua,bg='orange',fg='#272533', highlightthickness=0)
HapusSemuaa.grid(row=4, column=2, columnspan=2)

tambah.bind('<Button-1>', notiftertekan)
kurangi.bind('<Button-1>', notiftertekan)
kali.bind('<Button-1>', notiftertekan)
bagi.bind('<Button-1>', notiftertekan)
tombolnol.bind('<Button-1>', notiftertekan)
titik.bind('<Button-1>', notiftertekan)
jumlah.bind('<Button-1>', notiftertekan)


def Tes(event):
    print('Hai!')
    e = Event()
    e.widget = jumlah
    notiftertekan(e)


LayarHitung.bind('<Return>', Tes)

jendela.mainloop()
