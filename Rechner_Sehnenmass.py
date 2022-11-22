from tkinter import *
import math 

def buttonBinS():
    Bogenmass = float(entryBogenmass.get())
    Durchmesser1 = float(entryZylinderdurchmesser1.get())
    radius1 = Durchmesser1/2
    alpha = Bogenmass/radius1
    #Sehnenmass aurechnen, resultat1 = Sehnenmass
    resultat1 = 2 * radius1 * math.sin(alpha/2)
    resultat1Anzeige = str(round(resultat1*10)/10)
    labelSm.config(text=resultat1Anzeige)
    
    #Prozent Sehenmass
    ProzentS = resultat1/Durchmesser1*100
    
    ProzentSAnzeige = str(round(ProzentS*10)/10)
    labelSmP.config(text=ProzentSAnzeige)
    
def buttonSinB():
    
    Sehnenmass = float(entrySehenmass.get())
    Durchmesser2 = float(entryZylinderdurchmesser2.get())
    #Bogenmass ausrechnen, resulat2 = Bogenmass
    radius2 = Durchmesser2/2
    beta = 2*math.asin(Sehnenmass/(radius2*2))
    resultat2 = radius2*beta
    resultat2Anzeige = str(round(resultat2*10)/10)
    labelBm.config(text=resultat2Anzeige)
    
    #Prozent Sehnenmass
    ProzentB = Sehnenmass/Durchmesser2*100
    
    ProzentBAnzeige = str(round(ProzentB*10)/10)
    labelBmP.config(text=ProzentBAnzeige)


tkFenster = Tk()
tkFenster.title('Rechner')
tkFenster.geometry('600x235')

labelBogenmass = Label(master=tkFenster, bg='#FFCFC9', text='Bogenmass in mm:')
labelBogenmass.place(x=34, y=24, width=160, height=27)

entryBogenmass = Entry(master=tkFenster, bg='white')
entryBogenmass.place(x=204, y=24, width=60, height=27)

labelZylinderdurchmesser1 = Label(master=tkFenster, bg='#FFCFC9', text='Zylinderdurchmesser in mm:')
labelZylinderdurchmesser1.place(x=34, y=64, width=160, height=27)

entryZylinderdurchmesser1 = Entry(master=tkFenster, bg='white')
entryZylinderdurchmesser1.place(x=204, y=64, width=60, height=27)

buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='Berechnen', command=buttonBinS)
buttonBerechnen.place(x=34, y=104, width=160, height=27)

labelSmWert = Label(master=tkFenster, bg='#D5E88F', text='Sehnenmass in mm:')
labelSmWert.place(x=34, y=144, width=160, height=27)

labelSm = Label(master=tkFenster, bg='gray', text='')
labelSm.place(x=204, y=144, width=60, height=27)


labelSmPWert = Label(master=tkFenster, bg='#D5E88F', text='Prozent Sehnenmass:')
labelSmPWert.place(x=34, y=184, width=160, height=27)

labelSmP = Label(master=tkFenster, bg='gray', text='')
labelSmP.place(x=204, y=184, width=60, height=27)


print("")

labelSehenmass = Label(master=tkFenster, bg='#FFCFC9', text='Sehnenmass in mm:')
labelSehenmass.place(x=318, y=24, width=160, height=27)

entrySehenmass = Entry(master=tkFenster, bg='white')
entrySehenmass.place(x=488, y=24, width=60, height=27)

labelZylinderdurchmesser2 = Label(master=tkFenster, bg='#FFCFC9', text='Zylinderdurchmesser in mm:')
labelZylinderdurchmesser2.place(x=318, y=64, width=160, height=27)

entryZylinderdurchmesser2 = Entry(master=tkFenster, bg='white')
entryZylinderdurchmesser2.place(x=488, y=64, width=60, height=27)

buttonBerechnen = Button(master=tkFenster, bg='#FBD975', text='Berechnen', command=buttonSinB)
buttonBerechnen.place(x=318, y=104, width=160, height=27)

labelBmWert = Label(master=tkFenster, bg='#D5E88F', text='Bogenmass in mm:')
labelBmWert.place(x=318, y=144, width=160, height=27)

labelBm = Label(master=tkFenster, bg='gray', text='')
labelBm.place(x=488, y=144, width=60, height=27)

labelBmPWert = Label(master=tkFenster, bg='#D5E88F', text='Prozent Sehnenmass:')
labelBmPWert.place(x=318, y=184, width=160, height=27)

labelBmP = Label(master=tkFenster, bg='gray', text='')
labelBmP.place(x=488, y=184, width=60, height=27)

tkFenster.mainloop()