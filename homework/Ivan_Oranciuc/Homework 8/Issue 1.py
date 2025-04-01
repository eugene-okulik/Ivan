import random

salary = int(input("Введите свою нищенскую зарплату: "))
bonus = random.choice([True, False])


def salary_calculator():
    if bonus is True:
        final_check = salary + random.randint(1, 100)
        print(f"{salary}, {bonus} - '${final_check}'")
    else:
        print(f"{salary}, {bonus} - '${salary}'")


salary_calculator()
