Import random  


def judgement(confidential, guess )
    con_list = list(confidential)
    g_list = list(guess)
		Correct_dig = sum(c == g for c, g in zip(confidential, guess)):
		con_count=count(con_list)
		gue_count=count(g_list)
		m=min(con_count,gue_count)
		avail_dig = sum(  for m in g_list)
		return correct_dig, avail_dig-correct_dig
										

def Mastermind_Game():
	print("Welcome to the world of Mastermind")

	#player1 set the confidential number
	p1_con = int( input( " Player 1: Enter your confidential number: "))
	p2_tries = 0
	correct = False


	#Player2 guesses the confidential number
	while not correct:
		guess = int(input("Player 2: Guess the number: "))
		p2_tries +=1
		correct_dig , misplaced_dig = judgement(p1_con, guess)

		if correct_dig == len(p1_con):
			correct = True
			print(f"Player 2 guessed correctly in ", p2_tries ," attemopts!")
		else:
			print(f"Digit in correct place: ",cooerct_dig ,"\n Misplaced digit: ", misplaced_dig )
