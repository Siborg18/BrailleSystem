from brailleConversionLogic import grade_one_convert_word
from brailleConversionLogic import character_unicodes


class PrintBraille:
    def __init__(self, text_input):
        self.text = text_input
        self.converted_text = grade_one_convert_word(self.text.lower())

    def print_letters(self):
        for i in range(len(self.converted_text)):
            if self.text[i].isupper():
                print(f"{character_unicodes.get('caps')}", sep='', end='')
            print(f"{self.converted_text[i]}", sep='', end='')
        print(character_unicodes.get('space'), end='')

    def print_numbers(self):
        print(f"{character_unicodes.get('num')}", sep='', end='')
        for i in range(len(self.converted_text)):
            print(self.converted_text[i], sep='', end='')
        print(character_unicodes.get('space'), end='')

    def print_mix(self):
        for i in range(len(self.text)):
            if i > 0 and self.text[i].isalpha() and self.text[i - 1].isalpha():
                print(f"{self.converted_text[i]}", sep='', end='')
            elif i > 0 and self.text[i].isdigit() and self.text[i - 1].isdigit():
                print(f"{self.converted_text[i]}", sep='', end='')
            elif self.text[i].isalpha() and self.text[i - 1].isdigit() and self.text[i].isupper():
                print(f"{character_unicodes.get('word_symbol')}{character_unicodes.get('letters')}", sep='', end='')
                print(f"{self.converted_text[i]}", sep='', end='')
            elif self.text[i].isalpha() and i == 0 or self.text[i].isalpha() and self.text[i - 1].isdigit():
                print(f"{character_unicodes.get('letters')}", sep='', end='')
                print(f"{self.converted_text[i]}", sep='', end='')
            elif self.text[i].isdigit() and i == 0 or self.text[i].isdigit() and self.text[i - 1].isalpha():
                print(f"{character_unicodes.get('num')}", sep='', end='')
                print(f"{self.converted_text[i]}", sep='', end='')
            elif self.text[i].isascii():
                print(f"{character_unicodes.get(self.text[i])}", sep='', end='')
        print(character_unicodes.get('space'), end='')