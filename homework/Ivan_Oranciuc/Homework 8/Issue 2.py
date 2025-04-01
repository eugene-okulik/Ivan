import sys

sys.set_int_max_str_digits(1000000)

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_number_at(index, gen):
    for _ in range(index):
        next(gen)
    return next(gen)

fib_gen = fibonacci_generator()

fifth = get_fibonacci_number_at(4, fib_gen)
two_hundredth = get_fibonacci_number_at(199, fib_gen)
thousandth = get_fibonacci_number_at(999, fib_gen)
hundred_thousandth = get_fibonacci_number_at(99999, fib_gen)

print("Пятое число:", fifth)
print("Двухсотое число:", two_hundredth)
print("Тысячное число:", thousandth)
print("Стотысячное число:", hundred_thousandth)
