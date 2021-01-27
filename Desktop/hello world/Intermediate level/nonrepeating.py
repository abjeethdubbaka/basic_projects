def first_non_repeating_letter(string):
    lowercase=string.lower()
    for i,letter in enumerate(lowercase):
        if lowercase.count(letter)==1:
            return string[i]
    return ''


def first_non_repeating_letter(string):
    return next((x for x in string if string.lower().count(x.lower())==1), '')