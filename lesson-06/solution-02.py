import math

g1, g2, g3 = int(input("1-ая группа ")), int(input("2-ая группа ")), int(input("3-ая группа "))
groups = [g1, g2, g3]

groups = sum([math.ceil(i / 2) for i in groups])
print("Количество парт - ", str(groups))
