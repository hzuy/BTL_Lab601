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

