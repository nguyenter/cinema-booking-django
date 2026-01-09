# BỘ GIÁO DỤC VÀ ĐÀO TẠO
# TRƯỜNG ĐẠI HỌC MỞ THÀNH PHỐ HỒ CHÍ MINH

---

## MỤC LỤC

**Chương 1. Giới thiệu**  
1.1. Tổng quan đề tài  
1.1.1. Giới thiệu đề tài  
1.1.2. Lý do chọn đề tài  
1.1.3. Mục tiêu của đề tài  
1.2. Hạn chế của các phương pháp hiện tại  
1.3. Phương pháp đề xuất  
1.4. Đóng góp của đề tài  

**Chương 2. Nội dung dự án**  
2.1. Chức năng chính  
2.1.1. Đăng ký/Đăng nhập  
2.1.2. Xem danh sách phim và suất chiếu  
2.1.3. Chọn ghế  
2.1.4. Đặt vé  
2.1.5. Thanh toán trực tuyến  
2.1.6. Xem lịch sử đặt vé  
2.1.7. Quản lý phim, suất chiếu, người dùng (Admin)  
2.1.8. Quản lý thống kê và báo cáo (Admin)  
2.2. Công nghệ sử dụng  
2.2.1. Khái quát về Django Framework  
2.2.2. Khái quát về Python  
2.2.3. Khái quát về HTML5  
2.2.4. Khái quát về CSS3  
2.2.5. Khái quát về JavaScript và jQuery  
2.2.6. Khái quát về Bootstrap  
2.2.7. Khái quát về SQLite  
2.2.8. Khái quát về VNPay Payment Gateway  

**Chương 3. Phương pháp đề xuất**  
3.1. Tổng quan phương pháp  
3.2. Kiến trúc hệ thống  
3.3. Thiết kế cơ sở dữ liệu  
3.4. Quy trình xử lý nghiệp vụ  

**Chương 4. Kết quả và thực nghiệm**  
4.1. Giao diện người dùng  
4.2. Giao diện quản trị  
4.3. Kết quả kiểm thử chức năng  
4.4. Đánh giá hiệu năng  

**Chương 5. Kết luận**  
5.1. Tổng kết  
5.2. Hạn chế và hướng phát triển  

---

## DANH MỤC TỪ VIẾT TẮT

| STT | Viết tắt | Cụm từ |
|-----|----------|--------|
| 1 | HTML | HyperText Markup Language |
| 2 | CSS | Cascading Style Sheets |
| 3 | JS | JavaScript |
| 4 | API | Application Programming Interface |
| 5 | CRUD | Create, Read, Update, Delete |
| 6 | ORM | Object-Relational Mapping |
| 7 | MVC | Model-View-Controller |
| 8 | MVT | Model-View-Template |
| 9 | IPN | Instant Payment Notification |
| 10 | SHA | Secure Hash Algorithm |

---

# CHƯƠNG 1. GIỚI THIỆU

## 1.1. Tổng quan đề tài

### 1.1.1. Giới thiệu đề tài

Ngày nay, với sự phát triển mạnh mẽ của công nghệ thông tin và nhu cầu giải trí bằng điện ảnh ngày càng tăng cao, việc đặt vé xem phim trực tuyến đã trở thành xu hướng phổ biến. Tuy nhiên, nhiều website đặt vé hiện tại vẫn còn tồn tại những hạn chế về giao diện người dùng, tốc độ xử lý, tính bảo mật và trải nghiệm người dùng.

Vì vậy, đề tài **"Thiết kế và Xây dựng Website Đặt Vé Xem Phim CinemaPlus"** ra đời nhằm xây dựng một nền tảng trực tuyến hiện đại, thuận tiện và thân thiện với người dùng. Website được thiết kế theo hướng **trực quan – nhanh chóng – an toàn**, đáp ứng đầy đủ các chức năng cần thiết cho người dùng trong việc:

- Xem danh sách phim và thông tin chi tiết
- Tra cứu lịch chiếu và suất chiếu
- Chọn ghế ngồi trực quan trên sơ đồ
- Đặt vé và thanh toán trực tuyến qua VNPay
- Quản lý lịch sử đặt vé cá nhân
- Quản trị hệ thống (dành cho admin)

Bên cạnh đó, hệ thống còn tích hợp các tính năng quản lý nâng cao như thống kê doanh thu, quản lý phim, suất chiếu, người dùng thông qua giao diện admin tùy chỉnh với thiết kế hiện đại.

### 1.1.2. Lý do chọn đề tài

**• Phù hợp thực tế và có nhu cầu sử dụng cao**

Website đặt vé xem phim là một dịch vụ phổ biến trong đời sống hiện đại, có tính ứng dụng cao và gần gũi với người dùng. Việc xây dựng hệ thống này giúp sinh viên tiếp cận gần hơn với các mô hình thương mại điện tử đang được sử dụng rộng rãi trong thực tế, từ đó hiểu rõ hơn về quy trình phát triển phần mềm thương mại.

