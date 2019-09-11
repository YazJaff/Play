merchRs='RESTAURANTS185.00 Dr27/07/2019SWIGGY'
dateRs='10,052.54 Dr02/08/2019EMI INTEREST - 3/3, REF# 11134569'
nonDate='570.00 Cr**** End of Statement ****MY ZONE CREDIT CARD STATEMENTYour cheque should be payable to Axis Bank Card No.45145700****9801 . Please write your NAME & TELEPHONE No. on the reverse of the cheque.Dear Customer, pay your Axis Bank Credit Card bill from any bank account by registering for ECS at any Axis Bank branch. Visit axisbaation no.: 27AAACU2414K3ZD.IMPORTANT MES='
restaChk=merchRs.find('185')
dateDrChck=dateRs.find('Dr')
dateCrChck=dateRs.find('Cr')
NDDrChck=nonDate.find('Dr')
NDCrChck=nonDate.find('Cr')
print(restaChk)
print(merchRs)
print(dateDrChck)
print(dateRs[0:dateDrChck])
print(NDCrChck)
print(nonDate[0:NDCrChck])
print()
#RESTAURANTS -10
