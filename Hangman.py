import random

# A list of words that
potential_words = ["Girls Who Code", "Hollywood", "bonfire", "summer"]

word = random.choice(potential_words)
print(word)
# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = ["_"]*len(word) # TIP: the number of letters should match the word
print("Let's start! " + str(current_word))

# Some useful variables
guesses = []
maxfails = 6
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ")
    loss = True
	# check if the guess is valid: Is it one letter? Have they already guessed it?
    if len(guess) == 1 and guess not in guesses:
        # check if the letter is in the word
        for i in range(len(word)):
            if word[i] == guess:
                # replace underscore with the guess if it is in the word
                current_word[i] = guess
                # we don't lose any tries
                loss = False

        # store the letters that have been guessed
        guesses.append(guess)
    # invalid guess (not a letter, or have already been guessed)
    else:
        print("Invalid guess!")

    # print the current word
    print(current_word)
    # check if the current word is the original word
    if "".join(current_word) == word:
        print("YAY YOU SURVIVED! CONGRATS!The word was: " + str(word))
        break
    # if the guess was wrong, lose a trie
    if loss:
        fails = fails + 1
    print("You have " + str(maxfails - fails) + " tries left!")

# inform that the player failed
if fails == maxfails:
    print("OOOPS YOU LOSS! TRY AGAIN :)")
