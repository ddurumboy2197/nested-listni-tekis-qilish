def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]
print(flatten(nested_list))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
