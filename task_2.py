import random
from numpy import sort

# Параметри функції:
#   min — мінімальне можливе число у наборі (не менше 1).
#   max — максимальне можливе число у наборі (не більше 1000).
#   quantity — кількість чисел, які потрібно вибрати (значення між min і max).
# Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
# Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.
def get_numbers_ticket(min, max, quantity):
    numbers_ticket = []
    if min < 1 or max > 1000 or min >= max or quantity < min or quantity > max:
        return numbers_ticket
    else:
        # let's prefer using more memory over time (assuming generating unique numbers faster in random.sample)
        numbers_ticket = random.sample(range(min, max + 1), quantity)
        sort(numbers_ticket)
        return numbers_ticket

lottery_numbers = get_numbers_ticket(1, 1000, 6)
print("Ваші лотерейні числа:", lottery_numbers)