try:
    result = input("Введите выражение: ")
    parts = result.split()
    if len(parts) == 3:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])


    if (operator == "+" and (1 <= num1 <= 10) and (1 <= num2 <= 10)):
        print(int(num1 + num2))
    elif (operator == "-" and (1 <= num1 <= 10) and (1 <= num2 <= 10)):
        print(int(num1 - num2))
    elif (operator == "*" and (1 <= num1 <= 10) and (1 <= num2 <= 10)):
        print(int(num1 * num2))
    elif (operator == "/" and (1 <= num1 <= 10) and (1 <= num2 <= 10)):
        print(int(num1 / num2))
    else:
        print("Только числа от 0 до 10")
except NameError:
    print("Строка не является математической операцией")













