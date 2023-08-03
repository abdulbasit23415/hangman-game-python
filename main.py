import random
class Hangman():
    def __init__(self):
        self.score = 0
        self.lives = 5
        self.catagory=""
        self.word=""
        self.splitted = list()
        self.stored = list()
        self.dash = ['_','_','_','_']
        self.qwerty = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','z', 'x', 'c', 'v', 'b', 'n', 'm']
        self.word_list=[("food","cake"),("place","park"),("animals","lion"),("celestial","star"),("transportation","ship"),("sports","ball"),("celestial","moon"),("weather","rain"),("aquatic","fish"),("nature","tree")]
    def greetings(self):
        print("welcome to the hangman game")
    def get_random_words(self):
        number = random.randint(0,9)
        self.catagory,self.word=self.word_list[number]
        self.splitted = list(self.word)
        print(f"\n {self.catagory}\t\tScore:{self.score}\t\tLives:{self.lives}\n")
        for dash in self.splitted:
                print(" _",end=" ")
        print("\n")
        for char in self.qwerty:
            print(char,end=" ")
            if char == "p" or char == "l" or char == "m":
                print("\n")
        while True: 
            if len(self.stored) == len(self.splitted):
                break
            elif self.lives == 0:
                break
            self.user_input()
        self.announce()
    def layout(self,index,word):
        print(f"\n {self.catagory}\t\tScore:{self.score}\t\tLives:{self.lives}\n")
        if word in self.splitted:
            for i in index:
                self.dash.pop(i)
                self.dash.insert(i,word)

        for dash in self.dash:
                print(dash,end=" ")
        print("\n")
        for char in self.qwerty:
            print(char,end=" ")
            if char == "p" or char == "l" or char == "m":
                print("\n")
    def checker(self,char):
        ind = [index for index,letter in enumerate(self.splitted) if char == letter]
        if len(ind) > 0:
            for index in ind:
                self.stored.insert(index, char)
                self.score += 10
        else:
            self.lives -= 1
            print("\t\t\t\t",self.display_hangman(self.lives))
        self.qwerty.remove(char)
        return ind
    def user_input(self):
        word = input("Guess the word: ")
        resp = self.checker(word)
        self.layout(resp,word)

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
    
    def announce(self):
        if self.stored == self.splitted:
            print("\nYEAH! You WON!")
            print(f"Your score is: {self.score}")
        else:
            print("\nBetter luck next time :(") 

           

          

h = Hangman()
h.greetings()
h.get_random_words()


