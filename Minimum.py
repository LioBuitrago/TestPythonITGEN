# Дан двумерный массив из чисел. Необходимо найти номер строки и столбца с минимальными суммами.
# Оформить в виде функции minimum, где массив передается как аргумент.
# Функция должна вернуть массив из двух элементов: номер строки с минимальной суммой и номер столбца 
# с минимальной суммой.

def minimum(M):
    row_sums=[sum(i) for i in M]
    column_sums = [sum([row[i] for row in M]) for i in range(0,len(M[0]))]
    result = []
    if M != 0:
        c = column_sums.index(min(column_sums))
        r = row_sums.index(min(row_sums))
        result.append(r)
        result.append(c)
    # print(row_sums)
    # print(column_sums)
    # print(result)
    return result


print(minimum(
    [
        [7, 2, 7, 2, 8],
        [2, 9, 4, 1, 7],
        [3, 8, 6, 2, 4],
        [2, 5, 2, 9, 1],
        [6, 6, 5, 4, 5]
    ]))
    
print(minimum(
    [
        [-7, -2, -7, -2, -8],
        [-2, -9, -4, -1, -7],
        [-3, -8, -6, -2, -4],
        [-2, -5, -2, -9, -1],
        [-6, -6, -5, -4, -5]
    ]))
