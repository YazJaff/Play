import PyPDF2

file = open("C:\\Python38\\zYpython\\BankRepos\\Axis\\CreditCardStatement_AUG_2019.pdf",'rb')
reading = PyPDF2.PdfFileReader(file)
if reading.isEncrypted:
    reading.decrypt('KIMT9801')
pages = reading.getNumPages()
print(pages)
i=0
while i<pages:
    print('Reading page -',i+1)
    pg_content = reading.getPage(i)
    content = pg_content.extractText()
    contents=content.split('\n')
    #print(contentss)
    j=0
    while j<len(contents):
        check=contents[j].find('Please')
        if check !=-1:
            checkIm=contents[j].find('IMTHIYAZ AHMED')
            print(contents[j][checkIm:len(contents[j])])
        j+=1
    i+=1

