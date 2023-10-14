numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
total_len = 0
total_sum = 0
for num in numbers:
    total_len += 1
    if num is not None:
        total_sum += num
average = total_sum / total_len
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = average
        break
print("Измененный список:", numbers)
