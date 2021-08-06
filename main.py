import tkinter as tk
import yfinance as yf
import matplotlib.pyplot as plt
import os
from tkinter import *
from datetime import date
from PIL import Image, ImageTk

today = date.today()
root= tk.Tk()

d2 = str(today.strftime("%d"))
if(d2[0] == "0"):
    d2 = d2[1]
d3 = today.strftime("%B " + d2)

canvas1 = tk.Canvas(root, width = 900, height = 500, highlightthickness=0)
canvas1.pack(fill=tk.BOTH)

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
        plt.savefig(x1 + '.png', transparent = True)
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
def OnHover2(event):
    event.widget.config(bg='lightgrey', cursor="hand2")
def OnLeave2(event):
    event.widget.config(bg='#F0F0F0')

#'Get Stock Data' Button
button1 = Label(root, text='Get Stock Data', relief=FLAT)
button1.bind('<Button-1>', OnPressed)
button1.bind('<Enter>', OnHover2)
button1.bind('<Leave>', OnLeave2)
canvas1.create_window(89, 115, window=button1)

def getStockDataMenu(x1):
    try:
        ticker = yf.Ticker(x1)
        newtime = yf.download(x1, start = "2014-01-01")
        newtime['Close'].plot()
        plt.xlabel("Date")
        plt.ylabel("Price")
        label = yf.Ticker(x1)
        company_name = label.info['longName']
        plt.title(company_name + " Price Chart")
        plt.savefig(x1 + '.png', transparent = True)
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

def OnPressedMenu(event):
    search = str(event.widget)
    if(search[-1] == "4"):
        getStockDataMenu("AAPL")
    if(search[-1] == "5"):
        getStockDataMenu("MSFT")
    if(search[-1] == "6"):
        getStockDataMenu("TSLA")
    if(search[-1] == "7"):
        getStockDataMenu("GOOGL")  
    if(search[-1] == "8"):
        getStockDataMenu("AMZN")      
def OnHoverAPPL(event):
    event.widget.config(bg='lightgrey', cursor="hand2",padx=83, pady=13)
def OnLeaveAPPL(event):
    event.widget.config(bg='#F0F0F0' ,padx=0, pady=0)

AAPL = Label(root, text='AAPL', relief=FLAT)
AAPL.bind('<Button-1>', OnPressedMenu)
AAPL.bind('<Enter>', OnHoverAPPL)
AAPL.bind('<Leave>', OnLeaveAPPL)
canvas1.create_window(90, 167, window=AAPL)

def OnHoverMSFT(event):
    event.widget.config(bg='lightgrey', cursor="hand2",padx=83, pady=13)
def OnLeaveMSFT(event):
    event.widget.config(bg='#F0F0F0' ,padx=0, pady=0)

MSFT = Label(root, text='MSFT', relief=FLAT)
MSFT.bind('<Button-1>', OnPressedMenu)
MSFT.bind('<Enter>', OnHoverMSFT)
MSFT.bind('<Leave>', OnLeaveMSFT)
canvas1.create_window(90, 213, window=MSFT)

def OnHoverTSLA(event):
    event.widget.config(bg='lightgrey', cursor="hand2",padx=85, pady=14)
def OnLeaveTSLA(event):
    event.widget.config(bg='#F0F0F0' ,padx=0, pady=0)

TSLA = Label(root, text='TSLA', relief=FLAT)
TSLA.bind('<Button-1>', OnPressedMenu)
TSLA.bind('<Enter>', OnHoverTSLA)
TSLA.bind('<Leave>', OnLeaveTSLA)
canvas1.create_window(90, 260, window=TSLA)

def OnHoverGOOGL(event):
    event.widget.config(bg='lightgrey', cursor="hand2",padx=78, pady=14)
def OnLeaveGOOGL(event):
    event.widget.config(bg='#F0F0F0' ,padx=0, pady=0)

GOOGL = Label(root, text='GOOGL', relief=FLAT)
GOOGL.bind('<Button-1>', OnPressedMenu)
GOOGL.bind('<Enter>', OnHoverGOOGL)
GOOGL.bind('<Leave>', OnLeaveGOOGL)
canvas1.create_window(90, 308, window=GOOGL)

def OnHoverAMZN(event):
    event.widget.config(bg='lightgrey', cursor="hand2",padx=80, pady=13)
def OnLeaveAMZN(event):
    event.widget.config(bg='#F0F0F0' ,padx=0, pady=0)

AMZN = Label(root, text='AMZN', relief=FLAT)
AMZN.bind('<Button-1>', OnPressedMenu)
AMZN.bind('<Enter>', OnHoverAMZN)
AMZN.bind('<Leave>', OnLeaveAMZN)
canvas1.create_window(90, 355, window=AMZN)


canvas1.create_line(190,0,190,530)
canvas1.create_line(0,144,190,144)

#Border around get stock data button
canvas1.create_line(47,105,47,126)
canvas1.create_line(131,105,131,126)
canvas1.create_line(47,104,132,104)
canvas1.create_line(47,126,132,126)

canvas1.create_line(0,190,190,190)
canvas1.create_line(0,236,190,236)
canvas1.create_line(0,284,190,284)
canvas1.create_line(0,332,190,332)
canvas1.create_line(0,378,190,378)

canvas1.configure(bg='#F0F0F0')
root.title("Real-Time Stocks by Zak Haider")
root.resizable(False, False) 
root.mainloop()