def rockpaperscissor() :
    player1 = input("Rock, Paper, Scissor ? ")
    player2 = input("Rock, Paper, Scissor ? ")
    player1 = player1.upper()
    player2 = player2.upper()
    try_again = False
    try:
        if player1 == "ROCK" and player2 == "PAPER":
            print("Player 2 wins")
        elif player1 == "ROCK" and player2 == "SCISSOR":
            print("Player 1 wins")
        elif player1 == "PAPER" and player2 == "ROCK":
            print("Player 1 wins")
        elif player1 == "SCISSOR" and player2 == "ROCK":
            print("Player 2 wins")
        elif player1 == "PAPER" and player2 == "SCISSOR":
            print("Player 2 wins")
        elif player1 == "ROCK" and player2 == "ROCK":
            try_again = True
            print("Try Again")
        elif player1 == "PAPER" and player2 == "PAPER":
            try_again = True
            print("Try Again")
        elif player1 == "SCISSOR" and player2 == "SCISSOR":
            try_again = True
            print("Try Again")
        elif player1 == "SCISSOR" and player2 == "PAPER":
            print("Player 1 wins")

        if try_again == True:
            rockpaperscissor()
    except:
        print("Try Again")

rockpaperscissor()
