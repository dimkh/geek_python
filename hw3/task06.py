def capitalize_word(str_lowcase: str) -> str:
    """ Возвращает слово с первой заглавной буквой и маленькими остальными
    На входе: слово из маленьких букв
    На выходе: слово, где первая буква - заглавная
    """
    return str_lowcase.capitalize()

all_str_lowcase = 'this string consist of words with small letters'
split_str = all_str_lowcase.split()

result_str = [capitalize_word(elem) for elem in split_str]

print(f'\nОдно слово с заглавной буквой: {capitalize_word("word")}')
print(*result_str, sep = ' ')