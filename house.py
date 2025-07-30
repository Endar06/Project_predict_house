import streamlit as st
import joblib
import numpy as np
from streamlit_option_menu import option_menu

def house_predict():
    model = joblib.load('model_rumah.pkl')

    st.title('🏠 ESTIMASI HARGA RUMAH')
    st.image("https://chandu85.github.io/data-science/images/house-price.jpeg", width=150)

    col1, col2 = st.columns(2)

    with col1:
        communityAverage = st.number_input("Harga rata-rata komunitas (per m²)", min_value=10000, max_value=150000, value=50000)
        price = st.number_input("Harga per m²", min_value=5000, max_value=150000, value=40000)
        square = st.number_input("Luas rumah (m²)", min_value=10.0, max_value=1000.0, value=80.0)
        constructionTime = st.slider("Tahun Bangun", 1950, 2025, 2005)

        # Ganti: renovasiCondition jadi selectbox
        renov_input = st.selectbox(
            "Pilih Kondisi Renovasi:",
            ["Renovasi ringan", "Renovasi sedang", "Renovasi berat", "Renovasi keseluruhan"]
        )
        renovasi_mapping = {
            "Renovasi ringan": 0,
            "Renovasi sedang": 1,
            "Renovasi berat": 2,
            "Renovasi keseluruhan": 3
        }
        renovationCondition = renovasi_mapping[renov_input]

        followers = st.number_input('Input jumlah followers', min_value=0)

    with col2:
        livingRoom = st.number_input('Input jumlah ruang tamu', min_value=0)
        kitchen = st.number_input('Input jumlah dapur', min_value=0)
        bathRoom = st.number_input('Input jumlah kamar mandi', min_value=0)

        elevator_input = st.radio("Apakah ada elevator?", ["Yes", "No"])
        elevator = 1 if elevator_input == "Yes" else 0

        fiveYearsProperty_input = st.radio("Apakah properti berusia di bawah 5 tahun?", ["Yes", "No"])
        fiveYearsProperty = 1 if fiveYearsProperty_input == "Yes" else 0

        subway_input = st.radio("Apakah Ada Subway?", ["Yes", "No"])
        subway = 1 if subway_input == "Yes" else 0

    # Tombol Prediksi
    if st.button('🔍 Estimasi Harga'):
        input_data = np.array([[followers, price, square, livingRoom, kitchen, bathRoom,
                                constructionTime, renovationCondition, elevator,
                                fiveYearsProperty, subway, communityAverage]])
        
        predict = model.predict(input_data)[0]

        st.success(f"💰 Estimasi Harga Rumah: {round(predict, 2):,} Yuan")
        st.write(f"💸 Estimasi Harga dalam Rupiah (juta): Rp {round(predict * 2.276, 2):,} juta")
