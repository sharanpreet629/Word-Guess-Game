
#import library
import random
import os
#global variables
movielist = ["avatar","death note","demons slayer","gravity","my hero academia"]
wronglist = []
#user defined functions
def clearScreen():
	if os.name == 'posix':
		#For UNIX system 'posix':
		_ = os.system('clear')
	else:
		#For Windows system 'nt':
		_ = os.system('cls')

def gameplay():
    movie = random.choice(movielist)
    length = len(movie)
    print("****start the Movie guessing game*****")
    print("your movie name has {} charaters".format(length))
    
    turns = 2 + length
    print("the total number of chances to guess are: {}".format(turns))
    
    #create a variable to store the movie name 
    display = movie
    dash = "_"
    for i in range(length):
        if movie[i]==" ":
            display= display[0:i]+ " "+ display[i+1:]
        else:
            display= display[0:i]+ dash + display[i+1:]
    
    print(" ".join(display))
#taking input from player    
    while display!=movie and turns>0:
        
        guess_letter = input("guess a character:")
        if not guess_letter.isalpha():
            print("choose a charater only")
        elif len(guess_letter)>1:
              print("guess only one letter")
              
        elif guess_letter in wronglist:
              print("you have alraedy guess the letter")
        #checking if guessed letter is correct or not 
        if guess_letter in movie:
            for i in range(length):
                if movie[i]==" ":
                    display= display[0:i]+ " " + display[i+1:]
                if movie[i]== guess_letter :
                    display= display[0:i]+ guess_letter + display[i+1:]
            print(" ".join(display))
            print("Attempts left :",turns-1) 
        else:
             print("your guess was wrong")
             wronglist.append(guess_letter)
        turns-=1
        
        
       #checking if player won the guess then ending the game:
              
        if movie == display:
         
           print("****you have won the game****")
           print("the movie name is {}".format(movie))
           
           
        if movie!= display and turns==0:
            print("you lost the game")
            
         
def restartgame():
    choose = input("play again??\n yes or no: ")
    if choose.lower()=="yes":
        clearScreen()
        main()     
    else:
        print("GAME OVER")
   
        
#main function
def main():
    gameplay()
    restartgame()
    
if __name__=="__main__":
    main()
      
