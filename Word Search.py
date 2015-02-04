class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(word,0,i,j,board):
                    return True
        return False
    def search(self,word,index,x,y,board):
        if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
            return False
        if index==len(word)-1 and board[x][y]==word[-1]:
            return True
        if board[x][y]!=word[index] or board[x][y]=='0':
            return False
        c = board[x][y]
        board[x][y] = '0'
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if(abs(i)+abs(j)==1):
                    if self.search(word,index+1,x+i,y+j,board):
                        return True
        board[x][y] = c
        return False
        