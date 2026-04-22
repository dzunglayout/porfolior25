from google import genai
import os
import random
from datetime import datetime

# 1. Cấu hình Client mới
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 2. Chủ đề
topics = [
    "Chia sẻ kinh nghiệm du lịch bụi trải nghiệm cá nhân tại Nhật bản, Hàn Quốc, Singapore, Malaysia, Campuchia, Phú Quốc, Nha Trang, Vũng Tàu, Bảo Lộc...",
    "Tips dựng phim: Cách dùng Color Grading tạo cảm xúc.",
    "Cách phối hợp SFX chuyên nghiệp trong video du lịch.",
    "Thiết bị quay phim tối giản cho dân du lịch bụi."
]
selected_topic = random.choice(topics)

os.makedirs('_drafts', exist_ok=True)

try:
    # 3. Gọi Gemini 2.5 Flash
    prompt = f"""
    Bạn là một Filmmaker và Blogger du lịch.
    Nhiệm vụ:
    1. Viết bài blog HTML (nằm gọn trong thẻ <article>) về: {selected_topic}.
    2. Chèn 1 tấm ảnh Unsplash vào đầu bài viết: 
       <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80" style="width:100%; border-radius:8px;">
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    if response.text:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        file_path = f"_drafts/post-{timestamp}.html"
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"--- THÀNH CÔNG: Đã tạo file {file_path} ---")
    else:
        print("Lỗi: Không nhận được nội dung.")

except Exception as e:
    print(f"Lỗi: {e}")
