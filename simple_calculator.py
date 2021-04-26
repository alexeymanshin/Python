what = input("Выберете операцию + ; - ; * ; / ?")
a = float(input("введите первое число:"))
b = float(input('введите второе число:'))
if what == '+':
    c = a + b
    print(f'Результат {c}')
elif what == '-':
    c = a - b
    print(f'Результат {c}')
elif what == '*':
    c = a * b
    print(f'Результат {c}')
elif what == '/':
    c = a / b
    print(f'Результат {c}')
else:
    print('неверная операция')
