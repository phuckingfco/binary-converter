import streamlit as st

# Cấu hình trang (icon và tiêu đề trên trình duyệt)
st.set_page_config(page_title="Binary Converter", page_icon="🔢")

# 1. Phần Lời chào (Giao diện thay cho print)
st.title("🔢 CHƯƠNG TRÌNH ĐỔI SANG NHỊ PHÂN")
st.markdown("---")

# 2. Phần Nhập dữ liệu (Thay cho input)
du_lieu = st.text_input("Nhập vào số hoặc chữ để chuyển đổi:", placeholder="Ví dụ: 123 hoặc Hello")

# 3. Xử lý logic (Giữ nguyên logic của bạn nhưng thay print bằng st.write)
if du_lieu:
    if du_lieu.isdigit():
        so = int(du_lieu)
        ket_qua = bin(so).replace('0b', '')
        st.success(f"**Kết quả hệ nhị phân:**")
        st.code(ket_qua) # Hiển thị code cho dễ copy
    else:
        st.info(f"Hệ nhị phân của chuỗi '{du_lieu}':")
        # Tạo bảng để nhìn cho chuyên nghiệp
        for ky_tu in du_lieu:
            nhi_phan = format(ord(ky_tu), '08b')
            st.write(f"🔠 **{ky_tu}** : `{nhi_phan}`")

# 4. Phần chân trang
st.markdown("---")
st.caption("Tạm biệt Friend! Ỗn thì cho tôi 5 sao nhé^^.")
