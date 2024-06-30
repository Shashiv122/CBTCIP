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
										
