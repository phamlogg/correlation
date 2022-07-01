<<<<<<< HEAD
#	Correlation

### [ENG]

####Python script to calculate correlation between assets
 
 All input data should be put into "Data.xlsx" file.
 You may alter cells highlighted yellow. All else should not be touched, otherwise result maybe inaccurate.
 All assets should have same time period.

### [VN]
#### Script tính correlation giữa các tài sản

##### Cách sử dụng:
- Bước 1: Cài đặt công cụ cần thiết:
	- Trên Windows: Mở Powershell (Shell) hoặc Command Prompt (CMD) và nhập `python` rồi nhấn enter
		- Nếu trên Command Promt hoặc Powershell chuyển sang '>>>' thì chỉ cần thoát khỏi Shell hoặc CMD.
		- Nếu chưa có Python trên máy thì máy sẽ tự động mở Microsoft Store và từ đó hãy chọn Python version cao nhất và free (tại thời điểm viết bài này là 3.10).
		- 
- Bước 2: Di chuyển tới thu mục Correlation
	- Mở folder 'dist' và mở file setup
	- Đợi setup hoàn tất 
		
- Bước 3: Mở file Data.xlsx ở thu mực Correlation và nhập dữ liệu theo hướng dẫn

	- **Chỉ nhập dữ liệu vào những ô màu vàng, còn lại không được phép thay đổi, bao gồm cả tên file 'Data.xlsx'**
	- Nhập tên tài sản vào các cell A1, E1, I1, ...
	- Phía dưới tên tài sản là mốc thời gian, cái này optional có thể nhập hoặc bổ trống đều được
	- Phía dưới cột 'Open' và 'Close' lần lượt là giá mở cửa và giá đóng cửa của tài sản đó


![Hình file input](/pics/3.png)

- Bước 4: Sau khi nhập dữ liệu, xong, mở folder dist -> mở file script và đợi
- Bước 5: Kết quả nằm ở sheet 2 trong file Output.xlsx
=======
# correlation
Python script to calculate correlation-coefficient between assets for allocation
>>>>>>> fbedc37facf804f12ea6cb761a70654c9931c5b9