**• Cơ hội rèn luyện toàn diện kỹ năng lập trình web**

Đề tài yêu cầu vận dụng nhiều kiến thức và kỹ năng: frontend (HTML/CSS/JavaScript), backend (Django/Python), cơ sở dữ liệu (SQLite/ORM), xử lý thanh toán trực tuyến, quản lý session, bảo mật, và tích hợp API thanh toán. Đây là cơ hội tốt để rèn luyện và củng cố kỹ năng toàn diện trong phát triển web.

**• Tính hệ thống và mức độ thử thách phù hợp**

Website rạp chiếu phim bao gồm nhiều chức năng liên kết chặt chẽ với nhau, từ quản lý người dùng, quản lý phim, đặt vé, đến thanh toán. Tuy phức tạp nhưng hoàn toàn có thể thực hiện được trong phạm vi của một đồ án, giúp rèn luyện khả năng tự học, tự nghiên cứu và tự triển khai.

**• Hỗ trợ phát triển tư duy phân tích và thiết kế hệ thống**

Đề tài cho phép trải qua đầy đủ các bước của một dự án thực tế: phân tích yêu cầu, thiết kế giao diện người dùng, thiết kế cơ sở dữ liệu, xây dựng các chức năng nghiệp vụ, tích hợp thanh toán, kiểm thử và triển khai. Qua đó phát triển tư duy hệ thống và kỹ năng quản lý dự án.

**• Tạo nền tảng cho các dự án nâng cao trong tương lai**

Sau khi hoàn thiện phiên bản cơ bản, hệ thống có thể được mở rộng với nhiều tính năng nâng cao như: đề xuất phim theo sở thích người dùng (recommendation system), tích hợp nhiều cổng thanh toán, ứng dụng di động, hệ thống đánh giá và bình luận phim, chương trình khuyến mãi và tích điểm thành viên. Điều này phù hợp với định hướng nghề nghiệp trong lĩnh vực phát triển phần mềm và thương mại điện tử.

### 1.1.3. Mục tiêu của đề tài

**Mục tiêu chính:**
- Xây dựng một website đặt vé xem phim hoàn chỉnh với đầy đủ các chức năng cơ bản và nâng cao
- Tích hợp hệ thống thanh toán trực tuyến VNPay để xử lý giao dịch an toàn
- Thiết kế giao diện người dùng thân thiện, trực quan và responsive
- Xây dựng hệ thống quản trị với giao diện hiện đại, dễ sử dụng

**Mục tiêu cụ thể:**
- Phát triển hệ thống quản lý người dùng với đăng ký, đăng nhập, phân quyền
- Xây dựng module quản lý phim, suất chiếu, phòng chiếu và ghế ngồi
- Triển khai chức năng đặt vé với quy trình chọn phim → chọn suất chiếu → chọn ghế → thanh toán
- Tích hợp VNPay Payment Gateway với xác thực bảo mật SHA512
- Thiết kế giao diện admin tùy chỉnh với CSS hiện đại và các tính năng thống kê trực quan

## 1.2. Hạn chế của các phương pháp hiện tại

Trong thực tế, nhiều website đặt vé xem phim hiện tại vẫn còn tồn tại những hạn chế sau:

**• Giao diện người dùng chưa tối ưu:**
- Nhiều website có giao diện cũ kỹ, không responsive, khó sử dụng trên thiết bị di động
- Sơ đồ chọn ghế không trực quan, khó nhìn và dễ nhầm lẫn
- Thiếu các hiệu ứng tương tác, làm giảm trải nghiệm người dùng

**• Hiệu năng và tốc độ xử lý:**
- Một số hệ thống xử lý chậm khi có nhiều người dùng đồng thời
- Chưa tối ưu hóa truy vấn cơ sở dữ liệu, dẫn đến thời gian tải trang lâu
- Thiếu cơ chế cache và tối ưu hóa static files

**• Bảo mật và an toàn dữ liệu:**
- Một số website chưa áp dụng đầy đủ các biện pháp bảo mật như CSRF protection, XSS prevention
- Xử lý thanh toán chưa đảm bảo tính bảo mật cao
- Quản lý session chưa an toàn, dễ bị tấn công

**• Quản lý và thống kê:**
- Giao diện quản trị thường đơn điệu, khó sử dụng
- Thiếu các công cụ thống kê trực quan, biểu đồ để theo dõi doanh thu và hoạt động
- Quản lý suất chiếu và ghế ngồi chưa tự động hóa

**• Tích hợp thanh toán:**
- Nhiều website chưa tích hợp thanh toán trực tuyến, vẫn yêu cầu thanh toán tại rạp
- Chưa có cơ chế xác thực và xử lý callback từ cổng thanh toán một cách an toàn

