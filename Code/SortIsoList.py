def SortIsoList(UniqueLabelIsoList):
    IsoDegreeSorted = []
    for i in UniqueLabelIsoList:
        g = Graph(i[0])
        if g.degree_sequence() == [3,3,3,3,3,3,2,2,2]:
            IsoDegreeSorted.append(i)
    for i in UniqueLabelIsoList:
        g = Graph(i[0])
        if g.degree_sequence() == [3,3,3,3,3,3,2,1,1]:
            IsoDegreeSorted.append(i)   
    for i in UniqueLabelIsoList:
        g = Graph(i[0])
        if g.degree_sequence() == [3,3,3,3,3,2,2,2,1]:
            IsoDegreeSorted.append(i)
    for i in UniqueLabelIsoList:
        g = Graph(i[0])
        if g.degree_sequence() == [3,3,3,3,2,2,2,2,2]:
            IsoDegreeSorted.append(i)
    return IsoDegreeSorted

def writeSortedAppearanceChartForExcel(AppearanceChart, start, stop, filename, IsoDegreeSorted):
    myfile = file(filename, "w")
    counter = 0
    myfile.write("\t",)
    for i in range (start, stop + 1):
        myfile.write("h" + str(i) + "\t",)
    myfile.write("\n")
    for j in range(0, len(IsoDegreeSorted)):
        myfile.write(IsoDegreeSorted[j][len(IsoDegreeSorted[j])-1] + "\t",)
        counter = counter + 1
        for i in range(start, stop + 1):
            myfile.write(str(AppearanceChart[i][j]) + "\t",)
        myfile.write("\n")
    myfile.close()