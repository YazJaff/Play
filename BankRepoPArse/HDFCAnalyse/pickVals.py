def parseDatum(datum):
    dates=[]
    descs=[]
    debit=[]
    credit=[]
    bal=[]
    i=0
    print("In--------->>>>>> ParseDatum")
    num=['1','2','3','4','5','6','7','8','9','0']
    rsFlag=0
    while i< len(datum):
        if datum[i].find('/18') !=-1 or datum[i].find('/19') !=-1:
            print("Date     ->  ",datum[i])
        elif datum[i].find('NEFT') !=-1 or datum[i].find('Credit') !=-1:
            print("Credits     ->  ",datum[i])
        elif datum[i].find('UPI') !=-1 or datum[i].find('Credit') !=-1::
            pass
        if datum[i].find('.')!=-1:
            if datum[i][0] in num and datum[i][len(datum[i])-1] in num:
                if datum[i].count(".")==2:
                    print("Credit   ->", datum[i][0:datum[i].find(".")+3])
                    print("BalL    ->>",datum[i][datum[i].find(".")+3:len(datum[i])])
                    #print("Paise     ->  ",datum[i])
                else:
                    if rsFlag==0:
                        print("Debit        ->>",datum[i])
                        rsFlag=1
                    elif rsFlag==1:
                        print("Ballll       ->>",datum[i])
                        rsFlag=0
        #if datum[i][0] in num and datum[i][len(datum[i])-1] in num:
         #   print("IDsss     ->  ",datum[i])
        i+=1

