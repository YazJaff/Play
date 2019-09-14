import PyPDF2
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
            #datas.append(data[i][indxIMT:len(data[i])])
            datum=datum[datum.find('IMTHIYAZ'):len(datum)]
            #ate=datum[datum.find('/2019')-5:datum.find('/2019')+5]
            dates.append(datum[datum.find('/2019')-5:datum.find('/2019')+5])
            merchBuff=datum[datum.find('/2019')+5:len(datum)]
            print(dates)
            print(merchBuff)
            
            print('-------iii----->>>>>>>>>',datum)
        else :
            datas.append(data[i])
            print('------------>>>>>>>>>',data[i])
        i+=1
    
    print(len(datas))
        


file = open("C:\\Python38\\zYpython\\BankRepos\\Axis\\CreditCardStatement_JUL_2019.pdf",'rb')
reading = PyPDF2.PdfFileReader(file)
if reading.isEncrypted:
    reading.decrypt('KIMT9801')
pages = reading.getNumPages()
print(pages)
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

