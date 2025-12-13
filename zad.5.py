def list_contains(numbers: list, value: int) -> bool:
    return value in numbers


nums = [2, 3, 4, 5, 6, 12, 24, 48, 96]

result = list_contains(nums, 13)

print(result)
