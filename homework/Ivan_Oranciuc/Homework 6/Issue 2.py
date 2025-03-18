number = range(1, 101)

for numbers in number:
    if numbers % 5 == 0 and numbers % 3 == 0:
        print('FuzzBuzz')
    elif numbers % 5 == 0:
        print('Buzz')
    elif numbers % 3 == 0:
        print("Fuzz")
    else:
        print(numbers)