from tkinter.ttk import Combobox
import requests
import json
import pprint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


def update_b_label(event):
    code = b_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def update_t_label(event):
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()

    if t_code and b_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()
            data = response.json()
            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}')
            else:
                mb.showerror("Ошибка!", f"Валюта {t_code} не найдена!")
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
    'CAD': 'Канадский доллар',
    'USD': 'Американский доллар'
}

window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x300')

Label(text="Базовая валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)
b_combobox.bind('<<ComboboxSelected>>', update_b_label)

Label(text="Целевая валюта").pack(padx=10, pady=10)

t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind('<<ComboboxSelected>>', update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()

