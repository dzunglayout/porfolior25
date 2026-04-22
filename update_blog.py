import google.generativeai as genai
import os
import random
from datetime import datetime

# 1. Cấu hình
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# 2. Chủ đề
topics = [
    "Chia sẻ kinh nghiệm du lịch bụi trải nghiệm cá nhân tại Nhật bản, Hàn Quốc, Singapore, Malaysia, Campuchia, Phú Quốc, Nha Trang, Vũng Tàu, Bảo Lộc...",
    "Tips dựng phim: Cách sử dụng Color Grading để tạo cảm xúc.",
    "Cách phối hợp SFX chuyên nghiệp trong video du lịch.",
    "Hướng dẫn chọn thiết bị quay phim tối giản cho dân du lịch bụi."
]
selected_topic = random.choice(topics)

os.makedirs('_drafts', exist_ok=True)

try:
    # 3. Yêu cầu Gemini viết bài VÀ trích xuất từ khóa ảnh
    prompt = f"""
    Bạn là một chuyên gia Filmmaker và Blogger du lịch. 
    Hãy thực hiện 2 nhiệm vụ:
    1. Viết bài blog HTML (nằm trong thẻ <article>) về: {selected_topic}.
    2. Ở cuối bài, hãy thêm một thẻ <img> với cấu trúc: <img src="https://source.unsplash.com/featured/1200x600?keyword" alt="mô tả">
       Trong đó, hãy thay 'keyword' bằng 1 từ khóa tiếng Anh chính xác nhất liên quan đến bài viết (ví dụ: 'travel', 'cinematography', 'mountain').
    
    Yêu cầu: Văn phong lôi cuốn, chuyên nghiệp, mã HTML sạch sẽ.
    """
    
    response = model.generate_content(prompt)
    
    if response.text:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        file_path = f"_drafts/post-{timestamp}.html"
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"--- THÀNH CÔNG: Bài viết đã có kèm ảnh tự động ---")
    else:
        print("Không có nội dung trả về.")

except Exception as e:
    print(f"Lỗi: {e}")
