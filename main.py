import brailleConversionLogic
import socketserver
from brailleServer import MyTCPHandler, run_http_server
# add multithreading to check list while translating

if __name__ == "__main__":
    HOST, PORT = "localhost", 8000

    run_http_server()
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.handle()
        server.serve_forever()

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



