def search_min_and_max (*args, **kwargs):
    func_type = kwargs["func_type"]
    min_el = args[0]
    max_el = args[0]
    for element in args:
        if element < min_el:
            min_el = element
        if element > max_el:
            max_el = element
    if func_type == "min":
        return min_el
    if func_type == "max":
        return max_el

random_elements = []
for _ in range(10):
    random_el = random.randint(1, 100)
    random_elements.append(random_el)

