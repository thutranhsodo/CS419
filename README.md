# Xây dựng hệ thống truy xuất tin tức bằng tiếng Anh dựa trên Vector Space Model và Boolean Independence Model
### 1. Thực nghiệm hai mô hình VSM và BIM trên bộ ngữ liệu Cranfield:
* Kết quả thực nghiệm:
<table border="1">
  <tr>
    <td><b> </b>
    <td><b>VSM</b></td>
    <td><b>BIM</b></td>
  </tr>
  <tr>
    <td>Precision</td>
    <td>0.0058</td>
    <td>0.0058</td>
  </tr>
  <tr>
    <td>Recall</td>
    <td>0.9995</td>
    <td>0.9959</td>
  </tr>
  <tr>
    <td>F1-score</td>
    <td>0.0115</td>
    <td>0.0115</td>
  </tr>
  <tr>
    <td>Precision@5</td>
    <td>0.4089</td>
    <td>0.3289</td>
  </tr>
  <tr>
    <td>Precision@10</td>
    <td>0.2893</td>
    <td>0.2338</td>
  </tr>
  <tr>
    <td>Precision@20</td>
    <td>0.1938</td>
    <td>0.1600</td>
  </tr>
  <tr>
    <td>MAP</td>
    <td>0.3982</td>
    <td>0.3112</td>
  </tr>
  <tr>
    <td>MAPr</td>
    <td>0.4177</td>
    <td>0.3318</td>
  </tr>
</table>

### 2. Hệ thống truy xuất tin tức bằng Tiếng Anh dựa trên Vector Space Model:
* <b>Thu thâp dữ liệu: </b>

Thực hiện thu thập dữ liệu từ trang CNN bằng kỹ thuật web scraping thông qua thư viện Scrapy của Python.
Các chuyên mục chính được thu thập bao gồm:
  * Sport (bóng đá, tennis, Olympic),
  * Entertainment (phim ảnh, truyền hình, người nổi tiếng),
  * Health (thể chất, thực phẩm, giấc ngủ, tinh thần),
  * Business (công nghệ, tài chính),
  * Style (thời trang, thiết kế, làm đẹp)...

Với mỗi bài viết, hệ thống thu thập các trường thông tin quan trọng như tiêu đề (title), tác giả (author), ngày xuất bản (publication date), nội dung (content), và URL gốc (source url). Đồng thời, nó tự động gán một danh mục (cate) cho mỗi bài viết dựa trên URL của chuyên mục chứa nó (ví dụ: ’sport’, ’entertainment’).
* <b> Tiền xử lý và Lập chỉ mục: </b>

Thực hiện các bước tiền xử lý như: tách từ, lọc stopword, lọc ký tự và số, stemming. 

Xây dựng ma trận TF-IDF và Chỉ mục
* <b> Áp dụng Phương pháp Phân lớp để Tăng độ phủ của kết quả truy xuất: </b>

Sử dụng mô hình k-Nearest Neighbors (kNN) được huấn luyện trên toàn bộ tập văn bản đã chuẩn hóa để phân loại truy vấn vào các danh mục tin tức (sport, entertainment, health, business, style). sau đó chỉ tìm kiếm và xếp hạng các tài liệu trong cùng danh mục đó.
* <b> Xây dựng Website cho phép Truy xuất Văn bản: </b>

Giao diện tìm kiếm được triển khai bằng thư viện Streamlit, cho phép người dùng:
* Nhập truy vấn trực tiếp trên web.
* Nhận lại danh sách các bài viết phù hợp (hiển thị tiêu đề, chuyên mục, liên kết, điểm tương đồng) mặc định là top 10 bài có độ tương đồng cao nhất.
