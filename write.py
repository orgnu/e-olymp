test= [1024,1118,1265,1286,1351,1603,1606,1607,1609,1658,1952]
import os.path
save_path = 'C:/Users/Nurlan/Documents/GitHub/e-olymp/1000-2000'
for i in test:
    
    fileName = os.path.join(save_path, str(i)+".py")  
    filePy = open(fileName, "w")
    filePy.close() 
    print("|[ {} ](https://www.e-olymp.com/en/problems/{}) | [ 100% ](https://github.com/nurlangarash/e-olymp/blob/main/0000-1000/{}.py)| ".format(i,i,i))
      