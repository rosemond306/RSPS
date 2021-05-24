orderamount=int(input("pls enter total order amount")) #coming from frontend(customer)
rate=620 #coming from database
localdel=float(input("pls enter local del amount"))  #coming from database/input

if orderamount <50:
        commission=10
elif orderamount <=100:
        commission= 0.2
elif orderamount <=250:
        commission= 0.15
elif orderamount <=500:
        commission= 0.10
else:
    commission=0.075

commissionrate=commission*100
commission=commission*orderamount
subtotal=orderamount+commission+localdel
total=(subtotal*rate)

#print as invoice and send to whatsapp/email
print("OrderAmount:",orderamount) #display in £
print("LocalDel:",localdel) #display in £
print("Commission Due:",commissionrate) #display in %
print("Commission Amount:",commission) #display in  £
print("Subtotal:",subtotal) #display in  £
print("Rate:",rate) #display in  ₦
print("TotalDue:",total) #display in  ₦











    