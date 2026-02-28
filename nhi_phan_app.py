# 1. CẤU HÌNH TRANG 
import streamlit as st
st.set_page_config(
    page_title="PhucKing® - Bộ Chuyển Đổi Số", 
    page_icon="🔢",
    initial_sidebar_state="expanded" # Tự động nhảy vào Sidebar
)
# 2. CSS TỔNG HỢP 
st.markdown(
    """
    <style>
    /* 1. HIỆN Header để giữ Menu 3 gạch nhưng làm Header trong suốt */
    header {
        visibility: visible !important;
        background-color: rgba(0,0,0,0) !important;
    }

    /* 2. ẨN TRIỆT ĐỂ dòng "Fork me on GitHub" và nút Deploy */
    .viewerBadge_container__1QSob, 
    .stDeployButton, 
    [data-testid="stActionButtonIcon"] {
        display: none !important;
    }

    /* 3. HIỆN Menu 3 gạch và ẩn các mục thừa bên trong */
    #MainMenu {visibility: visible !important;}
    
    /* 4. ẨN Footer "Made with Streamlit" */
    footer {visibility: hidden;
    }
    /* Hiện lại Header để hiện tiêu đề khi gửi link */
    header {visibility: visible !important;}
    
    /* Chỉ ẩn Footer và Menu Streamlit để web chuyên nghiệp hơn */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    .viewerBadge_container__1QSob {display: none !important;}

    /* Nền App tối và hình nền chuyên nghiệp */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url("https://img.freepik.com/free-vector/abstract-binary-code-techno-background_1048-12836.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    /* Nền App tối và hình nền chuyên nghiệp */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url("https://img.freepik.com/free-vector/abstract-binary-code-techno-background_1048-12836.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
     /* 2. Sửa lỗi Sidebar bị trắng: Ép Sidebar luôn có màu tối */
    [data-testid="stSidebar"] {
        background-color: #111111 !important;
    }

    /* Khung nội dung chính */
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }
        /* Màu chữ và bóng đổ */
    h1, h2, h3, p, span, label {
        color: #FFFFFF !important;
        text-shadow: 1px 1px 3px black;
    }

    /* Tùy chỉnh ô nhập liệu */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid #4CAF50 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- HỆ THỐNG ỦNG HỘ PHUCKING® PREMIUM ---
with st.sidebar:
    st.divider()
    st.markdown("### ☕ Ủng hộ dự án")
    
    # Mức tiền gợi ý
    muc_donate = st.radio(
        "Chọn mức bạn muốn mời Phúc:",
        ["5.000 VNĐ", "10.000 VNĐ", "20.000 VNĐ", "Tùy tâm"],
        index=1
    )

    if st.button("Hiện mã QR Donate"):
        if muc_donate == "Tùy tâm":
            st.toast("Mọi sự ủng hộ từ bạn đều là động lực lớn cho Phúc! ❤️")
            loi_nhan = "Để xem tâm bạn như nào nha^^❤️!"
        else:
            st.toast(f"Cảm ơn bạn đã chọn mức {muc_donate}! 💖")
            loi_nhan = f"Vui lòng nhập đúng {muc_donate} khi quét mã ZaloPay/Ngân hàng"
        
        # Hiển thị ảnh QR
        st.image(
            "https://raw.githubusercontent.com/phuckingfco/bo-chuyen-doi-so_phucking-official/main/VCPank.jpg",
            caption=loi_nhan,
            use_container_width=True
        )
        
        st.info(f"Nội dung chuyển khoản: **PhucKing {muc_donate}**")


# 3. TIÊU ĐỀ & SIDEBAR 
st.title("🔢 Ứng dụng Chuyển đổi Hệ số")
st.sidebar.title("👑 Thương Hiệu")
st.sidebar.subheader("PhucKing® System")
st.sidebar.write("Chủ sở hữu: **Hoàng Phúc**")
st.sidebar.info("Phiên bản độc quyền 2026")

# 4. CHIA CÁC TAB
# Hệ thống 7 Tab chức năng của PhucKing®
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🔢 Chuyển đổi", 
    "📄 Văn bản", 
    "💡 Giải mã", 
    "➕ Cộng", 
    "➖ Trừ",
    "✖️ Nhân",
    "➕ Chia"
])

with tab1:
    st.header("Đổi sang Nhị Phân")
    du_lieu = st.text_input("Nhập vào số hoặc chữ:", key="input1")
    if du_lieu:
        if du_lieu.isdigit():
            ket_qua = bin(int(du_lieu)).replace('0b', '')
            st.markdown(f"<div style='background:#111; padding:15px; border-radius:10px; border:1px solid #4CAF50;'>Kết quả: {ket_qua}</div>", unsafe_allow_html=True)
        else:
            for ky_tu in du_lieu:
                ma_np = format(ord(ky_tu), '08b')
                st.write(f"**{ky_tu}** : `{ma_np}`")

with tab2:
    st.header("Đổi sang Thập Phân")
    nhi_phan = st.text_input("Nhập mã nhị phân:", key="input2")
    if nhi_phan:
        try:
            so_thap_phan = int(nhi_phan, 2)
            st.markdown(f"<div style='background:#111; color:#00FF00; padding:15px; border-radius:10px; border:1px solid #333; font-size:24px;'>{so_thap_phan:,}</div>", unsafe_allow_html=True)
        except:
            st.error("Chỉ nhập 0 và 1!")

with tab3:
    st.header("Đổi sang Chữ cái")
    input_nhi_phan = st.text_input("Nhập dãy nhị phân:", key="input3")
    if input_nhi_phan:
        try:
            danh_sach = input_nhi_phan.split()
            chu_ket_qua = "".join([chr(int(b, 2)) for b in danh_sach])
            st.success("Kết quả:")
            st.markdown(f"""
                <div style="background-color: #1a1a1a; color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #4CAF50; font-family: monospace; font-size: 20px; width: 100%;">
                    {chu_ket_qua}
                </div>
            """, unsafe_allow_html=True)
        except:
            st.error("Lỗi định dạng!")
])
with tab4:
    st.header("➕ Cộng hai số Nhị phân")
    col1, col2 = st.columns(2)
    with col1:
        bin1 = st.text_input("Nhập số nhị phân thứ nhất:", value="1010", key="add1")
    with col2:
        bin2 = st.text_input("Nhập số nhị phân thứ hai:", value="1100", key="add2")
    
    if st.button("Tính tổng"):
        try:
            # Chuyển từ nhị phân sang thập phân để tính toán
            sum_dec = int(bin1, 2) + int(bin2, 2)
            # Chuyển kết quả ngược lại nhị phân
            sum_bin = bin(sum_dec)[2:]
            st.success(f"Kết quả nhị phân: **{sum_bin}**")
            st.info(f"Giá trị thập phân: {sum_dec}")
        except ValueError:
            st.error("Vui lòng chỉ nhập số 0 và 1!")

with tab5:
    st.header("➖ Trừ hai số Nhị phân")
    col1, col2 = st.columns(2)
    with col1:
        bin_sub1 = st.text_input("Nhập số bị trừ (nhị phân):", value="1111", key="sub1")
    with col2:
        bin_sub2 = st.text_input("Nhập số trừ (nhị phân):", value="1010", key="sub2")
    
    if st.button("Tính hiệu"):
        try:
            val1 = int(bin_sub1, 2)
            val2 = int(bin_sub2, 2)
            if val1 < val2:
                st.warning("Kết quả sẽ là số âm!")
            
            sub_dec = val1 - val2
            # Xử lý hiển thị số âm trong nhị phân đơn giản
            if sub_dec >= 0:
                sub_bin = bin(sub_dec)[2:]
            else:
                sub_bin = "-" + bin(abs(sub_dec))[2:]
                
            st.success(f"Kết quả nhị phân: **{sub_bin}**")
            st.info(f"Giá trị thập phân: {sub_dec}")
        except ValueError:
            st.error("Vui lòng chỉ nhập số 0 và 1!")
with tab6:
    st.header("✖️ Nhân hai số Nhị phân")
    c1, c2 = st.columns(2)
    with c1:
        mul1 = st.text_input("Số thứ nhất:", value="101", key="mul1")
    with c2:
        mul2 = st.text_input("Số thứ hai:", value="11", key="mul2")
    
    if st.button("Tính tích"):
        try:
            # Chuyển sang thập phân để nhân cho chính xác
            res_dec = int(mul1, 2) * int(mul2, 2)
            res_bin = bin(res_dec)[2:]
            st.success(f"Kết quả nhị phân: **{res_bin}**")
            st.info(f"Giá trị thập phân: {res_dec:,}")
        except ValueError:
            st.error("Lỗi: Chỉ được nhập 0 và 1!")
with tab7:
    st.header("➕ Chia hai số Nhị phân")
    d1, d2 = st.columns(2)
    with d1:
        div1 = st.text_input("Số bị chia:", value="1100", key="div1")
    with d2:
        div2 = st.text_input("Số chia:", value="10", key="div2")
    
    if st.button("Tính thương"):
        try:
            v1 = int(div1, 2)
            v2 = int(div2, 2)
            if v2 == 0:
                st.error("Không thể chia cho số 0 (0000)!")
            else:
                quotient = v1 // v2 # Lấy phần nguyên
                remainder = v1 % v2 # Lấy phần dư
                st.success(f"Thương (nhị phân): **{bin(quotient)[2:]}**")
                if remainder > 0:
                    st.warning(f"Số dư (nhị phân): {bin(remainder)[2:]}")
                st.info(f"Thập phân: {quotient} dư {remainder}")
        except ValueError:
            st.error("Lỗi: Chỉ được nhập 0 và 1!")



