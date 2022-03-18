# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
# русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
# информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
# снаружи.
keys = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
values = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
num_translate = dict(zip(keys, values))


def num_translate(num):
    if num == 'one':
        print('один')
    elif num == 'two':
        print('два')
    elif num == 'three':
        print('три')
    elif num == 'four':
        print('четыре')
    elif num == 'five':
        print('пять')
    elif num == 'six':
        print('шесть')
    elif num == 'seven':
        print('семь')
    elif num == 'eight':
        print('восемь')
    elif num == 'nine':
        print('девять')
    elif num == 'ten':
        print('десять')
    elif num == 'zero':
        print('ноль')
        return num
    else:
        num == False
        return None


num_translate("three")


# 2. *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
# корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
# должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(num):
    new_dict = {'one': 'один',
                'two': 'два',
                'three': 'три',
                'four': 'четыре',
                'five': 'пять',
                'six': 'шесть',
                'seven': 'семь',
                'eight': 'восемь',
                'nine': 'девять',
                'ten': 'десять'}
    if num.istitle():
        result = new_dict.get(num.lower(), 'такагат нэт').title()
    else:
        result = new_dict.get(num, 'эт ни слова,пиши слова if == russki')
    print(result)
num_translate_adv("Three")


#
# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
# "И": ["Иван", "Илья"],
# "М": ["Мария"],
# "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется
# сортировка по ключам? Можно ли использовать словарь в этом случае?

def thesaurus(*names):
    # names.sort(key=lambda i[0]: i) погуглить
    names_dict = {key[0]: [name for name in names if name[0] == key[0]] for key in names}
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))

# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный",
# "мягкий"]
# Например:
# >>> get_jokes(2)

# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
# слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы
# сделать аргументы именованными?

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
              "мягкий"]

def jokes(n, Flag=False):
    for i in range(n):
        new_list = []
        result_list = []
        list1 = random.choice(nouns)
        list2 = random.choice(adverbs)
        list3 = random.choice(adjectives)
        new_list.append(list1)
        new_list.append(list2)
        new_list.append(list3)
        new_list = (f"{list1} {list2} {list3}")
        result_list.append(new_list)
        if Flag == True:
            nouns.remove(list1)
            adverbs.remove(list2)
            adjectives.remove(list3)

jokes(5)

