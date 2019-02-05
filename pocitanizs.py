#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:59:59 2019

@author: mah35070
"""

import tkinter as tk
from tkinter import Label,LabelFrame, Radiobutton, Entry, Button, StringVar
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
        
        self.radbt = Radiobutton(self, text='+',variable =self.p ,value ='+', command = self.plus)
        self.radbt.pack(anchor= 'w')
        
        self.radbt = Radiobutton(self, text='-',variable =self.p , value ='-', command = self.minus)
        self.radbt.pack(anchor= 'w')
        
        self.radbt = Radiobutton(self, text='*',variable =self.p , value ='*', command = self.krat)
        self.radbt.pack(anchor= 'w')
        
        self.radbt = Radiobutton(self, text='/',variable =self.p , value ='/', command = self.deleno)
        self.radbt.pack(anchor= 'w')
        
        self.lab = LabelFrame(self, text = 'Výpočet', font = 'Arial')
        self.lab.pack()
        
        self.en = Entry(self.lab, width=10, state ='readonly',font = 'Arial', )
        self.en.grid(row =1,column = 1 )
        
        self.en = Entry(self.lab, width=10, state ='readonly',font = 'Arial', )
        self.en.grid(row =1,column = 2 )
        #self.but = Button(self, text='Nový příklad', command = self.)
        
        self.bt = Button(self, text='Výpočet', command = self.vypocet)
        self.bt.pack()
        
        self.btn = Button(self, text='Quit', command = self.quit)
        self.btn.pack()
        
    def plus(self):
        self.x = randint(1,99)
        self.y = randint (0,100 - self.x)
        self.v = self.x + self.y
    
    
    def minus(self):
        self.x = randint(1,99)
        self.y = randint(0, self.x)
        self.v = self.x - self.y
    
    def krat(self):
        self.x = randint(1,9)
        self.y = randint(0, 9)
        self.v = self.x * self.y
    
    def deleno(self):
        self.x = randint(1,9)
        self.y = randint(0, 9)
        self.x = self.v * self.y
    
    def vypocet(self):
        Operace(self.plus, self.minus, self.krat, self.deleno)
        nahoda = randint(0, 3)
        funkce = Operace[nahoda]
        funkce()
        print()
        print(self.x, funkce.__name__, self.y, '=', self.vysl)
    
    
app = Application()
app.mainloop()