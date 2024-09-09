from tkinter.ttk import Combobox

import requests
import json
import pprint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def update_c_label(event):
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)


def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                c_name = cur[code]
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {c_name} за 1 доллар')
            else:
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произощла ошибка {e}!")
    else:
        mb.showwarning("Вниамние!", "Введите код валюты")


cur = {
    'RUB': 'Российский рубль',
    'EUR': 'Евро',
    'GBP': 'Британский Фунт',
    'JPY': 'Японская Йена',
    'CNY': 'Китайский Юань',
    'KZT': 'Казахский Тенге',
    'UZS': 'Узбекский Сум',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар'
}

window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x180')

Label(text="Выберите код валюты").pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind('<<ComboboxSelected>>', update_c_label)

c_label = ttk.Label()
c_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()

