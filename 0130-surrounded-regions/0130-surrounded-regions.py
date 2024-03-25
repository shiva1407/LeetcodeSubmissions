class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        
        rows = len(board)
        cols = len(board[0])
        
        
        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or board[i][j]!='O':
                return 
            board[i][j]="E"
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            return 
        
        
        for i in range(rows):
            dfs(i,0)
            dfs(i,cols-1)
            
        for i in range(cols):
            dfs(0,i)
            dfs(rows-1,i)
            
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='E':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
        
            
            
        