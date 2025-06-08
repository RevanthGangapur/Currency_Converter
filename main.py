import tkinter as tk
from currency_converter import CurrencyConverter
c=CurrencyConverter()

window = tk.Tk()
window.geometry("500x360")
window.title("CURRENCY CONVERTER")

def clicked():
    amount =int(entry1.get())
    cur1=entry2.get()
    cur2 = entry3.get()
    data = c.convert(amount,cur1,cur2)
    label4 = tk.Label(window,text=f"{data} in {cur2}").place(x=200,y=300)

label = tk.Label(window,text= "Currency Converter",font= "Times 20 bold").place(x=120,y=10)

label1 = tk.Label(window,text= "Amount:",font= "Times 16 bold").place(x=120,y=100)
entry1 = tk.Entry(window)

label2 = tk.Label(window,text= "From:",font= "Times 16 bold").place(x=120,y=150)
entry2 = tk.Entry(window)

label3 = tk.Label(window,text= "To:",font= "Times 16 bold").place(x=120,y=200)
entry3 = tk.Entry(window)

button = tk.Button(window,text= "convert",font = "Times 12 bold",command=clicked).place(x=220,y=240)
entry1.place(x=270,y=105)
entry2.place(x=270,y=155)
entry3.place(x=270,y=205)
label5= tk.Label(window,text="NOTE: Enter currency code in Uppercase ",font = "Times 12 bold").place(x=100,y=50)

window.mainloop()