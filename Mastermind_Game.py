#checkin both the numbers for feedback
def judgement(confidential, guess ):
        con_list = list(confidential)
        g_list = list(guess)
        correct_dig = sum(c == g for c, g in zip(confidential, guess))
        con_count=len(con_list)
        gue_count=len(g_list)
        m=min(con_count,gue_count)
        avail_dig = sum(min(con_list.count(d), g_list.count(d)) for d in set(g_list))
        return correct_dig, avail_dig-correct_dig


#main code for the game
def Mastermind_Game():
        print("Welcome to the world of Mastermind")

        #player1 set the confidential number
        p1_con = input( " Player 1: Enter your confidential number: ")
        p2_tries = 0
        correct = False


        #Player2 guesses the confidential number
        while not correct:
                guess = input("Player 2: Guess the number: ")
                p2_tries +=1
                correct_dig , misplaced_dig = judgement(p1_con, guess)

                if correct_dig == len(p1_con):
                        correct = True
                        print(f"Player 2 guessed correctly in ", p2_tries ," attemopts!")
                else:
                        print(f"Digit in correct place: ",correct_dig ,"Misplaced digit: ", misplaced_dig )



	#player2 set the confidential number
        p2_con = input( " Player 2: Enter your confidential number: ")
        p1_tries = 0
        correct = False


        #Player1 guesses the confidential number
        while not correct:
                guess = input("Player 1: Guess the number: ")
                p1_tries +=1
                correct_dig , misplaced_dig = judgement(p2_con, guess)

                if correct_dig == len(p2_con):
                        correct = True
                        print(f"Player 1 guessed correctly in ", p1_tries ," attempts!")
                else:
                        print(f"Digit in correct place: ",correct_dig ,"Misplaced digit: ", misplaced_dig )

	#winner announced
	winner(p1_tries,p2_tries)


#announcing the winner of Mastermind Game
def winner(p1_t,p2_t):
	if p1_t < p2_t:
		ptint(" Player 1 is the Mastermind! ")
	elif p1_t > p2_t :
		print(" Player 2 is the Mastermind! ")
	else:
		print(" It's a tie! ")
Mastermind_Game()
