import math

exit = False;
exit_2 = False;
exit_3 = False
r = False;
print("Добро пожаловать в самый точный калькулятор в диком МПТ!!");
while exit == False:
    exit_2 = False;
    print("\n 1 - Сложение \n 2 - Вычитание \n 3 - Умножение \n 4 - Деление \n 5 - Возведение в степень \n 6 - Квадратный корень \n 7 - Факториал \n 8 - Синус \n 9 - Косинус \n 10 - Тангенс \n 0 - Выйти из программы");
    try:
        answer_1 = int(input("Выберите действие: "));
    except ValueError:
        print("Ошибка: Введите число корректно.")
        continue
    if answer_1 == 1:
        while exit_2 == False:
            exit_3 = False;
            try:
                number_1 = float(input("Введите первое число: "));
                number_2 = float(input("Введите второе число: "));
            except ValueError:
                print("Ошибка: Введите число корректно.")
                continue
            sum = number_1 + number_2;
            print(number_1, " + ", number_2, " = ", sum);
            answer_2 = input("Выйти в главное меню? Да/Нет: ");
            if answer_2 == "Да":
                break;
            elif answer_2 == "Нет":
                continue
            elif answer_2 != "Нет" and answer_2 != "Да":
                while exit_3 == False:
                    answer_2 = (input("Недопустимое значение, попробуйте снова. \nВыйти в главное меню? Да/Нет: "))
                    if answer_2 == "Да":
                        exit_2 = True;
                        break
                    elif answer_2 == "Нет":
                        answer_2 = "";
                        exit_3 = True;
    elif answer_1 == 2:
        while exit_2 == False:
            exit_3 = False;
            try:
                number_1 = float(input("Введите первое число: "));
                number_2 = float(input("Введите второе число: "));
            except ValueError:
                print("Ошибка: Введите число корректно.")
                continue
            sum = number_1 - number_2;
            print(number_1, " - ", number_2, " = ", sum);
            answer_2 = input("Выйти в главное меню? Да/Нет: ");
            if answer_2 == "Да":
                break;
            elif answer_2 == "Нет":
                exit == False;
            elif answer_2 != "Нет" and answer_2 != "Да":
                while exit_3 == False:
                    answer_2 = (input("Недопустимое значение, попробуйте снова. \nВыйти в главное меню? Да/Нет: "))
                    if answer_2 == "Да":
                        exit_2 = True;
                        break
                    elif answer_2 == "Нет":
                        answer_2 = "";
                        exit_3 = True;
    elif answer_1 == 3:
        while exit_2 == False:
            exit_3 = False;
            try:
                number_1 = float(input("Введите первое число: "));
                number_2 = float(input("Введите второе число: "));
            except ValueError:
                print("Ошибка: Введите число корректно.")
                continue
            sum = number_1 * number_2;
            print(number_1, " * ", number_2, " = ", sum);
            answer_2 = input("Выйти в главное меню? Да/Нет: ");
            if answer_2 == "Да":
                break;
            elif answer_2 == "Нет":
                exit == False;
            elif answer_2 != "Нет" and answer_2 != "Да":
                while exit_3 == False:
                    answer_2 = (input("Недопустимое значение, попробуйте снова. \nВыйти в главное меню? Да/Нет: "))
                    if answer_2 == "Да":
                        exit_2 = True;
                        break
                    elif answer_2 == "Нет":
                        answer_2 = "";
                        exit_3 = True;
    elif answer_1 == 4:
        while exit_2 == False:
            exit_3 = False;
            try:
                number_1 = float(input("Введите первое число: "));
                number_2 = float(input("Введите второе число: "));
            except ValueError:
                print("Ошибка: Введите число корректно.")
                continue
            if number_2 == 0:
                print("Ошибка: Деление на ноль.")
                continue
            sum = number_1 / number_2;
            print(number_1, " / ", number_2, " = ", sum);
            answer_2 = input("Выйти в главное меню? Да/Нет: ");
            if answer_2 == "Да":
                break;
            elif answer_2 == "Нет":
                exit == False;
            elif answer_2 != "Нет" and answer_2 != "Да":
                while exit_3 == False:
                    answer_2 = (input("Недопустимое значение, попробуйте снова. \nВыйти в главное меню? Да/Нет: "))
                    if answer_2 == "Да":
                        exit_2 = True;
                        break
                    elif answer_2 == "Нет":
                        answer_2 = "";
                        exit_3 = True;
    elif answer_1 == 5:
        while exit_2 == False:
            exit_3 = False;
            try:
                number_1 = float(input("Введите первое число: "));
                number_2 = float(input("Введите степень числа: "));
            except ValueError:
                print("Ошибка: Введите число корректно.")
                continue
            sum = math.pow(number_1, number_2);
            print(number_1, " в степени ", number_2, " = ", sum);
            answer_2 = input("Выйти в главное меню? Да/Нет: ");
            if answer_2 == "Да":
                break;
            elif answer_2 == "Нет":
                exit == False;
            elif answer_2 != "Нет" and answer_2 != "Да":
                while exit_3 == False:
                    answer_2 = (input("Недопустимое значение, попробуйте снова. \nВыйти в главное меню? Да/Нет: "))
                    if answer_2 == "Да":
                        exit_2 = True;
                        break
                    elif answer_2 == "Нет":
                        answer_2 = "";
                        exit_3 = True;
    elif answer_1 == 6:
        while exit_2 == False:
            exit_3 = False;
            try:
                number_1 = float(input("Введите число: "));
            except ValueError:
                print("Ошибка: Введите число корректно.")
                continue
            if number_1 < 0:
                print("Ошибка: Квадратный корень из отрицательного числа.")
                continue
            sum = number_1 ** 0.5;
            print("Квадратный корень ", number_1, " = ", sum);
            answer_2 = input("Выйти в главное меню? Да/Нет: ");
            if answer_2 == "Да":
                break;
            elif answer_2 == "Нет":
                exit == False;
            elif answer_2 != "Нет" and answer_2 != "Да":
                while exit_3 == False:
                    answer_2 = (input("Недопустимое значение, попробуйте снова. \nВыйти в главное меню? Да/Нет: "))
                    if answer_2 == "Да":
                        exit_2 = True;
                        break
                    elif answer_2 == "Нет":
                        answer_2 = "";
                        exit_3 = True;
    elif answer_1 == 7:
        while exit_2 == False:
            exit_3 = False;
            try:
                number_1 = float(input("Введите число: "));
            except ValueError:
                print("Ошибка: Введите число корректно.")
                continue
            if number_1 < 0 or number_1 != int(number_1):
                print("Ошибка: Факториал применяется только к неотрицательным целым числам.")
                continue
            number = number_1;
            sum = 1;
            while number_1 > 1:
                sum = sum * number_1;
                number_1 = number_1 - 1;
            print("Факториал числа ", number, " = ", sum);
            answer_2 = input("Выйти в главное меню? Да/Нет: ");
            if answer_2 == "Да":
                break;
            elif answer_2 == "Нет":
                exit == False;
            elif answer_2 != "Нет" and answer_2 != "Да":
                while exit_3 == False:
                    answer_2 = (input("Недопустимое значение, попробуйте снова. \nВыйти в главное меню? Да/Нет: "))
                    if answer_2 == "Да":
                        exit_2 = True;
                        break
                    elif answer_2 == "Нет":
                        answer_2 = "";
                        exit_3 = True;
    elif answer_1 == 8:
        while exit_2 == False:
            exit_3 = False;
            try:
                number_1 = float(input("Введите число: "));
            except ValueError:
                print("Ошибка: Введите число корректно.")
                continue
            sum = math.sin(number_1);
            print("Синус числа ", number_1, " = ", sum);
            answer_2 = input("Выйти в главное меню? Да/Нет: ");
            if answer_2 == "Да":
                break;
            elif answer_2 == "Нет":
                exit == False;
            elif answer_2 != "Нет" and answer_2 != "Да":
                while exit_3 == False:
                    answer_2 = (input("Недопустимое значение, попробуйте снова. \nВыйти в главное меню? Да/Нет: "))
                    if answer_2 == "Да":
                        exit_2 = True;
                        break
                    elif answer_2 == "Нет":
                        answer_2 = "";
                        exit_3 = True;
    elif answer_1 == 9:
        while exit_2 == False:
            exit_3 = False;
            try:
                number_1 = float(input("Введите число: "));
            except ValueError:
                print("Ошибка: Введите число корректно.")
                continue
            sum = math.cos(number_1);
            print("Косинус числа ", number_1, " = ", sum);
            answer_2 = input("Выйти в главное меню? Да/Нет: ");
            if answer_2 == "Да":
                break;
            elif answer_2 == "Нет":
                exit == False;
            elif answer_2 != "Нет" and answer_2 != "Да":
                while exit_3 == False:
                    answer_2 = (input("Недопустимое значение, попробуйте снова. \nВыйти в главное меню? Да/Нет: "))
                    if answer_2 == "Да":
                        exit_2 = True;
                        break
                    elif answer_2 == "Нет":
                        answer_2 = "";
                        exit_3 = True;
    elif answer_1 == 10:
        while exit_2 == False:
            exit_3 = False;
            try:
                number_1 = float(input("Введите число: "));
            except ValueError:
                print("Ошибка: Введите число корректно.")
                continue
            sum = math.tan(number_1);
            print("Тангенс числа ", number_1, " = ", sum);
            answer_2 = input("Выйти в главное меню? Да/Нет: ");
            if answer_2 == "Да":
                break;
            elif answer_2 == "Нет":
                exit == False;
            elif answer_2 != "Нет" and answer_2 != "Да":
                while exit_3 == False:
                    answer_2 = (input("Недопустимое значение, попробуйте снова. \nВыйти в главное меню? Да/Нет: "))
                    if answer_2 == "Да":
                        exit_2 = True;
                        break
                    elif answer_2 == "Нет":
                        answer_2 = "";
                        exit_3 = True;
    elif answer_1 == 0:
        print("Досвидание, дайте оценку моему калькуялтору по пятибальной шкале, где 5 самый высокий балл, а 1 самый низкий :)");
        exit = True;
    elif answer_1 != 1 or answer_1 != 2 or answer_1 != 3 or answer_1 != 4 or answer_1 != 5 or answer_1 != 6 or answer_1 != 7 or answer_1 != 8 or answer_1 != 9 or answer_1 != 0:
        print("Недопустимое значение! Попробуйте еще раз.");