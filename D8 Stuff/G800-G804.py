def getD8Graphs():
    #this is simple a hardcoding of the 5 graphs of degree three on 8 vertices
    #they are returned as a list
    
    V8D3 = [
            [8,[2,2,-2,-2],2],#G800
            [8,[4,-2,4,2],2],#G801
            [8,[2,4,-2,3,3,4,-3,-3],1],#G802
            [8,[-3,3],4],#G803 Cube
            [8,[4],8],#G804
            ]
    GV8D3 = []

    
    for i in range(0,5):
        g = graphs.LCFGraph(V8D3[i][0], V8D3[i][1], V8D3[i][2])
        g.name("G8" + "{:0>2d}".format(i))
        GV8D3.append(g)
    
    
    return GV8D3