results = ["результат операции: 42",

           "результат операции: 54",

           "результат работы программы: 209",

           "результат: 2"]


def extract_number(s):
    return int(s.split()[-1])


def add_and_print(s):
    print(extract_number(s) + 10)


for result in results:
    add_and_print(result)
