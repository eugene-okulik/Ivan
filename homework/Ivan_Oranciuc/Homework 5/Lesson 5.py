# Solution 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person
print(person)

# Solution 2
results = ["результат операции: 42",
           "результат операции: 514",
           "результат работы программы: 9"]


first_result = results[0]
first_result_value = int(first_result[first_result.index(":") + 2:]) + 10
print(first_result_value)


second_result = results[1]
second_result_value = int(second_result[second_result.index(":") + 2:]) + 10
print(second_result_value)

third_result = results[2]
third_result_value = int(third_result[third_result.index(":") + 2:]) + 10
print(third_result_value)

# Solution 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students = ', '.join(students)
subjects = ', '.join(subjects)

text = "Students {0} study these subjects: {1}"
print(text.format(students, subjects))
