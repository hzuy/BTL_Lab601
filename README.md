# Phân Cụm FCM

## I. Phân cụm FCM

### 1. Hàm mục tiêu
- Hàm mục tiêu của FCM là tối ưu hóa sự phân cụm bằng cách giảm thiểu khoảng cách giữa các điểm dữ liệu và tâm cụm, dựa trên ma trận thành viên.

### 2. Nguyên lý hoạt động
#### Bước 1: Khởi tạo
- Khởi tạo ma trận thành viên ngẫu nhiên \( U \) (kích thước \( N \times C \), với \( N \) là số điểm dữ liệu, \( C \) là số cụm).
- Chuẩn hóa ma trận thành viên \( U \).

#### Bước 2: Tính tâm cụm
- Tính toán tâm cụm dựa trên ma trận thành viên \( U \).

#### Bước 3: Cập nhật ma trận thành viên
- Cập nhật ma trận thành viên dựa trên khoảng cách từ điểm dữ liệu đến các tâm cụm.

#### Bước 4: Lặp lại
- Lặp lại việc tính toán tâm cụm và cập nhật ma trận thành viên:
  - Dừng lặp khi hàm mục tiêu nhỏ hơn một ngưỡng cho trước.
  - Hoặc đạt được số vòng lặp tối đa.

---

## II. Ứng dụng trên ảnh viễn thám

### Bước 1: Đọc ảnh
- Tạo danh sách để lưu trữ ảnh.
- Đọc từng ảnh từ thư mục và lưu vào danh sách.
- Chuyển dữ liệu từ ảnh sang mảng numpy để thực hiện tính toán.

### Bước 2: Chuyển đổi và chuẩn hóa dữ liệu ảnh
- Gộp các mảng 4 chiều (nếu có) thành mảng 3 chiều.
- Chuyển vị ma trận (nếu cần).
- Chuyển mảng về dạng 2 chiều để thuận tiện cho phân cụm.

### Bước 3: Tô màu
- Tính toán nhãn (\( labels \)) và gán màu tương ứng cho từng nhãn.
- Reshape lại kích thước từ mảng 1 chiều về dạng \( W \times H \) (kích thước ảnh gốc).
- Khai báo mảng numpy chứa các giá trị RGB cho từng cụm.
- Gán màu cho từng cụm dựa trên nhãn phân cụm.
  
## Hướng Dẫn Sử Dụng

### 1. Chuẩn Bị Dữ Liệu
- Đảm bảo có sẵn nguồn ảnh viễn thám .
- Tệp dữ liệu `Scorer.csv` đã được đặt đúng vị trí trong thư mục làm việc.

### 2. Cấu Trúc Thư Mục
- **`FCM.py`**: Chứa lớp thực hiện phân cụm FCM.
- **`doc_du_lieu.py`**: Thực hiện việc đọc dữ liệu ảnh từ thư mục.
- **`elbowsFCM.py`**: Chạy thuật toán Elbows để xác định số cụm phù hợp.
- **`xu_ly_du_lieu.py`**: Xử lý dữ liệu ảnh để tô màu sau khi phân cụm.
- **`main.py`**: Tệp chính để chạy chương trình.

### 3. Quy Trình Thực Hiện
1. **Bước 1**: Khởi tạo và đọc dữ liệu.
   - Chạy `doc_du_lieu.py` để đọc và chuyển đổi dữ liệu ảnh thành mảng numpy.
2. **Bước 2**: Chọn số cụm.
   - Sử dụng `elbowsFCM.py` để tìm số cụm phù hợp.
3. **Bước 3**: Phân cụm bằng FCM.
   - Lớp `FCM` trong `FCM.py` sẽ thực hiện phân cụm dựa trên số cụm tìm được.
4. **Bước 4**: Tô màu cho ảnh.
   - Chạy `xu_ly_du_lieu.py` để thực hiện các bước tô màu cho ảnh đã phân cụm.
5. **Bước 5**: Chạy chương trình tổng hợp.
   - Chạy `main.py` để thực thi toàn bộ quy trình trên.

### 4. Kết Quả
- Các ảnh viễn thám được phân cụm và tô màu theo nhãn cụm.
- Biểu đồ hoặc giá trị tối ưu từ phương pháp Elbows.
- Kết quả phân cụm dữ liệu điểm thi THPTQG năm 2023 từ `Scorer.csv`.


