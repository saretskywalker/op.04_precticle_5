income_before_tax = float(input("Введите ваш доход: "))
tax = 0.13

calculated_tax = income_before_tax * tax

income_after_tax = income_before_tax - calculated_tax
print(f'''Общая сумма дохода составила: {f'{round(income_before_tax, 2):,}'.replace(',', ' ')}руб.
Сумма насчитанного налога составила {f"{round(calculated_tax,2):,}".replace(',', ' ')}руб.
Сумма после вычета налога {f"{round(income_after_tax,2):,}".replace(",", " ")}
''')
