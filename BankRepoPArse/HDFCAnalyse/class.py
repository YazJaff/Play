class Txnz:
  def __init__(txn, sno, narration,date,withAmt):
    txn.sno = sno
    txn.narration = narration
    txn.date = date
    txn.withAmt = withAmt
    txn.deposit = deposit
    txn.balance = balance

  def myfunc(txn):
    print("Sno - " , txn.sno)
    print("Desc - " , txn.narration)
    print("Date - " , txn.date)
    print("Withdraw - " , txn.withAmt)
    print("deposit - " , txn.deposit)
    print("balance - " , txn.balance)

import PyPDF2

file = open("C:\\Python38\\zYpython\\BankRepos\\Axis\\CreditCardStatement_AUG_2019.pdf",'rb')
reading = PyPDF2.PdfFileReader(file)
if reading.isEncrypted:
    reading.decrypt('')

pages = reading.getNumPages()
print(pages)
i=0
while i<pages:
  pg_content = reading.getPage(i)
  content = pg_content.extractText()
  contentss=content.split('\n')
  print(contentss)
  i=i+1

