import random,pygame,os
class Hangman():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.word_length = 0
        self.level = 1
        self.word_list= self.getWordList()
        self.score = 0
        self.lives = 7
        self.catagory=""
        self.word=""
        self.splitted = list()
        self.stored = list()
        self.qwerty = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','z', 'x', 'c', 'v', 'b', 'n', 'm']
        
    def initializer(self):
        self.word_list= self.getWordList()
        self.get_random_words()

    def dashDash(self,word):
        dashList = list()
        for dash in range(word):
            dashList.append("_")
        return dashList
    def getWordList(self):
        wordList = []
        f = open(f"levels/level{self.level}.csv","r")
        for data in f:
            words = data.strip().split(',')
            if len(words) == 2:
                wordList.append((words[0],words[1]))
        return wordList
        
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
        king_fisher = None
        while True:     #This loop will run to generate random words
            number = random.randint(0,len(self.word_list)-1)
            self.catagory,self.word=self.word_list[number]  #Storing the category and the word in their respective variables
            self.splitted = list(self.word) #Splitting the word
            self.dash = self.dashDash(len(self.word))
            self.layout("","")      #Layout here will also get called in a loop
            while True: #Main Loop
                option = None       #option is declared here so, we can access its value inside elif self.lives
                if len(self.stored) == len(self.splitted):
                    break
                elif self.lives == 0:
                    break
                self.user_input()
            if self.lives == 0:
                self.announce()
                option = input("Do you want to try again? (y/n) ")
                if option == "n":
                #The game will announce the result and exit
                    break
                else:
                    #The game will continue
                    os.system("cls")
                    self.stored = list()
                    self.dash = self.dashDash(self.word_length)
                    self.qwerty = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','z', 'x', 'c', 'v', 'b', 'n', 'm']
            else:
                if self.lives < 7:
                    self.lives += 1
                #The game will continue
                os.system("cls")
                self.stored = list()
                self.dash = ['_','_','_','_']
                self.qwerty = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','z', 'x', 'c', 'v', 'b', 'n', 'm']
            if self.score == 120:
                king_fisher = 1
                break
        if king_fisher:
            self.level += 1
            self.initializer()

    
    #Repeating Layout 
    def layout(self,index,word):
        print(f"\n {self.catagory}\t\tScore:{self.score}\t\tLives:{self.lives}\t\tLevel:{self.level}\n") #Displaying score and lives
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
        if self.score > 120:
            print("\nThe word was: ",self.word)
            print("\nYEAH! You played very well!")
            self.play_sound("music/Success2.wav")
            print(f"Your score is: {self.score}")

        else:
            self.play_sound("music/Fail.wav")
            print("\nThe word was: ",self.word)
            print("\nBetter luck next time :(") 
          
#Main
h = Hangman()
h.greetings()
h.get_random_words()
