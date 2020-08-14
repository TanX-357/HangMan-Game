




# tan=Entry(top,width=100,fg="blue",bg="green",borderwidth=10)
# tan.insert(0,"Available List of Letters: {}",get_available_letters([]))
# tan.pack()

from basic_func import get_guessed_word,is_word_guessed,clean_repr_of_str,get_available_letters


from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import string
import random
def show_hintt(y):
    global start_butt_,secret_word,letters_guessed,vowels,no_of_hints_taken
    no_of_hints_taken+=1
    if start_butt_["state"] is not DISABLED:
        popup("Please first start the game !!")
        return
    letters_not_guessed=""
    countt=0
    for i in range(len(letters_guessed)):
        if letters_guessed=='_':
            letters_not_guessed+=secret_word[i]
    for i in letters_not_guessed:
        if i in vowels:
            countt+=1
    popup("There are "+ str(countt)+" vowels remaining to be guessed")
def change_level_value(labels_name):
    global level
    level=labels_name

def close_window(rrot):
    global level
    rrot.destroy()
    act(level)

def choose_level_window():
    global level
    rrot=Tk()
    rrot.title("CHOOSE THE LEVEL!!")
    LEVELS={
        "BEGINNER":"beg",
        "INTERMEDIATE":"imd",
        "HARD":"hrd",
        "VERY HARD":"vhrd"
    }
    levell=StringVar(rrot,"beg")
    level="beg"
    for labels,labels_name in LEVELS.items():
        Radiobutton(rrot,text=labels,variable=levell,value=labels_name,command=lambda:change_level_value(levell.get())).pack()
    M=Button(rrot,text="START",padx=15,pady=15,activebackground="violet",activeforeground="pink",bd=4,command=lambda: close_window(rrot))
    M.pack()



def popup(strr):
    messagebox.showwarning("FROM HANGMAN GAME!!",strr)

def do_act(y):
    global start_butt_,letter_guessed,warn,guesses,top_label_,Guessed_lett,lett_left,guesses_left_,warnings_left_,sta,status,no_of_hints_taken,Highest_score,secret_word
    if len(y)==0:
        popup("Please guess a letter!!")
        return
    guesses_left_.configure(text="GUESSES LEFT : "+str(guesses))
    warnings_left_.configure(text="WARNINGS LEFT : "+str(warn))
    x=y.lower()
    if x in get_available_letters(''):
        if x in letter_guessed:
            warn -= 1
            if warn >=0:
                reslt_of_guess_lett_in_each_turn.configure(text="Oops!,You've already guessed that letter.")
                warnings_left_.configure(text="WARNINGS LEFT: "+str(warn))
                popup("YOU HAVE ALREADY ENTERED THAT LETTER BEFORE!!")
            else:
                reslt_of_guess_lett_in_each_turn.configure(text="Oops!,You've already guessed that letter.You have no warnings left,so you loose a guess")
                guesses -= 1
                guesses_left_.configure(text="GUESSES LEFT: "+str(guesses))


        else:
            letter_guessed +=x
            if x in secret_word:
                reslt_of_guess_lett_in_each_turn.configure(text="Well done Good guess!!!!")
                progress_.configure(text=clean_repr_of_str(get_guessed_word(secret_word,letter_guessed)))
            else:
                reslt_of_guess_lett_in_each_turn.configure(text="Oops! That letter is not in start_butt_ word")
                if x in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
                guesses_left_.configure(text="GUESSES LEFT: "+str(guesses))
    else:
        warn -= 1
        if warn >= 0:
            reslt_of_guess_lett_in_each_turn.configure(text="Oops! That is not a valid letter")
            popup("PLEASE ENTER VALID INPUT!!")
            warnings_left_.configure(text="WARNINGS LEFT: "+str(warn))
            progress_.configure(text=clean_repr_of_str(get_guessed_word(secret_word,letter_guessed)))
        else:
            popup("SINCE YOU HAVE EXCEEDED THE WARNINGS LIMIT...SO YOU LOOSE A GUESS!!!")
            reslt_of_guess_lett_in_each_turn.configure(text="Oops!,You've already guessed that letter.You have no warnings left,so you loose a guess")
            guesses -= 1
            guesses_left_.configure(text="GUESSES LEFT: "+str(guesses))
    list_of_avail_lett=clean_repr_of_str(get_available_letters(letter_guessed))

    lett_left.configure(text="Available Letters are : "+list_of_avail_lett)
    if is_word_guessed(secret_word, letter_guessed):
        reslt_of_guess_lett_in_each_turn.configure(text="Congratulations, you Won!")
        # print("Congratulations, you Won!")
        Highest_score = max(Highest_score,count*guesses-no_of_hints_taken)
        progress_.configure(text="Your total score for the game is   :"+str(count*guesses-no_of_hints_taken))
        stt="Hurrah!!! You WoN!!!!\nHighest Score :--   "+str(Highest_score)+"\nCurrent Game Score : --   "+str(count*guesses-no_of_hints_taken)
        if Highest_score == count*guesses-no_of_hints_taken:
            stt+="\nThis is also your Highest Score!!!"
        popup(stt)
        play_again_window()

    elif guesses<=0:
        reslt_of_guess_lett_in_each_turn.configure(text="You ran out of guesses")
        secret_word=secret_word.upper()
        popup("OOH !! YOU LOST THE GAME.....!!!\nBETTER LUCK NEXT TIME....!!!!\nTHE CORRECT WORD WAS : "+secret_word)
        play_again_window()
        progress_.configure(text=clean_repr_of_str(secret_word.upper()))
    Guessed_lett.delete(0, END)

