import random
my_list = []

for _ in range(10):
    my_list.append(random.randint(0, 100))
for element in my_list:
    if element > 10:
        my_sum = my_sum + element

print(my_sum)