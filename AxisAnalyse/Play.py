def parse(strSplits):
    leng=len(strSplits)
    i=0
    date=''
    merchant=''
    crAmt=0
    drAmt=0
    while i<leng:
        str=strSplits[i]
        if str.find('/2019')!=-1:
            print('--=========-',str)
            #print('---')
            #print(str.split(' '))
            #print('---')
        else:
            if len(str)>3:
                #print('--=========-')
                print(str)
                #print('--=========-')
        i+=1
str='IMTHIYAZ AHMED27/07/2019SWIGGY                   NOIDA        IN       RESTAURANTS185.00 Dr27/07/2019SWIGGY                   NOIDA        IN       RESTAURANTS118.00 Dr27/07/2019SWIGGY                   BENGALURU    IN       RESTAURANTS81.00 Dr28/07/2019WWW SWIGGY COM           GURGAON      IN       RESTAURANTS172.00 Dr02/08/2019EMI PRINCIPAL - 3/3, REF# 11134569              10,052.54 Dr02/08/2019EMI INTEREST - 3/3, REF# 11134569               100.53 Dr02/08/2019GST                                             18.10 Dr05/08/2019MOBILE PAYMENT # M09AB7WT1482                   11,000.00 Cr09/08/2019SWIGGY                   BENGALURU    IN       RESTAURANTS138.00 Dr09/08/2019LATE PAYMENT FEE                                700.00 Dr09/08/2019GST                                             126.00 Dr10/08/2019SWIGGY                   BENGALURU    IN       RESTAURANTS189.00 Dr11/08/2019WWW SWIGGY COM           GURGAON      IN       RESTAURANTS155.00 Dr14/08/2019DEBIT INTEREST                                  1,317.63 Dr14/08/2019GST                                             237.17 Dr15/08/2019MOBILE PAYMENT # 7CFH28LR4657                   570.00 Cr**** End of Statement ****MY ZONE CREDIT CARD STATEMENTYour cheque should be payable to Axis Bank Card No.45145700****9801 . Please write your NAME & TELEPHONE No. on the reverse of the cheque.Dear Customer, pay your Axis Bank Credit Card bill from any bank account by registering for ECS at any Axis Bank branch. Visit axisbank.com to download the form.Axis Bank Maharashtra GST registration no.: 27AAACU2414K3ZD.IMPORTANT MESSAGE* Axis Bank Maharashtra GST registration no.:27AAACU2414K3ZD* Please refer: https://www.axisbank.com/webforms/code-of-commitment.aspx for revised BCSBI code.'
strSplit=str.split('    ')
i=0
parse(strSplit)
