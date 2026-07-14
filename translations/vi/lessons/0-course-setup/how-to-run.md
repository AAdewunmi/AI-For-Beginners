# Cách Chạy Mã

Khóa học này bao gồm nhiều ví dụ và bài lab có thể thực thi mà bạn sẽ muốn chạy. Để làm được điều này, bạn cần khả năng thực thi mã Python trong các Jupyter Notebooks được cung cấp như một phần của khóa học này. Bạn có một số lựa chọn để chạy mã:

## Chạy cục bộ trên máy tính của bạn

Để chạy mã cục bộ trên máy tính của bạn, cần phải cài đặt Python. Một khuyến nghị là cài đặt **[miniconda](https://conda.io/en/latest/miniconda.html)** - đây là một bản cài đặt nhẹ hỗ trợ trình quản lý gói `conda` cho các **môi trường ảo** Python khác nhau.

Sau khi bạn cài đặt miniconda, sao chép repository và tạo một môi trường ảo để sử dụng cho khóa học này:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Sử dụng Visual Studio Code với Extension Python

Khóa học này hoạt động tốt nhất khi mở trong [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) với [Extension Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Lưu ý**: Khi bạn sao chép và mở thư mục trong VS Code, nó sẽ tự động đề xuất bạn cài đặt mở rộng Python. Bạn cũng cần cài miniconda như mô tả ở trên.

> **Lưu ý**: Nếu VS Code đề xuất bạn mở lại repository trong container, bạn nên từ chối để sử dụng cài đặt Python cục bộ.

### Sử dụng Jupyter trên trình duyệt

Bạn cũng có thể sử dụng môi trường Jupyter trên trình duyệt ngay trên máy tính của mình. Cả Jupyter cổ điển và JupyterHub đều cung cấp môi trường phát triển tiện lợi với tính năng tự động hoàn thành, tô sáng mã, v.v.

Để khởi động Jupyter cục bộ, hãy vào thư mục khóa học và thực thi:

```bash
jupyter notebook
```
 hoặc
```bash
jupyterhub
```
Sau đó bạn có thể điều hướng đến bất kỳ tệp `.ipynb` nào, mở chúng và bắt đầu làm việc.

### Chạy trong container

Một lựa chọn thay thế cho việc cài đặt Python là chạy mã trong container. Vì repository của chúng tôi cung cấp một thư mục `.devcontainer` đặc biệt hướng dẫn cách xây dựng container cho repo này, VS Code cung cấp cơ hội mở lại mã trong container. Điều này yêu cầu cài đặt Docker và cũng phức tạp hơn, nên chúng tôi khuyến nghị cách này cho người dùng có kinh nghiệm hơn.

## Chạy trên đám mây

Nếu bạn không muốn cài đặt Python cục bộ và có quyền truy cập vào một số tài nguyên đám mây - một lựa chọn tốt là chạy mã trên đám mây. Có một số cách bạn có thể làm điều này:

* Sử dụng **[GitHub Codespaces](https://github.com/features/codespaces)**, một môi trường ảo được tạo cho bạn trên GitHub, có thể truy cập qua giao diện trình duyệt VS Code. Nếu bạn có quyền truy cập vào Codespaces, bạn chỉ cần nhấn nút **Code** trong repo, bắt đầu một codespace và chạy ngay trong tích tắc.
* Sử dụng **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) cung cấp tài nguyên tính toán miễn phí trên đám mây cho bạn thử nghiệm mã trên GitHub. Có một nút ở trang chính để mở repository trong Binder - điều này sẽ nhanh chóng đưa bạn đến trang binder, nơi xây dựng một container nền và khởi động giao diện web Jupyter cho bạn một cách liền mạch.

> **Lưu ý**: Để ngăn chặn việc sử dụng sai mục đích, Binder chặn truy cập một số tài nguyên web. Điều này có thể khiến một số đoạn mã không hoạt động, đặc biệt là những đoạn lấy mô hình và/hoặc bộ dữ liệu từ Internet công cộng. Bạn có thể cần tìm các giải pháp thay thế. Ngoài ra, tài nguyên tính toán do Binder cung cấp khá cơ bản, nên việc huấn luyện sẽ chậm, đặc biệt trong các bài học phức tạp hơn.

## Chạy trên đám mây với GPU

Một số bài học sau trong khóa học này sẽ hưởng lợi rất nhiều từ việc hỗ trợ GPU. Việc huấn luyện mô hình, ví dụ, sẽ cực kỳ chậm nếu không có GPU. Có một vài lựa chọn bạn có thể theo, đặc biệt nếu bạn có quyền truy cập đám mây thông qua [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), hoặc qua tổ chức của bạn:

* Tạo [Máy ảo Khoa học Dữ liệu](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) và kết nối với nó qua Jupyter. Bạn có thể sao chép repository trực tiếp lên máy ảo và bắt đầu học. Máy ảo dòng NC hỗ trợ GPU.

> **Lưu ý**: Một số đăng ký, gồm Azure for Students, không hỗ trợ GPU ngay khi mới mở. Bạn có thể cần yêu cầu thêm lõi GPU thông qua yêu cầu hỗ trợ kỹ thuật.

* Tạo [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) và sử dụng tính năng Notebook tại đó. [Video này](https://azure-for-academics.github.io/quickstart/azureml-papers/) hướng dẫn cách sao chép repository vào notebook Azure ML và bắt đầu sử dụng.

Bạn cũng có thể dùng Google Colab, nơi có hỗ trợ GPU miễn phí, và tải Jupyter Notebooks lên đó để thực thi từng cái một.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->