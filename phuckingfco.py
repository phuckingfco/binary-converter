import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Bộ Chuyển Đổi Số", page_icon="🔢")

st.title("🔢 Ứng dụng Chuyển đổi Hệ số")

# Tạo 2 Tab để chia khung
tab1, tab2 = st.tabs(["➡️ Sang Nhị Phân", "⬅️ Sang Thập Phân"])

with tab1:
    st.header("Đổi Số/Chữ sang Nhị Phân")
    with st.container(border=True): # Tạo khung cho phần này
        du_lieu = st.text_input("Nhập vào số hoặc chữ:", key="input1")
        if du_lieu:
            if du_lieu.isdigit():
                so = int(du_lieu)
                ket_qua = bin(so).replace('0b', '')
                st.success(f"Kết quả: `{ket_qua}`")
            else:
                for ky_tu in du_lieu:
                    st.write(f"🔠 **{ky_tu}** : `{format(ord(ky_tu), '08b')}`")

with tab2:
    st.header("Đổi Nhị Phân sang Thập Phân")
    with st.container(border=True): # Tạo khung cho phần này
        nhi_phan = st.text_input("Nhập mã nhị phân (0 và 1):", key="input2")
        if nhi_phan:
            try:
                so_thap_phan = int(nhi_phan, 2)
                st.success(f"Kết quả thập phân: **{so_thap_phan}**")
            except ValueError:
                st.error("Lỗi: Vui lòng chỉ nhập 0 và 1!")

st.markdown("---")
st.caption("Tạm biệt Friend! Ổn thì cho tôi 5 sao nhé^^.")
