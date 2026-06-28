class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r={}
        c={}
        s={}
        for i in range (9):
            r[i]=[0]*9
            c[i]=[0]*9
            s[i]=[0]*9        
        for index,row in enumerate(board):
            print(index)
            for colindex,number in enumerate(row):
                a=r[index]
                if number != ".":
                    number=int(number)
                    a[number-1]+=1
                    if a[number-1]>1:
                        print(number,row,index)
                        return False
                    b=c[colindex]
                    b[number-1]+=1
                    if b[number-1]>1:
                        print(number,row,index)
                        return False
                    sq=(index // 3) * 3 + (colindex // 3)
                    c1=s[sq]
                    c1[number-1]+=1
                    if c1[number-1]>1:
                        print(number,row,index,sq,c1)
                        return False
            
        return True
