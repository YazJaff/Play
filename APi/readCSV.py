import csv
file =open("C:/Users/yaz14/Desktop/bulkBuildFile.csv")
content=csv.reader(file)
for elt in content:
    
"""
#content=csv.reader(file)
#print(len(content))
for elt in content:
    print(elt)
for elt in content:
    for cell in elt:
        #print (cell)
        if cell=='1':
            elt.append('2')
        elif cell=='5':
            elt.append('6')
        elif cell=='9':
            elt.append('10')
        elif cell=='13':
            elt.append('14')
    #print(elt)
file.close()
file =open("C:/Users/yaz14/Desktop/bulkBuildFile.csv")
content=csv.reader(file)
#content=csv.reader(file)
#print(len(content))
for elt in content:
    print(elt)
"""
