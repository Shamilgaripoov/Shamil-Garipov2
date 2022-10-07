time = int(input())
d, h, m, s = time // 86400,time // 3600, time // 60 % 60, time % 60
print(f'{d} дн {h} час {m} мин {s} cек')