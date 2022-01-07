

fileName = "AllEnergyForElectron.txt" 
file = open( fileName, "r")
l=0

runs = []
energy = []
meanX = []
meanY = []
spreadX = []
spreadY = []

dictBS = {'Run': [], 'Energy': [], 'impactX_Layer1': [], 'impactY_Layer1': [], 'SpreadX': [], 'SpreadY': []}

allLines = []

for line in file: 
     text = line.split()
     if l==0:
         l=l+1
         continue
     
     tmpruns, tmpenergy, tmpmeanX, tmpmeanY, tmpspreadX, tmpspreadY = line.split()
     runs.append(tmpruns)
     energy.append(tmpenergy)
     meanX.append(tmpmeanX)
     meanY.append(tmpmeanY)
     spreadX.append(tmpspreadX)
     spreadY.append(tmpspreadY)
     
     allLines.append(line)
#     print text
     l=l+1

dictBS['Run'].append(runs)
dictBS['Energy'].append(energy)
dictBS['impactX_Layer1'].append(meanX)
dictBS['impactY_Layer1'].append(meanY)
dictBS['SpreadX'].append(spreadX)
dictBS['SpreadY'].append(spreadY)

#if dictBS['Run']=='441':
#    print dictBS


print allLines

print ""
#runsToTake=['441','597','456', '468', '490', '502', '384', '645', '405']
#energyToTake=['20', '30', '50', '80', '100', '150', '200', '250', '300']

for lines in allLines:
    run = lines.split(" ", 1)
    print run
    if(run[0]=='441'):
        print run[1]
