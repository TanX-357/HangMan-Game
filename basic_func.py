import string
import random
def get_guessed_word(secret_word,letters_guessed):
    dict = {} #kepping track of guessed letters
    current_guessed_word_status = ''
    for letters in secret_word:
        if letters in letters_guessed:
            dict[letters] = letters
        else:
            dict[letters] = '_'
        current_guessed_word_status += dict[letters]+' '
    return current_guessed_word_status



def is_word_guessed(secret_word,letters_guessed):
    for word in secret_word:
        if word in letters_guessed:
            pass
        else:
            return False
    return True


def clean_repr_of_str(stringg):
    modified=""
    for i in stringg:
        modified+=i+"  "
    return modified


def get_available_letters(letters_guessed):
    import string
    str_of_avail_letters =''
    for letters in string.ascii_lowercase:
        if  letters in letters_guessed:
            pass
        else:
            str_of_avail_letters+=letters
    return str_of_avail_letters
