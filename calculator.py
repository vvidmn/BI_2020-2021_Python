x = float(input())
s = input()
y = float(input())

if s in ('+', '-', '*', '/'):
    if s == '+':
        print(x+y)
    elif s == '-':
        print(x-y)
    elif s == '*':
        print(x*y)
    elif s == '/':
        if y != 0:
            print(x/y)
        else:
            print("Деление на ноль!")
else:
    print("Неверный знак операции!")
