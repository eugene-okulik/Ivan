value = 4


while True:
    user_value = int(input("Введите число: "))
    if user_value != value:
        print("попробуйте снова")
    else:
        print("Поздравляю! Вы угадали!")
        break
