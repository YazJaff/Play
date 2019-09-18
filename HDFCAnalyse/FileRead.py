import PyPDF2
file = open("C:\Python38\zYpython\BankRepos\HDFC\\Aug21-21018ToSept08-2019.pdf",'rb')
reading = PyPDF2.PdfFileReader(file)
if reading.isEncrypted:
    reading.decrypt('KIMT9801')
pages = reading.getNumPages()
i=0
while i<1:
    print('---------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>------->>>>>>>>>>')
    print('Reading page : ',i+1 ,' / ',pages)
    pg_content = reading.getPage(i)
    content = pg_content.extractText()
    contents=content.split('\n')
    j=0
    while j<len(contents):
        print(contents[j])
        j+=1
    print('---------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>------->>>>>>>>>>')
    if i==3:
        break
    i+=1