## 1.3. Phương pháp đề xuất

Để khắc phục các hạn chế trên, đề tài đề xuất các phương pháp sau:

**• Sử dụng Django Framework:**
- Framework Python mạnh mẽ, có sẵn nhiều tính năng bảo mật
- ORM giúp tối ưu hóa truy vấn cơ sở dữ liệu
- Hệ thống template linh hoạt, dễ tùy chỉnh
- Admin interface mạnh mẽ, có thể tùy chỉnh hoàn toàn

**• Thiết kế giao diện hiện đại:**
- Sử dụng Bootstrap để tạo giao diện responsive
- CSS tùy chỉnh với gradient, shadow, animation
- JavaScript và jQuery để tăng tính tương tác
- Sơ đồ ghế trực quan, dễ sử dụng

**• Tích hợp VNPay Payment Gateway:**
- Xác thực bảo mật bằng SHA512 hash
- Xử lý IPN (Instant Payment Notification) để cập nhật trạng thái thanh toán
- Hỗ trợ cả sandbox và production environment

**• Tự động hóa quản lý:**
- Sử dụng Django Signals để tự động tạo ghế khi tạo phòng
- Tự động cập nhật trạng thái ghế khi đặt/hủy vé
- Management commands để tạo dữ liệu mẫu tự động

**• Tối ưu hóa hiệu năng:**
- Sử dụng select_related và prefetch_related để giảm số lượng truy vấn
- WhiteNoise để phục vụ static files hiệu quả
- Session management tối ưu

## 1.4. Đóng góp của đề tài

**• Đóng góp về mặt kỹ thuật:**
- Xây dựng một hệ thống đặt vé hoàn chỉnh sử dụng Django Framework
- Tích hợp thành công VNPay Payment Gateway với xác thực bảo mật
- Thiết kế giao diện admin tùy chỉnh với CSS hiện đại, dễ sử dụng
- Triển khai các tính năng tự động hóa quản lý bằng Django Signals

**• Đóng góp về mặt thực tiễn:**
- Cung cấp một giải pháp đặt vé trực tuyến có thể áp dụng trong thực tế
- Giao diện người dùng thân thiện, dễ sử dụng
- Hệ thống quản trị mạnh mẽ, hỗ trợ tốt cho việc quản lý rạp phim

**• Đóng góp về mặt học thuật:**
- Minh chứng việc áp dụng các công nghệ web hiện đại trong thực tế
- Cung cấp tài liệu tham khảo cho các dự án tương tự
- Rèn luyện kỹ năng phân tích, thiết kế và phát triển hệ thống

---

# CHƯƠNG 2. NỘI DUNG DỰ ÁN

## 2.1. Chức năng chính

### 2.1.1. Đăng ký/Đăng nhập

**Đăng ký tài khoản:**
- Người dùng có thể đăng ký tài khoản mới với các thông tin: username (tên đăng nhập), password (mật khẩu), name (họ tên), age (tuổi)
- Hệ thống kiểm tra tính hợp lệ của dữ liệu:
  - Username phải duy nhất, không trùng với tài khoản đã có
  - Password phải đáp ứng các yêu cầu: tối thiểu 8 ký tự, không toàn số, không giống username
  - Tuổi phải trong khoảng 0-100
  - Password và password_confirm phải trùng khớp
- Sau khi đăng ký thành công, hệ thống tự động đăng nhập người dùng

**Đăng nhập:**
- Người dùng đăng nhập bằng username và password
- Hệ thống xác thực thông tin đăng nhập
- Tùy chọn "Nhớ tài khoản" cho phép lưu session trong 14 ngày
- Sau khi đăng nhập thành công:
  - Nếu là staff/admin: chuyển hướng đến trang quản trị `/admin/`
  - Nếu là user thường: chuyển hướng đến trang đặt vé

**Đăng xuất:**
- Người dùng có thể đăng xuất khỏi hệ thống
- Session được xóa hoàn toàn
- Chuyển hướng về trang chủ

### 2.1.2. Xem danh sách phim và suất chiếu

**Danh sách phim:**
- Hiển thị tất cả các phim đang có trong hệ thống
- Mỗi phim hiển thị: poster, tiêu đề, thể loại, đạo diễn, ngày phát hành
- Layout dạng grid, responsive trên mọi thiết bị

**Thông tin chi tiết phim:**
- Mô tả đầy đủ về phim
- Thời lượng phim
- Danh sách các suất chiếu của phim đó

**Lịch chiếu:**
- Trang hiển thị lịch chiếu tổng hợp
- Có thể lọc theo ngày, phim, phòng chiếu
- Hiển thị thời gian bắt đầu và kết thúc của mỗi suất chiếu

**Chọn suất chiếu:**
- Mỗi phim có dropdown để chọn suất chiếu
- Chỉ hiển thị các suất chiếu đang hoạt động (is_active = True)
- Suất chiếu được sắp xếp theo thời gian

