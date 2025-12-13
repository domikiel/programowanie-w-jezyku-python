def show_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

numbers_list = list(range(1, 19))

show_even_numbers(numbers_list)
