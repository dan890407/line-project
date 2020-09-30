import os
import shutil
original_path='./texts//unprocess//'
processed_path='./texts//processed//'
original_files=os.listdir(original_path)
processed_files=os.listdir(processed_path)
namelist=[]

def createlist(path):

    with open('./texts//namelist.txt','w',encoding="utf-8") as f :
        for i in original_files:
            f.write(i+'\n')
    
def merge():
    for i in original_files:
        unprocess_link = './texts//unprocess//' + i
        processed_link = './texts//processed//' + i
        f = open(processed_link,'r',encoding="utf-8")   
        lines = f.readlines()
        last_line = lines[-1]
        f.close()
        print(last_line)
        
        k=open(unprocess_link,'r',encoding="utf-8") 
        c=open(processed_link,'a+',encoding="utf-8")          
        check = 0
        for line in k.readlines():
            if check == 1:
                c.write(line)
            if line == last_line:
                check = 1
        k.close()
        if check==0:
            k=open(unprocess_link,'r',encoding="utf-8")
            for line in k.readlines():
                c.write(line)

def delete_old():   
    pathTest = r"./texts//unprocess"
    try:
        shutil.rmtree(pathTest)
    except OSError as e:
        print(e)
    else:
        print("The directory is deleted successfully")
    os.mkdir('./texts//unprocess')    
merge()
delete_old()
createlist(processed_path)