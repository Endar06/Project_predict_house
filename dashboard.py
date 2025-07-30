import streamlit as st
import pandas as pd
import plotly.express as px

def house_dashboard():

    st.set_page_config(page_title="Dashboard Properti Beijing", layout="wide")

    st.title("🏠 Dashboard Interaktif - Properti Beijing")

    @st.cache_data
    def load_data():
        data = pd.read_csv("Bejing.csv", encoding='latin1', dtype={"id": str}, low_memory=False)
        return data

    data = load_data()

    st.sidebar.header("📊 Filter Data")

    districts = sorted(data['district'].dropna().unique())
    selected_district = st.sidebar.selectbox("Pilih Distrik", districts)

    building_types = data['buildingType'].dropna().unique()
    selected_type = st.sidebar.selectbox("Tipe Bangunan", building_types)

    renov_options = sorted(data['renovationCondition'].dropna().unique())
    selected_renov = st.sidebar.multiselect("Kondisi Renovasi", renov_options, default=renov_options)

    filtered_data = data[
        (data['district'] == selected_district) &
        (data['buildingType'] == selected_type) &
        (data['renovationCondition'].isin(selected_renov))
    ]

    st.subheader(f"📍 Data untuk Distrik: {selected_district} ({len(filtered_data)} properti)")

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Rata-rata Harga", f"{filtered_data['price'].mean():,.0f} Yuan")
    col2.metric("🏘️ Luas Median", f"{filtered_data['square'].median():.1f} m²")
    col3.metric("🚇 Dekat Subway", f"{filtered_data['subway'].sum()} properti")


    tab1, tab2 = st.tabs(["📈 Visualisasi", "📋 Tabel Data"])

    with tab1:
        st.markdown("### Distribusi Harga Properti")
        fig1 = px.histogram(filtered_data, x="price", nbins=50, color="renovationCondition")
        st.plotly_chart(fig1, use_container_width=True)

        st.markdown("### Luas vs Harga")
        fig2 = px.scatter(filtered_data, x="square", y="price", size="followers", color="elevator",
                        hover_data=["communityAverage", "floor"])
        st.plotly_chart(fig2, use_container_width=True)

    with tab2:
        st.markdown("### Data Properti")
        st.dataframe(filtered_data)

    st.markdown("---")
    st.markdown("📌 **Tips**: Gunakan filter di sidebar untuk melihat data berdasarkan distrik, tipe bangunan, dan kondisi renovasi.")
