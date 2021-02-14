def bits_Parse(datum):
    if datum.find('/2019')>0:
        date=datum[datum.find('/2019')-5:datum.find('/2019')+5]
        CorD=datum[datum.find('/2019')-7:datum.find('/2019')-5]
        nxtSale=datum[datum.find('/2019')+5:len(datum)]
        sale=datum[0:datum.find('/2019')-7]
        i=flg=init=fin=0
        rsIndx=[]
        num=['1','2','3','4','5','6','7','8','9','0']
        while i<len(sale):
            if sale[i] in num:
                rsIndx.append(i)
            i+=1
        amt=sale[rsIndx[0]:rsIndx[-1]]
        if amt.find(',')>0:
            amt=amt[0:amt.find(',')]+amt[amt.find(',')+1:len(amt)]
        if len(sale[0:rsIndx[0]])<2:
            sale='-'
        else:
            sale=sale[0:rsIndx[0]]
    else :
        date='-'
        sale='-'
        nxtSale='-'
        if datum.find('Dr')>0:
            amt=datum[0:datum.find('Dr')]
            if amt.find(',')>0:
                amt=amt[0:amt.find(',')]+amt[amt.find(',')+1:len(amt)]
            CorD=datum[datum.find('Dr'):datum.find('Dr')+2]
        elif datum.find('Cr')>0:
            amt=datum[0:datum.find('Cr')]
            if amt.find(',')>0:
                amt=amt[0:amt.find(',')]+amt[amt.find(',')+1:len(amt)]
            CorD=datum[datum.find('Cr'):datum.find('Cr')+2]
    ret_Arr=[]
    ret_Arr.append(sale)
    ret_Arr.append(float(amt))
    ret_Arr.append(CorD)
    ret_Arr.append(date)
    ret_Arr.append(nxtSale)
    #print(sale)
    #print(amt)
    #print(CorD)
    #print(date)
    #print(nxtSale)
    return ret_Arr

#datum='RESTAURANTS277.00 Dr27/06/2019SWIGGY'
#datum='231.59 Dr15/07/2019DEBIT INTEREST'
datum=' 1,286.63 Dr   EMI BALANCESAmazon Seller Services'
datum=' 100.00 Cr   EMI BALANCESAmazon Seller Service'
abc=bits_Parse(datum)
#print(abc)