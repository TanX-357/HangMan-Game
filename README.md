# HangMan-Game

> A word guessing game where a player has to first choose a level(beginner,intermediate,hard,very hard) and then based on that he needs to guess a word(word is choosen randomly from
large chunk of words) with constraints of a given no of warnings and guesses.


## RULES OF THE GAME
*  In this game one has to guess a letter each time and if the guess is present in the original word,then there is no changes in the no of guesses
*  But if he guesses a wrong letter then his guess decreases by 1 or 2(depending on whether the letter is consonant or vowel)
* If he enters an invalid input or same letter again which he had already guessed then he losses a warning,if the no of warning is 0,then he would lose a guess thereafter.
* So the user has to guess the correct and before he runs out of guesses.A list of available letters(letters which he has not guessed till now) are always displayed on the screen
* He can also take a hint which would tell him the no of vowels in the the intersection of his unguessed letters and the letters of the original word,the no of hints would reduce his final score
