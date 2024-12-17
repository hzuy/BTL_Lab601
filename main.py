from FCM import *
from doc_du_lieu import *
import numpy as np
import pandas as pd
from elbowsFCM import *
from xu_ly_du_lieu import *


images=['100/landsat8_b2_100.tif' ,'100/landsat8_b3_100.tif','100/landsat8_b4_100.tif', '100/landsat8_b5_100.tif']
if __name__=="__main__":
    data=docDuLieu()
    data,W,H=calculate_data(bands=data)
    print(data)
    
    
    # bands=read_img(img=images)
    # show_img(bands=bands)
    
    
    #phân cụm FCM
    fcm=FCM(clusters=6)
    centroids,U,new_clusters,i=fcm.fit(data)
    
    lables=fcm.calcutlate_labels(U)
    print("tâm cụm : ")
    print(centroids)
    print("Ma trận thành viên : ")
    print(U)
    print("Cụm dự đoán : ")
    print(new_clusters)
    print("số bước : ")
    print(i)
    # Elbow.calculate_K(data,k_max=10)
    
    visualize_img(lables,W,H)
    
    
    
    
    
    
    
    
    
    
    
    
  