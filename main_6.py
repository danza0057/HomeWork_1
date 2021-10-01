a = int(input("Введите а: "))
b = int(input("Введите b: "))
day = 1
while a < b:
    a *= 1.1
    day += 1
print(f"на {day}-й день спортсмен достиг результата — не менее {b} км")