import re
"""
======================= 1 ЗАДАНИЕ ===============================
    Вам дана строка. Выведите все подстроки, содержащие "cat".
"""
a = input(">")
b = a.split(" ")
for i in range(len(b)):
    match = re.search(r"cat", b[i])
    if match is not None:
        if match[0] != "":
            print(b[i])
"""
======================= 2 ЗАДАНИЕ ===============================
    Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
"""
a = input(">")
b = re.findall(r"z...z", a, 0)
for i in range(len(b)):
    print(b[i])
"""
======================= 3 ЗАДАНИЕ ===============================
    Номер должен быть длиной 10 знаков и начинаться с 8 или 9. 
    Есть список телефонных номеров, и нужно проверить их, используя регулярные выражения в Python
"""
a = [input(">") for i in range(3)]
for i in range(len(a)):
    number = re.fullmatch(r"[8, 9][0-9]{9}", a[i])
    if number:
        print(number[0])
"""
======================= 4 ЗАДАНИЕ ===============================
    Дана строка, выведите все вхождения слов, начинающиеся на гласную букву.
"""
a = input(">")
pattern = r"\b[aeyuioAEIOYUуеыаоэяиюУЕЕЫАОЯИЮ]\w*"
number = re.findall(pattern, a)
print(number)
"""
======================= 5 ЗАДАНИЕ ===============================
    Дана строка. Вывести все числа этой строки, как отрицательные так и положительные. 
"""
a = input(">")
b = re.findall(r"[-+]?\d+", a, 0)
for i in range(len(b)):
    print(b[i])
"""
======================= 6 ЗАДАНИЕ ===============================
    В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.
"""
a = input(">")
b = re.sub(r"human", r"computer", a)
print(b)
"""
======================= 7 ЗАДАНИЕ ===============================
    Извлечь дату из строки. Формат даты dd –mm-yyyy (например, 2022-02-28).
"""
a = input(">")
b = re.findall(r"\d\d.\d\d.\d{4}", a, 0)
for i in range(len(b)):
    print(b[i])
"""
======================= 8 ЗАДАНИЕ ===============================
    Найти все слова, в которых есть хотя бы одна буква ‘b’
"""
a = input(">")
b = a.split(" ")
for i in range(len(b)):
    match = re.search(r"b", b[i])
    if match is not None:
        if match[0] != "":
            print(b[i])
