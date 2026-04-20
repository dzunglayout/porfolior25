import google.generativeai as genai
import os
import random
from datetime import datetime

# 1. Cấu hình Gemini với API Key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY không tồn tại trong Secrets!")

genai.configure(api_key=api_key)

# 2. Sử dụng model 'gemini-1.5-flash-latest' (phiên bản ổn định nhất cho API v1beta)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# 3. Danh sách chủ đề
topics = [
    "Chia sẻ kinh nghiệm du lịch trải nghiệm cá nhân tại Hà Giang.",
    "Tips dựng phim: Cách sử dụng màu sắc để kể chuyện (Color Grading).",
    "Cách phối hợp SFX để tạo chiều sâu không gian cho video du lịch.",
    "Hướng dẫn chọn nhạc nền phù hợp với tiết tấu phim trải nghiệm."
]
selected_topic = random.choice(topics)

# 4. Đảm bảo thư mục tồn tại
os.makedirs('_drafts', exist_ok=True)

# 5. Gọi API
try:
    prompt = f"Bạn là blogger du lịch và filmmaker. Hãy viết một bài blog HTML (nằm trong thẻ <article>) về: {selected_topic}. Nội dung hấp dẫn, có tiêu đề h2."
    
    # Thêm tham số an toàn
    response = model.generate_content(prompt)
    
    if response and response.text:
        content = response.text
        # Tạo tên file theo ngày giờ
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        file_path = f"_drafts/post-{timestamp}.html"
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Thành công: Đã tạo file {file_path}")
    else:
        print("Lỗi: Gemini trả về nội dung rỗng.")

except Exception as e:
    with open("_drafts/error_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()}: {str(e)}\n")
    print(f"Lỗi phát sinh: {e}")
