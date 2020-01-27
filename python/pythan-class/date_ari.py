import datetime 
td=datetime.date.today()
print("Current date is :",td)
cd=datetime.timedelta(days=45)
print ("Converted number into date:",cd)
nd=td+cd
pd=td-cd
print ("Previous date is :",pd)
print ("Future Date is :",nd)
