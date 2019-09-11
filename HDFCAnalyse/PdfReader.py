import PyPDF2

def catchandPlay(date,desc,withdrw,bal):
    print(date+"    -"+desc+"   -"+withdrw+"   -"+bal)
    return 0

file = open("C:\\Python38\\zYpython\\BankRepos\\Axis\\CreditCardStatement_AUG_2019.pdf",'rb')
reading = PyPDF2.PdfFileReader(file)
if reading.isEncrypted:
    reading.decrypt('')

pages = reading.getNumPages()
print(pages)
pg_content = reading.getPage(0)
content = pg_content.extractText()
contentss=content.split("\n")

k=0
count=0
descCount=0
while k<len(contentss):
    print(contentss[k])
    k=k+1

