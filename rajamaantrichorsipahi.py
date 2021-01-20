import random
print("WELCOME TO THE GAME")
print("Points system: ")
print(" RAJA = 1000 pts")
print(" MANTRI = 800 pts")
print(" CHOR = 0 pts")
print(" SIPAHI = 500 pts")
score1=score2=score3=score4=0
player1=input("ENTER FIRST PLAYER NAME:- ")
player2=input("ENTER SECOND PLAYER NAME:- ")
player3=input("ENTER THIRD PLAYER NAME:- ")
player4=input("ENTER FOURTH PLAYER NAME:- ")
choice="y"
while(choice=="Y" or choice=="y"):
	randomno=random.randint(1,4)
	if randomno==1:
		print(player1, "is RAJA")
		score1+=1000
		print(player3, "is MANTRI")
		print(player3,end=" ")
		mantri=input(player3 +"FIND THE CHOR:- ")
		if mantri==player2:
			print(player3, " is right,",player2," is CHOR!")
			score2+=000
			score3+=800
			score4+=500
		else:
			print(player3, " is wrong," ,player2," is CHOR!")
			score2+=800
			score3+=000
			score4+=500
		print(player1, "score is ",score1)
		print(player2, "score is ",score2)
		print(player3, "score is ",score3)
		print(player4, "score is ",score4)

	elif randomno==2:
		print(player2, "is RAJA")
		score2+=1000
		print(player1, " is MANTRI")
		print(player1,end=" ")
		mantri=input( "FIND THE CHOR:- ")
		if mantri==player4:
			print(player1, " is right,",player4," is CHOR!")
			score1+=800
			score3+=500
			score4+=000
		else:
			print(player1, " is wrong,",player4," is CHOR!")
			score1+=000
			score3+=500
			score4+=800
		print(player1, "score is ",score1)
		print(player2, "score is ",score2)
		print(player3, "score is ",score3)
		print(player4, "score is ",score4)

	elif randomno==3:
		print(player3, "is RAJA")
		score3+=1000
		print(player4, " is MANTRI")
		print(player4,end=" ")
		mantri=input("FIND THE CHOR:- ")
		if mantri==player1:
			print(player4, " is right,",player1," is CHOR!")
			score1+=000
			score2+=500
			score4+=800
		else:
			print(player4, " is wrong,",player1," is CHOR!")
			score1+=800
			score2+=500
			score4+=000
		print(player1, "score is ",score1)
		print(player2, "score is ",score2)
		print(player3, "score is ",score3)
		print(player4, "score is ",score4)

	elif randomno==4:
		print(player4, "is RAJA")
		score4+=1000
		print(player2, " is MANTRI")
		print(player2,end=" ")
		mantri=input("FIND THE CHOR:- ")
		if mantri==player1:
			print(player2, " is right,",player1," is CHOR!")
			score1+=000
			score2+=800
			score3+=500
		else:
			print(player2, " is wrong,",player3," is CHOR!")
			score1+=800
			score2+=000
			score3+=500
		print(player1, "score is ",score1)
		print(player2, "score is ",score2)
		print(player3, "score is ",score3)
		print(player4, "score is ",score4)
		break

	else:
		print(player2, "is RAJA")
		score2+=1000
		print(player4, "is MANTRI")
		print(player4,end=" ")
		mantri=input("FIND THE CHOR:- ")
		if mantri==player3:
			print(player4, " is right,",player3," is CHOR!")
			score1+=500
			score3+=000
			score4+=800
		else:
			print(player4, " is wrong,",player3," is CHOR!")
			score1+=500
			score3+=800
			score4+=000
		print(player1, "score is ",score1)
		print(player2, "score is ",score2)
		print(player3, "score is ",score3)
		print(player4, "score is ",score4)
	choice=input("Wanna play more?(y/n)")

	
