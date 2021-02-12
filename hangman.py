import random 
import time
import os
import requests
from bs4 import BeautifulSoup



def giveup():
    time.sleep(1)
    playgame()
def win():
    time.sleep(1)
    print("Play again if you want. Press any key except for the power key. ")
    giveup()
def playgame():
    i = 0
    while i == 0:
        difficulty = input("Select a difficult level: easy, medium, hard: ")
        word_file = "hangmanwords.txt"
        answers = ["easy", "medium", "hard"]
        if difficulty not in answers:
            print("Defaulted to medium level. ")
            difficulty = "medium"
        WORDS =open(word_file).read().splitlines()
        word = random.choice(WORDS)
        if difficulty == "easy":
            while len(word)>5:
                word = random.choice(WORDS)
        elif difficulty == "medium":
            while len(word)>8:
                word = random.choice(WORDS)
        else:
            while len(word)<10:
                word = random.choice(WORDS)
        link = "https://www.dictionary.com/browse/" + word
        u = requests.get(link)
        soup = BeautifulSoup(u.content, 'html.parser')
        defin = soup.find("div", class_="css-1ghs5zt e1q3nk1v3").text 

        wordguessed = False
        correctguesses = []
        wrongguesses = []
        wordtoprint = ""
        while wordguessed != True:
            counter = 0
            print("")
            if len(wrongguesses) == 0:
                print("You haven't guessed any wrong letters yet. ")
            else:
                print("Stupid Guesses:" , *wrongguesses)
            if len(word)-len(wrongguesses) == len(word):
                print("")
                print("")
                print("")
                print("")
            elif len(word)-len(wrongguesses) == len(word)-1:
                print("   0   ")
                print(" ")
                print("   ")
                print(" ")
            elif len(word)-len(wrongguesses) == len(word)-2:
                print("   0   ")
                print("   I  ")
                print("   ")
                print(" ")
            elif len(word)-len(wrongguesses) == len(word)-3:
                print("   0   ")
                print("   I  ")
                print("   I   ")
                print("  ")
            elif len(word)-len(wrongguesses) == len(word)-4:
                print("   0   ")
                print("   I  ")
                print("   I   ")
                print(" /    ")
            elif len(word)-len(wrongguesses) == len(word)-5:
                print("   0   ")
                print("   I  ")
                print("   I   ")
                print(" /   \  ")
            elif len(word)-len(wrongguesses) == len(word)-6:
                print("   0   ")
                print("   I / ")
                print("   I   ")
                print(" /   \ ")
            elif len(word)-len(wrongguesses) == len(word)-7:
                print("   0   ")
                print(" \ I /  ")
                print("   I   ")
                print(" /   \ ")
            elif len(word)-len(wrongguesses) == len(word)-8:
                print("    0   ")
                print("  \ I / ")
                print("    I   ")
                print("  /   \ ")
                print("_________")
            elif len(word)-len(wrongguesses) == len(word)-9:
                print("|    0   ")
                print("|  \ I / ")
                print("|    I   ")
                print("|  /   \ ")
                print("|_________")
            elif len(word)-len(wrongguesses) == len(word)-10:
                print("__________")
                print("|")
                print("|    0   ")
                print("|  \ I / ")
                print("|    I   ")
                print("|  /   \ ")
                print("|_________")
            elif len(word)-len(wrongguesses) == len(word)-11:
                print("__________")
                print("|    |")
                print("|    0   ")
                print("|  \ I / ")
                print("|    I   ")
                print("|  /   \ ")
                print("|_________")
            else:
                input("You have run out of guesses, and your character is lying dead on the floor. Congrats. The word was " + word +". ")
                print("Meaning of word: " + defin)
                giveup()
            print("The word to guess is "+ str(len(word)) + " letters long: ") 
            for i in word:
                if i in correctguesses:
                    wordtoprint+=(" "+ i + " ")
                    
                else:
                    wordtoprint+=(" _ ")
            if "_" not in wordtoprint:
                    wordguessed=True
            print(wordtoprint)
            guess = ""
            if wordguessed==True:
                print("Well done, I guess. What do you want me to say? It's hangman! It's easy! ")
                print("Meaning of word: " + defin)
                win()

            while len(guess)!= 1:
                guess = input("Enter a letter to guess (Type a full stop to give up (if you're a coward)): ")
                if guess == "secretcode":
                    win()
                if guess == ".":
                    print("Oh, giving up are we? Well, the word was " + word +".")
                    print( "Yeah, sure, you were just about to guess that. Sure. " )
                    print(" ")
                    giveup()
                if guess in correctguesses or guess in wrongguesses:
                    guess = "?"

            if guess in word:
                print("Congratulations! " + guess + " is in the word!")
                correctguesses.append(guess)
                time.sleep(1)
            elif guess == "?":
                print("Don't guess letters you have already guessed. ")
                time.sleep(1)
            else:
                print("You absolute teaspoon, the letter " + guess + " is not in the word. Obviously. ")
                wrongguesses.append(guess)
                time.sleep(1)
            wordtoprint = ""   
            os.system('cls' if os.name == 'nt' else 'clear')  
playgame()