### 2.1.3. Chọn ghế

**Sơ đồ ghế:**
- Hiển thị sơ đồ ghế của phòng chiếu dựa trên suất chiếu đã chọn
- Ghế được hiển thị dạng grid, mỗi ghế có số ghế tương ứng
- Sử dụng AJAX để load sơ đồ ghế động khi chọn suất chiếu

**Trạng thái ghế:**
- **Ghế còn trống**: Hiển thị màu xanh, có thể click để chọn
- **Ghế đã đặt**: Hiển thị màu đỏ hoặc xám, không thể chọn
- **Ghế đang chọn**: Hiển thị màu vàng hoặc highlight khi user click

**Chọn nhiều ghế:**
- Người dùng có thể chọn nhiều ghế cùng lúc (tương ứng với số lượng vé)
- Hệ thống kiểm tra ghế còn trống trước khi cho phép chọn
- Validation để đảm bảo số ghế chọn = số lượng vé

### 2.1.4. Đặt vé

**Quy trình đặt vé:**
1. Chọn phim từ danh sách
2. Chọn suất chiếu từ dropdown
3. Chọn loại vé (Người lớn hoặc Trẻ em)
4. Chọn số lượng vé
5. Chọn ghế trên sơ đồ
6. Xác nhận thông tin đặt vé
7. Chuyển đến trang thanh toán

**Tính giá vé:**
- Vé người lớn: 100,000 VNĐ
- Vé trẻ em: 50,000 VNĐ
- Tổng tiền = (Giá vé × Số lượng)

**Validation:**
- Kiểm tra ghế còn trống (không bị đặt bởi người khác)
- Kiểm tra số lượng ghế chọn = số lượng vé
- Kiểm tra không có ghế trùng lặp
- Kiểm tra user đã đăng nhập

**Lưu thông tin:**
- Thông tin đặt vé được lưu vào session trước khi thanh toán
- Bao gồm: showtime_id, movie_id, room_id, selected_seats, type, quantity, total_amount

### 2.1.5. Thanh toán trực tuyến

**Tích hợp VNPay:**
- Hệ thống tích hợp VNPay Payment Gateway để xử lý thanh toán trực tuyến
- Hỗ trợ cả môi trường sandbox (test) và production

**Quy trình thanh toán:**
1. User xác nhận thông tin đặt vé
2. Hệ thống tạo order_id từ timestamp + user_id
3. Build payment URL với các thông tin:
   - vnp_Amount: Tổng tiền (đơn vị: xu)
   - vnp_TxnRef: Mã đơn hàng
   - vnp_OrderInfo: Mô tả đơn hàng
   - vnp_SecureHash: Hash SHA512 để bảo mật
4. Redirect user đến trang thanh toán VNPay
5. User thực hiện thanh toán trên VNPay
6. VNPay redirect về payment_return với kết quả
7. Hệ thống xác thực hash và xử lý kết quả

**Xử lý kết quả thanh toán:**
- **Thành công (Response Code = '00')**:
  - Tạo vé cho mỗi ghế đã chọn
  - Cập nhật trạng thái ghế (is_available = False)
  - Xóa booking_data khỏi session
  - Hiển thị thông báo thành công
- **Thất bại**: Hiển thị thông báo lỗi, không tạo vé

**IPN (Instant Payment Notification):**
- VNPay gọi IPN URL để cập nhật trạng thái thanh toán (server-to-server)
- Hệ thống xác thực hash và xử lý callback
- Đảm bảo tính toàn vẹn của giao dịch

### 2.1.6. Xem lịch sử đặt vé

**Danh sách vé đã đặt:**
- Hiển thị tất cả vé mà user đã đặt
- Thông tin mỗi vé:
  - Mã vé (ID)
  - Tên phim
  - Suất chiếu (thời gian)
  - Phòng chiếu
  - Số ghế
  - Loại vé (Người lớn/Trẻ em)
  - Giá vé
  - Ngày giờ đặt

**Hiển thị:**
- Sử dụng DataTables để hiển thị bảng với các tính năng:
  - Sắp xếp (sorting)
  - Tìm kiếm (searching)
  - Phân trang (pagination)
  - Tùy chỉnh ngôn ngữ tiếng Việt

**Truy vấn tối ưu:**
- Sử dụng select_related để giảm số lượng truy vấn database
- Load dữ liệu liên quan (movie, room, seat, showtime) trong một lần truy vấn

### 2.1.7. Quản lý phim, suất chiếu, người dùng (Admin)

**Quản lý phim:**
- CRUD đầy đủ (Create, Read, Update, Delete)
- Upload poster phim (sử dụng Pillow để xử lý ảnh)
- Quản lý suất chiếu inline (thêm/sửa suất chiếu ngay trong form phim)
- Hiển thị thumbnail poster trong danh sách
- Thống kê số suất chiếu của mỗi phim
- Preview ảnh poster lớn trong form

