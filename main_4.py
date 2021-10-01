a = int(input("Введите целое число: "))
max_a = -1
while a > 0:
    sel_a = a % 10
    a //= 10
    if sel_a > max_a:
        max_a = sel_a
print(max_a)