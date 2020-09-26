from tkinter import *
from tkinter import messagebox

window = Tk()
#function conver Kg to G
def ConvertKgtoG():
                tmp = float(txtIn.get())*1000;
                messagebox.showinfo('Kilograms To Grams',str(tmp) + ' Grams')
#function conver Kg to Metric Tons
def ConvertKgtoMT():
                tmp = float(txtIn.get())/1000;
                messagebox.showinfo('Kilograms to Metric Tons',str(tmp) + ' Metric Tons')
#function conver Kg to Pounds
def ConvertKgtoP():
                tmp = float(txtIn.get())*2.20462262;
                messagebox.showinfo('Kilograms to Pounds',str(tmp) + ' Pounds')
#Create input
txtIn = Entry(window,width = 20)
txtIn.grid(column = 0,row = 0)
window.title("Convert Kilogram")
#add Convert Gram Button
btnG = Button(window,bg ="darkblue",fg = "white",
                text="To Grams", command = ConvertKgtoG)
btnG.grid(column=1, row=0)
#add Convert miliGram Button
btnMG = Button(window,bg ="green",fg = "red",
               text="To Metric Tons", command = ConvertKgtoMT)
btnMG.grid(column=2, row=0)
#add COnver pounds Button
btnP = Button(window, bg ="Black",fg = "white" ,
              text="To Pounds", command = ConvertKgtoP)
btnP.grid(column=3, row=0)

window.mainloop()
