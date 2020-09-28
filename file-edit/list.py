import os
import shutil
original_path='C://Users//dan//Desktop//123//texts//unprocess//'
processed_path='C://Users//dan//Desktop//123//texts//processed//'
original_files=os.listdir(original_path)
processed_files=os.listdir(processed_path)
namelist=[]
def createlist(path):

    with open('C://Users//dan//Desktop//123//texts//namelist.txt','w') as f :
        for i in original_files:
            f.write(i+'\n')
    
def merge():
    for i in original_files:
        unprocess_link = 'C://Users//dan//Desktop//123//texts//unprocess//' + i
        processed_link = 'C://Users//dan//Desktop//123//texts//processed//' + i
        f = open(processed_link,'r',encoding="utf-8")   
        lines = f.readlines()
        last_line = lines[-1]
        f.close()
        print(last_line)
        
        with open(unprocess_link,'r',encoding="utf-8") as k: 
            with open(processed_link,'a+',encoding="utf-8") as c:            
                check = 0
                for line in k.readlines():
                    if check == 1:
                        c.write(line)
                    if line == last_line:
                        check = 1
def delete_old():   
    pathTest = r"C://Users//dan//Desktop//123//texts//unprocess"
    try:
        shutil.rmtree(pathTest)
    except OSError as e:
        print(e)
    else:
        print("The directory is deleted successfully")
    os.mkdir('C://Users//dan//Desktop//123//texts//unprocess')    
merge()
delete_old()
createlist(processed_path)

