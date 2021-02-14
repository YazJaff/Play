import PyPDF2
from Playyz import bits_Parse
def pickVals(data):
    dates=[]
    merchs=[]
    payments=[]
    merchBuff=''
    amtDrs=[]
    amtCrs=[]
    datas=[]
    i=0
    while i<len(data):
        datum=data[i]
        if datum.find('IMTHIYAZ')>0:
            datum=datum[datum.find('IMTHIYAZ'):len(datum)]
            dates.append(datum[datum.find('/2019')-5:datum.find('/2019')+5])
            merchBuff=datum[datum.find('/2019')+5:len(datum)]+'$'
        else :
            bits=bits_Parse(data[i])
            if bits[2]=='Dr':   #corD
                merchs.append(merchBuff+'~'+bits[0])
                merchBuff=bits[4]    
                amtDrs.append(bits[1])
            else:
                payments.append(merchBuff+'~'+bits[0])
                merchBuff=bits[4]
                amtCrs.append(bits[1])
        i+=1
    #print(len(merchs),' -   ',len(amtDrs))
    fee=bb=gst=interest=food=0
    j=0
    debitAmt=0
    for a in amtDrs:
        debitAmt+=a
    creditAmt=0
    for a in amtCrs:
        creditAmt+=a
    print("billed           -   ",debitAmt-29860.0)
    print('paid             -   ',creditAmt-29860.0)
    print('diff             -  ',debitAmt-creditAmt)
    while j<len(merchs) and j<len(amtDrs):
        if merchs[j].find('CASH ADVANCE FEE')>0 or merchs[j].find('LATE PAYMENT FEE')>0:
            fee+=amtDrs[j]
        if merchs[j].find('EMI PRINCIPAL')>0 or merchs[j].find('EMI INTEREST')>0:
            bb+=amtDrs[j]
        if merchs[j].find('GST')>0:
            gst+=amtDrs[j]
        if merchs[j].find('DEBIT INTEREST')>0:
            interest+=amtDrs[j]
        if merchs[j].find('SWIGGY')>0 or merchs[j].find('HOTELS')>0  or merchs[j].find('RESTAURANTS')>0:
            food+=amtDrs[j]
       # print(merchs[j],    '   ->>>>>>   ',amtDrs[j])
        j+=1
    #print(len(payments),' -   ',len(amtCrs))
    j=0
    paid=0
    while j<len(payments) and j<len(amtCrs):
        paid+=amtCrs[j]
        print(payments[j],    '   ->>>>>>   ',amtCrs[j])
        j+=1
    total=fee+bb+gst+interest+food
    print("billed           -   ",total)
    print('paid             -   ',paid)
    print('diff             -  ',total-paid)
monthsArr=['MAY','JUN','JUL','AUG']
z=0
dataArr=[]
for mnths in monthsArr:
    file = open("C:\\Python38\\zYpython\\BankRepos\\Axis\\CreditCardStatement_"+mnths+"_2019.pdf",'rb')
    reading = PyPDF2.PdfFileReader(file)
    if reading.isEncrypted:
        reading.decrypt('KIMT9801')
    pages = reading.getNumPages()
    i=0
    while i<pages:
        pg_content = reading.getPage(i)
        content = pg_content.extractText()
        contents=content.split('    ')
        contentsLen=len(contents )
        if contentsLen >3:
            print('Reading page -',i+1,'   Count   -',contentsLen)
            j=0
            while j<contentsLen:
                if len(contents[j])>1:
                    if contents[j].find('Dr')>0 or contents[j].find('Cr')>0:
                        #dataArr.append(contents[j])
                        #print(contents[j])
                        if contents[j].find("IMTHIYAZ")>0 or contents[j].find('Credit')==-1 :
                            if contents[j].find('/credit')==-1:
                                dataArr.append(contents[j])
                                print(contents[j])
                        elif contents[j].find("**** End of Statement ****")>0 :
                            dataArr.append(contents[j][0:contents[j].find("**** End of Statement ****")])
                            print(contents[j])
                j+=1
            print('--------------->>>>>>>>>>>>>>>>>>>>')
        i+=1
    z+=1
pickVals(dataArr)