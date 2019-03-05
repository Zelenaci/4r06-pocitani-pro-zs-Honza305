#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:59:59 2019

@author: mah35070
"""

import tkinter as tk
from tkinter import Label,LabelFrame, Radiobutton, Entry, Button, StringVar,IntVar, Message,END
from random import randint


class Application(tk.Tk):
    name = 'Počítání pro zš'

    def __init__(self):
        super().__init__(className=self.name)
        
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        
        self.lbl = tk.Button(self, text="Ahoj")
        self.lbl.pack()
    
        self.lbfoper = Label(self, text='Operace:', font = 'Arial')
        self.lbfoper.pack(padx = 20, pady= 10)
        
        self.p = StringVar()
        self.p.set('')
        
        #operace plus
        self.radbt = Radiobutton(self, text='+',variable =self.p ,value ='+', command = self.plus)
        self.radbt.pack(anchor= 'w')
        
        #operace minus
        self.radbt = Radiobutton(self, text='-',variable =self.p , value ='-', command = self.minus)
        self.radbt.pack(anchor= 'w')
        
        #operace krat
        self.radbt = Radiobutton(self, text='*',variable =self.p , value ='*', command = self.krat)
        self.radbt.pack(anchor= 'w')
        
        #operace deleno
        self.radbt = Radiobutton(self, text='/',variable =self.p , value ='/', command = self.deleno)
        self.radbt.pack(anchor= 'w')
        
        
        self.lab = LabelFrame(self, text = 'Výpočet', font = 'Arial')
        self.lab.pack()
        
        self.intA = IntVar()
        self.intA.set('')
       
        #A
        self.enA = Entry(self.lab, width=10, textvariable=self.intA , state ='readonly',font = 'Arial', )
        self.enA.grid(row = 1,column = 0 )
        
        #operace
        self.msg = Message(self.lab,textvariable= self.p)
        self.msg.grid(row = 1, column= 1)
        
        self.intB = IntVar()
        self.intB.set('')
        
        #B
        self.enB = Entry(self.lab, width=10,textvariable= self.intB, state ='readonly',font = 'Arial', )
        self.enB.grid(row = 1,column = 2 )
        
        #=
        self.ms = Message(self.lab, text='=', width = 30)
        self.ms.grid(row =1, column= 3)
        
        self.strV = StringVar()
        self.strV.set('')
        
        #vysledek
        self.en = Entry(self.lab,textvariable =self.strV, width=10,font = 'Arial', )
        self.en.grid(row = 1,column = 4 )
        
        
        
        #dobre/spatne
        self.labDS = LabelFrame(self, width = 5, text = 'D/Š')
        self.labDS.pack()
        
        #Dobře
        self.Dmess = Message(self.labDS, text = 'Dobře', font = 'Arial 18', pady = 15)
        self.Dmess.grid(row = 1, column = 1 ) 
        
        self.IntD = IntVar()
        self.IntD.set(0)
        
        self.envys = Entry(self.labDS, width = 10, textvariable = self.IntD )
        self.envys.grid(row = 1, column = 3)
        
        #Špatně
        self.Smess = Message(self.labDS, text = 'Špatně', font = 'Arial 18', pady = 10)
        self.Smess.grid(row = 2, column = 1)

        self.IntS = IntVar()
        self.IntS.set(0)
        
        self.envys = Entry(self.labDS, width = 10, textvariable = self.IntS )
        self.envys.grid(row = 2, column = 3)
        
        
        self.bt = Button(self, text='Výpočet', command = self.vypocet)
        self.bt.pack()
        
        self.btn = Button(self, text='Quit', command = self.quit)
        self.btn.pack()
        
        
    def plus(self):
        self.x = randint(1,99)
        self.y = randint (0,100 - self.x)
        self.v = self.x + self.y
        self.intA.set(self.x)
        self.intB.set(self.y)
        
    def minus(self):
        self.x = randint(1,99)
        self.y = randint(0, self.x)
        self.v = self.x - self.y
        self.intA.set(self.x)
        self.intB.set(self.y)
    
    def krat(self):
        self.x = randint(1,9)
        self.y = randint(0, 9)
        self.v = self.x * self.y
        self.intA.set(self.x)
        self.intB.set(self.y)
        
    def deleno(self):
        self.v = randint(1,9)
        self.y = randint(0, 9)
        self.x = self.v * self.y
        self.intA.set(self.x)
        self.intB.set(self.y)
    
    
    def vypocet(self):
        vys = str(self.v)
        uzi = self.strV.get()
        if vys == uzi:
          Dobre = self.IntD.get()  
          Dobre = Dobre +1
          self.IntD.set(Dobre)
        elif vys != uzi:
            Spatne = self.IntS.get()
            Spatne = Spatne + 1
            self.IntS.set(Spatne)
        
    def novypriklad(self):
        
        self.enA= randint(1,10)
        self.enB= randint(1,10)
         = self.enA * self.enB

        self.enA.delete(0, END)
        self.enB.insert(0, str(self.enA) )
        self.enA.delete(0, END)
        self.enB.insert(0, str(self.enB) )
        
        
        
    
app = Application()
app.mainloop()