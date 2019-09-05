

secret_word = ("Miles".lower())
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
guesses_left =  guess_limit - guess_count

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess my creators name, You have " + str(guesses_left) + " tries: ").lower()
        guess_count += 1

    else:
        out_of_guesses = True


if out_of_guesses:
    print("Sorry, you are out of guesses. YOU LOSE!!")
else:
    print("YOU WIN!!\nMy creator is none other than Miles - the super genius, and Disruptor of Industries!")

