import tkinter as tk
from forex_python.converter import CurrencyRates
selectedfrom = None
selectedto = None
rates = CurrencyRates()
get = rates.get_rate('GBP', 'USD')
print(get)


root = tk.Tk()
root.title("Currency Converter")
root.geometry("800x600")

welcome = tk.Label(root, text="Welcome to the Currency Converter!", font=("Helvetica", 16))
welcome.pack(pady=20)

Info = tk.Label(root, text="Please enter the amount to convert:", font=("Helvetica", 12))
Info.pack(pady=20)
box1 = tk.Spinbox(root, from_=0, to=10000, width=20)

info1 = tk.Label(root, text="Please select a currency to convert from:", font=("Helvetica", 12))
box1.pack(pady=10)
info1.pack(pady=5)


def onselect1(evt):
    global selectedfrom
    
    w = evt.widget
    index = int(w.curselection()[0])
    selectedfrom = w.get(index)
    print('You selected currency to convert from:', selectedfrom)
    
  
def onselect2(evt2):
    global selectedto
    w2 = evt2.widget
    index2 = int(w2.curselection()[0])
    selectedto = w2.get(index2)
    print('You selected currency to convert to:', selectedto)
    

lv1 = tk.Listbox(root, width=20, height=5, exportselection=False)

lv1.insert(1, "USD")
lv1.insert(2, "EUR")
lv1.insert(3, "GBP")
lv1.insert(4, "JPY")
lv1.insert(5, "AUD")
lv1.insert(6, "CAD")

lv1.pack(pady=10)

lv1.bind('<<ListboxSelect>>', onselect1)



    
info2 = tk.Label(root, text="Please select a currency to convert to:", font=("Helvetica", 12))
info2.pack(pady=5)

lv2 = tk.Listbox(root, width=20, height=5, exportselection=False)
lv2.insert(1, "USD")
lv2.insert(2, "EUR")
lv2.insert(3, "GBP")
lv2.insert(4, "JPY")
lv2.insert(5, "AUD")
lv2.insert(6, "CAD")

lv2.pack(pady=10)
lv2.bind('<<ListboxSelect>>', onselect2)

text = tk.Label(root,text="", font=("Helvetica", 12))

def convert():
    global v
    from_currency = lv1.get(lv1.curselection()[0])
    to_currency = lv2.get(lv2.curselection()[0])
    amount = rates.convert(from_currency, to_currency, round(float(box1.get()), 2))
    amt2 = round(amount,2)
    startamt = round(float(box1.get()),2)
    
    v = f"{startamt} {from_currency} is equal to {amt2} {to_currency}"
    text.config(text=v)

    print(startamt, from_currency, "is equal to",amt2, to_currency)


text.pack(pady=10)
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=20)
print(selectedfrom, selectedto)
root.mainloop()

#by rafaelcaruana
