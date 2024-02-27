


def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    # print(board)


    for i in range(len(board)):
        row = {}
        for j in range(len(board[i])):
            if(board[i][j]!="."):
                if row.get(board[i][j],None):
                    return False
                else:
                    row[board[i][j]] = 1
            if i==0:
                col = {}
                for k in range(len(board)):
                    if(board[k][j]!="."):
                        if col.get(board[k][j],None):
                            return False
                        else:
                            col[board[k][j]] = 1
    for i in range(0,len(board),3):
        for j in range(0,len(board[i]),3):
            digits= {}
            for p in range(i,i+3,1):
                for q in range(j,j+3,1):
                    if(board[p][q]!="."):
                        if digits.get(board[p][q],None):
                            return False
                        else:
                            digits[board[p][q]]= board[p][q]
                    

    return True
        
        
def isValidSudoku2(board):
    print(board)
    rows =[set() for i in range(9)]
    cols =[set() for i in range(9)]
    squares = [[set() for x in range(3)] for y in range(3)]
    print(squares)
    for r in range(9):
        for c in range(9):
            print(r,c)
            if board[r][c] == '.':
                continue
            if board[r][c] in rows[r] or board[r][c] in cols[r] or board[r][c] in squares[r//3][c//3]:
                return False
            
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            # for each 3 by 3 square all the elements in it are addded to the resepective set in below statement
            # this helps to avodi looping on it again 
            squares[r//3][c//3].add(board[r][c])
    print("squares",squares)
    return True

            






board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


# print(isValidSudoku(board))
print(isValidSudoku2(board))