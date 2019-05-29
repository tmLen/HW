# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Последняя буква в слове {word}: {word[-1]}')


# Вывести количество букв а в слове
word = 'Архангельск'
a_count = 0
for letter in word.lower():
    if letter == 'а':
        a_count += 1
print(f'Количество букв а в слове {word}: {a_count}')


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
vowels_count = 0
for letter in word.lower():
    if letter in vowels:
        vowels_count+=1
print('Вывести количество гласных букв в слове', vowels_count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'Количество слов в предложении "{sentence}": {len(sentence.split())}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(f'Выводим первые буквы предложеия {sentence}:')
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
avg_word_len = 0
for word in sentence.split():
    avg_word_len += len(word)
print(f'Усреднённая длина слова в предложении "{sentence}": {avg_word_len/len(sentence.split())}')