def mis_num(arr):
    missing_numbers = []
    fir_num = arr[0]
    last_num = arr[-1]

    arr = set(arr)

    for i in range(fir_num, last_num + 1):
        if i not in arr:
            missing_numbers.append(i)

    return missing_numbers


num1 = [1, 2, 4, 5, 6]
num2 = [1, 2, 3, 5, 6, 8, 10, 11, 14]


missing_numbers1 = mis_num(num1)
missing_numbers2 = mis_num(num2)
print("Missing numbers in arr_num1:", missing_numbers1)
print("Missing numbers in arr_num2:", missing_numbers2)
