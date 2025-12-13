def merged_lists_and_powered(list1: list, list2: list) -> list:
    merged = list1 + list2
    unique_values = set(merged)
    result = [value ** 3 for value in unique_values]
    return result

list_a = [2, 3, 8, 10, 11, 13]
list_b = [2, 3, 6, 9, 12, 15]

final_result = merged_lists_and_powered(list_a, list_b)

print(final_result)
