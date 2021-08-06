import tkinter as tk
from tkinter import *
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
from PIL import Image, ImageTk
import os

today = date.today()
root= tk.Tk()

d2 = str(today.strftime("%d"))
if(d2[0] == "0"):
    d2 = d2[1]
d3 = today.strftime("%B " + d2)

canvas1 = tk.Canvas(root, width = 900, height = 500,  relief = 'raised')
canvas1.pack()

#Stock Label
label1 = tk.Label(root, text='Stocks')
label1.config(font=('helvetica', 14))
canvas1.create_window(87, 25, window=label1)

#Date Label
label2 = tk.Label(root, text=d3)
label2.config(font=('helvetica', 10))
canvas1.create_window(87, 45, window=label2)

#Search Box
entry1 = tk.Entry (root) 
placeholder_text = 'Enter a stock symbol..'
entry1.insert(0, placeholder_text)
entry1.bind("<Button-1>", lambda args: entry1.delete('0', 'end'))
entry1.config(font=('helvetica', 10))
canvas1.create_window(92, 80, window=entry1)

#Graph
flag = False
def getStockData():
    try:
        x1 = entry1.get()
        ticker = yf.Ticker(x1)
        newtime = yf.download(x1, start = "2014-01-01")
        newtime['Close'].plot()
        plt.xlabel("Date")
        plt.ylabel("Price")
        label = yf.Ticker(x1)
        company_name = label.info['longName']
        plt.title(company_name + " Price Chart")
        plt.savefig(x1 + '.png')
        plt.clf()
        
        image1 = Image.open(x1 + ".png")
        test = ImageTk.PhotoImage(image1)
        label3 = tk.Label(root, image=test)
        label3.image = test
        label3.place(x=225,y=10)
        if(os.path.exists(x1 + ".png")):
            os.remove(x1 + ".png")
    except:
        error_label = tk.Label(root, text="Could not load stock data! Try again or type a new symbol")
        error_label.config(font=('helvetica', 14))
        error_label.place(x=300,y=200)

def OnPressed(event):
    getStockData()
def OnHover(event):
    event.widget.config(bg='navy', fg='white')
def OnLeave(event):
    event.widget.config(bg='white', fg='black')


#'Get Stock Data' Button
button1 = Label(root, text='Get Stock Data', bg='white', relief=FLAT)
button1.bind('<Button-1>', OnPressed)
button1.bind('<Enter>', OnHover)
button1.bind('<Leave>', OnLeave)
canvas1.create_window(89, 115, window=button1)


AAPL = Label(root, text='AAPL', bg='white', relief=FLAT)
AAPL.bind('<Button-1>', OnPressed)
AAPL.bind('<Enter>', OnHover)
AAPL.bind('<Leave>', OnLeave)
canvas1.create_window(125, 350, window=AAPL)



canvas1.create_line(190,-10,190,530)
canvas1.create_line(0,143,190,143)

#Border around get stock data button
canvas1.create_line(47,105,47,126)
canvas1.create_line(131,105,131,126)
canvas1.create_line(47,104,132,104)
canvas1.create_line(47,126,132,126)

canvas1.create_line(0,190,190,190)
canvas1.create_line(0,237,190,237)
canvas1.create_line(0,284,190,284)
canvas1.create_line(0,331,190,331)
canvas1.create_line(0,378,190,378)

root.title("Created by Zak Haider")
root.resizable(False, False) 
root.mainloop()