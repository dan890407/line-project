import os
import re
path='C://Users//dan//Desktop//123//texts//'
files=os.listdir(path)
n=0 
for i in files: 
  oldname=path+files[n] 
  newname=oldname.replace('.txt','')
  newname=newname+'_new.txt'
  os.rename(oldname,newname) 
  print(oldname+'>>>'+newname) 
  n=n+1




