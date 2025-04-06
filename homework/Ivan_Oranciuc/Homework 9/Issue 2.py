from statistics import fmean

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


def hight_temperatures(temperatures):
    return temperatures > 28


values_for_temperatures = list(filter(hight_temperatures, temperatures))

print(f'Max temperature: {max(values_for_temperatures)}')
print(f'Min temperature: {min(values_for_temperatures)}')
print(f'Avg temperature: {round(fmean(values_for_temperatures))}')
