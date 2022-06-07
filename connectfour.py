
turn = "Red"
def makeboard():
    result = []
    for _ in range(6):
        result.append(["0"]*7)
    return result

def formatboard(board):
    res = []
    for line in board:
        res.append(" ".join(x for x in line))
    for i in res:
        print(i)

def updateboard():
    print(turn + "'s turn!")
    while True:
        try:
            move = int(input("Where would you like to add your new piece?(1 - 7): "))
            if move < 0 or move > 7:
                print("Must be from 1 to 7")
            else:
                break
        except:
            print("Please enter a number")
    for i in range(len(board)):
        if board[i][move-1] != "0":
            if turn == "Red":
                board[i-1][move-1] = "R"
                break
            else:
                board[i-1][move-1] = "Y"
                break
        elif i == 5:
            if turn == "Red":
                board[i][move-1] = "R"
            else:
                board[i][move-1] = "Y"
    return board

def checkwin(board):
    for j, lane in enumerate(board):
        for i in range(7):
            try:
                if lane[i:i+4] == ["R","R","R","R"] or lane[i:i+4] == ["Y","Y","Y","Y"]:
                    return True
                elif board[j][i] == "R" and board[j+1][i] == "R" and board[j+2][i] == "R" and board[j+3][i] == "R":
                    return True
                elif board[j][i] == "Y" and board[j+1][i] == "Y" and board[j+2][i] == "Y" and board[j+3][i] == "Y":
                    return True
                if board[j][i] == "R" and board[j+1][i+1] == "R" and board[j+2][i+2] == "R" and board[j+3][i+3] == "R":
                    return True
                if board[j][i] == "Y" and board[j+1][i+1] == "Y" and board[j+2][i+2] == "Y" and board[j+3][i+3] == "Y":
                    return True
                if board[j][i] == "R" and board[j+1][i-1] == "R" and board[j+2][i-2] == "R" and board[j+3][i-3] == "R":
                    return True
                if board[j][i] == "Y" and board[j+1][i-1] == "Y" and board[j+2][i-2] == "Y" and board[j+3][i-3] == "Y":
                    return True
            except:
                continue
    return False
        
            

board = makeboard()
formatboard(board)
print("Welcome to Connect Four!")
while True:
    board = updateboard()
    formatboard(board)
    if checkwin(board):
        print(turn + " wins!")
        break
    if turn == "Red":
        turn = "Yellow"
    else:
        turn = "Red"
