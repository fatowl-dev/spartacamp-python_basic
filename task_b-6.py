import random
sur_num = int(input('サイコロの面の数は? : '))
trial = int(input('何回振りますか? : '))
# print('[', end='')
# for i in range(trial):
#     print(random.randrange(1, sur_num + 1), end='')
#     if i == trial - 1:
#         print(']')
#     else:
#         print(', ', end='')

# 短いバージョン
num_list = []
for i in range(trial):
    num_list.append(random.randint(1, sur_num))
print(num_list)