**Quản lý suất chiếu:**
- Tạo, sửa, xóa suất chiếu
- Gán phim vào phòng chiếu với thời gian cụ thể
- Tự động tính end_time dựa trên duration của phim
- Quản lý trạng thái (active/inactive)
- Thống kê ghế còn trống/đã đặt
- Biểu đồ trực quan về tình trạng ghế (progress bar)
- Lọc theo phim, phòng, ngày

**Quản lý người dùng:**
- Xem danh sách tất cả người dùng
- Quản lý thông tin: username, name, age
- Phân quyền: is_staff, is_superuser, is_active
- Badge trạng thái màu sắc (Hoạt động/Vô hiệu)
- Date hierarchy để lọc theo last_login
- Tìm kiếm theo username và name

**Quản lý phòng chiếu:**
- Tạo, sửa, xóa phòng chiếu
- Thiết lập sức chứa (capacity)
- Tự động tạo ghế khi tạo phòng (Django Signal)
- Thống kê số ghế, ghế còn trống với phần trăm
- Liên kết đến danh sách ghế của phòng

**Quản lý ghế:**
- Xem danh sách tất cả ghế
- Lọc theo phòng, trạng thái
- Badge trạng thái (Còn trống/Đã đặt)
- Tự động cập nhật trạng thái khi đặt/hủy vé

**Quản lý vé:**
- Xem tất cả vé đã được đặt
- Lọc theo user, phim, phòng, ngày
- Tìm kiếm vé
- Hiển thị thông tin đầy đủ: user, phim, phòng, ghế, giá, loại vé
- Badge loại vé (Người lớn/Trẻ em)
- Định dạng giá tiền

### 2.1.8. Quản lý thống kê và báo cáo (Admin)

**Thống kê suất chiếu:**
- Số ghế còn trống và đã đặt cho mỗi suất chiếu
- Phần trăm ghế đã bán
- Biểu đồ trực quan (progress bar) trong admin

**Thống kê phòng:**
- Tổng số ghế của phòng
- Số ghế còn trống
- Phần trăm ghế còn trống
- Màu sắc cảnh báo (xanh > 50%, cam 20-50%, đỏ < 20%)

**Thống kê phim:**
- Số suất chiếu của mỗi phim
- Liên kết đến danh sách suất chiếu

**Giao diện admin tùy chỉnh:**
- Header với gradient màu tím/xanh
- CSS hiện đại với shadows, rounded corners
- Badge trạng thái màu sắc
- Thumbnail ảnh
- Biểu đồ và progress bars
- Responsive design

## 2.2. Công nghệ sử dụng

### 2.2.1. Khái quát về Django Framework

**Django** là một web framework mã nguồn mở, cấp cao, được viết bằng Python. Django tuân theo mô hình MVT (Model-View-Template) và có triết lý "batteries included" - cung cấp sẵn nhiều tính năng cần thiết.

**Đặc điểm:**
- **ORM (Object-Relational Mapping)**: Cho phép tương tác với database bằng Python code thay vì SQL
- **Admin Interface**: Giao diện quản trị tự động, có thể tùy chỉnh
- **URL Routing**: Hệ thống routing linh hoạt, hỗ trợ regex
- **Template System**: Hệ thống template mạnh mẽ với template inheritance
- **Security**: Tích hợp sẵn CSRF protection, XSS prevention, SQL injection prevention
- **Session Management**: Quản lý session an toàn
- **Middleware**: Hệ thống middleware linh hoạt

**Trong dự án:**
- Django 5.0.3 được sử dụng làm framework chính
- Models để định nghĩa cấu trúc database
- Views để xử lý logic nghiệp vụ
- Templates để hiển thị giao diện
- Admin để quản lý dữ liệu
- Signals để tự động hóa các tác vụ

### 2.2.2. Khái quát về Python

**Python** là ngôn ngữ lập trình cấp cao, thông dịch, đa mục đích. Python nổi bật với cú pháp rõ ràng, dễ đọc và có hệ sinh thái thư viện phong phú.

**Đặc điểm:**
- Cú pháp đơn giản, dễ học
- Thư viện chuẩn phong phú
- Hỗ trợ nhiều mô hình lập trình (OOP, functional)
- Tự động quản lý bộ nhớ (garbage collection)
- Đa nền tảng (Windows, Linux, macOS)

**Trong dự án:**
- Python được sử dụng để viết toàn bộ backend
- Sử dụng các thư viện chuẩn: datetime, json, os, hmac, hashlib
- Tích hợp với Django framework

### 2.2.3. Khái quát về HTML5

**HTML5** (HyperText Markup Language version 5) là phiên bản mới nhất của ngôn ngữ đánh dấu HTML, được sử dụng để cấu trúc và trình bày nội dung trên web.

