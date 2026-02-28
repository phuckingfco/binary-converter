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
