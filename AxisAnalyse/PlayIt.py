str=['IMTHIYAZ AHMED22/05/2019SBI  PALAKKARAI','CASH WITHDRAWAL10,000.00 Dr22/05/2019SBI  PALAKKARAI']
for val in str:
    indx=str.find('2019')
    date=''
    desc=''
    cOrD=''
    amt=0
    date=str[indx-6:indx+4]
    desc=str[indx+4:len(str)]
    print(date)

print()