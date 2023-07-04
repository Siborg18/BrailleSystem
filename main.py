import brailleConversionLogic
import brailleServer
# add multithreading to check list while translating


def write_to_html(words_to_html):
    print("write to html")


html_file = "index.html"

user_input = input("Type some text to be converted to braille: ")
print(brailleConversionLogic.separate_multiple_words(user_input))
words = brailleConversionLogic.separate_multiple_words(user_input)
word_output = brailleConversionLogic.grade_one_translate(words)

for word in words:
    # check_if_word_in_dictionary(word)
    brailleConversionLogic.grade_two_alpha_wordsigns(word)
    brailleConversionLogic.grade_two_strong_contractions(word)
    brailleConversionLogic.grade_two_strong_wordsigns(word)
    brailleConversionLogic.grade_two_strong_group_signs(word)




# Absolutely essential!  This ensures that socket resuse is setup BEFORE
# it is bound.  Will avoid the TIME_WAIT issue


