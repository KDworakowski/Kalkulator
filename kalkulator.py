#kalkulator

from tkinter import *

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Kalkulator Kacperka")
root.config(bg = 'gray50')

Label(root, 
    text = "Kalkulator", 
    font = "arial 35 bold", 
    bg = "gray50", 
    fg = "snow"
).pack()

liczba1 = StringVar()
Label(root, 
    text = "Wpisz liczbe nr 1:", 
    font = "arial 15", bg = "gray50", 
    fg = "snow"
).place(y=45, x=115)
Entry(root, 
    font = "arial 15", 
    textvariable = liczba1, 
    bg = "gray50"
).place(y=70, x=115)

liczba2 = StringVar()
Label(root,
    text = "Wpisz liczbe nr 2:",
    font = "arial 15", bg = "gray50", 
    fg = "snow"
).place(y=110, x=115)
Entry(root, 
    font = "arial 15", 
    textvariable = liczba2, 
    bg = "gray50"
).place(y=135, x=115)

Button(root, 
    font = "arial 20 bold", 
    text = "+", 
    bg = "gray50", 
    fg = "snow",
    height = 2,
    width = 2,
    highlightbackground = "gray50"
).place(x=150, y=280)
Button(root, 
    font = "arial 20 bold", 
    text = "x", 
    bg = "gray50", 
    fg = "snow",
    height = 2,
    width = 2,
    highlightbackground = "gray50"
).place(x=200, y=280)
Button(root, 
    font = "arial 20 bold", 
    text = "-", 
    bg = "gray50", 
    fg = "snow",
    height = 2,
    width = 2,
    highlightbackground = "gray50"
).place(x=150, y=330)
Button(root, 
    font = "arial 20 bold", 
    text = "÷", 
    bg = "gray50", 
    fg = "snow",
    height = 2,
    width = 2,
    highlightbackground = "gray50"
).place(x=200, y=330)


#definicje
def dodaj(x, y):
    return x + y
def odejmij(x, y):
    return x - y
def pomnoz(x, y):
    return x * y
def podziel(x, y):
    return x / y
def wyjdz():
    root.destroy()

print("Wybierz co chcesz zrobic.")
print("1.Dodac")
print("2.Odjac")
print("3.Pomnozyc")
print("4.Podzielic")

while True:
    #pobranie od uzytkownika wyboru
    wybor = input("Wybierz (1/2/3/4):")

    #uzytkownik wykonuje wybor opcji co chce zrobic.
    if wybor in ('1','2','3','4'):
        num1 = float(input("Wpisz pierwsza liczbe:"))
        num2 = float(input("Wpisz druga liczbe:"))
        
        if wybor == '1':
            print(num1, "+", num2, "=", dodaj(num1, num2))
        elif wybor == '2':
            print(num1, "-", num2, "=", odejmij(num1, num2))
        elif wybor == '3':
            print(num1, "*", num2, "=", pomnoz(num1, num2))
        elif wybor == '4':
            print(num1, "/", num2, "=", podziel(num1, num2))
        break
    else:
        print("Bledne polecenie")