import random
#Rock Paper Scissor Game
def comaprison( p1, c):
        scorep1=0
        scorec=0
        if p1=="Rock"  and c=="Scissor":
                print("You win! \n Rock crushes Scissor!")
                scorep1+=1
        elif p1=="Scissor"  and c=="Paper":
                print("You win! \n Scissor cuts Paper!")
                scorep1+=1
        elif p1=="Paper" and c=="Rock":
                print("You win! \n Paper wraps Rock!")
                scorep1+=1
                
        elif c=="Rock" and p1=="Scissor":
                print("Computer wins!")
                scorec+=1
                print("Rock Crushes Scissor!")
        elif c=="Scissor"  and p1=="Paper" :
                print("Computer wins!")
                scorec+=1
                print("Scissor cuts Paper!")
        elif c=="Paper"  and p1=="Rock"  :
                print("Computer wins!")
                scorec+=1
                print("Paper wraps Rock!")
        else:
                print("Its a tie!")
        print("Score of Computer: ", scorec)
        print("Score of player: ", scorep1)
        return scorep1,scorec

def main():
        print("Welcome to the Game!")
        print("Lets begin!")
        
        #choice list
        choices=["Rock","Paper","Scissor"]
        
        #score initialization
        scorep1=0
        scorec=0

        while True:
            #player input choice (ROCK, paper Scissor)
            player = input(" ENTER YOUR CHOICE (ROCK, PAPER, SCISSOR): ").capitalize()
        
            if player not in choices:
                print("Invalid Choice. Please choose any one - rock, paper, or scissor.")
                continue
            
            #Computer choose now
            computer = random.choice(choices)
            print("COMPUTER'S CHOICE: ",computer)

            #function call- comaprison
            p_sc,c_sc=comaprison(player, computer)
            scorep1+=p_sc
            scorec+=c_sc
            
            #play again
            play_again = input("PLAY AGAIN (YES/NO): ").strip().lower()
            if play_again != "yes":
                break
                
        print("Final Score - Player:", scorep1, "Computer:", scorec)
        print("Thanks for playing!")
main()
