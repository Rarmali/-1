# Урок 1

# ДЗ 1
text = (input("Напиши что-нибудь: "))
num = int(input("Введите число: "))
print(text)
print(num)

# ДЗ 2
time = int(input("Введите время в секундах: "))
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print (f"{hour}:{minutes}:{seconds}")

# ДЗ 3
n = int(input("Введите число: "))
n1 = int(f"{n}")
n2 = int(f"{n}{n}")
n3 = int(f"{n}{n}{n}")
n_ans = n1 + n2 + n3
print(n_ans)

# ДЗ 4

# ДЗ 5
revenue = int(input("Введите выручки фирмы: "))
cost = int(input("Введите издержек фирмы: "))
profit = revenue - cost
if profit <= 0:
    print ("убыток")
else:
    print("прибыль")
    margin = profit/revenue*100
    print(f"{margin}%")
employees = int(input("численность сотрудников: "))
pay = profit/employees
print(f"Каждый сотрудник получает: {pay}")


a = int(input("Сколько километров Вы сегодня пробежали: "))
b = int(input("Какова ваша цель: "))
c = 0
while a < b:
    a = a*1.1
    c += 1
    print(f"День {c}-й: Вы пробежали {a} km")
    if a > b:
        a = round(a)
        print(f"на {c}-й  день вы пробежали {a} км")