print ("file Handling")
print ("------------")
fp=open("sample1.txt","a")
x=["BrainStackSolutions\n","Chennai\n","Devops\n","Kubernetis\n","Python\n","Thank u all\n"]
fp.writelines(x)
fp.close()
