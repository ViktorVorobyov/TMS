dict_eng_to_rus = {
    "apple": "яблоко",
    "house": "дом"
}

dict_rus_to_eng = {
    value: key
    for key, value in dict_eng_to_rus.items()
}


def from_eng_to_rus(eng):
     rus = dictonary[eng]
     return rus

#solution-01

new_text= text.replase('.', ',', ':')