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
    print(len(merchs),' -   ',len(amtDrs))
    j=0
    while j<len(merchs) and j<len(amtDrs):
        print(merchs[j],    '   ->>>>>>   ',amtDrs[j])
        j+=1
    print(len(payments),' -   ',len(amtCrs))
    j=0
    while j<len(payments) and j<len(amtCrs):
        print(payments[j],    '   ->>>>>>   ',amtCrs[j])
        j+=1
file = open("C:\\Python38\\zYpython\\BankRepos\\Axis\\CreditCardStatement_JUN_2019.pdf",'rb')
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
        dataArr=[]
        while j<contentsLen:
            if len(contents[j])>1:
                if contents[j].find('Dr')>0 or contents[j].find('Cr')>0:
                    if contents[j].find("IMTHIYAZ")>0 or contents[j].find('Credit')==-1 :
                        if contents[j].find('/credit')==-1:
                            dataArr.append(contents[j])
            j+=1
        pickVals(dataArr)
    i+=1

