file = open("C:\\Python38\\zYpython\\BankRepos\\Axis\\CreditCardStatement_JUN_2019.pdf",'rb')
reading = PyPDF2.PdfFileReader(file)
if reading.isEncrypted:
    reading.decrypt('KIMT9801')
pages = reading.getNumPages()
i=0
while i<pages:
    pg_content = reading.getPage(i)
    content = pg_content.extractText()
    contents=content.split('\n')
    if len(contents) >3:
        print(len(contents))