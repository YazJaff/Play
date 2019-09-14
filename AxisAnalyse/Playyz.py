num=['1','2','3','4','5','6','7','8','9','0']
#datum='RESTAURANTS277.00 Dr27/06/2019SWIGGY'
datum='231.59 Dr15/07/2019DEBIT INTEREST'
datum=' 1,286.63 Dr   EMI BALANCESAmazon Seller Services'
if datum.find('/2019')>0:
    date=datum[datum.find('/2019')-5:datum.find('/2019')+5]
    CorD=datum[datum.find('/2019')-7:datum.find('/2019')-5]
    nxtSale=datum[datum.find('/2019')+5:len(datum)]
    sale=datum[0:datum.find('/2019')-7]
    i=flg=init=fin=0
    print('Sale',sale)
    while i<len(sale):
        if sale[i] in num:
            if init==0:
                amt=sale
                sale='-'
                break
            else :
                if flg==0:
                    init=i
                    flg+=1
                fin=i
        i+=1
    if init != 0:
        amt=sale[init:fin+1]
        sale=sale[0:init]
else :
    date='-'
    sale='-'
    nxtSale='-'
    if datum.find('Dr'):
        amt=datum[0:datum.find('Dr')]
        CorD=datum[datum.find('Dr'):datum.find('Dr')+2]





print(sale)
print(amt)
print(CorD)
print(date)
print(nxtSale)

