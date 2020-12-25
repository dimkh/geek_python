words = input('\nВведите строку из нескольких слов через пробел: ')
words_list = words.split()

print('\nПронумерованные слова построчно, с ограничением 10 символов:')
for i in range(len(words_list)):
    print(f'{i + 1}: {words_list[i][:10]}')