def act(level):
    global hintt_butt_,guess_butt_,start_butt_,secret_word,guesses,count,dict,letter_guessed,vowels,top_label_,Guessed_lett,lett_left,guesses_left_,warnings_left_,sta,status,warn,no_of_hints_taken
    with open("list_of_words.txt", "r") as file:
        data = file.readlines()
        for line in data:
            wordd = line.split()
    if level == "beg":
        word=[i for i in wordd if len(i)<5]
    elif level == "imd":
        word=[i for i in wordd if 4<len(i)<7]
    elif level == "hrd":
        word=[i for i in wordd if 6<len(i)<9]
    else:
        word=[i for i in wordd if len(i)>8]
    reslt_of_guess_lett_in_each_turn.configure(text="Current Status : ACTIVE")
    guesses = 6
    warn=3
    count = 0
    no_of_hints_taken=0
    guesses_left_.configure(text="GUESSES LEFT:  "+str(guesses))
    warnings_left_.configure(text="WARNINGS LEFT:  "+str(warn))
    secret_word = random.choice(word)
    top_label_.configure(text="Loading word list from file... \n55,900 words loaded.\nWelcome to the game Hangman!\nI am thinking of word that is  "+str(len(secret_word))+"  letters long\nYou have three warnings left")
    for item in secret_word:
        if item in dict:
            dict[item] += 1
        else:
            dict[item]=1

    for ab in dict:
        count += 1 #after every guess counting the no of matches in guessed string and actual string(or actual word)
    status_of_curr_guess_word=""
    for i in range(len(secret_word)):
        status_of_curr_guess_word+="__  "
    progress_.configure(text=status_of_curr_guess_word)
    letter_guessed=[]
    vowels=['a','e','i','o','u']
    list_of_avail_lett=clean_repr_of_str(get_available_letters(letter_guessed))

    lett_left.configure(text="Available Letters are : "+list_of_avail_lett)
    start_butt_.configure(state=DISABLED)
    hintt_butt_.configure(state=NORMAL)
    guess_butt_.configure(state=NORMAL)
    Guessed_lett.delete(0, END)
def refresh():
    global status,top_label_,lett_left,guesses_left_,warnings_left_,sta,start_butt_,hintt_butt_,Guessed_lett,guess_butt_
    Guessed_lett.delete(0, END)
    start_butt_.configure(state=NORMAL)
    hintt_butt_.configure(state=DISABLED)
    guess_butt_.configure(state=DISABLED)
    top_label_.configure(text="TO START THE GAME PRESS THE START BUTTON")
    # L1.configure(text="Guess the letter:")
    lett_left.configure(text="LETTERS LEFT : Start the game to know this")
    guesses_left_.configure(text="GUESSES LEFT : INACTIVE")
    warnings_left_.configure(text="WARNINGS LEFT : INACTIVE")
    progress_.configure(text="Game has not been started yet")
    reslt_of_guess_lett_in_each_turn.configure(text="Current Status : INACTIVE")
