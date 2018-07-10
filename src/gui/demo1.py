#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
风选机风选风力计算软件
'''
from tkinter import *
import tkinter.messagebox as messagebox

import tkinter.font as tkFont
import math
from tkinter.ttk import Combobox

air_list = ['空气','氢气', '氧气', '氮气']
wind_size_list = ['大', '中', '小']
state = 'readonly'


def getDiameter(density, weight):
    temp = weight / density
    return round(1.24 * math.pow(temp, 1.0 / 3), 2)


def getLiquid(weight, density, p, c, r):
    top = 2 * weight * 9.8 * (density - p)
    bottom = c * density * p
    temp = top / bottom
    v = math.sqrt(abs(temp))
    return round(v * math.pi * (r ** 2),2)


class Application(Tk):
    def __init__(self):
        super().__init__()
        self.createWidgets()

    def createWidgets(self):
        self.weight_tip = StringVar()
        self.weight_tip.set('Tip:')
        self.density_tip = StringVar()
        self.density_tip.set('Tip:')
        self.weight_label = Label(self, height=8, width = 15,text='质量(单位kg):', font="Helvetica 12")
        self.weight_label.place(x = 70 + 30 , y = 0)
        self.weight_entry = Entry(self, width = 25, font="Helvetica 12", validate='focusout')
        self.weight_entry.bind('<Key>', self.judgeWeightText)
        self.weight_entry.place(x = 200 + 30 , y = 55)
        self.weight_tip_label = Label(self, height=8, width = 10, textvariable = self.weight_tip, font="Helvetica 12")
        self.weight_tip_label.place(x = 420 + 30 , y = 0)
        self.density_label = Label(self, height=5, width = 20,text='密度(单位kg/m3):', font="Helvetica 12")
        self.density_label.place(x = 50 + 30 , y = 80)
        self.density_entry = Entry(self, width = 25, font="Helvetica 12", validate='focusout')
        self.density_entry.bind('<Key>', self.judgeDensityText)
        self.density_entry.place(x = 200 + 30, y = 110)
        self.density_tip_label = Label(self, height=5, width = 10, textvariable = self.density_tip, font="Helvetica 12")
        self.density_tip_label.place(x = 420 + 30 , y = 80)
        self.liquid_label = Label(self, height=5, width = 20,text='流体:', font="Helvetica 12")
        self.liquid_label.place(x = 20 + 30, y = 130)
        self.air_list_box = Combobox(self, width=12, textvariable = StringVar(), font="Helvetica 12")
        self.air_list_box['value'] = air_list
        self.air_list_box['state'] = state
        self.air_list_box.current(0)
        self.air_list_box.place(x = 200 + 30, y = 160)
        self.caliber_label = Label(self, height=5, width=20, text='风机口径:', font="Helvetica 12")
        self.caliber_label.place(x=35 + 30, y=180)
        self.caliber_list_box = Combobox(self, width=12, textvariable=StringVar(), font="Helvetica 12")
        self.caliber_list_box['value'] = wind_size_list
        self.caliber_list_box['state'] = state
        self.caliber_list_box.current(0)
        self.caliber_list_box.place(x=200 + 30, y=210)
        self.alertButton = Button(self, width = 20, text = "计算", command = self.caculate, font="Helvetica 12")
        self.alertButton.place(x = 200 + 30, y = 250)
        self.result_label = Label(self, height=5, width=20, text='计算结果:', font="Helvetica 12")
        self.result_label.place(x=35 + 30, y=280)
        self.result_text = Text(self,height=5,width = 25, font="Helvetica 12")
        self.result_text.place(x=200 + 30, y=300)

    def caculate(self):
        global p, c
        weight = (float)(self.weight_entry.get())
        density = (float)(self.density_entry.get())
        print(self.air_list_box.get(), self.caliber_list_box.get())
        p, c = self.getAirParams(self.air_list_box.get())
        r = self.getRadius(self.caliber_list_box.get())
        d = getDiameter(density, weight)
        Q = getLiquid(weight, density, p, c, r)
        print("value", weight, density, p, c, r, d, Q)


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
            return 1.29, 3.02
        if param == '氢气':
            return 0.0899, 2.17
        if param == '氧气':
            return 1.429, 3.52
        if param == '氮气':
            return 1.25, 2.99

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
    app.title("风选机风选风力计算软件")
    app.geometry('600x500')
    app.mainloop()