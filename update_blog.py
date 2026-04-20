import google.generativeai as genai
import os
import random
from datetime import datetime

# 1. Cấu hình Gemini
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Không tìm thấy API Key!")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Danh sách chủ đề
topics = [
    "Chia sẻ kinh nghiệm du lịch trải nghiệm cá nhân tại vùng núi phía Bắc Việt Nam.",
    "Tips dựng phim: Cách sử dụng 'J-cut' và 'L-cut' để chuyển cảnh mượt mà.",
    "Hướng dẫn phối hợp Sound Effects (SFX) để tạo không khí rùng rợn hoặc kịch tính.",
    "Kể về một sự cố hài hước khi đi quay phim thực tế và bài học rút ra."
]
selected_topic = random.choice(topics)

# 3. Tạo Prompt
prompt = f"""
Bạn là một blogger chuyên nghiệp về du lịch và dựng phim.
Hãy viết một bài chia sẻ ngắn về: {selected_topic}
Yêu cầu:
- Ngôn ngữ: Tiếng Việt, phong cách gần gũi, chuyên nghiệp.
- Định dạng: Trả về duy nhất mã HTML nằm trong thẻ <article>.
- Có tiêu đề nằm trong thẻ <h2>.
- Nội dung chia làm các đoạn văn <p> hoặc danh sách <ul> <li>.
- Không dùng markdown (không có dấu ```html).
"""

# 4. Gọi API và Lưu file
try:
    response = model.generate_content(prompt)
    content_html = response.text

    if not os.path.exists('_drafts'):
        os.makedirs('_drafts')

    date_str = datetime.now().strftime("%Y-%m-%d")
    file_path = f"_drafts/post-{date_str}.html"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content_html)
    print(f"Thành công! Đã tạo bản nháp tại {file_path}")
except Exception as e:
    print(f"Lỗi: {e}")
