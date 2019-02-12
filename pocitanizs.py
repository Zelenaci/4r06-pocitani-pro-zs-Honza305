#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:59:59 2019

@author: mah35070
"""

import tkinter as tk
from tkinter import Label,LabelFrame, Radiobutton, Entry, Button, StringVar,IntVar, Message
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
        self.en = Entry(self.lab, width=10, textvariable=self.intA , state ='readonly',font = 'Arial', )
        self.en.grid(row = 1,column = 0 )
        
        #operace
        self.msg = Message(self.lab,textvariable= self.p)
        self.msg.grid(row = 1, column= 1)
        
        self.intB = IntVar()
        self.intB.set('')
        
        #B
        self.en = Entry(self.lab, width=10,textvariable= self.intB, state ='readonly',font = 'Arial', )
        self.en.grid(row = 1,column = 2 )
        
        #=
        self.ms = Message(self.lab, text='=', width = 30)
        self.ms.grid(row =1, column= 3)
        
        self.intV = IntVar()
        self.intV.set('')
        
        #vysledek
        self.en = Entry(self.lab,textvariable =self.intV, width=10,font = 'Arial', )
        self.en.grid(row = 1,column = 4 )
        
        #Hodnocení
        #self.labl = Label(self.lab,width= 10, text='?')
        #self.labl.grid(row = 2, column=0)
        
        #dobre/spatne
        self.labl= Label(self.lab,width= 5, text='D/Š')
        self.labl.grid(row=3,column = 3)
        
        self.labl = Label(self.lab,width= 5, text='0')
        self.labl.grid(row=3, column = 4)
        
        self.labl = Label(self.lab,width= 5, text='0')
        self.labl.grid(row=3, column = 5)
        
        #self.but = Button(self, text='Nový příklad', command = self.)
        
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
        Operace(self.plus, self.minus, self.krat, self.deleno)
        nahoda = randint(0, 3)
        funkce = Operace[nahoda]
        funkce()
        print()
        print(self.x, funkce.__name__, self.y, '=', self.vysl)
    
    
app = Application()
app.mainloop()