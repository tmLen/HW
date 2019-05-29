#Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
with open('referat.txt', 'r', encoding='utf-8') as fin:
    text = fin.read()
print(len(text))

#Подсчитайте количество слов в тексте
print(len(text.split()))

#Замените точки в тексте на восклицательные знаки
print(text.replace('.', '!'))

#Сохраните результат в файл referat2.txt
with open('referat2.txt', 'w', encoding='utf-8') as fout:
    fout.write(text.replace('.', '!'))