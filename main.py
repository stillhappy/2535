# файл изменен +++
# проверка
def prov():
    while True:
        x = input(" Введите выражение: ")
        if x == "":
            print("введите корректно ^_^")
            raise SystemExit
        a = "false"
        for i in x:
            if i not in (" ", "+", "-", "*", "/", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "^", ".", "(", ")"):
                print("введите корректно ^_^")
                raise SystemExit
            elif i.isdigit():
                a = "true"
        if a == "false":
            print("введите корректно ^_^")
            raise SystemExit
        return x

# удаление пробелов
def spacex(x):
    x = x.split()
    x = ''.join(x)
    return x

# преобразование строки
def chisznak(x):
    new = []
    a = ''
    b = 1
    for i in x:
        if i in ("+", "-", "*", "/", "^", "(", ")"):
            if a != '':
                a = int(a) * b
                new.append(int(a))
                a = ''
                b = 1
                new.append(i)
            elif a == '':
                if i == "-":
                    if new[-1] == ")":
                        b = 1
                        new.append(i)
                    else:
                        b = -1
                else:
                    b = 1
                    new.append(i)
        else:
            a += str(i)
    if len(new) > 1 and new[-1] == ")":
        return new
    else:
        a = int(a) * b
        new.append(int(a))
        return new

# приоритет действия
def priority(x):
    if x in ("+", "-"):
        return 1
    if x in ("*", "/"):
        return 2
    if x == "^":
        return 3

# вычисления
def comp1(stack1, stack2):
    a = stack2.pop()
    if a == "(":
        return 0
    elif a == ")":
        return 1
    else:
        num2 = stack1.pop()
        num1 = stack1.pop()
        if a == "^":
            stack1.append(num1 ** num2)
        elif a == "*":
            stack1.append(num1 * num2)
        elif a == "/":
            try:
                b = num1 / num2
            except ZeroDivisionError:
                print("You cant divide by 0! :(")
                print("the end of program ^_^")
                raise SystemExit
            else:
                stack1.append(b)
        elif a == "+":
            stack1.append(num1 + num2)
        elif a == "-":
            stack1.append(num1 - num2)
        return 2

# калькулятор
def comp(new):
    stack1 = []
    stack2 = []
    p1 = 0
    for i in new:
        if type(i) == int:
            stack1.append(i)
            continue
        elif i in ("+", "-", "*", "/", "^"):
            if len(stack2) == 0:
                p1 = priority(i)
                stack2.append(i)
                continue
            p2 = p1
            p1 = priority(i)
            if p1 > p2:
                stack2.append(i)
                continue
            else:
                comp1(stack1, stack2)
                stack2.append(i)
        elif i == "(":
            stack2.append(i)
            p1 = 0
        elif i == ")":
            comp1(stack1, stack2)
            while stack2 != []:
                p = comp1(stack1, stack2)
                if p == 0:
                    break
            p1 = 0
    while len(stack1) > 1:
        comp1(stack1, stack2)
    res = stack1[0]
    return res

x = prov()
print("загрузка програмы, подождите ;) ")
x = spacex(x)
new = chisznak(x)
res = comp(new)
print(str(res) + " is a result 0_o")
print("the end of program ^_^")





