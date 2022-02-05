from wordlist import word_list as words
import random
import string 

def word_corrector(words):
    word = random.choice(words)
    while "-" in word or " " in word or len(word)<4: 
        word = random.choice(words)
    return word
    

def hangman():
    word = word_corrector(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    lives = len(word) + 2
    attempts = 0
    while len(word_letters)> 0 and lives > 0:
        if attempts > 0:
            print("You have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Word: ", " ".join(word_list))
        guess = input("Guess a Letter: ").lower()
        attempts+=1

        if guess not in used_letters and guess in alphabet:
            used_letters.add(guess)

            if guess in word_letters:
                word_letters.remove(guess)
                if len(word_letters) == 0:
                    print("You win!")
            else:
                lives -= 1
                print(f"Wrong guess! Lives left:{lives}")
                if lives == 0:
                    print(f"Game over!\nThe word is {word} ") 

        elif guess in used_letters:
            print("You have already used this letter!")

        else:
            print("Invalid Character!")
            
hangman()