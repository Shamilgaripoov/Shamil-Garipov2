elif year % 100 == 0:
    if year % 400 == 0:
        print('Год високосный.')
    else:
        print('Год не високосный.')
else:
    print('Год високосный.')