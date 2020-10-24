import os

original_files=os.listdir('./1')
for i in original_files:
    raw='./1//'+i
    with open("data.txt","a+",encoding="utf-8") as f:
        with open(raw,"r",encoding="utf-8")as p:
            for line in p.readlines():
                f.write(line+'\n')