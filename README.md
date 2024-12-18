I.Phân cụm FCM
-Hàm mục tiêu
-Nguyên lý hoạt động:
B1:Khởi tạo
  +Khởi tạo ma trận thành viên ngẫu nhiên U (NxC)
  +Chuẩn hóa
B2:Tính tâm cụm
  +Tính toán tâm cụm dựa theo ma trận thành viên U
B3:Cập nhật ma trận thành viên theo khoảng cách đến tâm cụm
B4:Lặp lại bước cập nhật tâm cụm và hệ số thành viên 
  +Lặp cho đến khi hàm mục tiêu nhỏ hơn ngưỡng cho trước
  +Đạt được số vòng lặp tối đa
II.Ứng dụng trên ảnh viễn thám
B1:Đọc ảnh
  +Tạo danh sách để lưu trữ ảnh
  +Đọc từng ảnh rồi lưu vào danh sách
  +Chuyển dữ liệu từ ảnh sang mảng numpy để tính toán
B2:Chuyển đổi và chuẩn hóa dữ liệu ảnh
  +Gộp mảng 4 chiều thành 3 chiều
  +Chuyển vị ma trận
  +Chuyển mảng về dạng 2 chiều
B3:Tô màu
  +Tính labels và gán màu cho các nhãn
  +reshape lại kích thước từ mảng 1 chiều sang dạng WxH
  +Khai báo mảng numpy chứa các giá trị RGB cho từng cụm
  +Gán màu cho từng cụm
