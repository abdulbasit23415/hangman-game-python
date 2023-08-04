import random,pygame,os
class Hangman():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.score = 0
        self.lives = 7
        self.catagory=""
        self.word=""
        self.splitted = list()
        self.stored = list()
        self.dash = ['_','_','_','_']
        self.qwerty = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','z', 'x', 'c', 'v', 'b', 'n', 'm']
        self.word_list=[("food","cake"),("place","park"),("animals","lion"),("celestial","star"),("transportation","ship"),("sports","ball"),("celestial","moon"),("weather","rain"),("aquatic","fish"),("nature","tree")]
    # Greetings function
    def greetings(self):
        print("Welcome to the hangman game")
        self.play_sound("music/Success2.wav")
    
    # Playing sounds
    def play_sound(self,audio):
        pygame.mixer.music.load(audio)
        pygame.mixer.music.play()
    
    #Picking random words from the List of Tuples
    def get_random_words(self):
        number = random.randint(0,9)
        self.catagory,self.word=self.word_list[number]  #Storing the category and the word in their respective variables
        self.splitted = list(self.word) #Splitting the word
        print(f"\n\t\t\t {self.catagory}\t\tScore:{self.score}\t\tLives:{self.lives}\n") #Displaying score and lives
        #Printing the dash list
        for dash in self.dash:
                print("\t\t\t",dash,end=" ")
        print("\n")
        for char in self.qwerty: #Displaying the keyboard here
            print(char,end=" ")
            if char == "p" or char == "l" or char == "m":
                print("\n")
        
        while True: #Main Loop
            if len(self.stored) == len(self.splitted):
                break
            elif self.lives == 0:
                break
            self.user_input()
        self.announce()
    
    #Repeating Layout 
    def layout(self,index,word):
        print(f"\n\t\t\t {self.catagory}\t\tScore:{self.score}\t\tLives:{self.lives}\n\t\t\t\t") #Displaying score and lives
        if word in self.splitted:
            #Popping the dashes from the specified index and adding the word at that index
            for i in index:
                self.dash.pop(i)
                self.dash.insert(i,word)

        #Printing the dash list
        for dash in self.dash:
                print(dash,end=" ")
        print("\n")
        for char in self.qwerty:
            print(char,end=" ")
            if char == "p" or char == "l" or char == "m":
                print("\n")
    
    #Checker function to check whether the char exist in the generated word or not
    def checker(self,char):
        ind = [index for index,letter in enumerate(self.splitted) if char == letter]
        if len(ind) > 0:
            #If exists increase the score and play the success music
            for index in ind:
                self.stored.insert(index, char)
                self.score += 10
                self.play_sound("music/Success.wav")
        else:
            #Else decrease the lives and play the fail music
            self.lives -= 1
            print("\t\t\t\t",self.display_hangman(self.lives))
            self.play_sound("music/Error.wav")
        #Also remove that typed char from the keyboard
        self.qwerty.remove(char)
        return ind
    
    #Taking user input here
    def user_input(self):
        word = input("\nGuess the word: ")
        os.system("cls")
        indices = self.checker(word)
        self.layout(indices,word)

    #Hangman hangs here
    def display_hangman(self,lives):
        stages = [  # final state: head, torso, both arms, and both legs
                    """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
                    """,
                    # head, torso, both arms, and one leg
                    """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -
                    """,
                    # head, torso, and both arms
                    """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |      
                    -
                    """,
                    # head, torso, and one arm
                    """
                    --------
                    |      |
                    |      O
                    |     \|
                    |      |
                    |     
                    -
                    """,
                    # head and torso
                    """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                    """,
                    # head
                    """
                    --------
                    |      |
                    |      O
                    |    
                    |      
                    |     
                    -
                    """,
                    # initial empty state
                    """
                    --------
                    |      |
                    |      
                    |    
                    |      
                    |     
                    -
                    """
        ]
        return stages[lives]
    
    #Announcing the final results
    def announce(self):
        if self.stored == self.splitted:
            print("\nYEAH! You WON!")
            self.play_sound("music/Success2.wav")
            print(f"Your score is: {self.score}")

        else:
            self.play_sound("music/Fail.wav")
            print("The word was: ",self.word)
            print("\nBetter luck next time :(") 
          
#Main
h = Hangman()
h.greetings()
h.get_random_words()
