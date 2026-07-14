# Ví dụ AI thân thiện cho người mới bắt đầu

Chào mừng! Thư mục này chứa các ví dụ đơn giản, độc lập để giúp bạn bắt đầu với AI và học máy. Mỗi ví dụ được thiết kế thân thiện với người mới bắt đầu với các chú thích chi tiết và giải thích từng bước.

## 📚 Tổng quan về các ví dụ

| Ví dụ | Mô tả | Độ khó | Yêu cầu trước |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | Chương trình AI đầu tiên của bạn - nhận dạng mẫu đơn giản | ⭐ Người mới bắt đầu | Kiến thức cơ bản Python |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | Xây dựng mạng nơ-ron từ đầu | ⭐⭐ Người mới bắt đầu+ | Python, toán cơ bản |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | Phân loại hình ảnh với mô hình đã được huấn luyện sẵn | ⭐⭐ Người mới bắt đầu+ | Python, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | Phân tích cảm xúc văn bản (tích cực/tiêu cực) | ⭐⭐ Người mới bắt đầu+ | Python |

## 🚀 Bắt đầu

### Yêu cầu trước

Đảm bảo bạn đã cài đặt Python (khuyến nghị phiên bản 3.8 trở lên). Cài đặt các gói cần thiết:

```bash
# Cho các script Python
pip install numpy

# Cho các notebook Jupyter (bộ phân loại hình ảnh)
pip install jupyter numpy pillow tensorflow
```

Hoặc sử dụng môi trường conda từ chương trình chính:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Chạy các ví dụ

**Đối với các tập lệnh Python (.py):**
```bash
python 01-hello-ai-world.py
```

**Đối với sổ tay Jupyter (.ipynb):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Lộ trình học tập

Chúng tôi khuyên bạn nên làm theo thứ tự các ví dụ:

1. **Bắt đầu với "Hello AI World"** - Học cơ bản về nhận dạng mẫu
2. **Xây dựng Mạng Nơ-ron Đơn giản** - Hiểu cách mạng nơ-ron hoạt động
3. **Thử nghiệm Bộ phân loại hình ảnh** - Xem AI hoạt động với hình ảnh thực
4. **Phân tích cảm xúc văn bản** - Khám phá xử lý ngôn ngữ tự nhiên

## 💡 Mẹo cho người mới bắt đầu

- **Đọc kỹ các chú thích trong mã** - Chúng giải thích mỗi dòng làm gì
- **Thử nghiệm!** - Thử thay đổi các giá trị và xem kết quả
- **Đừng lo lắng nếu không hiểu hết mọi thứ** - Học là cả một quá trình
- **Hỏi khi có thắc mắc** - Sử dụng [Bảng thảo luận](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Bước tiếp theo

Sau khi hoàn thành các ví dụ này, hãy khám phá toàn bộ chương trình:
- [Giới thiệu về AI](../lessons/1-Intro/README.md)
- [Mạng Nơ-ron](../lessons/3-NeuralNetworks/README.md)
- [Thị giác máy tính](../lessons/4-ComputerVision/README.md)
- [Xử lý ngôn ngữ tự nhiên](../lessons/5-NLP/README.md)

## 🤝 Đóng góp

Bạn thấy các ví dụ này hữu ích? Giúp chúng tôi cải thiện chúng:
- Báo cáo lỗi hoặc đề xuất cải tiến
- Thêm nhiều ví dụ cho người mới bắt đầu
- Cải thiện tài liệu và chú thích

---

*Hãy nhớ: Mỗi chuyên gia đều từng là người mới bắt đầu. Chúc bạn học vui vẻ! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->