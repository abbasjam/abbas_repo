import re
str1='''
Vani got 98 in python 
Karthi got 98 in kubernetis
Anand got 98 in jenkins
Dinesh got 99 in git
'''
marks=re.findall('\d{1,3}',str1)
names=re.findall('[A-Z][a-z]*',str1)
print ('Marks are:',marks)
print ("Names are:",names)
