"""Вводим текст и создаем список слов методом .split"""
my_text = input("Введите текст: ").split()
len_word = ""

"""Сравниваем длинну элементов в списке. Самый длинный вносится в переменную len_word"""
for word in my_text:
    if len(word) > len(len_word):
        len_word = word
print("Самое длинное слово: ", len_word, "- ", len(len_word), "символов")

print("Самое частое слово: ", max(set(my_text), key=my_text.count))
# Не придумал как вывести число повторений :(