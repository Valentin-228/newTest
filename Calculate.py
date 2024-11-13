def main():
 try:
    result = input("Введите выражение: ")
    parts = result.split()
    if len(parts) == 3:
        num1 = int(parts[0])
        operator = parts[1]
        num2 = int(parts[2])


    if (operator == "+" and (1 <= num1 <= 10) and (1 <= num2 <= 10)):
        result = str(num1 + num2)
    elif (operator == "-" and (1 <= num1 <= 10) and (1 <= num2 <= 10)):
        result = str(num1 - num2)
    elif (operator == "*" and (1 <= num1 <= 10) and (1 <= num2 <= 10)):
        result = str(num1 * num2)
    elif (operator == "/" and (1 <= num1 <= 10) and (1 <= num2 <= 10)):
        result = str(num1 / num2)
    else:
        print("Только числа от 0 до 10")
 except NameError:
    print("Строка не является математической операцией")
 except ValueError:
    print("Только целые числа")
 print(result)
 print(type(result))

main()












