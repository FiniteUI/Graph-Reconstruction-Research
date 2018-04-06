#note: most of these are very specific and build off of eachother
load("G10.0-G10.18.py")
L = getMainGraphs()
load('BD_Decks.py')

def getAllCards():
    #this returns a list of all cards as graph objects, with one BD_Decks in each cell
    AllCards = []
    for i in range(0, len(L)):
        x = BD_Decks(L[i])
        AllCards.append(x)
    return AllCards
        
def makeList():
    #this builds a list of strings representing all cards
    MainList = []
    KocayList = []
    BigOleCardList = []
    for i in range(0, len(L)):
        p = []
        p.append(L[i].name())
        p.append(L[i].graph6_string())
        p.append(L[i].degree_sequence())
        MainList.append(p)
        x = BD_Decks(L[i])
        for j in x:
            if type(j) is not sage.graphs.graph.Graph:
                z = []
                for k in j:
                    y = []
                    y.append(k.name())
                    y.append(k.graph6_string())
                    y.append(k.degree_sequence())
                    z.append(y)
                BigOleCardList.append(z)
            else:
                z = []
                z.append(j.name())
                z.append(j.graph6_string())
                z.append(j.degree_sequence())
                KocayList.append(z)
    return MainList, KocayList, BigOleCardList       
         
          
def printCardList(BigOleCardList):
    #this prints the list from MakeList in an easier to view fashion
    print('Name\t\t\tgraph6\t\tDegree Sequence')
    print("-------------------------------------------------------")
    for i in BigOleCardList:
        for j in i:
            print
            for k in j:
                print(str(k) + "\t\t"),
                
def getUniqueCards(BigOleCardList):
    #This makes a list of the graph6 notation of each unique card
    AlreadySeenCard = []
    for i in BigOleCardList:
        for j in i:
            match = False
            g = Graph(j[1])
            for k in range(0, len(AlreadySeenCard)):
                f = Graph(AlreadySeenCard[k])
                if f.is_isomorphic(g):
                    match = True
                    break;
            if not match:
                AlreadySeenCard.append(j[1])
    return AlreadySeenCard 

def MakeIsoList(AlreadySeenCard, BigOleCardList):
    #this groups together all isomorphic cards
    UniqueCardList = []
    doneWith = []
    for i in range(0, len(AlreadySeenCard)):
        y = []
        y.append(AlreadySeenCard[i])
        g = Graph(AlreadySeenCard[i])
        for j in BigOleCardList:
            for k in j:
                if k[0] not in doneWith:
                    f = Graph(k[1])
                    if f.is_isomorphic(g):
                        y.append(k[0])
                        doneWith.append(k[0])
        UniqueCardList.append(y)
    return UniqueCardList

def printIsoList(UniqueCardList):
    #this prints the iso list in a slightly prettier fashion
    print "Isomorphisms:"
    print
    for i in UniqueCardList:
        print('\t' + i[0])
        for j in range(1, len(i)):
            print('\t\t' + i[j])
        print
        
def getDegreeLists(ISO):
    #this organizes the graphs from the isolist by degree sequences
    DSL = [[3,3,3,3,3,3,2,2,2], [], [3,3,3,3,3,3,2,1,1], [], [3,3,3,3,3,2,2,2,1], [], [3,3,3,3,2,2,2,2,2], []]
    for i in ISO:
        g = Graph(i[0])
        if g.degree_sequence() == DSL[0]:
            DSL[1].append(i)
        elif g.degree_sequence() == DSL[2]:
            DSL[3].append(i)
        elif g.degree_sequence() == DSL[4]:
            DSL[5].append(i)
        elif g.degree_sequence() == DSL[6]:
            DSL[7].append(i)
        else:
            print "Error: Unexpected degree sequence..."
            break
    return DSL

def printDegreeLists(DSL):
    #this prints the degree lists generated in the last function
    for i in range(0, len(DSL)):
        if i%2 == 0:
            print DSL[i]
        else:
            for j in range(0, len(DSL[i])):
                print "\t" + str(DSL[i][j][0])
                for k in range(1, len(DSL[i][j])):
                    print "\t\t" + str(DSL[i][j][k])
                print
            print "-------------------------------"

def getKocayIso(K):
    #this gets the isomorphism list for the kocay graphs
    done = []
    KISOList = []
    for i in K:
        KISOTemp = []
        g = Graph(i[1])
        if i[1] not in done:
            KISOTemp.append(i[1])
            KISOTemp.append(i[0])
            done.append(g.graph6_string())
            for j in K:
                if j[1] not in done:
                    f = Graph(j[1])
                    if f.is_isomorphic(g):
                        KISOTemp.append(j[0])
                        done.append(j[1])
            KISOList.append(KISOTemp)
    return KISOList

def printKisoList(KISOList):
    #this prints the kisolist generated in the last function
    for i in KISOList:
        print i[0]
        for j in range(1, len(i)):
            print '\t' + str(i[j])
        print