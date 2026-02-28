tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🔢 Chuyển đổi", 
    "📄 Văn bản", 
    "💡 Giải mã", 
    "➕ Cộng", 
    "➖ Trừ",
    "✖️ Nhân",
    "➕ Chia"
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


