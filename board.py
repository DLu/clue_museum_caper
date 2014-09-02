class Square:
    def __init__(self):
        self.north = None
        self.south = None
        self.west = None
        self.east = None

class Board:
    def __init__(self, filename="board.txt"):
        f = open(filename, 'r')
        flag = True
        y = 0
        self.board = []
        
        
        for line in f.readlines():
            line = line[:-1]
            if flag:
                if len(line)==0:
                    flag = False
                    continue
                row = []
                last = None
                for c in line:
                    if c == '|':
                        last = None
                    elif c==' ':
                        row.append(None)
                    elif c=='x':
                        sq = Square()
                        row.append(sq)
                        
                        if last:
                            last.east = sq
                            sq.west = last
                        
                        last = sq
                self.board.append(row)
            else:
                row = self.board[y]
                for x, sq in enumerate( row ):
                    if not sq:
                        continue
                    elif x > len(line) or line[x]==' ':
                        down = self.board[y+1][x]
                        sq.south = down
                        down.north = sq
            
        f.close()
        
        
#b = Board()