**Đặc điểm:**
- Semantic elements: `<header>`, `<nav>`, `<section>`, `<article>`, `<footer>`
- Form controls mới: date, email, number, range
- Media elements: `<audio>`, `<video>`
- Canvas và SVG cho đồ họa
- Local storage và session storage

**Trong dự án:**
- HTML5 được sử dụng để cấu trúc các trang web
- Semantic HTML để tăng khả năng truy cập và SEO
- Form elements cho các form đăng ký, đăng nhập, đặt vé
- Template inheritance với Django template system

### 2.2.4. Khái quát về CSS3

**CSS3** (Cascading Style Sheets level 3) là phiên bản mới nhất của CSS, cung cấp nhiều tính năng mới để tạo giao diện đẹp mắt và hiện đại.

**Đặc điểm:**
- **Gradients**: Linear và radial gradients
- **Shadows**: Box shadow và text shadow
- **Transitions và Animations**: Hiệu ứng chuyển động mượt mà
- **Flexbox và Grid**: Layout linh hoạt
- **Media Queries**: Responsive design
- **Transform**: Xoay, scale, translate elements
- **Border-radius**: Bo góc

**Trong dự án:**
- CSS3 tùy chỉnh cho từng trang (home.css, book_ticket.css, booking.css, schedule.css, modal.css)
- CSS tùy chỉnh cho admin interface (admin_custom.css)
- Sử dụng gradients, shadows, rounded corners
- Responsive design với media queries
- Animations và transitions cho các tương tác

### 2.2.5. Khái quát về JavaScript và jQuery

**JavaScript** là ngôn ngữ lập trình phía client, được sử dụng để tạo tính tương tác cho website.

**jQuery** là một thư viện JavaScript phổ biến, đơn giản hóa việc thao tác DOM, xử lý events và AJAX.

**Đặc điểm JavaScript:**
- Chạy trên trình duyệt (client-side)
- Hỗ trợ OOP và functional programming
- Asynchronous programming với Promises và async/await
- DOM manipulation

**Đặc điểm jQuery:**
- Cú pháp ngắn gọn, dễ sử dụng
- Cross-browser compatibility
- AJAX đơn giản
- Plugin ecosystem phong phú

**Trong dự án:**
- JavaScript thuần cho các tương tác cơ bản
- jQuery 3.6.4 cho DOM manipulation và AJAX
- Xử lý form submission
- Modal interactions
- AJAX để load sơ đồ ghế động
- DataTables plugin để hiển thị bảng dữ liệu

### 2.2.6. Khái quát về Bootstrap

**Bootstrap** là framework CSS front-end mã nguồn mở, cung cấp các component và utility classes để xây dựng giao diện responsive nhanh chóng.

**Đặc điểm:**
- Grid system 12 cột
- Responsive utilities
- Pre-built components: buttons, modals, carousel, navbar, cards
- Utility classes cho spacing, colors, typography
- JavaScript plugins

**Trong dự án:**
- Bootstrap 4.5.2 được sử dụng (CDN)
- Grid system cho layout responsive
- Components: navbar, modals, carousel, cards, buttons
- DataTables Bootstrap 4 integration
- Note: Crispy Forms sử dụng Bootstrap 5, nhưng templates chính dùng Bootstrap 4

### 2.2.7. Khái quát về SQLite

**SQLite** là hệ quản trị cơ sở dữ liệu quan hệ nhúng, nhẹ, không cần server riêng.

**Đặc điểm:**
- File-based database
- Không cần cấu hình server
- ACID compliant
- Hỗ trợ đầy đủ SQL
- Phù hợp cho development và ứng dụng nhỏ

**Trong dự án:**
- SQLite3 được sử dụng làm database mặc định
- Django ORM tương tác với SQLite
- Phù hợp cho development và testing
- Có thể chuyển sang PostgreSQL/MySQL cho production

### 2.2.8. Khái quát về VNPay Payment Gateway

**VNPay** là cổng thanh toán trực tuyến phổ biến tại Việt Nam, cung cấp giải pháp thanh toán cho các website thương mại điện tử.

**Đặc điểm:**
- Hỗ trợ nhiều ngân hàng
- Thanh toán qua thẻ ATM, thẻ tín dụng, ví điện tử
- Sandbox environment cho testing
- Production environment cho thực tế
- IPN (Instant Payment Notification) để cập nhật trạng thái

**Bảo mật:**
- SHA512 hash để xác thực giao dịch
- Secure hash validation
- Checksum verification

**Trong dự án:**
- Tích hợp VNPay Payment Gateway
- Module vnpay.py để xử lý thanh toán
- Xây dựng payment URL với hash SHA512
- Xử lý payment_return và payment_ipn
- Hỗ trợ cả sandbox và production mode

---

# CHƯƠNG 3. PHƯƠNG PHÁP ĐỀ XUẤT

## 3.1. Tổng quan phương pháp

