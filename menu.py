import streamlit as st 
from streamlit_option_menu import option_menu


#st.title("Portofolio Saya")
#st.header("Data Scientist & Data analyst")
#st.write("**Perkenalkan saya Endar Dwi Haryanto, dan ini adalah project kalkulator suhu sederhana saya di streamlit**")

with st.sidebar:
    selected = option_menu('Pilih Halaman',
    ['Tentang Saya','Dashboard',
     'Proyek', 'Kontak'],                       
    default_index=0)
    
if selected == 'Proyek':
    import house
    house.house_predict()
elif selected == 'Kontak':
    import kontak
    kontak.tampilkan_kontak()
elif selected == 'Tentang Saya':
    import tentang
    tentang.tentang()
elif selected == 'Dashboard':
    import dashboard
    dashboard.house_dashboard()