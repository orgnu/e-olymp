test= [2042,2043,2044,2071,2131,2162,2392,2606,2666,2667,2807,2862,2863,2864,]
import os.path
save_path = 'C:/Users/Nurlan/Documents/GitHub/e-olymp/2000-3000'
for i in test:

    fileName = os.path.join(save_path, str(i)+".py")  
    filePy = open(fileName, "w")
    filePy.close() 
    print("|[ {} ](https://www.e-olymp.com/en/problems/{}) | [ 100% ](https://github.com/nurlangarash/e-olymp/blob/main/0000-1000/{}.py)| ".format(i,i,i))
      