Hệ thống được xây dựng theo kiến trúc **MVT (Model-View-Template)** của Django, kết hợp với các best practices trong phát triển web hiện đại.

**Kiến trúc tổng thể:**
- **Frontend**: HTML5, CSS3, JavaScript, jQuery, Bootstrap
- **Backend**: Django Framework (Python)
- **Database**: SQLite (có thể nâng cấp PostgreSQL/MySQL)
- **Payment**: VNPay Payment Gateway
- **Deployment**: Gunicorn + WhiteNoise

## 3.2. Kiến trúc hệ thống

**Layers:**
1. **Presentation Layer**: Templates, Static files (CSS, JS, Images)
2. **Business Logic Layer**: Views, Forms, Custom logic
3. **Data Access Layer**: Models, ORM, Database
4. **External Services**: VNPay API

**Flow xử lý:**
1. User request → URL routing
2. URL → View function
3. View → Model (database queries)
4. View → Template (render HTML)
5. Response → User browser

## 3.3. Thiết kế cơ sở dữ liệu

**Các Models chính:**

1. **CustomUser**: Người dùng
   - username, password, name, age
   - is_staff, is_superuser, is_active
   - last_login

2. **Movie**: Phim
   - title, genre, duration, director
   - release_date, description, poster

3. **Room**: Phòng chiếu
   - name, capacity

4. **Seat**: Ghế
   - room (ForeignKey), seat_number, is_available

5. **Showtime**: Suất chiếu
   - movie (ForeignKey), room (ForeignKey)
   - start_time, end_time, is_active

6. **Ticket**: Vé
   - user, movie, room, seat, showtime (ForeignKeys)
   - price, type, date_time

**Relationships:**
- Movie → Showtime (One-to-Many)
- Room → Seat (One-to-Many)
- Room → Showtime (One-to-Many)
- Showtime → Ticket (One-to-Many)
- User → Ticket (One-to-Many)
- Seat → Ticket (One-to-Many)

**Signals:**
- `post_save` Room → Tự động tạo ghế
- `post_save` Ticket → Cập nhật trạng thái ghế
- `post_delete` Ticket → Cập nhật trạng thái ghế

## 3.4. Quy trình xử lý nghiệp vụ

**Quy trình đặt vé:**
1. User chọn phim → Load suất chiếu
2. User chọn suất chiếu → Load sơ đồ ghế (AJAX)
3. User chọn ghế → Validation
4. User xác nhận → Lưu vào session
5. User thanh toán → Redirect VNPay
6. VNPay callback → Xác thực hash
7. Thành công → Tạo vé, cập nhật ghế
8. Hiển thị kết quả

**Quy trình thanh toán:**
1. Build payment data
2. Tính SHA512 hash
3. Tạo payment URL
4. Redirect đến VNPay
5. User thanh toán trên VNPay
6. VNPay redirect về với kết quả
7. Validate hash
8. Xử lý kết quả (tạo vé hoặc báo lỗi)

---

# CHƯƠNG 4. KẾT QUẢ VÀ THỰC NGHIỆM

## 4.1. Giao diện người dùng

**Trang chủ:**
- Carousel hiển thị poster phim
- Thông báo và thông tin
- Modal đăng nhập/đăng ký
- Navigation bar responsive

**Danh sách phim:**
- Grid layout hiển thị phim
- Form đặt vé cho mỗi phim
- Dropdown chọn suất chiếu
- Responsive trên mọi thiết bị

**Chọn ghế:**
- Sơ đồ ghế trực quan
- Màu sắc phân biệt trạng thái
- AJAX load động
- Validation real-time

**Thanh toán:**
- Form thanh toán VNPay
- Hiển thị thông tin đặt vé
- Redirect an toàn

**Lịch sử đặt vé:**
- Bảng dữ liệu với DataTables
- Sorting, searching, pagination
- Hiển thị đầy đủ thông tin

## 4.2. Giao diện quản trị

**Admin Dashboard:**
- Header với gradient màu tím/xanh
- Module cards với shadows
- Thống kê trực quan

**Quản lý phim:**
- Thumbnail poster trong danh sách
- Preview ảnh lớn trong form
- Inline suất chiếu
- Thống kê số suất chiếu

**Quản lý suất chiếu:**
- Badge trạng thái màu sắc
- Biểu đồ ghế (progress bar)
- Định dạng thời gian đẹp
- Thống kê ghế còn trống/đã đặt

**Quản lý người dùng:**
- Badge trạng thái
- Date hierarchy
- Tìm kiếm nhanh

**Quản lý vé:**
- Badge loại vé
- Định dạng giá tiền
- Lọc và tìm kiếm mạnh mẽ

## 4.3. Kết quả kiểm thử chức năng

**Đăng ký/Đăng nhập:**
- ✅ Đăng ký thành công với validation đầy đủ
- ✅ Đăng nhập với remember me
- ✅ Phân quyền staff/user hoạt động đúng

