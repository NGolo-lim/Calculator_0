lang = 'EN'
lang_opt = input('Enter L to change language or other key to continue: ')
while lang_opt == 'l':
    if lang == "RU":
        lang = "EN"
        lang_opt = input('Enter L to change language or other key to continue: ')
    else:
        lang = "RU"
        lang_opt = input('Введите L, чтобы изменить язык, или любую другую клавишу, чтобы продолжить: ')    
if lang =="EN":
    s = "Choose operation(+, -, *, /, //, %, ^, sqrt): "
    a = "Press first number: "
    b = "Press second number: "
    r = "Result: "
    e = "Error: "
    p = "Press ENTER to continue: "
if lang == "RU":
    s = "Выберите операцию(+, -, *, /, //, %, ^, sqrt): "
    a = "Введите первое число: "
    b = "Введите второе число: "
    r = "Результат: "
    e = "Ошибка: "
    p = "Нажмите ENTER для продолжения: "

while True:
    oper = input(s)
    if oper == '0':
        break
    if oper not in('+', '-', '*', '/', '//', '%', '^', 'sqrt'):
        continue
   
    a_num = float(input(a))
    b_num = float(input(b))

    if oper == '+':
        sum = a_num + b_num
        print(r, sum)
    elif oper == '-':
        dif = a_num - b_num
        print(r, dif)
    elif oper == '*':
        product = a_num * b_num
        print(r, product)
    elif oper == '/':
        if b != 0:
            div = a_num / b_num
            print(r, div) 
        else:
            print(e)   
    elif oper == '//':
        int_div = a_num // b_num
        print('Деление без остатка равно: ', r, int_div)        
    elif oper == '%':
        rem_div = a_num % b_num
        print('Остаток от деления равен:', r, rem_div) 
    elif oper == '^':
        deg = a_num ** b_num
        print(r, deg)
    elif oper == 'sqrt':
        if a_num > 0:
            root = a_num ** (1 / b_num)
            print(r, round(root))
        else:
            print(e)       
        
     