def congo(x,y):
    # global status,top_label_,lett_left,guesses_left_,warnings_left_,sta,start_butt_
    messagebox.showinfo(title="Greetings", message="Congratulations!!!...You won!!!.....cheers!!!\n Your Points : "+str(x))
    yes_or_no=messagebox.askquestion("FROM HANGMAN GAME!!","DO YOU WANT TO PLAY AGAIN!!!??")
    if(yes_or_no=="yes"):
        refresh()
    else:
        sure_to_quit_window()
def play_again_window():
    # global status,top_label_,lett_left,guesses_left_,warnings_left_,sta,start_butt_
    yes_or_no=messagebox.askquestion("FROM HANGMAN GAME!!","DO YOU WANT TO PLAY AGAIN!! ??")
    if(yes_or_no=="yes"):
        refresh()
    else:
        sure_to_quit_window()

def sure_to_quit_window():
    # global status,top_label_,lett_left,guesses_left_,warnings_left_,sta,start_butt_
    yes_or_no=messagebox.askquestion("FROM HANGMAN GAME!!","ARE YOU SURE YOU WANT TO QUIT ??")
    if(yes_or_no=="yes"):
        exit()
    else:
        refresh()

def sure_to_restart_window():
    # global status,top_label_,lett_left,guesses_left_,warnings_left_,sta,start_butt_
    yes_or_no=messagebox.askquestion("FROM HANGMAN GAME!!","AR YOU SURE YOU WANT TO RESTART??")
    if(yes_or_no=="yes"):
        refresh()
    else:
        return

dict={} #keep_track_of_guessed_letters
level=""
top = Tk()
top.title("HANGMAN GAMES LIMITED!!")
Highest_score=0
top_label_=Label(top,
		 text="TO START THE GAME PRESS THE START BUTTON",
		 fg = "light green",
		 bg = "dark green",
         width=50,
		 font = "Helvetica 16 bold italic")
top_label_.pack()
Guessed_lett = Entry(top, width=50,fg="blue",bg="green",borderwidth=10)
Guessed_lett.pack() #entry of guessed letter
lett_left=Label(top,
        text="LETTERS LEFT : Start the game to know this",
        fg = "light green",
        bg = "dark green",
        width=80,
        font = "Helvetica 16 bold italic")
lett_left.pack()
guesses_left_ = Label(top,
        text="GUESSES LEFT : INACTIVE",
        fg = "light green",
        bg = "dark green",
        font = "Helvetica 16 bold italic")
guesses_left_.pack(side =LEFT)
warnings_left_ = Label(top,
        text="WARNINGS LEFT : INACTIVE",
        fg = "light green",
        bg = "dark green",
        font = "Helvetica 16 bold italic")
warnings_left_.pack(side =RIGHT)
progress_=Label(top,
        text="Game has not been started yet",
        fg = "light green",
        bg = "dark green",
        width=100,
        font = "Helvetica 16 bold italic")
progress_.pack()
reslt_of_guess_lett_in_each_turn=Label(top,
        text="Current Status : INACTIVE",
        fg = "light green",
        bg = "dark green",
        width=100,
        font = "Helvetica 16 bold italic")
reslt_of_guess_lett_in_each_turn.pack()
start_butt_=Button(top,text="START THE GAME",padx=25,pady=25,activebackground="violet",activeforeground="pink",bd=4,command= choose_level_window)
start_butt_.pack(side=LEFT)
end_butt_=Button(top,text="END THE GAME",padx=30,pady=30,activebackground="violet",activeforeground="pink",bd=4,command= sure_to_quit_window)
end_butt_.pack(side=RIGHT)
reset_butt=Button(top,text="RESET",padx=25,pady=25,activebackground="violet",activeforeground="pink",bd=4,command=lambda:sure_to_restart_window())
reset_butt.pack(side=RIGHT)
hintt_butt_=Button(top,text="HINT!!",state=DISABLED,padx=25,pady=25,activebackground="violet",activeforeground="pink",bd=4,command= lambda:show_hintt(Guessed_lett.get()))
hintt_butt_.pack(side=LEFT)
guess_butt_=Button(top,text="GUESS",state=DISABLED,padx=25,pady=25,activebackground="violet",activeforeground="pink",bd=4,command= lambda:do_act(Guessed_lett.get()))
guess_butt_.pack()

top.mainloop()
