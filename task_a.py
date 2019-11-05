import random

# A-1
users = ['Bob', 'Tom', 'Ken']
print(users)

# A-2
int_numbers = [n for n in range(1, 6)]
print(int_numbers)

# A-3
kazuma_info = ['Kazuma', 'Takahashi', 35]
print(kazuma_info)

# A-4
members = ['Kazuma', 'Makoto', 'Ohira']
print(members[1])
print(members[0])

# A-5
print(f'Name: {kazuma_info[1]} {kazuma_info[0]}, Age: 35')

# A-6
odd_numbers = [1, 3, 5, 7, 9]
for num in odd_numbers:
    print(num, end=' ')
print()

# A-7
even_numbers = [2, 4, 6, 8]
for num in even_numbers:
    print(num * 2, end=' ')
print()

# A-8
users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]

for user in users_info:
    print(f'"Name: {user[0]}, Age: {user[1]}"')

# A-9
kazuma_info = {'first_name': 'Kazuma', 'family_name': 'Takahashi', 'age': 35}
print(kazuma_info["first_name"]) # "Kazuma"
print(kazuma_info["family_name"]) # "Takahashi"
print(kazuma_info["age"]) # 35


# A-10
def dice():
    print(random.randrange(1, 7))


for i in range(0, 10):
    dice()

# A-11
height_m = float(input('Height(m)? > '))
weight_kg = float(input('Weight(kg)? > '))
print(f'Your BMI is {weight_kg / (height_m**2):.2f}')
