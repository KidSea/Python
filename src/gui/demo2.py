#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
生物质热裂解反应器设计软件
'''
from tkinter import *
import tkinter.messagebox as messagebox

import tkinter.font as tkFont
import math
from tkinter.ttk import Combobox

air_list = ['空气','氢气', '氧气', '氮气']
state = 'readonly'


def getLiquid(weight, density, p, c, r):
    top = 2 * weight * 9.8 * (density - p)
    bottom = c * density * p
    temp = top / bottom
    v = math.sqrt(abs(temp))
    return round(v * math.pi * (r ** 2),2)


def getDiameter(density, radius, p):
    global n
    Q = 11.31
    C1 = 33.7
    g = 9.8
    C2 = 0.0408
    ua = 3.258 * pow(10, -5)
    Ar = ((radius ** 3) * p * (density - p) * g) / (ua)
    Re = (pow(((C1 ** 2) + C2 * Ar), 1.0 / 2)) - C1
    umf = Re * ua / p * radius
    if Ar > 1000:
        n = 4
    elif Ar < 1000:
        n = 10
    u = n * umf
    return round((4 * Q / 3360 * math.pi * u) ** 0.5,2)


def getParams(D):
    global Dy, H, b
    Dy = 0.14 * D
    if D > 0.8:
        H = 15 * D
        b = 0.8
    elif D >=0.2 and D <= 0.8:
        H = 10 * D
        b = 0.4
    elif D < 0.2:
        H = 6 * D
        b = 0.2
    return round(Dy, 2), round(H, 2) ,round(b, 2)


class Application(Tk):
    def __init__(self):
        super().__init__()
        self.createWidgets()

    def createWidgets(self):
        self.weight_tip = StringVar()
        self.weight_tip.set('Tip:')
        self.density_tip = StringVar()
        self.density_tip.set('Tip:')
        self.radius_label = Label(self, height=7, width = 15,text='物料粒径(单位mm):', font="Helvetica 12")
        self.radius_label.place(x = 50 + 30 , y = 0)
        self.radius_entry = Entry(self, width = 25, font="Helvetica 12", validate='focusout')
        #self.weight_entry.bind('<Key>', self.judgeWeightText)
        self.radius_entry.place(x = 200 + 30 , y = 55)
        self.density_label = Label(self, height=0, width = 0,text='密度(单位kg/m3):', font="Helvetica 12")
        self.density_label.place(x = 65 + 30 , y = 110)
        self.density_entry = Entry(self, width = 25, font="Helvetica 12", validate='focusout')
        #self.density_entry.bind('<Key>', self.judgeDensityText)
        self.density_entry.place(x = 200 + 30, y = 110)
        self.liquid_label = Label(self, height=0, width = 0,text='流体:', font="Helvetica 12")
        self.liquid_label.place(x = 90 + 30, y = 160)
        self.air_list_box = Combobox(self, width=12, textvariable = StringVar(), font="Helvetica 12")
        self.air_list_box['value'] = air_list
        self.air_list_box['state'] = state
        self.air_list_box.current(0)
        self.air_list_box.place(x = 200 + 30, y = 160)
        self.alertButton = Button(self, width = 20, text = "计算", command = self.caculate, font="Helvetica 12")
        self.alertButton.place(x = 200 + 30, y = 220)
        self.result_label = Label(self, height=0, width=0, text='计算结果:', font="Helvetica 12")
        self.result_label.place(x=90 + 30, y=270)
        self.result_text = Text(self,height=5,width = 35, font="Helvetica 10")
        self.result_text.place(x=200 + 30, y=270)

    def caculate(self):
        global p, c
        radius = (float)(self.radius_entry.get())
        density = (float)(self.density_entry.get())
        #print(self.air_list_box.get(), self.caliber_list_box.get())
        p = self.getAirParams(self.air_list_box.get())
        #r = self.getRadius(self.caliber_list_box.get())
        D = getDiameter(density, radius, p)
        Dy, H, b = getParams(D)
        print("value", radius, density, p, D, Dy, H, b)
        self.result_text.insert(INSERT,'Dt=' + str(D) + ' Dy=' + str(Dy) + ' H=' + str(H) + ' b='+ str(b) + '\n')


    # def judgeWeightText(self):
    #     weight = (float)(self.weight_entry.get())
    #     if weight > 5:
    #         self.weight_tip.set('Tip : 1')
    #     elif weight < 0.01:
    #         self.weight_tip.set('Tip : 2')
    #     else:
    #         self.weight_tip.set('Tip : ')
    #
    # def judgeDensityText(self):
    #     density = (float)(self.density_entry.get())
    #     if density > 2:
    #         self.density_tip.set('Tip : 1')
    #     elif density < 0.5:
    #         self.density_tip.set('Tip : 2')
    #     else:
    #         self.density_tip.set('Tip : ')

    def getRadius(self,param):
        if param == "大":
            return 20
        if param == '中':
            return 18
        if param == '小':
            return 15

    def getAirParams(self, param):
        if param == '空气':
            return 1.29
        if param == '氢气':
            return 0.0899
        if param == '氧气':
            return 1.429
        if param == '氮气':
            return 1.25

    def judgeText(self, event):
        if self.weight_entry.focus_get():
            if self.weight_entry.get() != "":
                weight = float(self.weight_entry.get())
                if weight > 5:
                    self.weight_tip.set('Tip : 1')
                elif weight < 0.01:
                    self.weight_tip.set('Tip : 2')
                else:
                    self.weight_tip.set('Tip : ')
            else:
                pass
        elif self.density_entry.focus_get():
            if self.density_entry.get() != "":
                density = float(self.density_entry.get())
                if density > 2:
                    self.density_tip.set('Tip : 1')
                elif density < 0.5:
                    self.density_tip.set('Tip : 1')
                else:
                    self.density_tip.set('Tip : 1')
            else:
                return

    def judgeWeightText(self, event):
        if self.weight_entry.get() != "":
            weight = float(self.weight_entry.get())
            if weight > 5:
                self.weight_tip.set('Tip : 1')
            elif weight < 0.01:
                self.weight_tip.set('Tip : 2')
            else:
                self.weight_tip.set('Tip : ')
        else:
            pass

    def judgeDensityText(self, event):
        if self.density_entry.get() != "":
            density = float(self.density_entry.get())
            if density > 2:
                self.density_tip.set('Tip : 1')
            elif density < 0.5:
                self.density_tip.set('Tip : 2')
            else:
                self.density_tip.set('Tip : ')
        else:
            pass


def createPanel():
    window = Tk()

    Label(window, text='User name: ').place(x=50, y=150)
    Label(window, text='Password: ').place(x=50, y=190)

    window.mainloop()


if __name__ == '__main__':
    app = Application()
    app.title("生物质热裂解反应器设计软件")
    app.geometry('600x500')
    app.mainloop()