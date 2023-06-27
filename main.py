from printing import PrintBraille
from brailleConversionLogic import separate_multiple_words
from brailleConversionLogic import  grade_two_alpha_wordsigns
from brailleConversionLogic import grade_two_strong_contractions
from brailleConversionLogic import grade_two_strong_wordsigns


# add multithreading to check list while translating

def write_to_html(words_to_html):
    print("write to html")


html_file = "frontPage.html"

user_input = input("Type some text to be converted to braille: ")
print(separate_multiple_words(user_input))

words = separate_multiple_words(user_input)

for word in words:
    if any(char.isalpha() for char in word) and not any(char.isdigit() for char in word):
        my_letter = PrintBraille(word)
        my_letter.print_letters()
    elif any(char.isdigit() for char in word) and not any(char.isalpha() for char in word):
        my_numbers = PrintBraille(word)
        my_numbers.print_numbers()
    else:
        my_mix = PrintBraille(word)
        my_mix.print_mix()
for word in words:
    grade_two_alpha_wordsigns(word)
    grade_two_strong_contractions(word)
    grade_two_strong_wordsigns(word)

# def grade_one_convert_word(word_input):
#     braille_output = []
#     for character in word_input:
#         braille = character_unicodes.get(character)
#         braille_output += braille
#     return braille_output

# def check_contents(word_to_evaluate):
#     if any(char.isalpha() for char in word_to_evaluate) and not any(char.isdigit() for char in word_to_evaluate):
#         print_letters(word_to_evaluate)
#     elif any(char.isdigit() for char in word_to_evaluate) and any(char.isalpha() for char in word_to_evaluate):
#         print_mix(word_to_evaluate)
#     elif any(char.isdigit() for char in word_to_evaluate) and not any(char.isalpha() for char in word_to_evaluate):
#         print_numbers(word_to_evaluate)
#     elif any(char.isalpha() for char in word_to_evaluate) and not any(char.isdigit() for char in word_to_evaluate):
#         print_letters(word_to_evaluate)
#     else:
#         print("Something went wrong")


# def print_mix(word_to_evaluate):
#     stack = []
#     for i in range(0, len(word_to_evaluate)):
#         if word_to_evaluate[i].isalpha() and len(stack) == 0:
#             stack += word_to_evaluate[i]
#         elif word_to_evaluate[i].isdigit() and len(stack) == 0:
#             stack += word_to_evaluate[i]
#         elif word_to_evaluate[i].isalpha() and len(stack) != 0 and stack[-1].isalpha():
#             stack += word_to_evaluate[i]
#         elif word_to_evaluate[i].isdigit() and len(stack) != 0 and stack[-1].isdigit():
#             stack += word_to_evaluate[i]
#         elif word_to_evaluate[i].isdigit() and len(stack) != 0 and stack[-1].isalpha():
#             print_letters(stack)
#             stack.clear()
#             stack += word_to_evaluate[i]
#         elif word_to_evaluate[i].isalpha() and len(stack) != 0 and stack[-1].isdigit():
#             print_numbers(stack)
#             stack.clear()
#             stack += word_to_evaluate[i]
#         else:
#             print("Something went wrong")
#     if stack[-1].isdigit():
#         print_numbers(stack)
#     elif stack[-1].isalpha():
#         print_letters(stack)
#     else:
#         print("Something went wrong")


# def print_letters(letters_input):
#     for i in range(len(letters_input)):
#         letters_input = grade_one_convert_word(letters_input)
#     print(character_unicodes.get('letters'), sep=' ', end=' ')
#     print(letters_input[i], sep=' ', end=' ')


# def print_numbers(numbers_input):
#     numbers_input = grade_one_convert_word(numbers_input)
#     print(character_unicodes.get('num'), sep=' ', end=' ')
#     for i in range(len(numbers_input)):
#         print(numbers_input[i], sep=' ', end=' ')


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
