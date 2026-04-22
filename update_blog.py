import google.generativeai as genai
import os
import random
from datetime import datetime

# 1. Cấu hình
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# 2. CHỦ ĐỀ
topics = [
    "Chia sẻ kinh nghiệm du lịch bụi trải nghiệm cá nhân tại Nhật bản, Hàn Quốc, Singapore, Malaysia, Campuchia, Phú Quốc, Nha Trang, Vũng Tàu, BẢo Lộc...",
    "Tips dựng phim: Cách sử dụng Color Grading để tạo cảm xúc.",
    "Cách phối hợp SFX chuyên nghiệp trong video du lịch.",
    "Hướng dẫn chọn thiết bị quay phim tối giản cho dân du lịch bụi."
]
selected_topic = random.choice(topics)

# 3. Đảm bảo thư mục tồn tại
os.makedirs('_drafts', exist_ok=True)

# 4. GỌI GEMINI 2.5 FLASH
try:
    # Cập nhật tên model thành gemini-2.5-flash
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"Bạn là một chuyên gia Filmmaker và Blogger du lịch. Hãy viết một bài blog HTML (nằm gọn trong thẻ <article>) về: {selected_topic}. Văn phong lôi cuốn, chuyên nghiệp."
    
    response = model.generate_content(prompt)
    
    if response.text:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        file_path = f"_drafts/post-{timestamp}.html"
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"--- THÀNH CÔNG rực rỡ với Gemini 2.5: {file_path} ---")
    else:
        print("API 2.5 không trả về văn bản.")

except Exception as e:
    with open("_drafts/error_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()}: Lỗi phiên bản 2.5 - {str(e)}\n")
    print(f"Lỗi: {e}")
