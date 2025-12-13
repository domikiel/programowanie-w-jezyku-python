def version1(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


num = [2, 4, 6, 8, 12]

result_for = version1(num)
print(result_for)


def version2(numbers):
    return [number * 2 for number in numbers]


num = [2, 4, 6, 8, 12]
result_for = version2(num)
print(result_for)
