import shutil
import os

pathTest = "C://Users//dan//Desktop//123//texts//111"

try:
    shutil.rmtree(pathTest)
except OSError as e:
    print(e)
else:
    print("The directory is deleted successfully")

os.mkdir('C://Users//dan//Desktop//123//texts//111')