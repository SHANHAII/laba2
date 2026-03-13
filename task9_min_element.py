numbers = input("Введите числа через пробел: ").split()
if numbers:
    nums = [float(x) for x in numbers]
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    print(f"Минимальный элемент: {min_num}")
else:
    print("Список пуст.")