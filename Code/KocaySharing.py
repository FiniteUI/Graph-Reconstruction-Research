def getKocayCardSharing(AppearanceChartSorted):
    KocayCardSharing = []
    for i in AppearanceChartSorted:
        tempKCS = []
        for j in AppearanceChartSorted:
            shared = 0
            for k in range(0, len(j)):
                if i[k] != 0 and j[k] != 0:
                    if i[k] < j[k]:
                        shared = shared + i[k]
                    else:
                        shared = shared + j[k]
            tempKCS.append(shared) 
        KocayCardSharing.append(tempKCS)
    return KocayCardSharing
        
def printKocayCardSharing(KocayCardSharing):
    print "\t",
    for i in range(0, len(KocayCardSharing)):
        print "h" + str(i) + "\t",
    print
    for i in range(0, len(KocayCardSharing)):
        print "h" + str(i) + "\t",
        for j in range(0, len(KocayCardSharing)):
            print str(KocayCardSharing[j][i]) + "\t",
        print
        
def getKocayCardShared(AppearanceChartSorted, UniqueCardDegreesRaw):
    KocayCardShared = []
    icounter = 0
    for i in AppearanceChartSorted:
        jcounter = 0
        for j in AppearanceChartSorted:
            tempKCSD = []
            if jcounter != icounter:
                tempKCSD.append("h" + str(icounter) + " h" + str(jcounter))
                for k in range(0, len(j)):
                    if i[k] != 0 and j[k] != 0:
                        tempKCSD.append(UniqueCardDegreesRaw[k])
                jcounter = jcounter + 1
            if len(tempKCSD) > 1:
                KocayCardShared.append(tempKCSD)
        icounter = icounter + 1
    return KocayCardShared