import random
operators=["+", "-", "*"]
def primer():
    a=random.randint(0, 20)
    b=random.randint(0, 20)
    operator=random.choice(operators)
    primer=f"{a} {operator} {b}"
    return primer
correct_answers=0
# y=primer()
# print(y)
# try:
#     user_input = input("Введите ответ: ")
#     number = int(user_input)
#     print("Ваш ответ:", number)
# except ValueError:
#     print("Ошибка, введите корректное число.")
# d=eval(y)
# if d==number:
#     print("Правильно!")
# else:
#     print("Нет!")

for i in range(10):
    y = primer()
    print(y)
    try:
        user_input = input("Введите ответ: ")
        number = int(user_input)
        print("Ваш ответ:", number)
    except ValueError:
        print("Ошибка, введите корректное число.")
    d = eval(y)
    if d == number:
        print("Правильно!")
        correct_answers=correct_answers+1
    else:
        print("Нет!")
if correct_answers<=6:
    print("C grade, try again next day.")
elif correct_answers==7:
    print("B grade, not bad!")
elif correct_answers>=8:
    print("A grade, nice!")