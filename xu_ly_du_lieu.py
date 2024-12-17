import numpy as np
import matplotlib.pyplot as plt
import rasterio
from FCM import *

images=['100/landsat8_b2_100.tif' ,'100/landsat8_b3_100.tif','100/landsat8_b4_100.tif', '100/landsat8_b5_100.tif']

def read_img(img):
    #tạo danh sách để lưu trữ ảnh
    bands=[]
    #đọc từng ảnh và thêm vào danh sách
    for path in img :
        print(path)
        with rasterio.open(path) as src:
            band=src.read() #đọc kênh 
            print(band.shape)
            bands.append(band)    #(bands x W x H)
    bands = [np.array(band) for band in bands]
    return bands

def show_img(bands):
    # Tạo lưới 2x2 để hiển thị 4 ảnh
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
# Hiển thị từng ảnh lên subplot tương ứng
    for i, ax in enumerate(axs.flatten()):
        ax.imshow(bands[i].squeeze(), cmap='gray')  # Hiển thị ảnh xám
        ax.set_title(f'Band {i+2} landsat8')
        ax.axis('off')  # Tắt các trục
        
# Hiển thị lưới các ảnh
    plt.tight_layout()
    plt.show()
    
def calculate_data(bands):
    # Gộp mảng 4 chiều thành mảng 3 chiều
    data = np.concatenate(bands)  # [img, band, W, H] -> [band, W, H]
    # Chuyển vị ma trận dữ liệu
    data = np.transpose(data, (1, 2, 0))  # (W, H, bands)
    W, H, bands = data.shape
    print("Kích thước ảnh ban đầu : ", W, H, bands)
    data = data.reshape(W * H, bands)  # (WxH, bands)
    print("Kích thước dữ liệu cần phân cụm là : ", data.shape)
    return data,W,H  # Đảm bảo trả về dữ liệu đã được chuyển đổi
    
# Visualize hình ảnh

def visualize_img(labels,W, H):
    # Tạo hình ảnh phân cụm (reshape lại label về (W,H))
    labels=labels.reshape(W,H)
    colored_segmented_image = np.zeros((W, H, 3), dtype=np.uint8)
    color_map = np.array([
    [0, 0, 255],        # Class 1: Rivers, lakes, ponds
    [128, 128, 128],    # Class 2: Vacant land, roads
    [0, 255, 0],        # Class 3: Field, grass
    [1, 192, 255],      # Class 4: Sparse forest, low trees
    [0, 128, 0],        # Class 5: Perennial Plants
    [0, 64, 0],         # Class 6: Dense forest, jungle
], dtype=np.uint8)
    # Giả sử labels là mảng chứa nhãn cụm cho từng pixel
    for i in range(len(color_map)):
        colored_segmented_image[labels == i] = color_map[i]  # Gán màu cho từng cụm
    # Hiển thị hình ảnh phân cụm
    plt.imshow(colored_segmented_image)
    plt.title("Hình ảnh phân cụm")
    plt.axis('off')  # Tắt các trục
    plt.show()
    
    
    
    
    

