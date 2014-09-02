from board import Board

b = Board()
for row in b.board:
    s1 = ''
    s2 = ''
    s3 = ''
    for sq in row:
        if sq:
            if sq.west:
                s1 += '.'
                s2 += '.'
            else:
                s += '|'
                
            s += 'o'
            
            if sq.east:
                s += '.'
            else:
                s += '|'
        else:
            s1 += '   '
            s2 += '   '
            s3 += '   '
    print s1
    print s2
    print s3
