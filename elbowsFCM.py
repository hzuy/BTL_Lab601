import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from FCM import *

class Elbow:
    # hàm mục tiêu
   def WCSS(data,centroid,membership_matrix,m=2):
       wcss=0
       for i in range(data.shape[0]):
           for j in range (membership_matrix.shape[1]):
               distance=np.linalg.norm(data[i]-centroid[j])
               wcss=wcss+(membership_matrix[i,j]**m)*(distance**2)
       return wcss
   
   def calculate_K(data,k_max=10):
       wcss_list=[]
       for k in range(2,k_max+1):
           fcm=FCM(k)
           centroids,membership_matrix,_=fcm.fit(data)
           wcss=Elbow.WCSS(data,centroids,membership_matrix)
           wcss_list.append(wcss)
    
     # Vẽ biểu đồ Elbow
       plt.figure(figsize=(8, 5))
       plt.plot(range(2,k_max+1), wcss_list, marker="o")
       plt.xlabel("Number of clusters (k)")
       plt.ylabel("WCSS")
       plt.title("Elbow Method")
       plt.grid()
       plt.show()
        
                
        

