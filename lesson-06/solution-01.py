"""Вводим текст и создаем список слов методом .split"""
my_text = input("Введите текст: ").split
len_word = ""

"""Сравниваем длинну элементов в списке. Самый длинный вносится в переменную len_word"""
for word in my_text:
    if len(word) > len(len_word):
        len_word = word

print("Самое длинное слово: ", my_text[len_word], "- ", len(len_word), "символов")
# Количество символов пишет больше чем на самом деле. Почему так, не смог понять.

print("Самое частое слово: ", max(set(my_text), key=my_text.count))
