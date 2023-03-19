from tkinter import  messagebox , Label,Tk,ttk
from time import   strftime
from pygame import mixer
from tkinter.font import Font
import os 

window = Tk()
window.title("Horloge")
window.geometry("500x250")
window.config(bg="pink")
window.minsize(500,250)
window.maxsize(500,250)
mixer.init()

liste_heures = []
liste_minutes = []
liste_secondes = []

for i in range(24):
    liste_heures.append(i)
for i in range(60):
    liste_minutes.append(i)
    liste_secondes.append(i)

texte_heures = Label(window, text="Heures", bg="pink", fg="white", font=("Arial", 15))
texte_heures.grid(row = 1, column = 0, padx = 5, pady = 5)
texte_minutes = Label(window, text="Minutes", bg="pink", fg="white", font=("Arial", 15))
texte_minutes.grid(row = 1, column = 1, padx = 5, pady = 5)
texte_secondes = Label(window, text="Secondes", bg="pink", fg="white", font=("Arial", 15))
texte_secondes.grid(row = 1, column = 2, padx = 5, pady = 5)


combobox1 = ttk.Combobox(window, values = liste_heures , style = "TCombobox", justify='center',width='10', font='Arial')
combobox1.grid(row=2, column=0, padx =15, pady=5)
combobox1.current(0)
combobox2 = ttk.Combobox(window, values = liste_minutes , style = "TCombobox", justify='center',width='10', font='Arial')
combobox2.grid(row=2, column=1, padx =15, pady=5)
combobox2.current(0)
combobox3 = ttk.Combobox(window, values = liste_secondes, style = "TCombobox", justify='center',width='10', font='Arial')
combobox3.grid(row=2, column=2, padx =15, pady=5)
combobox3.current(0)


window.option_add('*TCombobox*Listbox*Background', 'white')
window.option_add('*TCombobox*Listbox*Foreground', 'black')
window.option_add('*TCombobox*Listbox*selectBackground', 'green2')
window.option_add('*TCombobox*Listbox*selectForeground', 'black')


alarme = Label(window, text="Alarme", bg="pink", fg="white", font=("mafont.TTF", 15))
alarme.grid(row = 3, column = 0, padx = 10, pady = 10)
repeter = Label(window, text="Répéter", bg="pink", fg="white", font=("Arial", 15))
repeter.grid(row = 3, column = 1, padx = 10, pady = 10)
quantite = ttk.Combobox(window, values = (1,2,3,4,5), justify='center',width='10', font='Arial')
quantite.grid(row=4, column=1, padx =15, pady=5)
quantite.current(0)


def alarme_sonne():
    x_heure = combobox1.get()
    x_minutes = combobox2.get()
    x_secondes = combobox3.get()

    heure = strftime('%H')
    minutes = strftime('%M')
    secondes = strftime('%S')

    heure_complete = (heure + ":" + minutes + ":" + secondes)
    texte_heures.config(text=heure_complete, font = ("font/font1.TTF", 25))

    heure_alarme = x_heure + ":" + x_minutes + ":" + x_secondes
    alarme['text'] = heure_alarme

    if int(heure) == int(x_heure):
        if int(minutes) == int(x_minutes):
            if int(secondes) == int(x_secondes):
                mixer.music.load("audio.mp3")
                mixer.music.play(loops = int(quantite.get()))
                messagebox.showinfo(message = heure_alarme, title= "Alarme")

    window.after(100, alarme_sonne)

texte_heures = Label(window, text="Heures", bg="pink", fg="white", font=("Arial", 25))
texte_heures.grid(row = 0, columnspan = 3, padx = 10, pady = 10)



alarme_sonne()




window.mainloop()
