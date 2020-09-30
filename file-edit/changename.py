import os
import re
import shutil
path='./texts//'
files=os.listdir('./texts//unprocess//')
n=0 
for i in files: 
  oldname=path+'unprocess//'+files[n]
  newname='./texts//processed//'+files[n]
  shutil.copy(oldname,newname)
  n+=1




