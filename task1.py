def calculator(numbOne = float(input("Введите первое число ")),
               numbTwo = float(input("Введите второе число ")),
               Op = int(input('введите операцию: 1.сложение; 2.вычитание; 3.умножение; 4.деление '))):

    if Op == 1:
        print( numbOne + numbTwo)

    elif Op == 2:
        print(numbOne - numbTwo)

    elif Op == 3:
       print(numbOne * numbTwo)

    elif Op == 4:
        if numbTwo == 0:
            print('на ноль делить нелзя')
        else:
            print(numbOne / numbTwo)

    else:
        print('такой операции нет')


calculator()
