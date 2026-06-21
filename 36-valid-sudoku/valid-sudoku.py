class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=len(board)
        col=len(board[0])
        for i in range(row):
            arr=[]
            for j in range(col):
                if board[i][j]!=".":
                    arr.append(board[i][j])
            if len(arr)!=len(set(arr)):
                return False
        for j in range(col):
            arr2=[]
            for i in range(row):
                if board[i][j]!=".":
                    arr2.append(board[i][j])
                
            if len(arr2)!=len(set(arr2)):
                return False
        for box_row in range(0, 9, 3):      # 0, 3, 6
            for box_col in range(0, 9, 3):  # 0, 3, 6

                arr = []

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):

                        if board[i][j] != ".":
                            arr.append(board[i][j])

                if len(arr) != len(set(arr)):
                    return False    
        return True
        



        
        
