def MakeChart(UniqueLabelKocayIsoList, UniqueLabelIsoList):
    AppearanceChart = []
    for i in UniqueLabelKocayIsoList:
        TempChart = []
        g = Graph(i[0])
        for k in UniqueLabelIsoList:
            counter = 0
            f = Graph(k[0])
            for j in g:
                x = copy(g)
                x.delete_vertex(j)
                if x.is_isomorphic(f):
                    counter = counter + 1
            TempChart.append(counter)
        AppearanceChart.append(TempChart)
    return AppearanceChart

def printAppearanceChart(AppearanceChart, start, stop):
    counter = 0
    print "    ",
    for i in range (start, stop + 1):
        print "h" + str(i),
    print
    for j in range(0, 240):
        if j < 10:
            print "c" + str(counter) + "  ",
        elif j < 100:
            print "c" + str(counter) + " ",
        else:
            print "c" + str(counter),
        counter = counter + 1
        for i in range(start, stop + 1):
            print str(AppearanceChart[i][j]) + "  ",
        print
        
def writeAppearanceChart(AppearanceChart, start, stop, filename):
    myfile = file(filename, "w")
    counter = 0
    myfile.write("    ",)
    for i in range (start, stop + 1):
        myfile.write("h" + str(i) + "  ",)
    myfile.write("\n")
    for j in range(0, 240):
        if j < 10:
            myfile.write("c" + str(counter) + "  ",)
        elif j < 100:
            myfile.write("c" + str(counter) + " ",)
        else:
            myfile.write("c" + str(counter),)
        counter = counter + 1
        for i in range(start, stop + 1):
            myfile.write(str(AppearanceChart[i][j]) + "   ",)
        myfile.write("\n")
    myfile.close()
    
def writeAppearanceChartForExcel(AppearanceChart, start, stop, filename):
    myfile = file(filename, "w")
    counter = 0
    myfile.write("\t",)
    for i in range (start, stop + 1):
        myfile.write("h" + str(i) + "\t",)
    myfile.write("\n")
    for j in range(0, 240):
        myfile.write("c" + str(counter) + "\t",)
        counter = counter + 1
        for i in range(start, stop + 1):
            myfile.write(str(AppearanceChart[i][j]) + "\t",)
        myfile.write("\n")
    myfile.close()
    
def writeAppearanceChartForExcel_8(AppearanceChart, start, stop, filename):
    myfile = file(filename, "w")
    counter = 0
    myfile.write("\t",)
    for i in range (start, stop + 1):
        myfile.write("h(8)" + str(i) + "\t",)
    myfile.write("\n")
    for j in range(0, len(AppearanceChart[0])):
        myfile.write("c(8)" + str(counter) + "\t",)
        counter = counter + 1
        for i in range(start, stop + 1):
            myfile.write(str(AppearanceChart[i][j]) + "\t",)
        myfile.write("\n")
    myfile.close()