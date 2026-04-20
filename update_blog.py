import google.generativeai as genai
import os
import random
from datetime import datetime

# 1. Cấu hình Gemini
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Danh sách chủ đề
topics = [
    "Chia sẻ kinh nghiệm du lịch trải nghiệm cá nhân.",
    "Tips dựng phim chuyên nghiệp.",
    "Cách phối hợp SFX hiệu quả."
]
selected_topic = random.choice(topics)

# 3. Tạo thư mục _drafts ngay lập tức (để tránh lỗi Git không tìm thấy)
if not os.path.exists('_drafts'):
    os.makedirs('_drafts')

# Tạo file log nhỏ để chắc chắn thư mục không trống
with open("_drafts/.keep", "w") as f:
    f.write("")

# 4. Gọi API
try:
    prompt = f"Viết một bài blog HTML ngắn về: {selected_topic}. Chỉ trả về code trong thẻ <article>."
    response = model.generate_content(prompt)
    
    # Kiểm tra nếu có nội dung
    if response.text:
        date_str = datetime.now().strftime("%Y-%m-%d")
        file_path = f"_drafts/post-{date_str}.html"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Đã tạo file: {file_path}")
    else:
        print("Gemini không trả về nội dung.")
except Exception as e:
    print(f"Lỗi rồi: {e}")
