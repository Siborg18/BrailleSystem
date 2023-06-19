character_unicodes = {'a': '\u2801', 'b': '\u2803', 'k': '\u2805', 'l': '\u2807', 'c': '\u2809', 'i': '\u280A',
                      'f': '\u280B', 'm': '\u280D', 's': '\u280E', 'p': '\u280F', 'e': '\u2811', 'h': '\u2813',
                      'o': '\u2815', 'r': '\u2817',
                      'd': '\u2819', 'j': '\u281A', 'g': '\u281B', 'n': '\u281D', 't': '\u281E', 'q': '\u281F',
                      'u': '\u2825', 'v': '\u2827',
                      'x': '\u282D', 'z': '\u2835', 'w': '\u283A', 'y': '\u283D', 'num': '\u283C', 'caps': '\u2820',
                      '.': '\u2832', 'cont': '\u2810', 'letters': '\u2820',
                      "'": '\u2804', ',': '\u2802', '-': '\u2824', '/': '\u280C', '!': '\u2816',
                      '?': '\u2826',
                      '$': '\u2832', ':': '\u2812', '@': '\u2801',
                      ';': '\u2830', '(': '\u2836', ')': '\u2836', ' ': '\u2800', '1': '\u2801', '2': '\u2803',
                      '3': '\u2809', '4': '\u2819',
                      '5': '\u2811', '6': '\u280B', '7': '\u281B', '8': '\u2813', '9': '\u280A', '0': '\u281A'}

numberPunctuations = ['.', ',', '-', '/', '$']
escapeCharacters = ['\n', '\r', '\t']

contraction_unicodes = {'be': '\u2806', 'ar': '\u281C', 'st': '\u280C', 'in': '\u2814', 'for': '\u283F'}

html_file = "frontPage.html"


def split_to_words(text_input):
    words = text_input.split(' ')
    return words


def grade_one_convert_word(word_input):
    word_input = word_input.lower()
    braille_output = []
    for character in word_input:
        braille = character_unicodes.get(character)
        braille_output += braille
    return braille_output


def print_braille(words_in_braille):
    for i in range(len(words_in_braille)):
        print(words_in_braille[i], sep=' ', end=' ')


def check_contents(word_to_evaluate):
    if any(char.isalpha() for char in word_to_evaluate) \
            and not any(char.isdigit() for char in word_to_evaluate) \
            and any(char.isupper() for char in word_to_evaluate):
        print_letters(word_to_evaluate)
    elif any(char.isdigit() for char in word_to_evaluate) and any(char.isalpha() for char in word_to_evaluate):
        print_mix(word_to_evaluate)
    elif any(char.isdigit() for char in word_to_evaluate) and not any(char.isalpha() for char in word_to_evaluate):
        print_numbers(word_to_evaluate)
    elif any(char.isalpha() for char in word_to_evaluate) and not any(char.isdigit() for char in word_to_evaluate):
        print_letters(word_to_evaluate)
    else:
        print("Something went wrong")


def print_mix(word_to_evaluate):
    stack = []
    for i in range(0, len(word_to_evaluate)):
        if word_to_evaluate[i].isalpha() and len(stack) == 0:
            stack += word_to_evaluate[i]
        elif word_to_evaluate[i].isdigit() and len(stack) == 0:
            stack += word_to_evaluate[i]
        elif word_to_evaluate[i].isalpha() and len(stack) != 0 and stack[-1].isalpha():
            stack += word_to_evaluate[i]
        elif word_to_evaluate[i].isdigit() and len(stack) != 0 and stack[-1].isdigit():
            stack += word_to_evaluate[i]
        elif word_to_evaluate[i].isdigit() and len(stack) != 0 and stack[-1].isalpha():
            print_letters(stack)
            stack.clear()
            stack += word_to_evaluate[i]
        elif word_to_evaluate[i].isalpha() and len(stack) != 0 and stack[-1].isdigit():
            print_numbers(stack)
            stack.clear()
            stack += word_to_evaluate[i]
        else:
            print("Something went wrong")
    if stack[-1].isdigit():
        print_numbers(stack)
    elif stack[-1].isalpha():
        print_letters(stack)
    else:
        print("Something went wrong")


def print_letters(letters_input):
    for i in range(len(letters_input)):
        if letters_input[i].isupper():
            print(character_unicodes.get('caps'), sep=' ', end=' ')
    letters_input = grade_one_convert_word(letters_input)
    print(character_unicodes.get('letters'), sep=' ', end=' ')

    print(letters_input[i], sep=' ', end=' ')


def print_numbers(numbers_input):
    numbers_input = grade_one_convert_word(numbers_input)
    print(character_unicodes.get('num'), sep=' ', end=' ')
    for i in range(len(numbers_input)):
        print(numbers_input[i], sep=' ', end=' ')


def write_to_html(words_to_html):
    print("write to html")


user_input = "AA"

words = split_to_words(user_input)

for word in words:
    check_contents(word)

# take user input

# output braille using braille font

# make grade 1 letter by letter translator both directions braille >> text >> braille

# make grade 1 to grade 2 converter

# file = open("brailleSymbolTable.json", encoding='unicode-escape')
# data = json.load(file)
# unicode_symbol = '\\' + data[0]["symbol"]
# print(unicode_symbol)

# def get_braille_symbols():
#     braille_symbols = []
#     file1 = open('symbolsSample.txt', 'r', encoding='unicode-escape')
#     lines = file1.readlines()
#     for line in lines:
#         x = line.find('"')
#         braille_symbols += line[x + 1]
#     return braille_symbols
#
#
# def get_braille_numeric_names():
#     numeric_names = []
#     file1 = open('symbolsSample.txt', 'r', )
#     lines = file1.readlines()
#     for line in lines:
#         line = line.split(',')
#         numeric_names += line
#
#     for name in numeric_names:
#         if "u" in name:
#             numeric_names.remove(name)
#     return numeric_names


# array1 = get_braille_symbols()
# array2 = get_braille_numeric_names()

# for i in range(len(array1)):
# print(f"{array2[i]} {array1[i]}")
# Using readlines()


# decoded_line = bytes(line, 'utf-8').decode('unicode-escape')

# before_the_line = line[0:x]
# print(f'before the line: ')
# print(f'braille symbol: {line[x + 1]}')


# for line in lines:
#     list_of_lines += line
# for i in range(len(list_of_lines)):
#     print(f'A word: {list_of_lines[i]}')
