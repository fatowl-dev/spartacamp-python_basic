def get_sum(numbers):
    sum_num = 0
    for num in numbers:
        sum_num += num

    return sum_num


def get_max(numbers):
    max_num = numbers[0]
    for i in range(1, len(numbers)):
        if max_num < numbers[i]:
            max_num = numbers[i]

    return max_num


def get_min(numbers):
    min_num = numbers[0]
    for i in range(1, len(numbers)):
        if min_num > numbers[i]:
            min_num = numbers[i]

    return min_num


def get_average(numbers):
    sum_num = get_sum(numbers)
    return sum_num / len(numbers)


input_str = input('データを入力してください(スペース区切り) > ')
number_list = []
for s in input_str.split(' '):
    number_list.append(int(s))

print(f'合計値: {get_sum(number_list)}')
print(f'最大値: {get_max(number_list)}')
print(f'最小値: {get_min(number_list)}')
print(f'平均値: {get_average(number_list)}')
