import random
my_list = []

for _ in range(10):
    my_list.append(random.randint(0, 100))
for element in my_list:
    if element > 10:
        my_sum = 0
        my_sum = my_sum + element

print(my_sum)



my_str = input()
my_int = int(my_str)

for x in my_str:
    pass

my_str = input()
my_int = int(my_str)
counter = 0
my_sum1 = 0
while counter < my_int:
    my_pwd = counter ** 3
    my_sum1 += my_sum1 + my_pwd
    counter += 1

print(my_sum1)