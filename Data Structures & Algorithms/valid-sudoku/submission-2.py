class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(len(board)):
            s = set()
            for el in board[i]:
                if el == ".":
                    continue
                elif el in s:
                    print("rows")
                    return False
                else:
                    s.add(el)
        # check cols
        for i in range(len(board[0])):
            s = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in s:
                    return False
                else:
                    s.add(board[j][i])
        # check squares
        for i in range(2):
            for j in range(2):
                s = set()
                for x in range(3*i, 3*i + 3):
                    for y in range(3*j, 3*j + 3):
                        if board[x][y] == ".":
                            continue 
                        elif board[x][y] in s:
                            print("squares")
                            return False
                        else:
                            s.add(board[x][y])

        return True
    

