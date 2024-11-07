Bước 1: Tải Code từ Google Drive
Truy cập vào đường link Google Drive: [LINK_GOOGLE_DRIVE] (thay thế với liên kết thực tế).
Tải toàn bộ mã nguồn của dự án về máy tính của bạn.


Bước 2: Cài Đặt XAMPP và Thiết Lập Cơ Sở Dữ Liệu
Tải và cài đặt XAMPP từ https://www.apachefriends.org/index.html.
Khởi động XAMPP Control Panel, bật Apache và MySQL.
Truy cập phpMyAdmin bằng cách vào http://localhost/phpmyadmin.
Tạo một cơ sở dữ liệu mới tên là cnc.
Tải tệp cnc.sql từ mã nguồn đã tải về trong Google Drive.
Trong phpMyAdmin, chọn cơ sở dữ liệu cnc vừa tạo và nhấn Import để nhập tệp cnc.sql vào cơ sở dữ liệu.


Bước 3: Thiết Lập Mã Nguồn Web
Giải nén mã nguồn web đã tải từ Google Drive.
Sao chép toàn bộ mã nguồn web và dán vào thư mục C:/xampp/htdocs/.
Mở trình duyệt và truy cập vào trang web qua địa chỉ http://localhost/OOAD để kiểm tra xem trang web đã hoạt động hay chưa.


Bước 4: Cài Đặt Môi Trường Python và Thư Viện Yêu Cầu
Đảm bảo rằng Python đã được cài đặt trên máy tính của bạn. Nếu chưa, tải Python từ https://www.python.org/downloads/.

Cài đặt các thư viện cần thiết cho Selenium bằng cách mở Command Prompt hoặc Terminal và chạy các lệnh sau:

bash

pip install selenium

pytest


Đảm bảo rằng ChromeDriver (hoặc WebDriver tương ứng với trình duyệt của bạn) có phiên bản phù hợp với trình duyệt bạn đang sử dụng. Tải ChromeDriver tại https://sites.google.com/chromium.org/driver/. Sau đó, đặt ChromeDriver vào thư mục chứa mã nguồn hoặc thêm vào PATH của hệ điều hành.

Bước 5: Chạy Code Kiểm Thử Python
