import pandas as pd
import numpy as np
import rasterio
import os

def docDuLieu():
    # Đọc dữ liệu từ file CSV
    # data = pd.read_csv("scores.csv")

    # #Lấy các cột Toán, Văn, Anh của 100 sinh viên đầu tiên
    # selected_data = data[['Mathematics', 'Literature', 'Foreign language','Physics','Chemistry','Biology','History','Geography','Civic education']]

    # #chuyển sinh viên có điểm null thành 0
    # selected_data = selected_data.fillna(0)
    
    # return np.array(selected_data)
   
   
#    Đường dẫn đến folder chứa ảnh
    folder_path = "100"
    images = []

    # Lặp qua tất cả các file trong folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.tif'):  # Chỉ đọc các file .tif
            file_path = os.path.join(folder_path, filename)
            with rasterio.open(file_path) as src:
                band = src.read()  # Đọc kênh đầu tiên
                images.append(band)  # Thêm vào danh sách
    return images