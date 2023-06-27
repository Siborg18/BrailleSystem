character_unicodes = {'a': '\u2801', 'b': '\u2803', 'k': '\u2805', 'l': '\u2807', 'c': '\u2809', 'i': '\u280A',
                      'f': '\u280B', 'm': '\u280D', 's': '\u280E', 'p': '\u280F', 'e': '\u2811', 'h': '\u2813',
                      'o': '\u2815', 'r': '\u2817',
                      'd': '\u2819', 'j': '\u281A', 'g': '\u281B', 'n': '\u281D', 't': '\u281E', 'q': '\u281F',
                      'u': '\u2825', 'v': '\u2827',
                      'x': '\u282D', 'z': '\u2835', 'w': '\u283A', 'y': '\u283D', 'num': '\u283C', 'caps': '\u2820',
                      '.': '\u2832', 'cont': '\u2810',
                      'letters': '\u2820', 'space': '\u2800', 'word_symbol': '\u2830',
                      "'": '\u2804', ',': '\u2802', '-': '\u2824', '/': '\u280C', '!': '\u2816',
                      '?': '\u2826',
                      '$': '\u2832', ':': '\u2812', '@': '\u2801',
                      ';': '\u2830', '(': '\u2836', ')': '\u2836', ' ': '\u2800', '1': '\u2801', '2': '\u2803',
                      '3': '\u2809', '4': '\u2819',
                      '5': '\u2811', '6': '\u280B', '7': '\u281B', '8': '\u2813', '9': '\u280A', '0': '\u281A'}

numberPunctuations = ['.', ',', '-', '/', '$']
escapeCharacters = ['\n', '\r', '\t']

strong_contraction_unicodes = {'for': '\u283F', 'and': '\u282F', 'of': '\u2837', 'the': '\u282E', 'with': '\u283E'}
lower_group_sign_unicodes = {'be': '\u2806', 'in': '\u2814'}
strong_group_sign_unicodes = {'ar': '\u281C', 'st': '\u280C'}
strong_wordsign_unicodes = {'child': '\u2821'}


def grade_one_convert_word(word_input):
    braille_output = []
    for character in word_input:
        braille = character_unicodes.get(character)
        braille_output += braille
    return braille_output


def separate_multiple_words(words_input):
    words = words_input.split(' ')
    return words


def grade_two_alpha_wordsigns(word_input):
    alpha_wordsigns = {"but", "can", "do", "every", "from", "go", "have", "just", "knowledge",
                       "like", "more", "not", "people", "quite", "rather", "so", "that", "us",
                       "very", "will", "it", "you", "as"}
    if word_input in alpha_wordsigns:
        print(character_unicodes.get(word_input[0]))
        return character_unicodes.get(word_input[0])


def grade_two_strong_contractions(word_input):
    if word_input in strong_contraction_unicodes:
        print(strong_contraction_unicodes.get(word_input))
        return strong_contraction_unicodes.get(word_input)


def grade_two_strong_wordsigns(word_input):
    if word_input in strong_wordsign_unicodes:
        print(strong_wordsign_unicodes.get(word_input))
        return strong_wordsign_unicodes.get(word_input)
