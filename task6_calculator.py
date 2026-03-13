print("КАЛЬКУЛЯТОР")
while True:
    print("\n1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Выход")
    choice = input("Выберите операцию: ")
    if choice == "5":
        print("Выход из программы.")
        break
    if choice in ("1", "2", "3", "4"):
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if choice == "1":
            print(f"Результат: {a + b}")
        elif choice == "2":
            print(f"Результат: {a - b}")
        elif choice == "3":
            print(f"Результат: {a * b}")
        elif choice == "4":
            if b != 0:
                print(f"Результат: {a / b}")
            else:
                print("Ошибка: Деление на ноль!")
    else:
        print("Неверный ввод. Попробуйте снова.")