# def spin_words(sentence):
#     new_sentence =sentence.split(" ")
#     new_word = []
#     for w in new_sentence:
#         if len(w) >= 5:
#             new_word.append(w[::-1])
#         else:
#             new_word.append(w)
#     return ' '.join(new_word)


# comprehension
def spin_words(sentence):
    new_sentence = sentence.split(" ")
    new_word = [w[::-1] if len(w)>=5 else w for w in new_sentence]
    return ' '.join(new_word)
    