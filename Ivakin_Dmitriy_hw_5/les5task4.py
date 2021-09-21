src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [num for idx, num in enumerate(src) if num > src[idx - 1] and idx != 0]
print(result)