**Đặt vé:**
- ✅ Chọn phim và suất chiếu
- ✅ Load sơ đồ ghế bằng AJAX
- ✅ Chọn nhiều ghế
- ✅ Validation ghế còn trống

**Thanh toán:**
- ✅ Tích hợp VNPay thành công
- ✅ Xác thực hash SHA512
- ✅ Xử lý payment_return
- ✅ Xử lý IPN callback
- ✅ Tạo vé sau thanh toán thành công

**Quản lý:**
- ✅ CRUD đầy đủ cho tất cả models
- ✅ Tự động tạo ghế khi tạo phòng
- ✅ Tự động cập nhật trạng thái ghế
- ✅ Thống kê và biểu đồ hoạt động đúng

## 4.4. Đánh giá hiệu năng

**Tối ưu hóa:**
- Sử dụng select_related để giảm số lượng queries
- WhiteNoise để phục vụ static files hiệu quả
- Session management tối ưu

**Bảo mật:**
- CSRF protection
- XSS prevention
- SQL injection prevention (ORM)
- Password hashing (PBKDF2)
- Secure hash validation (SHA512)

---

# CHƯƠNG 5. KẾT LUẬN

## 5.1. Tổng kết

Đề tài **"Thiết kế và Xây dựng Website Đặt Vé Xem Phim CinemaPlus"** đã được hoàn thành với các kết quả sau:

**Về mặt chức năng:**
- ✅ Xây dựng đầy đủ các chức năng cơ bản: đăng ký, đăng nhập, xem phim, đặt vé, thanh toán
- ✅ Tích hợp thành công VNPay Payment Gateway
- ✅ Hệ thống quản trị mạnh mẽ với giao diện tùy chỉnh đẹp mắt
- ✅ Tự động hóa quản lý ghế và suất chiếu

**Về mặt kỹ thuật:**
- ✅ Sử dụng Django Framework hiệu quả
- ✅ Thiết kế database hợp lý với relationships rõ ràng
- ✅ Giao diện responsive, thân thiện với người dùng
- ✅ Bảo mật tốt với các biện pháp bảo vệ đầy đủ

**Về mặt thực tiễn:**
- ✅ Hệ thống có thể áp dụng trong thực tế
- ✅ Quy trình đặt vé rõ ràng, dễ sử dụng
- ✅ Quản trị thuận tiện với các công cụ thống kê trực quan

## 5.2. Hạn chế và hướng phát triển

**Hạn chế:**
- Database SQLite phù hợp cho development, cần nâng cấp PostgreSQL/MySQL cho production
- Chưa có hệ thống đánh giá và bình luận phim
- Chưa có chương trình khuyến mãi và tích điểm
- Chưa có hệ thống đề xuất phim theo sở thích
- Chưa có ứng dụng di động

**Hướng phát triển:**
1. **Nâng cấp database**: Chuyển sang PostgreSQL hoặc MySQL cho production
2. **Tích hợp nhiều cổng thanh toán**: Momo, ZaloPay, PayPal
3. **Hệ thống đánh giá**: Cho phép user đánh giá và bình luận phim
4. **Recommendation system**: Đề xuất phim dựa trên lịch sử xem
5. **Chương trình khuyến mãi**: Mã giảm giá, tích điểm, thành viên VIP
6. **Ứng dụng di động**: React Native hoặc Flutter
7. **Real-time updates**: WebSocket để cập nhật ghế real-time
8. **Email notifications**: Gửi email xác nhận đặt vé
9. **Báo cáo và analytics**: Dashboard thống kê chi tiết
10. **Multi-language**: Hỗ trợ nhiều ngôn ngữ

---

# TÀI LIỆU THAM KHẢO

[1] Django Software Foundation. (2024). *Django Documentation*. https://docs.djangoproject.com/

[2] Python Software Foundation. (2024). *Python Documentation*. https://docs.python.org/

[3] VNPay. (2024). *VNPay Payment Gateway Integration Guide*. https://sandbox.vnpayment.vn/apis/

[4] Bootstrap Team. (2024). *Bootstrap Documentation*. https://getbootstrap.com/docs/4.5/

[5] jQuery Foundation. (2024). *jQuery Documentation*. https://api.jquery.com/

[6] DataTables. (2024). *DataTables Documentation*. https://datatables.net/

[7] Pillow. (2024). *Pillow Documentation*. https://pillow.readthedocs.io/

[8] Django Crispy Forms. (2024). *Django Crispy Forms Documentation*. https://django-crispy-forms.readthedocs.io/

[9] WhiteNoise. (2024). *WhiteNoise Documentation*. https://whitenoise.evans.io/

[10] Gunicorn. (2024). *Gunicorn Documentation*. https://docs.gunicorn.org/

---

*Báo cáo được hoàn thành vào tháng [Tháng/Năm]*
