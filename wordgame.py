
def get_guessed_word(secret_word,letters_guessed):
    dict = {}
    copyy = ''
    for letters in secret_word:
        if letters in letters_guessed:
            dict[letters] = letters
        else:
            dict[letters] = '_'
        copyy += dict[letters]
        copyy += ' '
    return copyy



def is_word_guessed(secret_word,letters_guessed):
    for word in secret_word:
        if word in letters_guessed:
            pass
        else:
            return False
    return True




def get_available_letters(letters_guessed):
    import string
    copy =''
    for letters in string.ascii_lowercase:
        if  letters in letters_guessed:
            pass
        else:
            copy+=letters
    return copy







with open("list_of_words.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()

import string
import random
secret_word = random.choice(word)
print(secret_word)
guesses = 6
count = 0

warn=3;
dict={}
print("Loading word list from file... \n55,900 words loaded.\nWelcome to the game Hangman!\nI am thinking of word that is",len(secret_word),"letters long\nYou have three warnings left.\n--------------")
for item in secret_word:
    if item in dict:
        dict[item] += 1
    else:
        dict[item]=1

for ab in dict:
    count += 1

letter_guessed=[]

vowels=['a','e','i','o','u']
while guesses != 0 :
    print("You have",guesses,"guesses left")
    print("Available letters:", get_available_letters(letter_guessed))
    y = input("Please guess a letter: ")
    x=y.lower()
    if x in get_available_letters(''):
        if x in letter_guessed:
            warn -= 1
            if warn >=0:
                print("Oops!,You've already guessed that letter.You have",warn,"warnings left:\n",get_guessed_word(secret_word,letter_guessed))
            else:
                print("Oops!,You've already guessed that letter.You have no warnings left,so you loose a guess:\n",get_guessed_word(secret_word,letter_guessed))
                guesses -= 1

        else:
            letter_guessed +=x
            if x in secret_word:
                print("Good guess:",get_guessed_word(secret_word,letter_guessed))
            else:
                print("Oops! That letter is not in my word")
                if x in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
    else:
        warn -= 1
        if warn >= 0:
            print("Oops! That is not a valid letter.You have", warn, "warnings left:",get_guessed_word(secret_word, letter_guessed))
        else:
            print("Oops!,You've already guessed that letter.You have no warnings left,so you loose a guess:\n",get_guessed_word(secret_word, letter_guessed))
            guesses -= 1

    if is_word_guessed(secret_word, letter_guessed):
        print("Congratulations, you Won!")
        print("Your total score for the game is",count*guesses)
        exit()

print("You ran out of guesses.The word was",secret_word.upper())
