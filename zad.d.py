def show_every_second(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])

numbers_list = list(range(1, 19))

show_every_second(numbers_list)
