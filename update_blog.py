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
    "Chia sẻ kinh nghiệm du lịch trải nghiệm cá nhân tại Hà Giang.",
    "Tips dựng phim: Cách sử dụng màu sắc để kể chuyện (Color Grading).",
    "Cách phối hợp SFX để tạo chiều sâu không gian cho video du lịch.",
    "Hướng dẫn chọn nhạc nền phù hợp với tiết tấu phim trải nghiệm."
]
selected_topic = random.choice(topics)

# 3. Đảm bảo thư mục tồn tại
os.makedirs('_drafts', exist_ok=True)

# 4. Gọi API với xử lý lỗi chặt chẽ
try:
    prompt = f"Bạn là blogger du lịch và filmmaker. Hãy viết một bài blog HTML (nằm trong thẻ <article>) về: {selected_topic}. Nội dung hấp dẫn, có tiêu đề h2."
    response = model.generate_content(prompt)
    
    # Lấy nội dung văn bản
    content = response.text
    
    # Tạo tên file theo ngày giờ để không bao giờ bị trùng
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_path = f"_drafts/post-{timestamp}.html"
    
    # Ghi file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"--- THÀNH CÔNG: Đã tạo file {file_path} ---")

except Exception as e:
    # Nếu lỗi, ghi lỗi vào một file để bạn biết tại sao
    with open("_drafts/error_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()}: Lỗi {str(e)}\n")
    print(f"Lỗi: {e}")
